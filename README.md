# SeleniumPython
Selenium tests on Dockerized instance of GitLab's UI

Here is a detailed note about this project: 

https://medium.com/@sowmyaaji/how-to-write-tests-with-pytest-selenium-plugin-12362c811211

## Overview: 

I decided to write a series of user-interface (UI) tests for the GitLab website as an exercise to test out the pytest-selenium plugin.

The plugin works as a pytest fixture. Instead of passing a web driver through the tests, as is typical in selenium testing, it passes selenium as the argument. The plugin also takes care of the setup and teardown of each test and unless you specifically want a setup/teardown inside the scope of a function, you don’t need to write them at all. For simple, basic testing of the UI, its a great facilitating tool.

## Installation

Needs Python 3.6
[https://www.python.org/downloads/]


## Set up local Docker instance

If you don't have Docker on your machine, go to:

https://docs.docker.com/v17.12/docker-for-mac/install/

Then carry out the following steps:

1. ```
$ mkdir mydockerimage
$ curl -k https://gist.githubusercontent.com/SowmyaAji/4f3bb2ad5b9477c4b965bffb6d27f8e3/raw/ecd7e30bd5b7b446cbde18ba392ba93c8942f305/dockerseleniumfile.txt > mydockerimage/Dockerfile
```
2.
 Now build a container with the dockerfile created. This container will have gitlab code + my SeleniumPython directory + everything needed for it including chrome driver. 
 
 ```
 $ docker build -t myseleniumimage:latest mydockerimage
```

3. Run the built container with:
``` 
$ docker run --name myseleniumcontainer --detach myseleniumimage:latest 

```


## Output

Run these commands: 

```
$ sleep 120

```

Wait for the 2 minute sleep to end. Then type:

```
$ docker exec -it myseleniumcontainer /bin/bash -c "pytest -v --driver chrome /SeleniumPython/test_gitlab.py"

```

The tests will execute in headless Chrome and will pass. Sometimes, Chrome takes time to load the Gitlab image and the tests may fail as the image did not get loaded in time. Please just run the docker exec command again. 