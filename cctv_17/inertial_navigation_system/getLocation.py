def get_location(path):
    sep = ','
    protocal = '$GPRMC'
    list_c = [3, 5]
    location = list(list())

    with open(path, 'r', encoding='utf-8') as fp:

        for line in fp.readlines():
            split_line = line.strip().split(sep)
            data = list()
            lat = split_line[6]
            lon = split_line[5]
            if lat != '' and lon != '':
                # data.append(float(lat) / 100 + 0.0696629999999985)
                data.append(float(lat) / 100)
                # data.append(float(lon) / 100 + 0.17116)
                data.append(float(lon) / 100)
                # print(data)
                location.append(data)
        # print(location)
    return location


file2 = r'../inertial_navigation_system/data_source/WTGPS-300_2021-09-29-15-05-48-8808.txt'

location_1 = get_location(file2)
for e in location_1:
    print(e)
