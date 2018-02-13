<h2>Application 3: Create a Website Blocker application </h2>

We create an application that will help you to be more productive. During your working program or a specified time will block some websites specified by you.

The script will check the time frequently. If the current time is between your work program, will add the blocked links into <code>/etc/hosts</code> so the specified sites won't be accessible. If the time is outside your working hours, the links will be deleted from the file so you will be able to access them.

For manipulate the time we used: <code>datetime.now()</code>, a function from <b>datetime module</b> that gives us the current time. 

For read the file, edit its content and place the pointer where we need it, we used:  <code>file.readlines(), file.truncate(),  file.seek(0)</code>
