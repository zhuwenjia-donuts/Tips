#pdfからcsvに変換するのに使う。ページ指定で1枚ずつしか一気に使えないです。
from tabula import wrapper
#pdfのページ数を数えるのに使う
import PyPDF2
import pandas as pd 

#任意のファイルパスをここに記載
FILE_PATH = "/Users/zhu.wenjia/PdfExtract/tabulaTest/rireki.pdf"
base_url = "/Users/zhu.wenjia/PdfExtract/tabulaTest/"
CSV_PATH = base_url + "rireki.csv"
wrapper.convert_into(FILE_PATH, CSV_PATH, pages="all", encoding = "cp932", output_format="csv")

"""
#ページ数を取得
with open(FILE_PATH, mode='rb') as f:
    pages = PyPDF2.PdfFileReader(f).getNumPages()

test_rireki = {}
#このデータフレームに全ページのデータを入れます
df = pd.DataFrame(test_rireki)  

#全ページのテーブルデータを一つのデータフレームに
for i in range(pages+1):
    base_url = "/Users/zhu.wenjia/PdfExtract/tabulaTest/"
    tmp = wrapper.read_pdf(FILE_PATH, pages = i, encoding = "utf-8_sig", spreadsheet=True, multiple_tables = True)
    df.to_csv( base_url + "rireki_" + str(i) + ".txt", index=None)
    print("Successfully Output Page" + str(i))
    print(tmp)
    # df.extend(tmp)
    # df = pd.concat([df, tmp], ignore_index=True)

#df.to_csv("/Users/zhu.wenjia/PdfExtract/tabulaTest/rireki.csv")
"""