from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 初始化选项，选择主题，这里选择了LIGHT主题
pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

# 添加数据和标签
pie.add(series_name='测试执行结果',
        data_pair=[('用例1', 10), ('用例2', 20), ('用例3', 30), ('用例4', 40)],
        radius=["30%", "70%"])  # 设置饼图的内外半径，这里内半径为30%，外半径为70%

# 设置全局配置，例如标题
pie.set_global_opts(title_opts=opts.TitleOpts(title='饼图示例', subtitle="这是一个简单的饼图"))

# 渲染图表并保存为HTML文件
pie.render('test.html')

