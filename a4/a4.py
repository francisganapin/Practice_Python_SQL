def linear_search(arr,target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1 



linear_search([10,20,30,40,50],30)

print(linear_search([10,20,30,40,50],30))