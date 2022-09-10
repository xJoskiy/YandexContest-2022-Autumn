import re


def isCorrect(braces):
    bal = 0
    for i in range(len(braces)):
        if braces[i] == '{':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal == 0


def main():
    expression = input()
    braces = re.sub(r'[^{}]', '', expression)
    stack, index = [], -1

    for i in range(len(expression)):
        if braces[i] == '{':
            stack.append('{')




if __name__ == '__main__':
    main()
