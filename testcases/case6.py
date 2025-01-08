from businesskeys.public import login, judge_task
from businesskeys.scan import change_directory, switch_tabs, scan_task_search, scan_task_click
from webkeys.webkeys import BrowserController


# 删除扫描任务
class DeleteScanTask:
    def __init__(self, driver):
        self.driver = driver

    def login_and_navigate(self, tab):
        login(self.driver)
        change_directory(self.driver)
        switch_tabs(self.driver, tab)

    def delete_task(self, task_name, source, tab, tag):
        # 登录并进入扫描任务
        self.login_and_navigate(tab)
        # 搜索框搜索
        scan_task_search(self.driver, task_name, source)
        # 点击删除
        scan_task_click(self.driver, task_name, tag)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()
        return task_name


if __name__ == '__main__':
    driver = BrowserController('edge')
    browser_study = DeleteScanTask(driver)
    task_name = browser_study.delete_task(task_name='自动化创建30938353', source='手动创建', tab='扫描任务', tag='删除')
    sql_template = "select * from neptune_artifact_scan_task where task_name = %s and is_deleted = 'Y'"
    judge_task(sql_template, task_name)

