import numpy as np
import pandas as pd

## Import data
frames = []
file_name = 'total_raw'

for i in range(400):
    file_path = "data/" + str(file_name) + "." + str(i) + ".csv"
    df = pd.read_csv(file_path)
    frames.append(df)

df = pd.concat(frames)

dropped_cols = ['velocity:2', 'force:2', 'total displacement:2', 'coordinate:2', 'material', 'viscosity', 'effective viscosity',
       'elem number', 'mesh quality', 'node number']
df = df.drop(dropped_cols, axis=1)

df.to_csv("data/" + str(file_name) + "_concatenate.csv", index=False)

print('Finished saving data')