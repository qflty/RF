import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# 获取固定长度随机数
def get_number(length):
    num = random.randint(10 ** (length - 1), 10 ** length - 1)
    return num


class BrowserController:
    # 构造函数
    def __init__(self, browser_type='chrome', implicit_wait=3):
        """
        初始化浏览器控制器
        :param browser_type: 浏览器类型，默认为chrome
        :param implicit_wait: 隐式等待时间，默认为3秒
        """
        self.driver = self._initialize_driver(browser_type)
        self.driver.implicitly_wait(implicit_wait)  # 设置隐式等待时间
        self.driver.maximize_window()  # 最大化窗口

    def _initialize_driver(self, browser_type):
        """
        根据浏览器类型初始化WebDriver
        :param browser_type: 浏览器类型
        :return: WebDriver对象
        """
        if browser_type == 'chrome':
            from selenium.webdriver.chrome.service import Service as ChromeService
            from selenium.webdriver.chrome.options import Options
            options = Options()
            # 可以在这里添加更多的Chrome选项
            return webdriver.Chrome(service=ChromeService(), options=options)
        elif browser_type == 'firefox':
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from selenium.webdriver.firefox.options import Options
            options = Options()
            # 可以在这里添加更多的Firefox选项
            return webdriver.Firefox(service=FirefoxService(), options=options)
        elif browser_type == 'edge':
            from selenium.webdriver.edge.service import Service as EdgeService
            from selenium.webdriver.edge.options import Options
            options = Options()
            # 可以在这里添加更多的Edge选项
            return webdriver.Firefox(service=EdgeService(), options=options)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

    # 等待
    def sleep(self, t=3):
        time.sleep(t)

    # 访问url
    def open(self, url):
        self.driver.get(url)
        self.sleep(3)

    # 刷新
    def refresh(self):
        self.driver.refresh()

    # 关闭浏览器
    def close(self):
        self.driver.quit()

    # 显式等待
    def according_wait(self, method, locator, node='less', total=10, interval=1):
        """
        :param method: 定位方式
        :param locator: 元素路径
        :param node: 是否多路径
        :param total: 总共等待时间
        :param interval: 等待间隔
        :return: 元素定位路径
        """
        if node == 'less':
            Ele = WebDriverWait(self.driver, total, interval).until(EC.visibility_of_element_located((method, locator)))
        else:
            Ele = WebDriverWait(self.driver, total, interval).until(
                EC.visibility_of_element_located((method, locator)))
        return Ele

    # 元素定位+显式等待
    def locate(self, method, locator, node='less', Sign=True):
        """
        :param node: 是否多路径
        :param method: 定位方式r
        :param locator: 元素路径
        :param Sign: 定位失败是否跳过（True抛出异常，False跳过）
        """
        try:
            return self.according_wait(method, locator, node)
        except NoSuchElementException as e:
            if Sign:
                raise
            else:
                return False

    # 元素定位(无法显式定位)
    def locato(self, method, locator):
        return self.driver.find_element(method, locator)

    # 元素点击
    def click(self, method, locator, node='less', Sign=True):
        """
        :param node: 是否多路径
        :param method: 定位方式
        :param locator: 元素路径
        :param Sign: 定位失败是否跳过（True抛出异常，False跳过）
        """
        try:
            self.locate(method, locator, node, Sign).click()
        except:
            self.locato(method, locator).click()

    # 输入文本
    def input(self, method, locator, text, node='less', Sign=True):
        """
        :param node: 是否多路径
        :param method: 定位方式
        :param locator: 元素路径
        :param text: 输入文本
        :param Sign: 定位失败是否跳过（True抛出异常，False跳过）
        """
        try:
            self.locate(method, locator, node, Sign).send_keys(text)
        except:
            self.locato(method, locator).send_keys(text)

    # 获取文本
    def get_text(self, method, locator, node='less', Sign=True):
        """
        :param node: 是否多路径
        :param method: 定位方式
        :param locator: 元素路径
        :param Sign: 定位失败是否跳过（True抛出异常，False跳过）
        """
        try:
            text = self.locate(method, locator, node, Sign).text
        except:
            text = self.locato(method, locator).text
        return text

    # 清除文本
    def clear_text(self, method, locator, node='less', Sign=True):
        """
        :param node: 是否多路径
        :param method: 定位方式
        :param locator: 元素路径
        :param Sign: 定位失败是否跳过（True抛出异常，False跳过）
        """
        local = self.locate(method, locator, node, Sign)
        local.clear()

    # 等待元素消失,消失后返回True
    def existence_waite(self, method, locator, total=3, interval=1):
        """
        :param method: 定位方式
        :param locator: 元素路径
        :param total: 总共等待时间
        :param interval: 等待间隔
        :return: bool
        """
        try:
            WebDriverWait(self.driver, total, interval).until_not(EC.presence_of_element_located(method, locator))
        except Exception:
            return False
        return True

    # 切换iframe
    def change_iframe(self, num=0):
        """
        :param num: 默认进入第一次iframe
        """
        try:
            iframe = self.driver.find_elements(by=By.TAG_NAME('iframe'))[num]
            return self.driver.switch_to.frame(iframe)
        except Exception as e:
            return print(f"Failed to switch to iframe with index {num}: {e}")

    # 释放iframe
    def release_iframe(self):
        self.driver.switch_to.default_content()

    # 获取当前页面URL
    def get_url(self):
        return self.driver.current_url

    # 切换到新的窗口句柄
    def change_handle(self):
        # 获取当前所有窗口句柄
        handles = self.driver.window_handles
        # 检查是否有多个窗口打开
        if len(handles) > 1:
            # 切换到最后一个窗口句柄（通常是最新打开的窗口）
            self.driver.switch_to.window(handles[-1])
            print("Switched to the new window handle.")
        else:
            print("No new window to switch to.")

    # 截图并保存
    def capture(self, folder_path='screenshot'):
        # 确保文件夹存在，如果不存在则创建它
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 获取当前时间戳，用于生成唯一的文件名
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        screenshot = self.driver.get_screenshot_as_png()
        with open(file_path, 'wb') as file:
            file.write(screenshot)

    # 判断元素是否存在
    def are_there(self, method, locator, node='less'):
        """
        :param node: 是否多路径
        :param method: 定位方式
        :param locator: 元素路径
        :param return: bool
        """
        Flag = True
        try:
            self.locate(method, locator, node)
            return Flag
        except:
            Flag = False
            return Flag

    # 页面缩放
    def page_zoom(self, num=0.5):
        """
        :param num: 缩放比例
        """
        zoom = "document.body.style.zoom='{}'".format(num)
        self.driver.execute_script(zoom)

    # 得到元素属性值
    def get_attribute_text(self, method, locator, attr_name):
        """
        :attr_name: 属性名称
        """
        return self.locate(method, locator).get_attribute(attr_name)

    # 改变元素标签属性
    def change_attribute(self, method, locator, value, txt, node='less', Sign=True):
        path = self.locate(method, locator, node, Sign)
        js = 'arguments[0].{}="{}"'.format(value, txt)
        self.driver.execute_script(js, path)

    # 内嵌滚动条滚动
    def div_rolling(self, classname, method='div', direction='left', num=0, num2=0):
        """
        :param classname: 内嵌div的classname
        :param method: 内嵌windows/div
        :param direction: 滚动条滚动方向
        :param num: 左边距
        :param num2: 上边距
        """
        try:
            if method == 'div':
                if direction == 'top':
                    js = 'document.getElementsByClassName("{}")[0].scrollTop=' \
                         '{}'.format(classname, num)
                    self.driver.execute_script(js)
                elif direction == 'left':
                    js = 'document.getElementsByClassName("{}")[0].scrollLeft=' \
                         '{}'.format(classname, num)
                    self.driver.execute_script(js)
                else:
                    pass
            if method == 'window':
                js = "window.scrollTo({},{})".format(num, num2)
                return self.driver.execute_script(js)
        except Exception as e:
            raise e

    def longitudinal_rolling(self, num):
        js = "var q=document.getElementById('id').scrollTop=" + num
        self.driver.execute_script(js)

    def execute_js(self, js, element):
        self.driver.execute_script(js, element)

    # 将x,y插入js字符串
    def change_js(self, x, y):
        js = "window.scrollTo(,);"
        str_js1 = list(js)
        scrollTo_x = str_js1.index(',')
        str_js1.insert(scrollTo_x, str(x))
        js1 = ''.join(str_js1)
        str_js2 = list(js1)
        scrollTo_y = str_js2.index(')')
        str_js2.insert(scrollTo_y, str(y))
        js2 = ''.join(str_js2)
        return js2

    # 通过坐标(x, y)控制横向和纵向滚动条
    def transverse_rolling(self, x, y):
        js = self.change_js(x, y)
        self.driver.execute_script(js)

