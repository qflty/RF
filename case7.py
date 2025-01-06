from businesskeys.public import login, judge_task
from businesskeys.scan import change_directory, switch_tabs, scan_task_search, scan_task_click
from testcases.case6 import DeleteScanTask
from webkeys.webkeys import BrowserController


# 执行扫描任务
class ExecuteScanTask:
    def __init__(self, driver):
        self.driver = driver

    def login_and_navigate(self, tab):
        login(self.driver)
        change_directory(self.driver)
        switch_tabs(self.driver, tab)

    def execute_task(self, tab, task_name, source, tag):
        # 登录并进入扫描任务
        self.login_and_navigate(tab)
        # 搜索框搜索
        scan_task_search(self.driver, task_name, source)
        # 点击执行
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
    task_name = browser_study.delete_task(tab='扫描任务', task_name='lq-nexus-generic', source='手动创建', tag='执行')
    sql_template = "select * from neptune_artifact_scan_task where id in (select task_id from neptune_artifact_scan_task_exec_his where task_id in (select id from neptune_artifact_scan_task where task_name ='lq-nexus-generic') and task_status = '1' order by trigger_time desc limit 1)"
    judge_task(sql_template, task_name)



