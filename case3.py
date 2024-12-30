from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, scan_program_search
from position.consants import DELETE_SCANNER_PROGRAM, DELETE_PROGRAM_CONFIRM_BUTTON, DELETE_CONFIRM
from sql.sql1 import getpgsql
from webkeys.webkeys import BrowserController


class scan_program_delete:
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

    # 删除扫描方案
    def delete_program(self, program_name):
        # 点击扫描方案tab
        self.switch_tabs_succeed('扫描方案')
        # 搜索扫描方案
        self.scan_program_search_succeed(txt=program_name)
        # 点击删除扫描方案
        self.driver.click(method=By.XPATH, locator=DELETE_SCANNER_PROGRAM)
        # 删除弹窗
        self.driver.according_wait(method=By.XPATH, locator=DELETE_CONFIRM)
        # 弹窗点击确定
        self.driver.click(method=By.XPATH, locator=DELETE_PROGRAM_CONFIRM_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()


def judge(program):
    try:
        sql1 = f"select * from neptune_artifact_scan_plan where plan_name = '{program}' and is_deleted = 'Y'"
        results = getpgsql(sql=sql1)
        if results:  # 检查是否有返回结果
            if results[0]['plan_name'] == program:
                print(f"自动化删除扫描方案成功: {program}")
            else:
                print("查询结果与预期不符")
        else:
            print("自动化删除扫描方案失败：未找到该方案")
    except Exception as e:
        print(f"数据库操作失败：{e}")


def main():
    driver = BrowserController(browser_type='edge')
    browser_study = scan_program_delete(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    browser_study.delete_program('扫描方案B81595050')


if __name__ == '__main__':
    main()
    judge('扫描方案B81595050')
