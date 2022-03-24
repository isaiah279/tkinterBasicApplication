"""#Import Library
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://abhijithchandradas.medium.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("medium.png")"""


class Mainclass():
    def __init__(self, name, student, age):
        self.name = name
        self.student = student
        self.age = age

    def members(self):
        print(self.name, self.student)


d1 = Mainclass('name', 45, 56)
print(d1.members())


