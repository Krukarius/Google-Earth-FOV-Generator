# Google-Earth-FOV-Generator
Generator of Field of View for any place defined in Google Earth


This is the simply Python tool, in which you can provide the relevant data for creating the Google Earth tour file.
The inputs are:
- Name
- Coordinates (to pe basted optionally from Google Maps)
- Altitude of sight (above ground)
- Azimuth of view
- Tilt (90 degrees as default - deaded roughly on the horizon)
- FOV (Definition of the Field of View value (minimum 10, which corresponds to 200mm focal length)
- Range of View 

With the following input the application creates the .kml file, which can be loaded to Google Earth quickly.

It's very useful in the case when we want to visuzlize the telephoto or wide-angle view from specified location not necessarily ground-based.

<B>REQUIRED:</B>

pyautogui library


<b>CURRENT VERSION</B>

1.0
