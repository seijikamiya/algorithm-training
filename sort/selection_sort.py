def selection_sort(A):
    count = 0
    for i in range(len(A)):
        min = i

        for j in range(min, len(A)):
            if A[min] > A[j]:
                min = j
        
        if i != min:
            A[i], A[min] = A[min], A[i]
            count += 1

    print(" ".join(map(str, A)))
    print(count)


def main():
    N = int(input()) #the number of elements in the sequence
    A = list(map(int, input().split())) #N elements of the sequence are given separated by a single space
    selection_sort(A)

if __name__ == "__main__":
    main()