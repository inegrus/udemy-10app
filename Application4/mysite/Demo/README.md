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
