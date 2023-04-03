import imghdr
import os

from BMP import BMP
from Binary import Binary
from TextASCII import TextASCII
from TextUNICODE import TextUNICODE

import xml.etree.ElementTree as Et

from XMLFile import XMLFile

#tree = et.parse('Input.xml')
#root = tree.getroot()

if __name__ == '__main__':
    ASCII = []
    UNICODE = []
    Bin = []
    xmlFormat = []
    BitMap = []
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    for root, subdirs, files in os.walk(ROOT_DIR):
        for file in os.listdir(root):

            file_path = os.path.join(root, file)

            if os.path.isfile(file_path):
                # deschide fișierul spre acces binar
                f = open(file_path, 'rb')

                try:
                    # în content se va depune o listă de octeți
                    content = f.read()

                    frequency = [0] * 256

                    for byte in content:
                        frequency[byte] = frequency[byte] + 1

                    freqASCIImare = sum(frequency[9:10]) + frequency[13] + sum(frequency[32:127])
                    freqASCIImici = sum(frequency[0:8]) + sum(frequency[11:12]) + sum(frequency[15:31]) + sum(frequency[128:255])
                    freqTotal = sum(frequency[0:255])
                    if freqTotal != 0:
                        if freqASCIImare/freqTotal >= 0.9 and freqASCIImici/freqTotal <= 0.1:
                            split = os.path.splitext(file)
                            if split[1] == '.xml':
                                tree = Et.parse(file_path)
                                troot = tree.getroot()
                                xmlFormat.append(XMLFile(file_path, frequency, troot))
                            else:
                                ASCII.append(TextASCII(file_path, frequency))

                        elif frequency[0]/freqTotal >= 0.3:
                            UNICODE.append(TextUNICODE(file_path, frequency))

                        else:
                            BitMap.append(BMP(file_path, frequency, int.from_bytes(content[18:21], byteorder='little'),
                                          int.from_bytes(content[22:25], byteorder='little')))

                finally:
                    f.close()

    for i in BitMap:
        print(i.get_path())
#        i.show_info()

    for i in xmlFormat:
        print(i.get_path())
        print(i.get_first_tag())
#    for i in UNICODE:
#        print(i.get_path())
