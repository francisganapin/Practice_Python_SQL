def linearSearch(arr,targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1
    

mylist = [3,7,2,9,5,1,8,4,6,4]
x = 12

result = linearSearch(mylist,x)


if result != -1:
    print('Foudn at index',result)
else:
    print('Not found')