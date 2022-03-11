def queue(A, q):
    result = []
    time = 0

    while A != []:
        if int(A[0][1]) <= q:
            a = A.pop(0)
            time += a[1]
            result.append([a[0], time])
        else:
            time += q
            A.append(A.pop(0))
            A[-1][1] -= q

    for i in result:
        print(*i)


if __name__ == "__main__":
    A = []
    N = list(input().split())
    for i in range(int(N[0])):
        tmp = input().split()
        tmp[1] = int(tmp[1]) 
        A.append(tmp)

    queue(A, int(N[1]))


    
"""
example answer is below
    
def parse(l):
name, time = l.split()
return (name, int(time))


n, q = map(int, input().split())
queue = list(parse(input()) for _ in range(n))
time = 0

while queue:
    (name, remain_time) = queue.pop(0)
    if remain_time > q:
        time += q
        queue.append((name, remain_time - q))
    else:
        time += remain_time
        print(name, time)

"""