import pandas as pd

wt = pd.read_csv('../data_source/wait_for_analysis.csv')
fk = pd.read_csv('../data_source/frakiss_diff(1).csv')
wt = wt.loc[385:525]
fk = fk.loc[130:270]

mean_wt = wt.loc[wt.vt == 0, 'ac_x'].mean()
wt_run = wt.loc[wt.vt != 0]
wt_run['tran_a'] = wt_run.ac_x - mean_wt
wt_run['speed'] = wt_run.tran_a.cumsum()
wt_run['long'] = wt_run.speed.cumsum()

mean_fk = fk.loc[fk.speed_r == 0, 'ac_x'].mean() + 0.058
fk_run = fk.loc[fk.speed_r != 0]
fk_run['tran_a'] = fk_run.ac_x - mean_fk
fk_run['speed'] = fk_run.tran_a.cumsum()
fk_run['long'] = fk_run.speed.cumsum()
print()