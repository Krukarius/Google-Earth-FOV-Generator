import pyautogui



name = pyautogui.prompt(text='Please provide the name', title='Observation point')
geom = pyautogui.prompt(text='Paste Coordinates', title='Geolocation')
lat, lng = geom.split(',')
alt = pyautogui.prompt(text='Set the altitude of your sight', title='Altitude', default='2')
#if(pressed=='Cancel'):
        #alert(text='Have you changed your mind?', title='Input calcellation')
hd = pyautogui.prompt(text='Specify azimuth', title='Direction of view')
tlt = pyautogui.prompt(text='Specify tilt', title='The level of view', default='90')
fov = pyautogui.prompt(text='What field of view do you wish?', title='Enlargement', default='10')
rng = pyautogui.prompt(text='Define range of your view', title='Nearest foothold', default='1500')




vantage_point = pyautogui.confirm(
    title = name + ' - Confirmation',
    text = ' Coordinates: ' + lat + ',' + lng + '\n Altitude: ' + alt + '\n Azimuth: ' + hd + '\n Tilt: ' + tlt + '\n Field of View: ' + fov + '\n Range of View: ' + rng,
    buttons=['OK', 'Cancel']
)

if vantage_point == "Cancel":
    pyautogui.alert(title = 'Cancellation',
                    text = 'Do you want to cancel?',
                    button = 'Yes')
    quit()
                    
    
else:

    pyautogui.alert(title = 'Basic gudeline',
                text = """
                Load the file in Google Earth\n
                Please wait until Google Earth render your view.\n
                It might take up to a few minutes!\n
                ENJOY THE PANORAMA!
                """,
                button = 'Got it!')


#coord = geom.split(',')

#lat = coord[0]
#lng = coord[1]



with open (name + ' - FOV.kml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2"')
    f.write(' xmlns:gx="http://www.google.com/kml/ext/2.2"')
    f.write(' xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n')
    f.write("\t<gx:Tour>\n")
    f.write("<name>" + name + "</name>\n")
    f.write("<gx:Playlist>\n")
    f.write("<gx:FlyTo>\n")
    f.write("<LookAt>\n")
    f.write("<longitude>" + str(lng) + "</longitude>\n")
    f.write("<latitude>" + str(lat) + "</latitude>\n")
    f.write("<altitude>" + str(alt) + "</altitude>\n")
    f.write("<heading>" + str(hd) + "</heading>\n")
    f.write("<tilt>" + str(tlt) + "</tilt>")
    f.write("<range>" + str(rng) + "</range>")
    f.write("<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>\n")
    f.write("<gx:horizFov>" + str(fov) + "</gx:horizFov>\n")
    f.write("</LookAt>\n")
    f.write("</gx:FlyTo>\n")
    f.write("<gx:Wait><gx:duration>2.239990635644062e-006</gx:duration>\n")
    f.write("</gx:Wait>\n")
    f.write("</gx:Playlist>\n")
    f.write("</gx:Tour>\n")    
    f.write("\t</kml>\n")
    f.close()



