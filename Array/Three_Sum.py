def three_sum(array):
    array.sort()
    
    for i in range(len(array)):
        a = array[i]
        
        sum = -a
        start = i + 1
        end = len(array)-1
        
        while(start<end):
            tempSum = array[start] + array[end]
            if(tempSum == sum):
                print("Found 3 elements whose sum is = 0")
                print('Elements are %s, %s and %s.'%(a, array[start], array[end]))
                return
            elif(tempSum<sum):
                start+=1
            else:
                end-=1
                
                
result = three_sum([3,-1,-7,-4,-5,9,10])