from pyecharts.charts import Bar
from pyecharts import options as opts


# 创建一个柱状图对象
bar = Bar()

# 添加X轴数据
bar.add_xaxis(['衬衣', '毛衣', '领带', '裤子', '风衣', '高跟鞋', '袜子'])

# 添加Y轴数据（商家A的销售情况）
bar.add_yaxis('商家A', [114, 55, 27, 101, 125, 27, 105])

# 设置全局配置项，如标题
bar.set_global_opts(title_opts=opts.TitleOpts(title='某商场销售情况'))

# 渲染图表并保存为HTML文件
bar.render('sales_bar_chart.html')
