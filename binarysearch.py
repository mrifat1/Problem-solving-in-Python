def binary_search(arr, low, high, x): 
  
    if high >= low: 
  
        mid = (high + low) // 2
         
        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: 
            return binary_search(arr,low,mid-1,x)


        else: 
            return binary_search(arr,mid+1,high,x) 
  
    else:
        return -1
  

arr = [] 
for i in range(0,5):
    elem = int(input())
    arr.append(elem)

#arr = [2,4,5,6,10]

x = int(input())
arr.sort()
result = binary_search(arr,0,len(arr)-1,x) 
  
if result != -1: 
    print("Element is present at index", result)
else: 
    print("Element is not present in array")