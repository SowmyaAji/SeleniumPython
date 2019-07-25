# SeleniumPython
Selenium tests on Dockerized instance of GitLab's UI

Here is a detailed note about this project: 

https://medium.com/@sowmyaaji/how-to-write-tests-with-pytest-selenium-plugin-12362c811211

## Overview: 

I decided to write a series of user-interface (UI) tests for the GitLab website as an exercise to test out the pytest-selenium plugin.

The plugin works as a pytest fixture. Instead of passing a web driver through the tests, as is typical in selenium testing, it passes selenium as the argument. The plugin also takes care of the setup and teardown of each test and unless you specifically want a setup/teardown inside the scope of a function, you don’t need to write them at all. For simple, basic testing of the UI, its a great facilitating tool.

## Installation

Needs Python 3.6

$ pipenv shell
$ pip install -r requirements.txt

## Set up local Docker instance

If you don't have Docker on your machine, go to:

https://docs.docker.com/v17.12/get-started/#recap-and-cheat-sheet

Go to home directory ($ cd or $ ~)
$ mkdir data
$ cd data
$ mkdir gitlab/config:/etc/gitlab
$ mkdir gitlab/logs:/var/log/gitlab
$ mkdir gitlab/data:/var/opt/gitlab

Modify following code (put your name in place of **** after Users/) and run it:

$ docker run — detach \
 — hostname localhost \
 — publish 443:443 — publish 80:80 — publish 22:22 \
 — name gitlab \
 — restart always \
 — volume /Users/****/data/gitlab/config:/etc/gitlab \
 — volume /Users/****/data/gitlab/logs:/var/log/gitlab \
 — volume /Users/****/data/gitlab/data:/var/opt/gitlab \
 gitlab/gitlab-ce:latest

A Docker container will be created. 


## Output

Run this file from command line as pytest -v --driver chrome test_gitlab.py

[two of the tests will fail]

For individual tests, run from command line: pytest -v --driver chrome test_gitlab.py -k [name of the test without args,like this: test_login]
