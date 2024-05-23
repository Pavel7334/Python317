# pip install qrcode

import qrcode

imghdr = qrcode.make("Hello World")
imghdr.save("qrcode.png")
