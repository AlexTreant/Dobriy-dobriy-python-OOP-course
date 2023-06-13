def dirReduc(arr):
    sample = [("NORTH", "SOUTH"), ("SOUTH", "NORTH"), ("EAST", "WEST"), ("WEST", "EAST")]
    flag = 20
    while flag != 0:
        for i in range(len(arr)):
            try:
                x = (arr[i].upper(), arr[i+1].upper())
                if x in sample:
                    arr.pop(i)
                    arr.pop(i+1)
                    break
            except:
                continue
        return arr
    
asd = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
print(dirReduc(asd))