
def _print(txt):
    return txt.capitalize()

def hprint(txt="hello"):
    print _print(txt) + " World"

if __name__ == '__main__':
    hprint()
