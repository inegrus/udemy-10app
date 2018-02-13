<h2>Application 5: Building a Desktop Database Application</h2>

We created a mac application that stores books information into a database. We can search a book by title, author, a year or an ISBN code. We can add a book to our database, view all the books, update or delete an existing one.

For this app, we used <b>Tkinter</b>, a module that helps us to create the <b>GUI (Graphical User Interface)</b> and in the backend we used <b>SQLite 3</b> that helps us to store the books into a database.

First, we created a sketch how would like to be the frontend of our program.
<p align="center">
  <img src="/Application5/BookStore/sketch.png" width="500"/>
</p>

After that, we created the backend, the connection with the database and all the functions that we need for our application (create the table, insert in it, select, search and update).

<p>For each functionality, we need to create a connection with the database, create a cursor, execute SQL commands, save the changes and close the database.</p>
<pre><code>
def insert(title, author, year, isbn): <br>
    conn = sqlite3.connect("books.db") <br>
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()
</code></pre>
<p>In the example, we added NULL as a parameter because there should be the Primary Key but it is updated automatically by the program.</p>

The third part was to create the frontend part and connect each button with his functionality from the backend. 

<ul>From Tkinter we used:
<li>window</li>
<li>label</li>
<li>entry</li>
<li>listbox</li>
<li>scrollbar</li>
<li>button</li>
</ul>

The final part was to create the application file (.app) that helps us to use our program without to execute the script in a terminal.
Here we used the <b>py2applet</b>, a Python setup tool command. It needs to be installed and it uses a setup.py file for the settings as what external files to use (database), what Python file to run and other details. 

<p align="center">
  <img src="/Application5/BookStore/App5.png" width="500"/>
</p>
