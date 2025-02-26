from time import sleep
import allure
import pytest
from businesskeys.public import read_excel_data
from position.constants import URL_TEST, USERNAME_LOCATER, PASSWORD_LOCATER, LOGIN_BUTTON, USER_BUTTON, LOGOUT_BUTTON


@allure.title('登录验证')
# 登录函数
def login(page, username, password):
    with allure.step('步骤1：打开页面'):
        page.goto(URL_TEST)  # 替换为登录URL
        sleep(5)
    with allure.step('步骤2：输入账号和密码'):
        try:
            page.fill(USERNAME_LOCATER, str(username))
            sleep(2)
            page.fill(PASSWORD_LOCATER, str(password))
        except Exception as e:
            print(f"输入账号密码失败，错误信息：{e}")
    with allure.step('步骤3：点击登录按钮'):
        try:
            page.click(LOGIN_BUTTON)
        except Exception as e:
            print(f"点击登录失败，错误信息：{e}")
    with allure.step('步骤4：判断是否登录成功'):
        try:
            sleep(3)
            page.hover(USER_BUTTON)
            print(f"登录成功:{username}")
            page.click(LOGOUT_BUTTON)
            sleep(3)
        except Exception as e:
            print(f"登录失败:{username},错误{e}")
            raise


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')  # 替换为你的Excel文件路径和Sheet名称
)
def test_login(page, username, password):
    login(page, username, password)
