def stack(A):
    list = []
    for i in A:
        if i.isdigit():
            list.append(int(i))
        else:
            b = list.pop()
            a = list.pop()

            if i == "+":
                list.append(a + b)
            elif i == "-":
                list.append(a - b)
            else:
                list.append(a * b)

    return list[0]

if __name__ == "__main__":
    A = list(input().split())
    print(stack(A))
