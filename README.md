Donation APP
=======

You've got python installed right? 
Let's proceed to set up a virtual enviroment for our app. 

- Clone this repository in a location of yur choice. 

- Create a virtual enviroment using  `python3 -m venv venv`

- Initialize the virtual enviroment `source venv/bin/activate`

- Install the requiremernts using `pip install -r requirements.txt`

- `export FLASK_APP=hello.py`

- Allow debugging so changes can be made in real time.             `export FLASK_DEBUG=1`

- set up database migrations by running.


- `flask db init`
- `flask db migrate`
- `flask db upgrade. `



The app is set. 
Run by typing `flask run`. 

- for ease of disposal, the default db is sqlite. 
tThis can be changed to MySQL or any other SQL database by changing the config.py  `"mysql://username:password@hostname/database`


That's all!
