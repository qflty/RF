# 定义常量，使用大写字母和下划线命名
# 测试环境 --------------------
# 数据库连接
# pgsql
pg_test_user = 'postgres'
pg_test_password = 'Cubeinfo_2024'
pg_test_host = '172.28.38.22'
pg_test_port = 5432
pg_test_database = "mantis"
# mysql
my_test_user = 'tst_tu_5df5682'
my_test_password = 'tst_tu_5df5682_3a6c4c'
my_test_host = 'rm-bp106y19fa3992tt9613.mysql.rds.aliyuncs.com'
my_test_port = 3306
my_test_database = 'tech_magic_base_t_00'
# 环境地址
URL_TEST = "http://cube-front.product.poc.za-tech.net"
# 账号
USERNAME_LOCATER = "username"
USERNAME = "admin"
# 密码
PASSWORD_LOCATER = "temppassword"
PASSWORD = "Admin@2024"
# 登录按钮
LOGIN_BUTTON = "login-btn"
# 登录后弹窗
BUTTON1 = "//span[contains(text(),'我知道了')]"
BUTTON2 = "//span[contains(text(),'工作台')]"
# 用户名称
USER_BUTTON = "(//span[contains(text(),'梅')]/..)[1]"
LOGOUT_BUTTON = "//span[contains(text(),'登出')]/.."
# 菜单
ARTIFACT_MANAGEMENT_BUTTON = "//li[@name='制品管理']"
ARTIFACT_SCANNER_BUTTON = "//li[@name='制品管理']/ul/li[@name='制品扫描']"
# 制品扫描定位：扫描方案 ---------------------------------------
# 制品扫描tab页
ROGRAM_TAB = "//div[contains(text(),'制品扫描')]/../li/span[contains(text(),'扫描方案')]/.."
TASK_TAB = "//div[contains(text(),'制品扫描')]/../li/span[contains(text(),'扫描任务')]/.."
# 创建按钮
CREATE_BUTTON = "//*[@id='app']/div/section/div/main/div/div[1]/div[1]/button"
# 方案名称
PLAN_NAME_LOCATER = "//label[contains(text(),'方案名称')]/../div/div/div/input"
# 设为默认
STE_DEFAULT = "//label[contains(text(),'设为默认')]/../div/div/div/span"
# 方案描述
PLAN_DESCRIPTION_INPUT = "//label[contains(text(),'描述')]/../div/div/div/textarea"
# 添加按钮
ADD_BUTTON = "//span[contains(text(),'添加')]/.."
# 导入编号按钮
INPORT_NUMBER_BUTTON = "//span[text()=' 导入编号 ']/.."
# 导入编号文件
IMPORT_NUMBER_FILE_lOCATER = "//input[@type='file']"
# 漏洞编号文件
VULNERABILITY_NUMBER_FILE = "D:\下载\文档下载\漏洞白名单模板.xlsx"
# 导入编号确定按钮
IMPORT_NUMBER_CONFIRM_BUTTON = "//div[2]/div/div[2]/button[2]"
# 输入漏洞编号
CVE_NUMBER_INPUT = "//*[@placeholder='请输入内容']"
# 确定按钮
PLAN_CONFIRM_BUTTON = "//*[@id='app']/div/section/div/main/div/div[2]/div/div/section/div/div[3]/button[2]"
# 扫描方案搜索框
SCAN_PLAN_SEARCH_ELE = "//input[@placeholder='请输入方案名称搜索']"
# 点击查询
SCAN_CLICK_SEARCH = "//span[contains(text(),'查询')]/.."
# 点击编辑扫描方案
EDIT_SCANNER_PLAN = "//*[@id='app']/div/section/div/main/div/div[1]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/div/a[1]"
# 点击删除扫描方案
DELETE_SCANNER_PLAN = "//*[@id='app']/div/section/div/main/div/div[1]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/div/a[2]"
# 删除弹窗
DELETE_CONFIRM = "//*[contains(text(), '确定删除当前方案吗')]"
# 删除方案点击确定
DELETE_PLAN_CONFIRM_BUTTON = "//*[contains(text(), '确 定')]/.."
# 创建扫描任务页面
CREATE_TASK = "//*[contains(text(),'创建扫描任务')]"
# 所属节点
BELONGING_NODE = "//label[contains(text(), '所属节点')]/../div/div"
# 选择节点-test-nexus
CHOOSE_NODE = "//span[contains(text(),'test-nexus')]/.."
# 方案名称
CHOOSE_PLAN_NAME = "//label[contains(text(),'方案名称')]/../div/div/div/div"
# 任务名称
SCAN_TASK_NAME = "//label[contains(text(),'任务名称')]/../div/div/div/input"
# 质量门禁
QUALITY_CONTROL = "//label[contains(text(),'质量门禁')]/../div/div/div"
# 严重等级
SERIOUS_LEVEL = "//span[contains(text(),'严重')]/../../../../../td[3]/div/div/div/div/div/input"
# 高危等级
HIGH_RISK_LEVEL = "//span[contains(text(),'高危')]/../../../../../td[3]/div/div/div/div/div/input"
# 中危等级
MODERATE_RISK_LEVEL = "//span[contains(text(),'中危')]/../../../../../td[3]/div/div/div/div/div/input"
# 低危等级
LOW_RISK_LEVEL = "//span[contains(text(),'低危')]/../../../../../td[3]/div/div/div/div/div/input"
# 未定级等级
UNRATED_LEVEL = "//span[contains(text(),'未定级')]/../../../../../td[3]/div/div/div/div/div/input"
# 仅保存按钮
SAVE_ONLY_BUTTON = "//span[contains(text(),'仅保存')]/.."
# 保存并立即执行
SAVE_AND_EXECUTE_BUTTON = "//span[contains(text(),'保存并立即执行')]/.."
# 搜索框任务来源
TASK_SOURCE_IN_SEARCH_BOX = "//input[@placeholder='请选择任务来源']"
# 搜索框输入关键字
ENTER_KEYWORDS_IN_SEARCH_BOX = "//input[@placeholder='请输入任务名称、仓库名称搜索']"
# 搜索框制品类型
PRODUCT_TYPE_IN_SEARCH_BOX = "//input[@placeholder='请选择制品类型']"
