def insert(idx, num, arr):
    arr.append(0)
    for i in range(len(arr)-1, idx, -1):
        arr[i] = arr [i-1]
    arr[idx] = num
    
def erase(idx, arr):
    for i in range (idx, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    
def printArr(arr):
    print(' '.join(map(str, arr)))
    print("\n")

def insert_test():
    print("***** insert_test *****")
    arr = [10, 20, 30]
    insert(3, 40, arr)  # 10 20 30 40
    printArr(arr)
    insert(1, 50, arr)  # 10 50 20 30 40
    printArr(arr)
    insert(0, 15, arr)  # 15 10 50 20 30 40
    printArr(arr)

def erase_test():
    print("***** erase_test *****")
    arr = [10, 50, 40, 30, 70, 20]
    erase(4, arr)  # 10 50 40 30 20
    printArr(arr)
    erase(1, arr)  # 10 40 30 20
    printArr(arr)
    erase(3, arr)  # 10 40 30
    printArr(arr)

def main():
    insert_test()
    erase_test()

if __name__ == "__main__":
    main()
