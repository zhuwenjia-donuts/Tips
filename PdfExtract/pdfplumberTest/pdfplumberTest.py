import pdfplumber
import pandas as pd

# File path
FILE_PATH = "/Users/zhu.wenjia/PdfExtract/pdfplumberTest/rireki.pdf"
base_url = "/Users/zhu.wenjia/PdfExtract/pdfplumberTest/"
CSV_PATH = base_url + "rireki.csv"

with pdfplumber.open(FILE_PATH) as pdf:
    page = pdf.pages[0]   # fist page
    table = page.extract_tables()
    for t in table:
        df = pd.DataFrame(t[1:], columns=t[0])
        # print(df)

df.to_csv("/Users/zhu.wenjia/PdfExtract/pdfplumberTest/rireki01.csv")

with pdfplumber.open(FILE_PATH) as pdf:
    page = pdf.pages[1]   # second page
    table = page.extract_tables()
    for t in table:
        df = pd.DataFrame(t[1:], columns=t[0])
        # print(df)

df.to_csv("/Users/zhu.wenjia/PdfExtract/pdfplumberTest/rireki02.csv")