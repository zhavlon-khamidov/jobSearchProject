# Job Search Project 
This project is developed for learning pupose with IT&Business College students Ritchie group.

## How to run the project
Go to step by step on below command lines.  
In Ubuntu by default in case of command `python` use `python3`. Or if you want to make available `python` command run on terminal command  
$ ```sudo ln -s /usr/bin/python3 /usr/bin/python```

1. $ ```git clone https://github.com/zhavlon-khamidov/jobSearchProject.git```

1. open folder in vs code or any ide

1. In terminal $ ```python -m virtualenv env```
1. In linux OS $ ```source env/bin/activate```, and in [Widnows OS](https://medium.com/@astontechnologies/how-to-setup-a-virtual-development-environment-for-python-with-windows-powershell-4cd34b2f9f9b) `PS > .\env\Scripts\activate`. 
   Pay attention, when your environment activated in console you'll see the name of your virtual environment. ![](venv-active.png)
1. $ ```pip install -r requirements.txt```
1. $ ```python manage.py migrate```
1. $ ```python manage.py createsuperuser```  
      and fill username, email(optional) and password (keep type password even if you can't see it on your screen)
1. $ ```python manage.py runserver``` 
2. Go on your browser to http://127.0.0.1:8000/