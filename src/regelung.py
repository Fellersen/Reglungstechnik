from pedantic import pedantic


@pedantic
def addieren(a: int, b: int) -> int:
    return a+b


if __name__ == '__main__':
    print("Hello World! Marco")
    print(addieren(a=1, b=9))
