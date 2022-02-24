def run():
    text = input('string: ').lower()
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    n = []
    for i in text:
        if i in alphabet:
            n.append(alphabet.index(i)+1)
        else:
            n.append(i)
    cadena = "".join([str(_) for _ in n])
    print(cadena)

if __name__ == "__main__":
    run()