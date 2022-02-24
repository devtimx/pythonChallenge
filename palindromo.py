# checks if a string is a palindrome
def run():
    myText = input('Enter your text: ')
    reverse_txt = myText[::-1]
    if myText.replace(" ","").lower() == reverse_txt.replace(" ","").lower():
        result= print("is palindromo")
    else:
        result= print("no is palindromo")
    return result

if __name__ == "__main__":
    run()