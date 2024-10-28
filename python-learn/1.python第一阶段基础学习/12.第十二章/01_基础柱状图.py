

from  pyecharts.charts import Bar
from pyecharts import options as opts
#使用Bar构建基础柱状图
bar =Bar()
#添加x轴数据
bar.add_xaxis(["中国","美国","英国"])
#添加y轴数据
bar.add_yaxis("GDP",[30,20,10],labers_opts=opts.LabelOpts(position="right"))


#反转x,y轴方向
bar.reversal_axis()

bar.render("基础柱状图.html")
