# projectnata
# Project Status
The project is not finished version of the IntenetShop.
# About the project
This Internet Shop is a product of Tutorials using Python Code.
It is not a production version of the WebSite. 

The project was adopted using MacBook Air (4Gb).


# Apps Used and Installed
Download and istall:

- PyCharm Pro 

- pip (just istall, it's a built in app),

- Python (last version),

- Docker.


# Usage
1) Create an Account, New Project and give a Name to your Repository
 on GitHub (your project can be uploaded and saved there later)

2) Use docker-compose up command to built and run a container:
docker-compose up

3) Open CLI in Docker Dashboard and make migrations of Data Base:
python manage.py migrate

4) Create SUPERUSER. Use CLI and type a command:

   python manage.py createsuperuser

Now You can use Django Administration at
http://localhost:8000/admin/

When you successfully have done all mentioned above, 
clone the projectnata or download it as a zip file onto you computer.

Unpack and run it.
You should see the website like this:
http://localhost:8000/

Now you can use it as admin and add products (using admin page), 
or make changes in a code (Python, JS, HTML). 

All these changes will stay on your computer untill you commit and push the changes.

But first, be sure the website still works or become better.

Don't use it in a harmful way.

# Composition and Structure of the projectnata
1 - the entry files in a "shop" files are:

internetsop/settings.py

internetsop/urls.py

2-each folder in "shop" (api1, cart, contacts, goods, home, userprofile)
 consist of the folder "migrations"and python files:

__init__.py,

admin.py,

apps.py,

models.py,

tests.py,

urls.py,

views.py.

3-folder "data" include all pictures from your InternetShop

4-static - here you have all js, css, etc.

5-templates - html  codes, django_registration plus registration folder



# Authors and acknowledgment
The project was done with the help and under supervision of 
ITStep Academy (Kharkiv office) teacher, Puchkov Yuriy, by student Natalia Shyriaieva

Thanks to my family for supporting my efforts in DevOps.
 
