import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from businesskeys.public import read_excel_data
from position.constants import URL_TEST, USERNAME_LOCATER, PASSWORD_LOCATER, LOGIN_BUTTON, USER_BUTTON, LOGOUT_BUTTON


# @allure.suite('测试套件示例')
# @allure.epic('项目示例')
# @allure.feature('模块示例')
# @allure.story('子模块示例')
# @allure.title('测试用例标题')
# @allure.severity('CRITICAL')
# @allure.description('这是一个测试用例的描述')
# @allure.testcase('https://example.com/testcase')
@allure.title('登录验证')
# 登录函数
def login(driver, username, password):
    with allure.step('步骤1：打开页面'):
        driver.get(URL_TEST)  # 替换为登录URL
    with allure.step('步骤2：输入账号和密码'):
        try:
            username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, USERNAME_LOCATER))  # 替换为实际的用户名输入框ID
            )
            username_input.send_keys(username)
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PASSWORD_LOCATER))  # 替换为实际的密码输入框ID
            )
            password_input.send_keys(password)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"输入账号密码失败，错误信息：{e}")
    with allure.step('步骤3：点击登录按钮'):
        try:
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON))  # 替换为实际的登录按钮ID
            )
            login_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"点击登录失败，错误信息：{e}")
    with allure.step('步骤4：判断是否登录成功'):
        try:
            username_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, USER_BUTTON))
            )
            actions = ActionChains(driver)
            actions.move_to_element(username_button).perform()
            print(f"登录成功:{username}")
            logout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, LOGOUT_BUTTON))
            )
            logout_button.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, USERNAME_LOCATER))
            )
        except Exception as e:
            print(f"登录失败:{username},错误{e}")


# pytest参数化测试，使用 fixture 管理 WebDriver
# 'function'表示这个fixture将在每个测试函数执行之前被调用，并在测试函数执行完毕后立即清理
@pytest.fixture(scope='function')
def driver():
    d = webdriver.Edge()
    yield d  # 关键字在这里用于将控制权交还给测试函数，同时传递d（Edge浏览器实例）给测试函数；当测试函数执行完毕后，控制权会再次回到这个fixture函数，继续执行yield之后的代码
    d.quit()


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')  # 替换为你的Excel文件路径和Sheet名称
)
def test_login(driver, username, password):
    login(driver, username, password)


# if __name__ == '__main__':
#     pytest.main(["-s", "-v", "--alluredir=allure_file"])

# 自动操作
# 用subprocess的方法操作命令行
# subprocess.call('allure generate allure_file -o allure_report --clean', shell=True)
# subprocess.call('allure open -h 127.0.0.1 -p 9999 allure_report', shell=True)

# 手动操作
# 执行前删除allure_file
# pytest -v --alluredir=allure_file 或者 pytest  test_login.py -v --alluredir=allure_file
# allure generate allure_file -o allure_report --clean
# allure open allure_report 或者 allure serve allure_file
