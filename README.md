# SeleniumPython
Selenium tests on Dockerized instance of GitLab's UI

Here is a detailed note about this project: 

https://medium.com/@sowmyaaji/how-to-write-tests-with-pytest-selenium-plugin-12362c811211

##Overview: 

I decided to write a series of user-interface (UI) tests for the GitLab website as an exercise to test out the pytest-selenium plugin.

The plugin works as a pytest fixture. Instead of passing a web driver through the tests, as is typical in selenium testing, it passes selenium as the argument. The plugin also takes care of the setup and teardown of each test and unless you specifically want a setup/teardown inside the scope of a function, you don’t need to write them at all. For simple, basic testing of the UI, its a great facilitating tool.

##Installation

Needs Python 3.6

$pipenv shell
$pipenv install selenium, pytest, pytest-selenium
