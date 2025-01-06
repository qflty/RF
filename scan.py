from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from position.constants import ARTIFACT_MANAGEMENT_BUTTON, ARTIFACT_SCANNER_BUTTON, \
    ROGRAM_TAB, TASK_TAB, CVE_NUMBER_INPUT, SCAN_PLAN_SEARCH_ELE, SCAN_CLICK_SEARCH, CHOOSE_PLAN_NAME, \
    ENTER_KEYWORDS_IN_SEARCH_BOX, PRODUCT_TYPE_IN_SEARCH_BOX, TASK_SOURCE_IN_SEARCH_BOX


# 进入制品扫描
def change_directory(driver):
    # 点击制品管理
    driver.click(method=By.XPATH, locator=ARTIFACT_MANAGEMENT_BUTTON)
    driver.sleep(1)
    # 点击制品扫描
    driver.click(method=By.XPATH, locator=ARTIFACT_SCANNER_BUTTON)
    driver.sleep(1)


# 制品扫描选择tab页
def switch_tabs(driver, tab):
    try:
        # 点击扫描方案tab
        if tab == '扫描方案':
            driver.click(method=By.XPATH, locator=ROGRAM_TAB)
            driver.sleep(1)
        elif tab == '扫描任务':
            driver.click(method=By.XPATH, locator=TASK_TAB)
            driver.sleep(1)
    except NoSuchElementException:
        print("无法在指定时间内找到tab页面")


# 添加漏洞编号
def input_cve_number(driver, num, txt):
    driver.according_wait(method=By.XPATH, locator=f"{CVE_NUMBER_INPUT}[{num}]")
    try:
        driver.input(method=By.XPATH, locator=CVE_NUMBER_INPUT, text=txt)
    except:
        print(f'输入第{num}个漏洞编号失败')


# 扫描方案搜索框
def scan_plan_search(driver, txt):
    driver.input(method=By.XPATH, locator=SCAN_PLAN_SEARCH_ELE, text=txt)
    driver.click(method=By.XPATH, locator=SCAN_CLICK_SEARCH)


# 选择方案名称
def choose_plan(driver, plan_name):
    driver.click(method=By.XPATH, locator=CHOOSE_PLAN_NAME)
    try:
        driver.click(method=By.XPATH,
                     locator=f"//div[@class='v-modal']/../div/div/div/ul//li/span[contains(text(),'{plan_name}')]/..")
    except NoSuchElementException:
        print("该方案不存在")
    except Exception as e:
        print(f"choose_plan发生错误：{str(e)}")


# 选择制品类型
def choose_product_type(driver, product_type='Generic'):
    try:
        driver.click(method=By.XPATH,
                     locator=f"//label[contains(text(),'制品类型')]/../div/div/div/div/div[contains(text(),'{product_type}')]/..")
    except NoSuchElementException:
        print("该制品类型不存在")
    except Exception as e:
        print(f"choose_product_type发生错误：{str(e)}")


# 选择扫描范围
def choose_scan_scope(driver, scope='指定制品扫描'):
    try:
        driver.click(method=By.XPATH,
                     locator=f"//label[contains(text(),'扫描范围')]/../div/div/div/div/label/span[contains(text(),'{scope}')]/..")
    except NoSuchElementException:
        print("该扫描范围不存在")
    except Exception as e:
        print(f"choose_scan_scope发生错误：{str(e)}")


