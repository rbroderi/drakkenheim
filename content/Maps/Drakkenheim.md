---
publish: true
---
```leaflet  
id: MapCalcExample ### Must be unique with no spaces  
image: [[drakkenheim_map.png]] ### Link to the map image file  
bounds: [[0,0], [3508, 4069]] ### Size of the map in px Width_x, Height_y  
height: 650px ### Size of the leaflet embed in px on your screen  
width: 95% ### Size of the leaflet embed in your note  
lat: 2200 ### To center the map, make this half of the map width.  
long: 1821 ### To center the map, make this half of the map height.  
minZoom: -2.5 ### Controls how far away from the map you can zoom out. Hover over the target icon to see the current level.  
maxZoom: 0.9 ### Controls how far towards the map you can zoom in. Hover over the target icon to see the current level.  
defaultZoom: -2 ### Sets the default zoom level when the map loads. Hover over the target icon to see the current level.  
zoomDelta: 0.5 ### Adjust how much the zoom changes when you zoom in or out.  
unit: miles ### The value displayed when measuring so you know what type of unit is being measure.  
scale: 0.0005850006177606178 ### Only required if you are using the measurement tool. Real units/px (resolution) of your map  
recenter: false  
darkmode: false ### marker  
```
Shift Click to measure distances.