## Running the project

IMPORTANT: I installed Django (and possibly other dependencies) in a virtual environment. The requirements.txt file should contain all dependencies needed to run the project.

Start the system and ssh into it:

	$ vagrant up
	$ vagrant ssh

Run the following commands to install and setup Python Virtual Environment, then install Django (and other requirements):

	$ sudo apt install python3-venv 
	$ python3 -m venv venv 
	$ source venv/bin/activate
	$ cd project
	$ pip install -r requirements.txt

Once everything is installed, run the following to get the project running:

	$ python3 manage.py runserver 0:8080

Open the web page using the url http://localhost:8080/calculation/

I have created a superuser with admin capabilites:<br/>
Username: vagrant<br/>
Password: simonfraser<br/>