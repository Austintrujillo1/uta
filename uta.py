import requests
import xml.etree.ElementTree as etree

api_key = "UPIIJBD0QEG"

url = "http://api.rideuta.com/SIRI/SIRI.svc/"
url += "StopMonitor?stopid=" #Query type
url += "TX136084" #Stop ID
url += "&minutesout=30" #How far in the future to query
url += "&onwardcalls=false" #Include vehicle calls inbetween current location and stop
url += "&filterroute=" #Filter vehicles
url += "&usertoken="
url += api_key

r = requests.get(url)
xml = r.content

root = etree.fromstring(xml)

for child in root[1][2]:
   print(child.tag, child.attrib)
   
