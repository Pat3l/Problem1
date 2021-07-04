import qrcode
from qrcode import constants

qr = qrcode.QRCode(
    version= None,
    error_correction= constants.ERROR_CORRECT_H,
    box_size= 10,
    border= 4,
    image_factory= None,
    mask_pattern= None
)

data = input("Enter an URL or Text to convert it into QR:")

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill = 'black', back_color = 'white')
img.save("qrcode1.png")