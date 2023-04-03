class GenericFile:
    def __init__(self, file_path, frequency):
        self.path = file_path
        self.freq = frequency

    def get_path(self):
        raise NotImplementedError("get_path not implemented")

    def get_freq(self):
        raise NotImplementedError("get_freq not implemented")
