# -*- encoding: utf-8 -*-

"""
惯导数据速度与时间提取
"""


def get_active_speed():
    return None


def get_active_time():
    return None


def cal_displacement():
    return None


if __name__ == '__main__':
    file = r'../inertial_navigation_system/data_source/pure_guandao_data_0927.txt'
    sep = ','
    speed_protocal = '$GNVTG'
    time_protocal = '$GNZDA'
    count = 0

    with open(file, 'r') as fp:
        data = list()
        for line in fp.readlines():
            split_line = line.strip().split(sep)
            if split_line[0] == speed_protocal:
                # print('协议：', split_line[0], 'Sog=', split_line[5], 'kph=', split_line[7])
                for i in [0, 5, 7]:
                    data.append(split_line[i])
                count += float(split_line[7]) / 60 / 60
            # count = count + 1
            if split_line[0] == time_protocal:
                for i in [0, 4, 3, 2, 1]:
                    data.append(split_line[i])
            # print('日期：', split_line[4], '年', split_line[3], '月', split_line[2], '日')
            if len(data) != 0 and len(data) % 8 == 0:
                print(data)
            if len(data) % 8 == 0:
                data.clear()
    print(count)
