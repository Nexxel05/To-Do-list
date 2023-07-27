# Todo-list-project

Simple Django project to track day-to-day tasks


## Installation

Python3 must be already installed

```shell
git clone https://github.com/Nexxel05/To-Do-list.git
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create .env file in root directory and store there your SECRET_KEY like shown in .env_sample 
```
python manage.py migrate
python manage.py runserver
```

## What can you do with it?

* Create different tags
* Create tasks associated with tags
* Change status of task on completion