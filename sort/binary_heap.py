def upAdjust(arr):
    childIndex = len(arr) - 1
    parentIndex = (childIndex - 1) // 2
    temp = arr[childIndex]
    while childIndex > 0 and temp > arr[parentIndex]:
        arr[childIndex], arr[parentIndex] = arr[parentIndex], arr[childIndex]
        childIndex = parentIndex
        parentIndex = (parentIndex - 1) // 2
    arr[childIndex] = temp

def downAdjust(arr, parentIndex, length):
    temp = arr[parentIndex]
    childIndex = 2 * parentIndex + 1
    while childIndex < length:
        if childIndex + 1 < length and arr[childIndex] < arr[childIndex + 1]:
            childIndex += 1
        if temp >= arr[childIndex]:
            break
        arr[parentIndex], arr[childIndex] = arr[childIndex], arr[parentIndex]
        parentIndex = childIndex
        childIndex = 2 * childIndex + 1
    arr[parentIndex] = temp

def buildHeap(arr):
    for i in range((len(arr) - 2) // 2, -1, -1):
        downAdjust(arr, i, len(arr))

def heapSort(arr):
    for i in range(len(arr) - 2 // 2, -1, -1):
        downAdjust(arr, i, len(arr))
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        downAdjust(arr, 0, i) # 被取出的数据放在了数组最后一个位置，如果i + 1的话，就会占用这个位置了

if __name__ == '__main__':
    arr = [10, 9, 8, 7, 5, 2, 3, 1, 6, 11]
    upAdjust(arr)
    print(arr)

    arr = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    buildHeap(arr)
    print(arr)

    arr = [1,3,2,6,5,7,8,9,10,0]
    heapSort(arr)
    print(arr)