from tabula import wrapper
import PyPDF2
import pandas as pd 

# File path
FILE_PATH = "/Users/zhu.wenjia/PdfExtract/tabulaTest/rireki.pdf"
base_url = "/Users/zhu.wenjia/PdfExtract/tabulaTest/"
CSV_PATH = base_url + "rireki.csv"
# エンコード指定は効かない
wrapper.convert_into(FILE_PATH, CSV_PATH, pages="all", encoding = "cp932", output_format="csv")

"""
#　Get num of Pages
with open(FILE_PATH, mode='rb') as f:
    pages = PyPDF2.PdfFileReader(f).getNumPages()

# Initialise
test_rireki = {}
df = pd.DataFrame(test_rireki)  

# Extract for each page and then cancat them
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