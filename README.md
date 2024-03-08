#create virtual environment
python.exe -m venv venv

#activate virtual env
.\venv\Scripts\activate

#installed required packages
pip install Django
pip install django-crispy-forms
pip install Pillow
pip install crispy-bootstrap4

#Start project
python .\manage.py runserver
