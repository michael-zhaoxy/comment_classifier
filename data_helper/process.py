import pandas as pd
import numpy as np
import jieba

# df = pd.read_csv('../data/comment.txt', delimiter=' ')
str = jieba.cut("要是有字幕就好了,可以学习了")
for _ in str:
    print(_)