# 选择制品
def choose_product(driver, warehouse, product_name, version, product_path, position=1):
    try:  # 仓库名称
        driver.click(method=By.XPATH,
                     locator=f"(//div[contains(text(),'仓库名称')]/../../../../../../div[3])[2]/table/tbody/tr[{position}]/td[1]/div/div/div/div")
        driver.click(method=By.XPATH,
                     locator=f"//div[@class='v-modal']/../div/div/div/ul/li/span[contains(text(),'{warehouse}')]/..")
    except NoSuchElementException:
        driver.capture()
        print("该仓库不存在")
    except Exception as e:
        print(f"选择仓库发生错误：{str(e)}")
    try:  # 制品名称
        driver.click(method=By.XPATH,
                     locator=f"(//div[contains(text(),'仓库名称')]/../../../../../../div[3])[2]/table/tbody/tr[{position}]/td[2]/div/div/div/div")
        driver.click(method=By.XPATH,
                     locator=f"//div[@class='v-modal']/../div/div/div/ul/li/span[contains(text(),'{product_name}')]/..")
    except NoSuchElementException:
        driver.capture()
        print("该制品不存在")
    except Exception as e:
        print(f"选择制品发生错误：{str(e)}")
    try:  # 制品版本
        driver.click(method=By.XPATH,
                     locator=f"(//div[contains(text(),'仓库名称')]/../../../../../../div[3])[2]/table/tbody/tr[{position}]/td[3]/div/div/div/div")
        driver.click(method=By.XPATH,
                     locator=f"//div[@class='v-modal']/../div/div/div/ul/li/span[contains(text(),'{version}')]/..")
    except NoSuchElementException:
        driver.capture()
        print("该制品版本不存在")
    except Exception as e:
        print(f"选择版本发生错误：{str(e)}")
    try:  # 制品路径
        driver.click(method=By.XPATH,
                     locator=f"(//div[contains(text(),'仓库名称')]/../../../../../../div[3])[2]/table/tbody/tr[{position}]/td[4]/div/div/div/div")
        driver.click(method=By.XPATH,
                     locator=f"//div[@class='v-modal']/../div/div/div/ul/li/span[contains(text(),'{product_path}')]/..")
    except NoSuchElementException:
        driver.capture()
        print("该制品路径不存在")
    except Exception as e:
        print(f"选择路径发生错误：{str(e)}")


# 复制制品
def clone_product(driver, position=1):
    try:
        driver.click(method=By.XPATH, locator=f"(//div[contains(text(),'仓库名称')]/../../../../../../div[3])[2]/table/tbody/tr[{position}]/td[5]/div/div/div/div/a[1]")
        return position + 1
    except NoSuchElementException:
        driver.capture()
        print("该制品不存在")
    except Exception as e:
        print(f"clone_product发生错误：{str(e)}")


# 删除制品
def delete_product(driver, position=1):
    try:
        driver.click(method=By.XPATH,
                     locator=f"(//div[contains(text(),'仓库名称')]/../../../../../../div[3])[2]/table/tbody/tr[{position}]/td[5]/div/div/div/div/a[2]")
    except NoSuchElementException:
        driver.capture()
        print("该制品不存在")
    except Exception as e:
        print(f"delete_product发生错误：{str(e)}")


# 扫描任务搜索框
def scan_task_search(driver, task_name, task_source):
    try:
        # 点击来源框
        driver.click(method=By.XPATH, locator=TASK_SOURCE_IN_SEARCH_BOX)
        # 选择来源
        driver.click(method=By.XPATH, locator=f"//div[@id='z-index-manage']/../div/div/div/ul/li/span[contains(text(),'{task_source}')]/..")
        # 输入搜索框
        driver.input(method=By.XPATH, locator=ENTER_KEYWORDS_IN_SEARCH_BOX, text=task_name)
        # 点击查询
        driver.click(method=By.XPATH, locator=SCAN_CLICK_SEARCH)
    except NoSuchElementException:
        driver.capture()
        print("查询失败")
    except Exception as e:
        print(f"task_source_in_search_box发生错误：{str(e)}")


# 扫描任务点击编辑
def scan_task_click_edit(driver, task_name):
    try:
        driver.click(method=By.XPATH, locator=f"(//span[contains(text(),'{task_name}')]/../../../../td[10]/div/div/div/a/span[contains(text(),'编辑')]/..)[3]")
    except NoSuchElementException:
        driver.capture()
        print('扫描任务不存在')
    except Exception as e:
        print(f"scan_task_click_edit发生错误：{str(e)}")

