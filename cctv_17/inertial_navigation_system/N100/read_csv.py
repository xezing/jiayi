import pandas as pd

"""
从csv文件中读取数据并计算里程
"""

def cal_distance_11(df,first):
    try:
        vt = 0
        distance = 0
        ax = 0

        for row in first.index.values:
            acc_x = float(df.iloc[row, 1]) + 0.04
            vt = vt + acc_x
            if (vt < 0 ):
                vt = 0
            distance = distance + vt
            ax = ax + acc_x

        print(distance)



    except Exception as e:
        print(e)
def cal_distance_12(df,first):
    try:
        vt = 0
        distance = 0
        ax = 0

        for row in first.index.values:
            acc_x = float(df.iloc[row, 4]) * -1 -0.03
            vt = vt + acc_x
            if (vt < 0 ):
                vt = 0
            distance = distance + vt
            ax = ax + acc_x

        print(distance)



    except Exception as e:
        print(e)

def get_ats():
    return 1
if __name__ == '__main__':
    if(get_ats() == 1):
        try:
            df1 = pd.read_csv(r'D:\workspace\jiayi\cctv_17\inertial_navigation_system\data_source\frakiss_diff(1).csv')
            first1 = df1.iloc[130:270]
            df2 = pd.read_csv(r'D:\workspace\jiayi\cctv_17\inertial_navigation_system\data_source\wait_for_analysis.csv')
            first2 = df2.iloc[385:525]
            cal_distance_11(df1,first1)
            cal_distance_12(df2,first2)
        except Exception as e:
            print(e)
        # cal_distance()
