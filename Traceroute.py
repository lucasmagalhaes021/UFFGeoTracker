import subprocess
import requests
import re
import threading
import time
from tabulate import tabulate  # Biblioteca para formatar a saída em tabela

def traceroute(target, tracerouteResult):
    command = ['tracert', target]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    CommandOutput, _ = process.communicate()
    CommandOutput = CommandOutput.decode('utf-8', 'ignore')
    
    formattedIpList = re.findall(r'\d+\.\d+\.\d+\.\d+', CommandOutput)
    tracerouteResult.extend(formattedIpList)

def SpinnerAnimation(event):
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
    address = input("Digite a URL: ")
    tracerouteResult = []
    doneEvent = threading.Event()
    
    tracerouteThread = threading.Thread(target=traceroute, args=(address, tracerouteResult))
    loadingThread = threading.Thread(target=SpinnerAnimation, args=(doneEvent,))
    
    tracerouteThread.start()
    loadingThread.start()
    
    tracerouteThread.join()
    doneEvent.set()
    loadingThread.join()
    
    ipMapperList = []
    headers = ["IP Address", "Latitude", "Longitude", "Provedor de Internet", "Cidade", "País"]
    for ip in tracerouteResult:
        info = getIpDetails(ip)
        if info and info['status'] == 'success':
            ipData = [ip, info['lat'], info['lon'], info['isp'], info['city'], info['country']]
            ipMapperList.append(ipData)
    
    # Formata e exibe os resultados em uma tabela bonita
    print(tabulate(ipMapperList, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()