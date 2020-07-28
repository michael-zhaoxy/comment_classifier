import pandas as pd
import numpy as np

df = pd.read_csv('../data/comment.csv')

with open('../data/comment.txt', 'w') as f:
    f.write('comment\r\n')
    for i in range(1000):
        com = str(df['content'][i])
        if len(com) >=5:
            f.write(com+'\r\n')


