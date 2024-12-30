from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, input_cve_number
from position.consants import CREATE_PROGRAM_BUTTON, PROGRAM_NAME_LOCATER, STE_DEFAULT, PROGRAM_DESCRIPTION_INPUT, \
    ADD_BUTTON, PROGRAM_CONFIRM_BUTTON
from webkeys.webkeys import BrowserController, get_number
from sql.sql1 import getpgsql


class scan_program_create:
    def __init__(self, driver):
        self.driver = driver

    # 登录页面
    def login_succeed(self):
        login(self.driver)

    # 进入制品扫描
    def change_directory_succeed(self):
        change_directory(self.driver)

    # 制品扫描选择tab页
    def switch_tabs_succeed(self, tab):
        switch_tabs(self.driver, tab=tab)

    # 添加漏洞编号
    def input_cve_number_succeed(self, num, txt):
        input_cve_number(self.driver, num=num, txt=txt)

    def create_program(self, name, description, number, position=1):
        """
        :param name: 方案名称
        :param description: 描述
        :param number: 漏洞编号
        :param position: 编号位置
        """
        # 点击扫描方案tab
        self.switch_tabs_succeed('扫描方案')
        # 点击创建按钮
        self.driver.click(method=By.XPATH, locator=CREATE_PROGRAM_BUTTON)
        # 输入方案名称
        scan_program_name = name + str(get_number(8))
        try:
            self.driver.input(method=By.XPATH, locator=PROGRAM_NAME_LOCATER, text=scan_program_name)
        except TimeoutException:
            # 处理超时异常，例如记录日志、重试或给出用户提示
            print("无法在指定时间内找到方案名称")
        # 设为默认
        self.driver.click(method=By.XPATH, locator=STE_DEFAULT)
        # 输入描述
        scan_program_description = description + str(get_number(8))
        self.driver.input(method=By.XPATH, locator=PROGRAM_DESCRIPTION_INPUT, text=scan_program_description)
        # 点击添加
        self.driver.click(method=By.XPATH, locator=ADD_BUTTON)
        # 输入漏洞编号
        self.input_cve_number_succeed(num=position, txt=number)
        self.driver.click(method=By.XPATH, locator=PROGRAM_CONFIRM_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()


def judge():
    try:
        sql1 = "select * from neptune_artifact_scan_plan where is_deleted = 'N' order by gmt_created desc limit 1;"
        results = getpgsql(sql=sql1)
        if results:  # 检查是否有返回结果
            if "扫描方案C" in results[0][0]:
                print(f"自动化创建扫描方案成功:{results[0][0]}")
            else:
                print("自动化创建扫描方案失败")
        else:
            print("自动化创建扫描方案失败：未找到该方案")
    except Exception as e:
        print(f"数据库连接失败：{e}")


def main():
    # 创建 BrowserStudy 类的实例
    driver = BrowserController(browser_type='edge')
    browser_study = scan_program_create(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    browser_study.create_program(name="扫描方案C", description="自动化创建扫描方案", number="CVE-2024-0530")


if __name__ == '__main__':
    main()
    judge()
