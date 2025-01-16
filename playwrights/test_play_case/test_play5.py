import allure
import playwright
import pytest
from businesskeys.public import read_excel_data
from position.page_index import select_add, shop_cart_link, check_out, first_name, last_name, postal_code, \
    continue_button, finish_button, complete, url_test, login_ele


@allure.title('客户购买物品')
def select_and_buy(page, username, password, items):
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
    with allure.step('选择物品'):
        for item in items:
            item = item.strip()  # 去除物品名称中可能存在的空白字符
            try:
                page.locator(select_add.get(item)).click()
            except KeyError:
                pytest.fail(f"No locator found for item: {item}")
            except playwright._impl._errors.TimeoutError:
                pytest.fail(f"定位商品{item}超时")
    with allure.step('进入购物车'):
        page.locator(shop_cart_link).click()
    with allure.step('进入信息页面'):
        page.locator(check_out).click()
    with allure.step('输入个人信息'):
        page.locator(first_name).fill(username)
        page.locator(last_name).fill(username)
        page.locator(postal_code).fill('magua')
    with allure.step('进入结算页面'):
        try:
            page.locator(continue_button).click()
        except playwright._impl._errors.TimeoutError:
            pytest.fail(f"{username}点击结算超时")
    with allure.step('点击完成'):
        try:
            page.locator(finish_button).click()
        except playwright._impl._errors.TimeoutError:
            pytest.fail(f"{username}点击完成超时")
    with allure.step('感谢惠顾'):
        try:
            aspect_text = page.locator(complete).text_content()
        except playwright._impl._errors.TimeoutError:
            pytest.fail(f"{username}获取感谢文本超时")
    return aspect_text


@pytest.mark.parametrize(
    'username, password, items_str, expect_text, error_info1',
    read_excel_data('test_data.xlsx', 'Sheet5')
)
def test_select_and_buy(page, username, password, items_str, expect_text, error_info1):
    # 将 items_str 拆分成列表
    try:
        items = items_str.split(',')
    except AttributeError as e:
        pytest.fail("items_str数据格式错误")
    aspect_text = select_and_buy(page, username, password, items)
    assert aspect_text == expect_text, error_info1