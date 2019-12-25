from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re 

def gettext(pdfname,txtname):
    # PDFファイル名が未指定の場合は、空文字列を返して終了
    if (pdfname == ''):
        return ''
    else:
        # 処理するPDFファイルを開く/開けなければ
        try:
            fp = open(pdfname, 'rb')
        except:
            return ''
        
    # リソースマネージャインスタンス
    rsrcmgr = PDFResourceManager()
    # 出力先インスタンス
    outfp = StringIO()
    # パラメータインスタンス
    laparams = LAParams()
    # 縦書き文字を横並びで出力する
    laparams.detect_vertical = True
    # デバイスの初期化
    device = TextConverter(rsrcmgr, outfp, laparams=laparams)
    # テキスト抽出インタプリタインスタンス
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # 対象ページを読み、テキスト抽出する。（maxpages：0は全ページ）
    for page in PDFPage.get_pages(fp, pagenos=None, maxpages=0, password=None,caching=True, check_extractable=True):
        interpreter.process_page(page)
    #取得したテキストをすべて読みだす
    ret = outfp.getvalue()
    # 後始末をしておく    
    fp.close()
    device.close()
    outfp.close()
    # 空白と改行をとりさり一塊のテキストとして返す
    ret = re.sub(r"\s|　",'',ret)
    file = open(txtname, 'w')  #書き込みモードでオープン
    file.write(ret)
    return ret


# File path
FILE_PATH = "/Users/zhu.wenjia/PdfExtract/pdfminerTest/rireki.pdf"
base_url = "/Users/zhu.wenjia/PdfExtract/pdfminerTest/"
TXT_PATH = base_url + "rireki.txt"
result = gettext(FILE_PATH, TXT_PATH)
print(result)