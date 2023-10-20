def findMinElemWithIndex(listForSearch: list):
    if len(listForSearch) == 0:
        return -1, None
    
    min_id = 0
    min_elem = listForSearch[0]
    
    for i in range(1, len(listForSearch)):
        if listForSearch[i] < min_elem:
            min_elem = listForSearch[i]
            min_id = i
    
    return min_id, min_elem

def findMaxElemWithIndex(listForSearch: list):
    if len(listForSearch) == 0:
        return -1, None
    
    max_id = 0
    max_elem = listForSearch[0]
    
    for i in range(1, len(listForSearch)):
        if listForSearch[i] > max_elem:
            max_elem = listForSearch[i]
            max_id = i
    
    return max_id, max_elem

def main():
    listOfData = [11, 14, 22, 33, 7, 88, 123, 345, 64, 10, 5, 55, 66, 44, 20]
    
    min_result = findMinElemWithIndex(listOfData)
    print(f"Min id: {min_result[0]}, Min value: {min_result[1]}") 

    max_result = findMaxElemWithIndex(listOfData)
    print(f"Max id: {max_result[0]}, Max value: {max_result[1]}") 

if __name__ == "__main__":
    main()
