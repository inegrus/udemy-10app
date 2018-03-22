<h2>Application 1: Building an Interactive Dictionary</h2>

<p align="left">
  <img src="/Application1/app1.png" width="500"/>
</p>
<p>We created a dictionary using Python 3.6.3 Version and a JSON file where we have stored definitions of the words.</p>
<p>The JSON data it is stored like a Python dictionary datatype: key: value. For our needs, in this situation, the key represents the word that we are searching and the value is a list that contains one or more definitions for that word.</p>

<h4>Step number 1</h4>
<p>We load the JSON data into a Python dictionary, search the word in it and return the definition or a message if it isn't there. We used JSON library for importing the data</p>
<pre><code> 
import json
data = json.load(open(“data.json”)) 
</code></pre>

<h4>Step number 2</h4>
<p>We need to take care of possible values that user may inputs. They can be lowercase, UPPERCASE, comBinEd and stored as lowercase in the dictionary so before the search, we will make all the letters to be lowercase.
May exist some situations when the user searches for some words with uppercase letters that they may exist in this way, in our dictionary so we should take care of them. E.g. USA, NATO, Delhi.
</p>

<h4> Step number 3</h4>
<p>It is possible that the word introduced to be written wrong from a mistake. E.g. rainn and not rain. In that case, the program will suggest the most similar word from the dictionary. </p>
<code>
from difflib import get_close_matches
matches = get_close_matches(word, possibilities, n=3, cutoff = 0.6)
</code>

<ul>
  <li>posibilities = a list of sequences which mach the word, ordered</li>
  <li>n = maxim number of close matches <- optional</li>
  <li>cutoff = ration, a float number in [0,1] <- optional</li>
</ul>
