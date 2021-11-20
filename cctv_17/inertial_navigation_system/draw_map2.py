import folium
import webbrowser

## 初始化地图，指定上海市
m = folium.Map(
    location=[31.2389, 121.4992],
    zoom_start=12,
    # tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}', # 高德街道图
    tiles='http://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',  # 高德卫星图
    # tiles='https://mt.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', # google 卫星图
    # tiles='https://mt.google.com/vt/lyrs=h&x={x}&y={y}&z={z}', # google 地图
    attr='default'
)

# # 添加marker到地图
# folium.Marker([31.2453, 121.4857], popup='123', tooltip='tooltip', icon=folium.Icon(color='red')).add_to(m)
# folium.Marker([31.2418, 121.4953], popup='456', tooltip='tooltip',
#               icon=folium.Icon(color='green', icon='info-sign')).add_to(m)


# 标记一个实心圆
# folium.CircleMarker(
#     location=[31.2453, 121.4857],
#     radius=100,
#     popup='popup',
#     color='#DC143C',  # 圈的颜色
#     fill=True,  # 是否填充
#     fill_color='#6495ED'  # 填充颜色
# ).add_to(m)

folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
    locations=[[31.263543-0.00055,121.294789-0.006345],[31.27291-0.006055,121.291285-0.006345]],  # 将坐标点连接起来
    weight=3,  # 线的大小为3
    color='red',  # 线的颜色为橙色
    opacity=0.8  # 线的透明度
).add_to(m)  # 将这条线添加到刚才的区域m内

m.save('f1.html')
webbrowser.open('f1.html')
