#Thang Le
#Running time O (log n)
#will need a logic to check s1 and s2 are characters only. 
#this only work on assumption of the list is in accending order

count = 0

def binary_search(input,k):
    global count
    count = count + 1
    mid_point = input[len(input)/2]
    print mid_point
    
    half = len(input)/2
    first_half = input[:half]
    second_half = input[half:]
    
    if mid_point == k:
        print "Found after :", count, " times"
        return True
    else:
        if mid_point > k:
            binary_search(first_half, k)
        else:
            binary_search(second_half, k)
            
binary_search([1,4,6,7,12,16,23,45,52,56,67,89,90,123,234,456,567], 567)
    