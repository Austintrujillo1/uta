import requests
import xmldict

from clint.textui import colored, puts
#{"STOP NAME":("NB ID", "SB ID")}
STOPDB = {"SALT LAKE CENTRAL":("XXXTX101394","XXXTX101404"),
            "OLD GREEKTOWN":("TX101396","XXXTX101406"),
            "PLANETARIUM":("TX101405", "XXXTX101395"),
            "ARENA":("TX125067", "XXXTX125069"),
            "TEMPLE SQUARE":("TX125078","XXXTX125084"),
            "CITY CENTER":("TX128001","TX128002"),
            "GALLIVAN PLAZA":("TX126071","TX126073"),
            "COURTHOUSE":("TX125085","TX125091"),
            "900 SOUTH":("TX136085","TX136084"),
            "BALLPARK":("TX125092","TX125093"),
            "CENTRAL POINTE":("TX125094","TX125096"),
            "MILLCREEK":("TX136033","TX136034"),
            "MEADOWBROOK":("TX136035","TX136036"),
            "MURRAY NORTH":("TX136045","TX136048"),
            "MURRAY CENTRAL":("TX153027","TX153034"),
            "FASION PLACE WEST":("TX153041","TX153045"),
            "MIDVALE FORT UNION":("TX153046","TX153047"),
            "MIDVALE CENTER":("TX153048","TX153049"),
            "HISTORIC SANDY":("TX173021","TX173022"),
            "SANDY EXPO":("TX173129","TX173130"),
            "SANDY CIVIC CENTER":("TX173026","TX173029"),
            "CRESCENT VIEW":("TX198093","TX198094"),
            "KIMBALLS LANE":("TX198095","TX198096"),
            "DRAPER TOWN CENTER":("TX198097","TX198098")
            }


qStopID = str(STOPDB["900 SOUTH"][1]) #0 - NB 1 - SB

api_key = "UPIIJBD0QEG"

url = "http://api.rideuta.com/SIRI/SIRI.svc/"
url += "StopMonitor?stopid=" #Query type
url += qStopID #Stop ID
url += "&minutesout=180" #How far in the future to query
url += "&onwardcalls=false" #Include vehicle calls inbetween current location and stop
url += "&filterroute=" #Filter vehicles
url += "&usertoken="
url += api_key

r = requests.get(url)
xml = r.content

d = xmldict.xml_to_dict(xml)

d2 = d['{http://www.siri.org.uk/siri}Siri']['{http://www.siri.org.uk/siri}StopMonitoringDelivery']['{http://www.siri.org.uk/siri}MonitoredStopVisit']['{http://www.siri.org.uk/siri}MonitoredVehicleJourney']

#Print Query Header
print ("\nQUERY STATION: %s \n" % colored.black(d['{http://www.siri.org.uk/siri}Siri']['{http://www.siri.org.uk/siri}StopMonitoringDelivery']['{http://www.siri.org.uk/siri}Extensions']['{http://www.siri.org.uk/siri}StopName']))

#Print query data
for x in d2:

    xname = str(x['{http://www.siri.org.uk/siri}PublishedLineName'])
    xlinenumber = str(x['{http://www.siri.org.uk/siri}LineRef'])
    xdest = str(x['{http://www.siri.org.uk/siri}DirectionRef'])
    xtime = int(x['{http://www.siri.org.uk/siri}MonitoredCall']['{http://www.siri.org.uk/siri}Extensions']['{http://www.siri.org.uk/siri}EstimatedDepartureTime'])
    xtime = xtime / 60 #convert to minutes
    if xname == "RED LINE":

        if xdest == 'TO DAYBREAK':
            xdest = "SB"
        elif xdest == 'TO MEDICAL':
            xdest = "NB"

        puts(colored.red("Line Name: %s" % xname))
        puts(colored.red("Line Number: %s" % xlinenumber))
        puts(colored.red("Direction: %s" % xdest))
        puts(colored.red("Est Departure: %s Minutes" % xtime))
        print "\n"
    elif xname == "GREEN LINE":

        if xdest == 'TO WEST VALLEY':
            xdest = "SB"
        else:
            xdest = "NB"

        puts(colored.green("Line Name: %s" % xname))
        puts(colored.green("Line Number: %s" % xlinenumber))
        puts(colored.green("Direction: %s" % xdest))
        puts(colored.green("Est Departure: %s Minutes" % xtime))
        print "\n"
    elif xname == "BLUE LINE":

        if xdest == 'TO DRAPER':
            xdest = "SB"
        elif xdest == 'TO SALT LAKE CT':
            xdest = "NB"

        puts(colored.blue("Line Name: %s" % xname))
        puts(colored.blue("Line Number: %s" % xlinenumber))
        puts(colored.blue("Direction: %s" % xdest))
        puts(colored.blue("Est Departure: %s Minutes" % xtime))
        print "\n"
