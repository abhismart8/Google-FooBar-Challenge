import math
def solution(area):
    area = round(area)
    if area < 0:
        splitVar = str(area).split('-')
        area = int(splitVar[1])

    finalArray = []
    i = area
    while i > 0:
        var = int(math.sqrt(i))
        if var*var == i:
            newObj = var*var

            sum2 = 0
            for y in finalArray:
                sum2 = sum2 + y

            if sum2+newObj <= area:
                finalArray.append(newObj)
        i-=1
        
    sum1 = 0
    for z in finalArray:
        sum1 = sum1  + z

    diff = int(area - sum1)
    if diff == 0:
        return finalArray
    else:
        for j in range(diff):
            finalArray.append(1);

    return finalArray

print(solution(12))