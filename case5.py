from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, scan_task_search, set_quality_gates, scan_task_click
from position.constants import QUALITY_CONTROL, SERIOUS_LEVEL, HIGH_RISK_LEVEL, MODERATE_RISK_LEVEL, LOW_RISK_LEVEL, \
    UNRATED_LEVEL, SAVE_ONLY_BUTTON
from webkeys.webkeys import BrowserController


# 编辑扫描任务
class EditScanTask:
    def __init__(self, driver):
        self.driver = driver

    def login_and_navigate(self, tab):
        login(self.driver)
        change_directory(self.driver)
        switch_tabs(self.driver, tab)

    def edit_task(self, task_name, source, tab, tag, gates):
        # 登录并进入扫描任务
        self.login_and_navigate(tab)
        # 搜索框搜索
        scan_task_search(self.driver, task_name, source)
        # 点击编辑
        scan_task_click(self.driver, task_name, tag)
        # 点击质量门禁并设置质量门禁
        self.driver.click(By.XPATH, QUALITY_CONTROL)
        set_quality_gates(self.driver, gates)
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
    browser_study.edit_task(task_name='自动化创建30938353', source='手动创建', tab='扫描任务', tag='编辑',
                            gates={SERIOUS_LEVEL: '10', HIGH_RISK_LEVEL: '20', MODERATE_RISK_LEVEL: '30',
                                   LOW_RISK_LEVEL: '40', UNRATED_LEVEL: '50'})
