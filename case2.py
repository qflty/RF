from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, scan_program_search
from position.consants import EDIT_SCANNER_PROGRAM, IMPORT_NUMBER_FILE_lOCATER, VULNERABILITY_NUMBER_FILE, \
    INPORT_NUMBER_BUTTON, IMPORT_NUMBER_CONFIRM_BUTTON, PROGRAM_CONFIRM_BUTTON, STE_DEFAULT
from webkeys.webkeys import BrowserController


class scan_program_edit:
    def __init__(self, driver):
        self.driver = driver

    def login_succeed(self):
        login(self.driver)

    # 进入制品扫描
    def change_directory_succeed(self):
        change_directory(self.driver)

    # 制品扫描选择tab页
    def switch_tabs_succeed(self, tab):
        switch_tabs(self.driver, tab=tab)

    # 扫描方案搜素框
    def scan_program_search_succeed(self, txt):
        scan_program_search(self.driver, txt=txt)

    # 编辑扫描方案
    def edit_program(self, program_name):
        # 点击扫描方案tab
        self.switch_tabs_succeed('扫描方案')
        # 搜索扫描方案
        self.scan_program_search_succeed(txt=program_name)
        # 点击编辑扫描方案
        self.driver.click(method=By.XPATH, locator=EDIT_SCANNER_PROGRAM)
        # 点击导入编号
        ele = self.driver.locato(method=By.XPATH, locator=INPORT_NUMBER_BUTTON)
        self.driver.execute_js("arguments[0].click();", ele)
        # 导入漏洞编号文件
        self.driver.input(method=By.XPATH, locator=IMPORT_NUMBER_FILE_lOCATER, text=VULNERABILITY_NUMBER_FILE)
        self.driver.click(method=By.XPATH, locator=IMPORT_NUMBER_CONFIRM_BUTTON)
        self.driver.click(method=By.XPATH, locator=PROGRAM_CONFIRM_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()


def main():
    driver = BrowserController(browser_type='edge')
    browser_study = scan_program_edit(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    browser_study.edit_program('扫描方案C98187994')


if __name__ == '__main__':
    main()
