import subprocess
import requests
import re
import threading
import time

def traceroute(target, tracerouteResult):
    # Executa o traceroute e armazena o resultado na variável tracerouteResult
    command = ['tracert', target]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    CommandOutput, _ = process.communicate()
    CommandOutput = CommandOutput.decode('utf-8', 'ignore')
    
    formattedIpList = re.findall(r'\d+\.\d+\.\d+\.\d+', CommandOutput)
    tracerouteResult.extend(formattedIpList)

def SpinnerAnimation(event):
    # Exibe uma animação de loading até que o evento de término seja setado
    spinner = "|/-\\"
    idx = 0
    while not event.is_set():
        print(f"\rTraçando Rota {spinner[idx % len(spinner)]}", end="")
        idx += 1
        time.sleep(0.1)
    print("\rRota Traçada!               ")

def getIpDetails(ip):
    url = f"http://ip-api.com/json/{ip}"
    apiResponse = requests.get(url)
    if apiResponse.status_code == 200:
        return apiResponse.json()
    else:
        return None

def main():
    address = 'salateorica.com.br'  # Exemplo de destino para o traceroute
    tracerouteResult = []

    # Evento para sinalizar quando o traceroute está concluído
    doneEvent = threading.Event()
    
    # Thread para o traceroute
    tracerouteThread = threading.Thread(target=traceroute, args=(address, tracerouteResult))
    
    # Thread para o loading
    loadingThread = threading.Thread(target=SpinnerAnimation, args=(doneEvent,))
    
    # Inicia as threads
    tracerouteThread.start()
    loadingThread.start()
    
    # Espera o traceroute terminar e sinaliza o término para a animação de loading
    tracerouteThread.join()
    doneEvent.set()
    loadingThread.join()

    # Processa e imprime os resultados
    ipMapperList = []
    for ip in tracerouteResult:
        info = getIpDetails(ip)
        if info and info['status'] == 'success':
            line = f"IP: {ip} | Lat: {info['lat']}, Lon: {info['lon']}"
            ipMapperList.append(line)

    for ipLine in ipMapperList:
        print(ipLine)

if __name__ == "__main__":
    main()
