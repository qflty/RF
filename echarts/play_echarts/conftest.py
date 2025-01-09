import json
from pyecharts.charts import Bar
from pyecharts import options as opts


def pytest_sessionfinish(session, exitstatus):
    # 从 session 对象上获取 results_file 路径
    results_file_path = session.results_file_path
    # 读取并处理结果文件
    with open(results_file_path, 'r') as f:
        results = json.load(f)
    print(f"测试会话结束后的最终结果：{results}")
    success_count = results['success']  # 直接访问字典中的值
    failure_count = results['failure']
    # 创建柱状图
    bar = Bar()
    bar.add_xaxis(['成功', '失败'])
    bar.add_yaxis('测试结果', [success_count, failure_count])
    bar.set_global_opts(title_opts=opts.TitleOpts(title='登录测试结果'))
    # 渲染图表并保存为HTML文件
    bar.render('login_test_results.html')
