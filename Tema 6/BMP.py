from Binary import Binary


class BMP(Binary):
    def __init__(self, file_path, freq, width, height):
        super().__init__(file_path, freq)
        self.width = width
        self.height = height
        if height != 0:
            self.bpp = width/height
        else:
            self.bpp = 0

    def show_info(self):
        print("Width = " + self.width)
        print("Height = " + self.height)
        print("Bits per pixel = " + self.bpp)
