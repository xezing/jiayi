# import pandas as pd
import os
import zipfile

for root, dirs, files in os.walk('/home/ap/ailog/log_storage/'):
    if len(files) == 0:
        continue
    else:
        for i in range(len(files)):
            dr = root + '/' + files[i]
            # df = pd.read_csv(dr)
            # df[['times']] = df[['times']].astype(int)
            # fd = df.sort_values('times', inplace=False)
            # fd.to_csv(dr, index=None)
            name = root + '/' + 'zpfile.zip'
            zp = zipfile.ZipFile(name, 'a', zipfile.ZIP_DEFLATED)
            zp.write(dr, arcname=files[i])
            zp.close()
            os.remove(dr)
