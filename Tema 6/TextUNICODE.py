from GenericFile import GenericFile


class TextUNICODE(GenericFile):

    def __init__(self, file_path, freq):
        super().__init__(file_path, freq)

    def get_path(self):
        return self.path

    def get_freq(self):
        return self.freq
