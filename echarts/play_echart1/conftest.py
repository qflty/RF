import json
import pytest
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from playwright.sync_api import sync_playwright


# 定义一个浏览器实例的 fixture，其作用范围为整个模块
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
        yield browser
        browser.close()


# 定义一个浏览器页面的 fixture，其作用范围为每个测试函数
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def pytest_sessionfinish(session, exitstatus):
    # 从 session 对象上获取 results_file 路径
    results_file_path = session.results_file_path
    try:
        # 读取并处理结果文件
        with open(results_file_path, 'r') as f:
            results = json.load(f)
        print(f"测试会话结束后的最终结果：{results}")
        success_count = results['success']
        failure_count = results['failure']
        # 创建柱状图
        bar = Bar()
        bar.add_xaxis(['成功', '失败'])
        bar.add_yaxis('测试结果', [success_count, failure_count])
        bar.set_global_opts(title_opts=opts.TitleOpts(title='登录测试结果'))
        # 渲染图表并保存为HTML文件
        bar.render('login_test_results1.html')

        # 创建饼图
        pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        # 添加数据和标签
        pie.add(series_name='测试执行结果',
                data_pair=[('成功', success_count), ('失败', failure_count)],
                radius=["30%", "70%"])  # 设置饼图的内外半径，这里内半径为30%，外半径为75%
        # 设置全局配置，例如标题
        pie.set_global_opts(title_opts=opts.TitleOpts(title='登录测试', subtitle="这是一个简单的饼图"))
        # 渲染图表并保存为HTML文件
        pie.render('login_test_results2.html')

    except FileNotFoundError:
        print(f"结果文件 {results_file_path} 未找到")
    except json.JSONDecodeError:
        print(f"无法解析结果文件 {results_file_path} 中的JSON数据")
    except Exception as e:
        print(f"处理结果文件时发生错误: {e}")

