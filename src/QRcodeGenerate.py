import qrcode

def generate_code_qr(URL):
    img = qrcode.make(URL)
    img.save('./res/qr-code.png')
