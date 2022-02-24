# calculate the factorial of a given number
def run():
    num = int(input('Enter number: '))
    i=1
    while num > 1:
        i *=num
        num -=1
    print(i)


if __name__ == "__main__":
    run()