# locieWeb
Website of locie

Pure Development of Locie Website
Currently in pre-launch phase.

pip install venv
mkdir locieSite
cd locieSite
pythom3 -m venv locieEnv
source bin/activate
django-admin startproject locieWeb
./manage.py startapp locie
./manage.py makemigrations locie
./manage.py migrate
./manage.py runserver

