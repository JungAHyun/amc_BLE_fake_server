import pandas as pd

# 읽어올 엑셀 파일 지정
filename = "아산병원_BLEScanner.xlsx"

# 엑셀 파일 읽어 오기
df = pd.read_excel(filename, engine="openpyxl", header=0)
print(df.iloc[:, 2:3])
