import folium
import os


def draw_gps(locations1, locations2, color1, color2):
    """
    绘制gps轨迹图
    :param locations: list, 需要绘制轨迹的经纬度信息，格式为[[lat1, lon1], [lat2, lon2], ...]
    :param output_path: str, 轨迹图保存路径
    :param file_name: str, 轨迹图保存文件名
    :return: None
    """
    m1 = folium.Map(locations1[0], zoom_start=15, attr='default')  # 中心区域的确定
    m2 = folium.Map(locations2[0], zoom_start=15, attr='default')  # 中心区域的确定

    folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        locations1,  # 将坐标点连接起来
        weight=3,  # 线的大小为3
        color=color1,  # 线的颜色为橙色
        opacity=0.8  # 线的透明度
    ).add_to(m1)  # 将这条线添加到刚才的区域m内

    folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        locations2,  # 将坐标点连接起来
        weight=3,  # 线的大小为3
        color=color2,  # 线的颜色为橙色
        opacity=0.8  # 线的透明度
    ).add_to(m2)  # 将这条线添加到刚才的区域m内

    # 起始点，结束点
    folium.Marker(locations1[0], popup='<b>Starting Point</b>').add_to(m1)
    folium.Marker(locations2[-1], popup='<b>End Point</b>').add_to(m2)

    m1.save(os.path.join('D://', '12.HTML'))  # 将结果以HTML形式保存到指定路径
    m2.save(os.path.join('D://', '21.HTML'))  # 将结果以HTML形式保存到指定路径


def get_location():
    file = r'../inertial_navigation_system/data_source/0928GPS.txt'
    sep = ','
    protocal = '$GPRMC'
    list_c = [3, 5]
    location = list(list())

    with open(file, 'r', encoding='utf-8') as fp:

        for line in fp.readlines():
            split_line = line.strip().split(sep)
            data = list()
            if split_line[0] == protocal:
                lat = split_line[3]
                lon = split_line[5]
                if lat != '' and lon != '':
                    # data.append(float(lat) / 100 + 0.0696629999999985)
                    data.append(float(lat) / 100)
                    # data.append(float(lon) / 100 + 0.17116)
                    data.append(float(lon) / 100)
                    # print(data)
                    location.append(data)
        print(location)
    return location


location_x = get_location()

draw_gps(location_x, location_x, 'red', 'orange')
