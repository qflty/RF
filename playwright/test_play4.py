import allure
import pytest
from businesskeys.public import read_excel_data
from position.page_index import url_test, login_ele


@allure.title('登录购物网址')
def login(page, username, password):
    with allure.step('输入网址'):
        try:
            page.goto(url_test)
        except TimeoutError as e:
            pytest.fail(f"Failed to navigate to {url_test}: {str(e)}")
    with allure.step('输入账号'):
        page.locator(login_ele['UserName']).fill(username)
    with allure.step('输入密码'):
        page.locator(login_ele['PassWord']).fill(password)
    with allure.step('点击登录'):
        page.locator(login_ele['Login_Button']).click()
    return page.url


@pytest.mark.parametrize(
    'username, password, expect_url, error_info1',
    read_excel_data('test_data.xlsx', 'Sheet4')
)
def test_login(page, username, password, expect_url, error_info1):
    aspect_url = login(page, username, password)
    assert aspect_url == expect_url, error_info1