
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# tests using selenium-python plugin to test the UI of Gitlab
# these tests are run from a Docker instance of GitLab, running on the local host


# from command line, run: pytest -v --driver chrome test_gitlab.py to run all the tests
# from command line, run: pytest -v --driver chrome test_gitlab.py -k test_page_title to run just the first test. Replace 'test_page_title' with the name of whichever individual test to be run.


# pass selenium fixture (from python-selenium plugin) to each test
# test to see if Gitlab is in the title of the local host page
def test_page_title(selenium):
    selenium.get('http://localhost')
    assert 'GitLab' in selenium.title

# test of the login button on the Gitlab home page


def test_login_button(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    selenium.get('http://localhost/users/sign_in')
    elem = selenium.find_element_by_link_text("Sign in")
    elem.click()

# test the login functionality using  'root' as username and 'p455w0rd' as the password


def test_login(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    selenium.get('http://localhost')
    selenium.find_element_by_id('user_login').send_keys('root')
    selenium.find_element_by_id('user_password').send_keys('p455w0rd')
    selenium.find_element_by_name('commit').click()

# test the search bar to find repositories that have 'Python' in their title


def test_search_repos(selenium):
    test_login(selenium)
    elem = selenium.find_element_by_id('search')
    assert elem is not None
    elem.send_keys("Python")
    elem.send_keys(Keys.RETURN)
    assert 'Python' in selenium.title

# test the create new repository button
# if there is no project at all in your repository


def test_new_project_button1(selenium):
    test_login(selenium)
    selenium.find_element_by_class_name('blank-state-link').click()
    selenium.find_element_by_link_text('New project').click()


# if there is at least one project in your repository
def test_new_project_button2(selenium):
    test_login(selenium)
    selenium.find_element_by_link_text('New project').click()


# test to create a new project
def test_create_new_project(selenium):
    test_new_project_button2(selenium)
    selenium.find_element_by_id('project_name').send_keys('my crazy project')
    selenium.find_element_by_id('project_path').send_keys('crazy-project')
    selenium.find_element_by_id(
        'project_description').send_keys('details awaited')
    selenium.find_element_by_id('project_visibility_level_20').click()
    selenium.find_element_by_name('commit').click()

# test to create a new file
# if this is the very first file in the project


def test_create_new_file1(selenium):
    test_login(selenium)
    selenium.find_element_by_partial_link_text('crazy').click()
    selenium.find_element_by_link_text('New file').click()
    selenium.find_element_by_class_name('dropdown-toggle-text').click()
    selenium.find_element_by_link_text('.gitignore').click()
    selenium.find_element_by_id('file_name').send_keys('abcd')
    selenium.find_element_by_class_name(
        'ace_text-input').send_keys('random text')
    selenium.find_element_by_name('commit_message').send_keys('yay commit')
    selenium.find_element_by_id('file_name').send_keys(Keys.RETURN)

# if a file already exists/existed in the project


def test_create_new_file2(selenium):
    test_login(selenium)
    selenium.find_element_by_partial_link_text('crazy').click()
    selenium.find_element_by_class_name("add-to-tree").click()
    selenium.find_element_by_link_text('New file').click()
    selenium.find_element_by_class_name('dropdown-toggle-text').click()
    selenium.find_element_by_link_text('.gitignore').click()
    selenium.find_element_by_id('file_name').send_keys('abcd')
    selenium.find_element_by_class_name(
        'ace_text-input').send_keys('random text')
    selenium.find_element_by_name('commit_message').send_keys('yay commit')
    selenium.find_element_by_id('file_name').send_keys(Keys.RETURN)

# test to find files in the repository


def test_find_file(selenium):
    test_login(selenium)
    selenium.find_element_by_partial_link_text('crazy').click()
    selenium.find_element_by_link_text('Find file').click()
    selenium.find_element_by_id('file_find').send_keys('abcd')

# test to edit/update an existing file in the repository


def test_edit_file(selenium):
    test_find_file(selenium)
    time.sleep(5)
    selenium.find_element_by_id("file_find").send_keys(Keys.RETURN)
    selenium.find_element_by_link_text('Edit').click()
    selenium.find_element_by_class_name('ace_content').click()
    selenium.find_element_by_class_name('ace_text-input').send_keys('more')
    selenium.find_element_by_class_name('commit-btn').click()

# test to delete an existing file


def test_delete_file(selenium):
    test_find_file(selenium)
    time.sleep(5)
    selenium.find_element_by_id("file_find").send_keys(Keys.RETURN)
    selenium.find_element_by_class_name('btn-remove').click()
    selenium.find_element_by_class_name('btn-remove-file').click()
