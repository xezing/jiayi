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
    folium.Marker(locations2[0], popup='<b>End Point</b>').add_to(m2)

    m1.save(os.path.join('../inertial_navigation_system/map', 'GPS.HTML'))  # 将结果以HTML形式保存到指定路径
    m2.save(os.path.join('../inertial_navigation_system/map', 'inertial_nav.HTML'))  # 将结果以HTML形式保存到指定路径


def get_location(path):
    sep = ','
    protocal = '$GPRMC'
    list_c = [3, 5]
    location = list(list())

    with open(path, 'r', encoding='utf-8') as fp:

        for line in fp.readlines():
            split_line = line.strip().split(sep)
            data = list()
            if split_line[0] == protocal:
                lat = calc_gps_pos(split_line[3])
                lon = calc_gps_pos(split_line[5])
                if lat != '' and lon != '':
                    # data.append(float(lat) / 100 + 0.0696629999999985)
                    data.append(lat)
                    # data.append(float(lon) / 100 + 0.17116)
                    data.append(lon)
                    # print(data)
                    location.append(data)
        # print(location)
    return location


def get_location_win(path):
    sep = ','
    location = list(list())
    with open(path, 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            split_line = line.strip().split(sep)
            data = list()
            # lat = calc_gps_pos(split_line[6])
            # lon = calc_gps_pos(split_line[5])
            # lat = float(split_line[1]) + 0.0003
            # lon = float(split_line[0]) - 0.00741
            lat = float(split_line[3])
            lon = float(split_line[2])
            if lat != '' and lon != '':
                # data.append(float(lat) / 100 + 0.0696629999999985)
                data.append(lat)
                # data.append(float(lon) / 100 + 0.17116)
                data.append(lon)
                # print(data)
                location.append(data)
        # print(location)
    return location


def cal_displacement():
    return 0


def calc_gps_pos(gps_info):
    gps_degree = int(float(gps_info) / 100)
    gps_cent = float(gps_info) - gps_degree * 100.0
    gps_value = gps_degree + gps_cent / 60.0
    return gps_value


file1 = r'../inertial_navigation_system/data_source/gps_092915.txt'
# file2 = r'../inertial_navigation_system/data_source/WTGPS-300_2021-09-29-15-05-48-8808.txt'
file2 = r'../inertial_navigation_system/data_source/line_14.csv'

location_1 = get_location(file1)
location_2 = get_location_win(file2)
#
# l1 = [l2 for l in location_1 for l2 in l]
# l2 = [l4 for l3 in location_2 for l4 in l3]
#
# print(len(l1))
# print(len(l2))
#
# union = set(l1) & set(l2)
# print(len(union))
# print(union)
draw_gps(location_2, location_2, 'red', 'red')
# print(location_1)
print(location_2)