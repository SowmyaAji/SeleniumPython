from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    selenium.find_element_by_id('user_password').send_keys('Minnal17!')
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
    selenium.find_element_by_link_text(
        'New project').click()


def test_create_new_project(selenium):
    test_new_project_button(selenium)
    selenium.find_element_by_id('project_name').send_keys('my crazy project')
    selenium.find_element_by_id('project_path').send_keys('crazy-project')
    selenium.find_element_by_id(
        'project_description').send_keys('details awaited')
    selenium.find_element_by_id('project_visibility_level_20').click()
    selenium.find_element_by_name('commit').click()


def test_find_file(selenium):
    test_login(selenium)
    selenium.find_element_by_partial_link_text('crazy').click()
    selenium.find_element_by_link_text('Find file').click()
    selenium.find_element_by_id('file_find').send_keys('abcd')
    selenium.find_element_by_id("file_find").send_keys(Keys.RETURN)

#     selenium.find_element_by_link_text("Edit").click()

# def test_edit_file(selenium):
#     test_find_file(selenium)

#     selenium.find_element_by_class_name('ace-content').send_keys('more')
#     selenium.find_element_by_name('commit').click()

    # selenium.find_element_by_class_name('dropdown').click()
    # selenium.find_element_by_link_text('.gitignore').click()
    # selenium.find_element_by_id('file_name').send_keys('fresh file')
    # selenium.find_element_by_class_name(
    #     'ace_text-input').send_keys('random text')
    # selenium.find_element_by_name('commit_message').send_keys('yay commit')
    # selenium.find_element_by_name('button').click()
