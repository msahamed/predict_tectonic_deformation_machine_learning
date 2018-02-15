import numpy as np
import pandas as pd

## Import data
frames = []
for i in range(400):
    file_name = "data/data."+ str(i) +".csv"
    df = pd.read_csv(file_name)
    frames.append(df)
    
df = pd.concat(frames)

dropped_cols = ['velocity:2', 'force:2', 'total displacement:2', 'coordinate:2', 'material', 'viscosity', 'effective viscosity',
       'elem number', 'mesh quality', 'node number']
df = df.drop(dropped_cols, axis=1)

df.to_csv("data/deviatoric_concatenate.csv", index=False)

print('Finished saving data')