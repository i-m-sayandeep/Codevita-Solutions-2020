# def combinations(arr,n):
#     if n == 0:
#         return([])
#     a =[] 
#     for i in range(0, len(arr)):  
#         x = arr[i] 
#         rem = arr[i + 1:]   
#         for j in combinations(rem, n-1): 
#             a.append([x]+j)
#     return(a) 

letter = {0:'zero',
        1:'one', 2: 'two' , 3:'three', 4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
        11 :'eleven',12:'twelve',13:'thirteen', 14:'fourteen', 15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen', 20: 'twenty',
        21:'twenty one', 22:'twenty two', 23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six', 27:'twenty seven',28:'twenty eight',29:'twenty nine', 30:'thirty',
        31:'thirty one',32:'thirty two',33:'thirty three', 34:'thirty four', 35:'thirty five', 36:'thirty six',37:'thirty seven',38:'thirty eight',39:'thirty nine',40:'forty',
        41:'forty one', 42:'forty two', 43:'forty three', 44:'forty four', 45:'forty five', 46:'forty six', 47:'forty seven', 48:'forty eight',49:'forty nine', 50:'fifty',
        51:'fifty one', 52:'fifty two', 53:'fifty three', 54:'fifty four', 55:'fifty five', 56:'fifty six', 57:'fifty seven', 58:'fifty eight', 59:'fifty nine', 60:'sixty',
        61:'sixty one', 62:'sixty two', 63:'sixty three', 64:'sixty four', 65:'sixty five', 66:'sixty six', 67:'sixty seven', 68:'sixty eight', 69:'sixty nine', 70:'seventy',
        71:'seventy one', 72:'seventy two', 73:'seventy three', 74:'seventy four', 75:'seventy five', 76:'seventy six', 77:'seventy seven', 78:'seventy eight', 79:'seventy nine', 80:'eighty',
        81:'eighty one', 82:'eighty two', 83:'eighty three', 84:'eighty four', 85:'eighty five', 86:'eighty six', 87:'eighty seven', 88:'eighty eight',89:'eighty nine', 90:'ninety',
        91:'ninety one', 92:'ninety two', 93:'ninety three', 94:'ninety four', 95:'ninety five', 96:'ninety six', 97:'ninety seven', 98:'ninety eight', 99:'ninety nine',100:'hundred' }

values = {0: 2,
        1: 2, 2: 1, 3: 2, 4: 2, 5: 2, 6: 1, 7: 2, 8: 2, 9: 2, 10: 1,
        11: 3, 12: 2, 13: 3, 14: 4, 15: 3, 16: 3, 17: 4, 18: 4, 19: 4, 20: 1, 
        21: 3, 22: 2, 23: 3, 24: 3, 25: 3, 26: 2, 27: 3, 28: 3, 29: 3, 30: 1, 
        31: 3, 32: 2, 33: 3, 34: 3, 35: 3, 36: 2, 37: 3, 38: 3, 39: 3, 40: 1, 
        41: 3, 42: 2, 43: 3, 44: 3, 45: 3, 46: 2, 47: 3, 48: 3, 49: 3, 50: 1, 
        51: 3, 52: 2, 53: 3, 54: 3, 55: 3, 56: 2, 57: 3, 58: 3, 59: 3, 60: 1, 
        61: 3, 62: 2, 63: 3, 64: 3, 65: 3, 66: 2, 67: 3, 68: 3, 69: 3, 70: 2, 
        71: 4, 72: 3, 73: 4, 74: 4, 75: 4, 76: 3, 77: 4, 78: 4, 79: 4, 80: 2, 
        81: 4, 82: 3, 83: 4, 84: 4, 85: 4, 86: 3, 87: 4, 88: 4, 89: 4, 90: 2, 
        91: 4, 92: 3, 93: 4, 94: 4, 95: 4, 96: 3, 97: 4, 98: 4, 99: 4, 100: 2}

N = int(input())
numArr = list(map(int,input().split()[:N]))


count = 0
for i in numArr:
    count+=values[i]


uoPair = 0
for i in range(len(numArr)):
    for j in range(i+1,len(numArr)):
        if( numArr[i]+numArr[j] == count ):
            if([numArr[i],numArr[j]] ==  sorted([numArr[i],numArr[j]])):
                uoPair+=1

if(uoPair>100):
    print("greater 100", end="")
else:   
    print(letter[uoPair], end="")