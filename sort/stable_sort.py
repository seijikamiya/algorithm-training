def bubble_sort(A):
    for i in range(len(A)):

        for j in reversed(range(i+1, len(A))):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]

    return A

def selection_sort(A):
    for i in range(len(A)):
        min = i
        for j in range(min, len(A)):
            if A[min][1] > A[j][1]:
                min = j
        
        A[i], A[min] = A[min], A[i]

    return A


def main():
    N = int(input()) #the number of elements in the sequence
    A = list(input().split()) #Each card is represented by two characters. Two consecutive cards are separated by a space character.
    B = A[:]
    bubble_sort_result = bubble_sort(A)
    print(*bubble_sort_result)
    print("Stable")

    selection_sort_result = selection_sort(B)
    print(*selection_sort_result)
    if bubble_sort_result ==selection_sort_result:
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()
