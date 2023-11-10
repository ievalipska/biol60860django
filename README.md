**Load the variant database app locally**

<br>

1. Clone the repository

 `git clone https://github.com/ievalipska/biol60860django.git`

<br>

2. Create a Python 3 virtual environment

  `python3 -m venv <venv name>`

<br>

3. Activate virtual environment

`source <venv name>/bin/activate`

<br>

4. Install requirements

  `pip install -r requirements.txt`

<br>

5. We have committed our database to git so Django migrations shouldn't need to be run (If this was real clinical data we would not have committed the database to git). If you would like to double check whether migrations need to be run use the following commands.

  `python manage.py makemigrations`

  `python manage.py migrate`

<br>

6. To bring up the server

  `python manage.py runserver`

<br>



