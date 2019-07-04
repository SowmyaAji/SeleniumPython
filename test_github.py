import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options


# options = webdriver.ChromeOptions()
# options.add_experimental_option('w3c', False)


def test_page_title(selenium):
    selenium.get('http://localhost')
    assert 'GitLab' in selenium.title


def test_login_button(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    selenium.get('http://localhost/users/sign_in')
    elem = selenium.find_element_by_link_text("Sign in")
    elem.click()


def test_login(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    selenium.get('http://localhost')
    selenium.find_element_by_id('user_login').send_keys('root')
    selenium.find_element_by_id('user_password').send_keys('p455w0rd')
    selenium.find_element_by_name('commit').click()


def test_search_repos(selenium):
    test_login(selenium)
    elem = selenium.find_element_by_id('search')
    assert elem is not None
    elem.send_keys("Python")
    elem.send_keys(Keys.RETURN)
    assert 'Python' in selenium.title


def test_new_project_button(selenium):
    test_login(selenium)
    selenium.find_element_by_link_text('New project').click()
    # selenium.find_element_by_class_name('blank-state-link').click()


def test_create_new_project(selenium):
    test_new_project_button(selenium)
    selenium.find_element_by_id('project_name').send_keys('my crazy project')
    selenium.find_element_by_id('project_path').send_keys('crazy-project')
    selenium.find_element_by_id(
        'project_description').send_keys('details awaited')
    selenium.find_element_by_id('project_visibility_level_20').click()
    selenium.find_element_by_name('commit').click()


def test_create_new_file(selenium):
    test_login(selenium)
    selenium.find_element_by_partial_link_text('new').click()
    selenium.find_element_by_class_name("add-to-tree").click()
    selenium.find_element_by_link_text('New file').click()
    selenium.find_element_by_class_name('dropdown-toggle-text').click()
    selenium.find_element_by_link_text('.gitignore').click()
    selenium.find_element_by_id('file_name').send_keys('fresh file')
    selenium.find_element_by_class_name(
        'ace_text-input').send_keys('random text')
    selenium.find_element_by_name('commit_message').send_keys('yay commit')
    selenium.find_element_by_id('file_name').send_keys(Keys.RETURN)


def test_find_file(selenium):
    test_login(selenium)
    selenium.find_element_by_partial_link_text('crazy').click()
    selenium.find_element_by_link_text('Find file').click()
    selenium.find_element_by_id('file_find').send_keys('abcd')


def test_edit_file(selenium):
    test_find_file(selenium)
    selenium.find_element_by_id("file_find").send_keys(Keys.RETURN)
    selenium.find_element_by_link_text('Edit').click()
    selenium.find_element_by_class_name('ace_content').click()
    selenium.find_element_by_class_name('ace_text-input').send_keys('more')
    selenium.find_element_by_class_name('commit-btn').click()
