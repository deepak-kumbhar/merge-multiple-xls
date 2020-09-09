import os
import xlwt
import pandas as pd

#files are in same directory
cwd = os.path.abspath('')
files = os.listdir(cwd)

df = pd.DataFrame()

for file in files:
    if file.endswith('.xls'):
        df = df.append(pd.read_excel(file), ignore_index=True)

df.to_excel('total_report.xls')