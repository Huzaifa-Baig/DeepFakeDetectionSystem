IMPORTANT!!!
Make sure you have Python 3.* and MySQL installed on the system.

pip install virtualenv
py -m venv env
env\Scripts\activate

pip install -r requirements.txt

then, 
flask run
or
use the debug button at the top to run app

The following commands will help with database management
flask db migrate - m "message"
flask db upgrade