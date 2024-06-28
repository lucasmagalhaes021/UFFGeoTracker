import subprocess
import requests
import re
import threading
import time
import simplekml

def traceroute(target, tracerouteResult):
    command = ['tracert', target]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    CommandOutput, _ = process.communicate()
    CommandOutput = CommandOutput.decode('utf-8', 'ignore')
    formattedIpList = re.findall(r'\d+\.\d+\.\d+\.\d+', CommandOutput)
    if formattedIpList:
        formattedIpList.pop(0)
    tracerouteResult.extend(formattedIpList)

def SpinnerAnimation(event):
    spinner = "|/-\\"
    idx = 0
    while not event.is_set():
        print(f"\rTraçando Rota {spinner[idx % len(spinner)]}", end="")
        idx += 1
        time.sleep(0.1)
    print("\rRota Traçada!")

def getIpDetails(ip):
    url = f"http://ip-api.com/json/{ip}"
    apiResponse = requests.get(url)
    if apiResponse.status_code == 200:
        return apiResponse.json()
    else:
        return None

def createKML(city, longitude, latitude, host):
    kml = simplekml.Kml(name="TracerouteMap Map", open=1)
    tour = kml.newgxtour(name="Packet Route")
    playlist = tour.newgxplaylist()

    for i in range(len(city)):
        pnt = kml.newpoint(name=city[i])
        pnt.coords = [(longitude[i], latitude[i])]
        pnt.style.labelstyle.color = simplekml.Color.red
        pnt.style.labelstyle.scale = 3
        pnt.style.iconstyle.icon.href = 'https://cdn2.iconfinder.com/data/icons/social-media-8/512/pointer.png'
        pnt.style.iconstyle.scale = 2
        flyto = playlist.newgxflyto(gxduration=7)
        flyto.camera.longitude = longitude[i]
        flyto.camera.latitude = latitude[i]
        playlist.newgxwait(gxduration=3)

    filename = "Traceroute_endereco_" + host + ".kml"

    for i in range(len(city) - 1):
        name = city[i] + " to " + city[i+1]
        lin = kml.newlinestring(name=name)
        lin.coords = [(longitude[i], latitude[i]), (longitude[i+1], latitude[i+1])]
        lin.style.linestyle.width = 8
        lin.style.linestyle.color = simplekml.Color.cyan
        lin.tessellate = 1
        lin.altitudemode = simplekml.AltitudeMode.clamptoground

    kml.save(filename)
    return filename

def main():
    while True:
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
        
        city = []
        longitude = []
        latitude = []

        for ip in tracerouteResult:
            info = getIpDetails(ip)
            if info and info['status'] == 'success':
                city.append(info['city'])
                longitude.append(info['lon'])
                latitude.append(info['lat'])

        if len(city) > 0:
            filename = createKML(city, longitude, latitude, address)
            print(f"Arquivo KML criado: {filename}")

        user_choice = input("Digite 1 para fazer uma nova busca, ou 2 para sair: ")
        if user_choice == "2":
            break

if __name__ == "__main__":
    main()
