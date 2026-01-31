import qrcode
import json
from itog_project import settings

import os
a = 0


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

        global a
        a += 1
        self.save_qr_to_static()

    def save_qr(self):
        global a
        save_path = os.path.join(settings.MEDIA_ROOT)
        self.images[-1].save(f"qr.png{a}")


    def show_qrcode(self):
        self.images[-1].show(self.img)
        self.qr.clear()
        global a
        print(f"QR-код создан и сохранен как qr.png{a}")


    def save_qr_to_static(qr_instance):
        """Сохраняет QR-код из экземпляра класса в папку static"""
        global a

        if not qr_instance.images:
            print("Нет изображений для сохранения!")
            return None

        static_dir = os.path.join(settings.BASE_DIR, 'static')
        os.makedirs(static_dir, exist_ok=True)

        static_filename = f"qr_{a}.png"
        full_static_path = os.path.join(static_dir, static_filename)
        qr_instance.images[-1].save(full_static_path)
        data_json_path = os.path.join(settings.BASE_DIR, 'static', 'data.json')
        data = {"value": a}

        with open(data_json_path, 'w') as f:
            json.dump(data, f)

        print(f"QR-код сохранен в static как: {full_static_path}")
        print(f"data.json сохранен в: {data_json_path}")
