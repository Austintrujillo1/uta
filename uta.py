import requests
import xmldict

from clint.textui import colored, puts

api_key = "UPIIJBD0QEG"

url = "http://api.rideuta.com/SIRI/SIRI.svc/"
url += "StopMonitor?stopid=" #Query type
url += "TX153041" #Stop ID
url += "&minutesout=30" #How far in the future to query
url += "&onwardcalls=false" #Include vehicle calls inbetween current location and stop
url += "&filterroute=" #Filter vehicles
url += "&usertoken="
url += api_key

r = requests.get(url)
xml = r.content

d = xmldict.xml_to_dict(xml)
d2 = d['{http://www.siri.org.uk/siri}Siri']['{http://www.siri.org.uk/siri}StopMonitoringDelivery']['{http://www.siri.org.uk/siri}MonitoredStopVisit']['{http://www.siri.org.uk/siri}MonitoredVehicleJourney']
print "\n"
print "QUERY STATION: ", d['{http://www.siri.org.uk/siri}Siri']['{http://www.siri.org.uk/siri}StopMonitoringDelivery']['{http://www.siri.org.uk/siri}Extensions']['{http://www.siri.org.uk/siri}StopName']
print "\n"
for x in d2:

    xname = str(x['{http://www.siri.org.uk/siri}PublishedLineName'])
    xlinenumber = str(x['{http://www.siri.org.uk/siri}LineRef'])
    xdest = str(x['{http://www.siri.org.uk/siri}DirectionRef'])

    if xname == "RED LINE":

        if xdest == 'TO DAYBREAK':
            xdest = "SB"
        else:
            xdest == "NB"

        puts(colored.red("Line Name: %s" % xname))
        puts(colored.red("Line Number: %s" % xlinenumber))
        puts(colored.red("Direction: %s" % xdest))
        print "\n"
    elif xname == "GREEN LINE":

        if xdest == 'TO WEST VALLEY':
            xdest = "SB"
        else:
            xdest == "NB"

        puts(colored.green("Line Name: %s" % xname))
        puts(colored.green("Line Number: %s" % xlinenumber))
        puts(colored.green("Direction: %s" % xdest))
        print "\n"
    elif xname == "BLUE LINE":

        if xdest == 'TO DRAPER':
            xdest = "SB"
        else:
            xdest == "NB"

        puts(colored.blue("Line Name: %s" % xname))
        puts(colored.blue("Line Number: %s" % xlinenumber))
        puts(colored.blue("Direction: %s" % xdest))
        print "\n"
