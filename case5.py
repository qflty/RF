from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, scan_task_search, scan_task_click_edit
from position.constants import QUALITY_CONTROL, SERIOUS_LEVEL, HIGH_RISK_LEVEL, MODERATE_RISK_LEVEL, LOW_RISK_LEVEL, \
    UNRATED_LEVEL, SAVE_ONLY_BUTTON
from webkeys.webkeys import BrowserController


# 编辑扫描任务
class EditScanTask:
    def __init__(self, driver):
        self.driver = driver

    # # 登录页面
    # def login_succeed(self):
    #     login(self.driver)
    #
    # # 进入制品扫描
    # def change_directory_succeed(self):
    #     change_directory(self.driver)
    #
    # # 制品扫描选择tab页
    # def switch_tabs_succeed(self, tab):
    #     switch_tabs(self.driver, tab)
    #
    # # 扫描任务搜索框
    # def scan_task_search_succeed(self, name, source):
    #     scan_task_search(self.driver, name, source)
    #
    # # 扫描任务点击编辑
    # def scan_task_click_edit_succeed(self, name):
    #     scan_task_click_edit(self.driver, name)

    # 编辑扫描任务
    def edit_task(self, task_name, source):
        login(self.driver)
        change_directory(self.driver)
        # 点击扫描方案tab
        switch_tabs(self.driver, '扫描任务')
        # 搜索框搜索
        scan_task_search(self.driver, task_name, source)
        # 点击编辑
        scan_task_click_edit(self.driver, task_name)
        # 点击质量门禁
        driver.click(By.XPATH, QUALITY_CONTROL)
        # 设置质量门禁
        self.driver.input(By.XPATH, SERIOUS_LEVEL, '10')
        self.driver.input(By.XPATH, HIGH_RISK_LEVEL, '20')
        self.driver.input(By.XPATH, MODERATE_RISK_LEVEL, '30')
        self.driver.input(By.XPATH, LOW_RISK_LEVEL, '40')
        self.driver.input(By.XPATH, UNRATED_LEVEL, '50')
        # 点击保存
        self.driver.click(By.XPATH, SAVE_ONLY_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()
        return task_name


if __name__ == '__main__':
    driver = BrowserController('edge')
    browser_study = EditScanTask(driver)
    # browser_study.login_succeed()
    # browser_study.change_directory_succeed()
    browser_study.edit_task(task_name='自动化创建30938353',source='手动创建')

