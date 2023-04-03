from TextASCII import TextASCII


class XMLFile(TextASCII):
    def __init__(self, file_path, freq, first_tag):
        super().__init__(file_path, freq)
        self.first_tag = first_tag

    def get_first_tag(self):
        return self.first_tag
    