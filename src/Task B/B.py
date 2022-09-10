def main():
    n = int(input())
    total = {discipline: {"max": int(max_people), "people": []} for _ in range(n) for discipline, max_people in [input().split(',')]}

    k = int(input())
    for _ in range(k):
        name, discipline, stunts, penalty = input().split(',')
        total[discipline].setdefault("people").append([name, int(stunts), int(penalty)])

    print(total)
    for discipline in total.values():
        finalists = sorted(discipline["people"], key=lambda x: (x[1], -x[2]))
        print(finalists[discipline["max"]::-1])


if __name__ == '__main__':
    main()

