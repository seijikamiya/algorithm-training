def bubble_sort(A):

    count = 0

    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):    
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                count += 1

    print(" ".join(map(str, A)))
    print(count)

def main():
    N = int(input()) #the number of elements in the sequence
    A = list(map(int, input().split())) #N elements of the sequence are given separated by a single space
    bubble_sort(A)

if __name__ == "__main__":
    main()