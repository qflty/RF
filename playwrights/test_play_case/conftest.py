import pytest
from playwright.sync_api import sync_playwright


# 定义一个浏览器实例的 fixture，其作用范围为整个模块
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        # 生成浏览器驱动
        browser = p.chromium.launch(headless=False, channel='msedge')
        yield browser
        browser.close()


# 定义一个浏览器页面的 fixture，其作用范围为每个测试函数
@pytest.fixture(scope="function")
def page(browser):
    # 生成浏览器上下文（context）对象
    context = browser.new_context()
    # 生成浏览器页面page
    page = context.new_page()
    page.set_default_navigation_timeout(60000)  # 设置默认导航超时时间为60秒
    yield page
    context.close()