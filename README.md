# django-quiz-app
It is django based quiz app for multiple choice questions.


### Snaps of project 
  Login:
  ![alt text](https://github.com/sswapnil2/django-quiz-app/blob/master/screenshots/login.png "login page")
  <br>
  
  quiz:
  ![alt text](https://github.com/sswapnil2/django-quiz-app/blob/master/screenshots/quiz_page.png  "quiz page")
  <br>
  
  results:
  ![alt text](https://github.com/sswapnil2/django-quiz-app/blob/master/screenshots/results.png "results")
  <br>
  
# Instructions 

1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/sswapnil2/django-quiz-app.git`<br>
  `cd django-quiz-app`
  
2) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
3) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
4) ### Create superuser
  To create super user run. <br>
  `python manage.py createsuperuser` <br>
  After running this command it will ask for username, password.
  You can access admin panel from `localhost:8000/admin/`

4) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
 
5) ### Reference
  I have refernced this quizz app from [tomwalker's](https://github.com/tomwalker) original repo. 
  Reference link to the quiz app repo is [here](https://github.com/tomwalker/django_quiz)
  
