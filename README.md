<h1> Udemy Course </h1>
<p>The Python Mega Course: Build 10 Real World Applications </p>

<h2>Application 1: Building an Interactive Dictionary</h2>

<p align="left">
  <img src="/Application1/app1.png" width="500"/>
</p>
<p>We created a dictionary using Python 3.6.3 Version and a JSON file where we have stored definitions of the words.</p>
<p>The JSON data it is stored like a Python dictionary datatype: key: value. For our needs, in this situation, the key represents the word that we are searching and the value is a list that contains one or more definitions for that word.</p>

<h4>Step number 1</h4>
<p>We load the JSON data into a Python dictionary, search the word in it and return the definition or a message if it isn't there. We used JSON library for importing the data</p>
<code> 
import json
data = json.load(open(“data.json”)) 
</code>

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

<p align="left">
  <img src="/Application2/app2.png" width="800"/>
</p>

<ul> For creating this application we used:
<li> Leaflet.js => an open-source JavaScript library for interactive maps.</li>
<li> Folium => a library that makes it easy to visualize data maipulated in Python, on an interactive Leaflet map. </li>
</ul>

We created some circle on the map that represents the volcanoes from the USA. The red ones are the volcanoes with the biggest elevation and the green ones are with the smallest elevation. For this details, we used the <code>CircleMarker</code> function from Folium.

We decided to add some colours to the map to represent the population from those zones. The red colour represents the most populated zone and the green one the less populated. 

Using the methods: <code>FeatureGroup</code> and <code>add_child</code> from Folium we organise our application in 2 parts (for population and for volcanoes). The <code>LayerControl</code> method helps us with a small menu from where we can choose what part we want to see on the map.

<h2>Application 3: Create a Website Blocker application </h2>

We create an application that will help you to be more productive. During your working program or a specified time will block some websites specified by you.

The script will check the time frequently. If the current time is between your work program, will add the blocked links into <code>/etc/hosts</code> so the specified sites won't be accessible. If the time is outside your working hours, the links will be deleted from the file so you will be able to access them.

For manipulate the time we used: <code>datetime.now()</code>, a function from <b>datetime module</b> that gives us the current time. 

For read the file, edit its content and place the pointer where we need it, we used:  <code>file.readlines(), file.truncate(),  file.seek(0)</code>

<h2>Application 4: Building a website with Python and Flask</h2>

We created a website that, at the moment, contains only 2 pages: Home and About. 

As a web framework for Python, we used Flask. It is called a micro framework because it does not require particular tools or libraries. Our application contains one folder named <b>static</b> where we have the CSS and JS files, another folder <b>templates</b> where we keep the HTML files and also the layout and separated we have the python file.

We used Heroku, a cloud platform as a service that uses our scripts and can be deployed with Git commands. It is simple to install and use.

As an HTTP server, we used <b>Gunicorn</b> that is simply implemented and compatible with a number of web frameworks. It is necessary to have a file named Procfile, without extensions. Here we write what server we use and the details like: <b>web: gunicorn app4:app</b> (app4 is the name of the .py file, app is the name of the variable that store the Flask instance).

We need another two files: requirements.txt and runtime.txt. The runtime file contains our Python's version:<b>python-3.6.4</b> The requirements file contains the packages needed for the app:
<ul style="list-style-type:none">
<li>click==6.7 </li>
<li>Flask==0.12.2 </li>
<li>gunicorn==19.7.1 </li>
<li>itsdangerous==0.24 </li>
<li>Jinja2==2.10 </li>
<li>MarkupSafe==1.0 </li>
<li>Werkzeug==0.14.1</li>
</ul>

<p>To see only this packages we used the <code>pip freeze</code> command.</p> 
