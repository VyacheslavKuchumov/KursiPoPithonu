start = 1
end = 100


def createList():
    global start, end
    return list(range(start, end + 1))
    

def search(list, item):
    global start
    end = len(list) - 1
     
    while start <= end:
        mid = (start + end) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            end = mid - 1
        else:
            start = mid + 1
    
    return(None)
    
    
myList = createList()

print(myList[search(myList, 70)])
    
