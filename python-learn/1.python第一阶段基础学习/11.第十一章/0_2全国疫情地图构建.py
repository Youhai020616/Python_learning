
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts
from pyecharts.options import *

#读取数据文件
f = open("D:/百度网盘/Baidu_Downloads/资料/可视化案例数据/地图数据/疫情.txt","r",encoding="utf-8")
data = f.read()
#关闭文件
f.close()

#取到各个省份数据
#将字符串json转换为python字典
data_dict = json.loads(data)
#从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]

#组装省份和确诊人数数据为元组，并将各个省份数据进行封装到列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name,province_confirm))



#创建地图对象
map = Map()
#添加数据
map.add("各个省份确诊人数",data_list,"china")
#设置全局变量
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#ccffff"},
            {"min":100,"max":999,"label":"100-9999","color":"#ffff99"},
            {"min":1000,"max":4999,"label":"1-99","color":"#ff9966"},
            {"min":5000,"max":9999,"label":"1-99","color":"#ff6666"},
            {"min":10000,"max":99999,"label":"1-99","color":"#cc3333"},
            {"min":100000,"label":"100000+","color":"#990033"},
        ]
    )
)

map.render("全国疫情地图.html")