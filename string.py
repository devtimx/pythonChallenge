# in process, replace characters of a string 
def run():
    text = input('num1: ')
    a="M"
    b="N"
    textM=[pos for pos, char in enumerate(text) if char == a]
    print(textM)
    textN=[pos for pos, char in enumerate(text) if char == b]
    print(textN)

if __name__ == "__main__":
    run()