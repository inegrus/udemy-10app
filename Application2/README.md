<h2>Application 2: Create a web map visualising volcano and population data </h2>

<p align="left">
  <img src="/Application2/app2.png" width="800"/>
</p>

<ul> For creating this application we used:
<li> Leaflet.js => an open-source JavaScript library for interactive maps.</li>
<li> Folium => a library that makes it easy to visualise data manipulated in Python, on an interactive Leaflet map. </li>
</ul>

We created some circle on the map that represents the volcanoes from the USA. The red ones are the volcanoes with the biggest elevation, and the green ones are with the smallest elevation. For this details, we used the <code>CircleMarker</code> function from Folium.

We decided to add some colours to the map to represent the population from those zones. The red colour represents the most populated zone and the green one the less populated. 

Using the methods: <code>FeatureGroup</code> and <code>add_child</code> from Folium we organise our application in 2 parts (for population and volcanoes). The <code>LayerControl</code> method helps us with a small menu from where we can choose what part we want to see on the map.
