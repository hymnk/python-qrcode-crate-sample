import qrcode
import os

url = "https://github.com/hymnk/python-qrcode-create-sample"
output_dir = "results"
output_img_filename = "qr.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

qr_code_path = output_dir + "/" + output_img_filename
img.save(qr_code_path)
