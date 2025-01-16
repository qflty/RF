import allure
import pytest
from businesskeys.public import read_excel_data
from position.constants import URL_TEST, USERNAME_LOCATER, PASSWORD_LOCATER, LOGIN_BUTTON, USER_BUTTON, LOGOUT_BUTTON


@allure.title('登录验证')
# 登录函数
def login(page, username, password):
    with allure.step('步骤1：打开页面'):
        page.goto(URL_TEST)
    with allure.step('步骤2：输入账号和密码'):
        page.wait_for_selector(USERNAME_LOCATER)
        page.type(USERNAME_LOCATER, str(username))
        page.type(PASSWORD_LOCATER, str(password))
    with allure.step('步骤3：点击登录按钮'):
        page.click(LOGIN_BUTTON)
    with allure.step('步骤4：判断是否登录成功'):
        try:
            page.wait_for_selector(USER_BUTTON)
            page.hover(USER_BUTTON)
            page.wait_for_selector(LOGOUT_BUTTON)
            page.click(LOGOUT_BUTTON)
            page.wait_for_selector(USERNAME_LOCATER)
            return True
        except Exception:
            # allure.attach.text(f"登录失败: {username}, 错误: {e}", name="登录错误")
            return False


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')
)
def test_login(page, username, password):
    assert login(page, username, password), f"登录失败：{username}"

