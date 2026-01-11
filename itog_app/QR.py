import qrcode


class QrCode:
    def __init__(self, link, images=None, qr=qrcode.QRCode(
        version=None,  # Размер QR-кода (от 1 до 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Уровень коррекции ошибок
        box_size=10,  # Размер одного "пикселя" QR-кода
    )):
        if images is None:
            self.images = []
        self.img = None
        self.link = link
        self.qr = qr

    def make_qr_img(self, fill_col="black", bg_col="white"):
        self.qr.add_data(self.link)
        self.qr.make(fit=True)
        self.img = self.qr.make_image(fill_color=fill_col, back_color=bg_col)  # Создаем изображение QR-кода
        self.images.append(self.img)

    def show_qrcode(self):
        self.images[-1].save("qrcode.png")
        self.images[-1].show(self.img)
        self.qr.clear()
        return "QR-код создан и сохранен как example_qr.png"