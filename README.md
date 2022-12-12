# Test-task-Django

**Table of contents:**
- [Installation](#install)
- [Run](#run)


First of all, clone this repository in the folder and open it in cmd

```
git clone https://github.com/khasanovmma/Test-task.git
```

## Install

Use the package manager pip to install foobar

```
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy env.example and paste in the root project directory and configure it

```
.env.local
```

.env.local configuration

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=
```

## Run

Default Run the web service
```
python manage.py runserver
```

