import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\dell\AppData\Local\Tesseract-OCR\tesseract.exe"   

def getText(img):
    txt = pytesseract.image_to_string(img, lang='eng')
    return txt