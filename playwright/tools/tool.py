import pytest

from position.constants import ARTIFACT_MANAGEMENT_BUTTON, ARTIFACT_SCANNER_BUTTON, PLAN_BUTTON, TASK_BUTTON, \
    CVE_NUMBER_INPUT


# 进入制品扫描
def change_directory(page):
    # 点击制品管理
    page.click(ARTIFACT_MANAGEMENT_BUTTON)
    # 点击制品扫描
    page.wait_for_selector(ARTIFACT_SCANNER_BUTTON)
    page.click(ARTIFACT_SCANNER_BUTTON)


# 制品扫描选择tab页
def switch_tabs(page, tab):
    try:
        # 点击扫描方案tab
        if tab == '扫描方案':
            page.click(PLAN_BUTTON)
        elif tab == '扫描任务':
            page.click(TASK_BUTTON)
    except Exception as e:
        print(f"无法在指定时间内找到tab页面:{e}")
        pytest.fail("无法在指定时间内找到tab页面,停止测试")


def input_cve_number(page, num, txt):
    try:
        page.wait_for_selector(f"{CVE_NUMBER_INPUT}[{num}]")
        page.locator(CVE_NUMBER_INPUT).fill(txt)
    except Exception as e:
        print(f'输入第{num}个漏洞编号失败:{e}')
        pytest.fail(f'输入第{num}个漏洞编号失败，停止测试')
