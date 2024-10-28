#读取文件
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("D:/百度网盘/Baidu_Downloads/资料/可视化案例数据/地图数据/疫情.txt","r",encoding="utf-8")
data =f.read()
#关闭文件
f.close()

#获取河南省数据
data_dict =json.loads(data)
#提取河南省数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]


#准备数据构建元组并放入list中
data_list = []
for city_data in cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm))




data_list.append(("济源市",5))

#构建地图


map = Map()
map .add("河南省疫情地图",data_list, maptype="河南")

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

#绘图
map.render("河南省疫情地图.html")