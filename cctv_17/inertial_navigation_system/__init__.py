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
    protocal = '$GNVTG'
    count = 0
    # data = list()
    with open(file, 'r') as fp:
        for line in fp.readlines():
            split_line = line.strip().split(sep)
            if split_line[0] == protocal:
                print('协议：', split_line[0], 'Sog=', split_line[5], 'kph=', split_line[7], 'time =', count/60)
                count = count + 1
        print(count)
