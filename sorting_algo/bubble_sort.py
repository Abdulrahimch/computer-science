arr = [1,2,10,9,5,3,7,1]

def bubble_sort(arr):
    for i in range(len(arr)):
        for index in range(len(arr) -i -1):
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
    return arr

print('the orginal array is: ', arr)
print("POST-OPTIMIZED ITERATION COUNT: {0}".format(bubble_sort(arr)))