def insertion_sort(A, N):
    for i in range(N):
        tmp = A[i]
        j = i -1

        while j >= 0 and A[j] > tmp:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = tmp
        print(" ".join(map(str, A)))

if __name__ == "__main__":
    N = int(input()) #the number of elements in the sequence
    A = list(map(int, input().split())) #N elements of the sequence are given separated by a single space
    insertion_sort(A, len(A))