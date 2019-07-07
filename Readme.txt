Installation Instructions:

Step 01: First Install Python 3.6 or above with path configured.
Step 02: Open Command Prompt(Windows) or Terminal(Linux) and type
         pip install -r requirements.txt
         or for Linux
         sudo pip3 install -r requirements.txt
Step 03: Setup Mysql and Postgresql in OS.
Step 04: Create Databases by the name database_1 and database_2 in Postgresql.
Step 05: Create Databases by the name database_3, database_4 and database_5 in Mysql.
Step 06: Migrating databases,Open Command Prompt or Terminal at project's main directory, type:
         python manage.py makemigrations
         python manage.py migrate
         python manage.py migrate --database=database_1
         python manage.py migrate --database=database_2
         python manage.py migrate --database=database_3
         python manage.py migrate --database=database_4
         python manage.py migrate --database=database_5
Step 07: Now Create superuser i.e. admin again type in command prompt or terminal:
         python manage.py createsuperuser
Step 08: To run the developmental server
         python manage.py runserver
Step 09: Explore the project by registering a new user.
