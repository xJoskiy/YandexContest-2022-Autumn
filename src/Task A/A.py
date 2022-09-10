def main():
    A, B = input(), input()
    total = {}
    string = [""] * len(A)
    for i in A:
        total[i] = total.get(i, 0) + 1

    for i in range(len(A)):
        if A[i] == B[i]:
            string[i] = "P"
            total[A[i]] = total.get(A[i], 0) - 1

    for i in range(len(A)):
        if not string[i]:
            if total.get(B[i], False):
                string[i] = "S"
                total[B[i]] = total.get(B[i], 0) - 1
            else:
                string[i] = "I"

    print(*string, sep='')


if __name__ == '__main__':
    main()