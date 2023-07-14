import qrcode
from PIL import Image

def generate_qr_code(information, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(information)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

information = "Jeewan Rai, Associate Analysis, Drive Division, InnoTech Department"
filename = "test.png"
generate_qr_code(information, filename)

