<h1> Udemy Course </h1>
<p>The Python Mega Course: Build 10 Real World Applications </p>

<h2>Application 1: Building an Interactive Dictionary</h2>
<p>We created a dictionary using Python 3.6.3 Version and a JSON file where we have stored definitions of the words.</p>
<p>The JSON data it is stored like a Python dictionary datatype: key: value. For our needs, in this situation, the key represents the word that we are searching and the value is a list that contains one or more definitions for that word.</p>

<h4>Step number 1</h4>
<p>We load the JSON data into a Python dictionary, search the word in it and return the definition or a message if it isn't there. We used JSON library for importing the data</p>
<code> 
import json
data = json.load(open(“data.json”)) 
</code>

![alt text](https://github.com/ravarioana/udemy-10app/tree/master/Application1/app1.png)



<h4>Step number 2</h4>
<p>We need to take care of possible values that user may inputs. They can be lowercase, UPPERCASE, comBinAted and stored as lowercase in the dictionary so before the search, we will make all the letters to be lowercase.
May exist some situations when the user searches for some words with uppercase letters that they may exist in this way, in our dictionary so we should take care of them. Eg: USA, NATO, Delhi.
</p>

<h4> Step number 3</h4>
<p>It is possible that the word introduced to be written wrong from a mistake. Eg: rainn and not rain. In that case, the program will suggest the most similar word from the dictionary. </p>
<code>
from difflib import get_close_matches
matches = get_close_matches(word, possibilities, n=3, cutoff = 0.6)
</code>

<ul>
  <li>posibilities = a list of sequences which mach the word, ordered</li>
  <li>n = maxim number of close matches <- optional</li>
  <li>cutoff = ration, a float number in [0,1] <- optional</li>
</ul>


<h2>Application 2: Create a web map visualizing volcano and population data </h2>


<ul> For creating this application we used:
<li> Leaflet.js => an open-source JavaScript library for interactive maps.</li>
<li> Folium => a library that makes it easy to visualize data maipulated in Python, on an interactive Leaflet map. </li>
</ul>

We created some circle on the map that represents the volcanoes from the USA. The red ones are the volcanoes with the biggest elevation and the green ones are with the smallest elevation. For this details, we used the <code>CircleMarker</code> function from Folium.

We decided to add some colours to the map to represent the population from those zones. The red colour represents the most populated zone and the green one the less populated. 


Using the methods: <code>FeatureGroup</code> and <code>add_child</code> from Folium we organise our application in 2 parts (for population and for volcanoes). The <code>LayerControl</code> method helps us with a small menu from where we can choose what part we want to see on the map.
