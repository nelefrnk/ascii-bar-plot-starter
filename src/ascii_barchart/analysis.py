# averages = average_value1_by_type(rows)
sumA = 0
sumB = 0
sumC = 0
sumD = 0

countA = 0
countB = 0
countC = 0
countD = 0

def average_value1_by_type(data_list):
    for item_type, val1, val2 in data_list:
        if item_type == 'A':
            sumA = sumA + val1
            countA += 1

        if item_type == 'B':
            sumB = sumB + val1
            countB += 1

        if item_type == 'C':
            sumC = sumC + val1
            countC += 1

        if item_type == 'D':
            sumD = sumD + val1
            countD += 1

    avgA = sumA / countA
    avgB = sumB / countB
    avgC = sumC / countC
    avgD = sumD / countD
        
    return [('A', avgA), ('B', avgB), ('C', avgC), ('D', avgD)]