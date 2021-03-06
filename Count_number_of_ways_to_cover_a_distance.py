def printCountRec(dist):
     
    # Base cases
    if dist < 0:
        return 0
         
    if dist == 0:
        return 1
 
    # Recur for all previous 3 and      
   # add the results
    return (printCountRec(dist-1) +
            printCountRec(dist-2) +
            printCountRec(dist-3))
 
# Driver code
dist = int(input())
print(printCountRec(dist))
# This code is contributed by Anant Agarwal.