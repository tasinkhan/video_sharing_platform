# video_sharing_platform

## Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/tasinkhan/video_sharing_platform.git
$ cd video_sharing_platform
```

Install python if it is not installed in the system:

```sh
$ sudo apt install python3.8
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ mkvirtualenv env -p python3.8
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
