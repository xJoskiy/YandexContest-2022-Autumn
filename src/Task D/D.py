def search(plan, x, y):
    if plan[x + 1][y] == '0':
        plan[x + 1] = plan[x + 1][:y] + 'U' + plan[x + 1][y + 1:]
        search(plan, x + 1, y)

    if plan[x - 1][y] == '0':
        plan[x - 1] = plan[x - 1][:y] + 'D' + plan[x - 1][y + 1:]
        search(plan, x - 1, y)

    if plan[x][y + 1] == '0':
        plan[x] = plan[x][:y + 1] + 'L' + plan[x][y + 2:]
        search(plan, x, y + 1)

    if plan[x][y - 1] == '0':
        plan[x] = plan[x][:y - 1] + 'R' + plan[x][y:]
        search(plan, x, y - 1)


def main():
    N, M = map(int, input().split())
    plan = [input().replace('.', '0') for _ in range(N)]

    start_x, start_y = 0, 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if plan[i][j] == 'S':
                start_x, start_y = i, j
    search(plan, start_x, start_y)

    print(*plan, sep="\n")


if __name__ == '__main__':
    main()
