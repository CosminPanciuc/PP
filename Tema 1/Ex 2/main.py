
if __name__ == '__main__':

    f = open("data.txt", "r")
    modif = f.read()
    for punct in [".", ",", "?", "!", "-", "_", ":", ";", "/", "(", ")", "'", '"']:
        modif = modif.replace(punct, "")
    print(modif)
    modif = modif.upper()
    print(modif,end="")
    f.close()
