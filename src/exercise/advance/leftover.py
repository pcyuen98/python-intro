leftover1 = [19.7, 20.0, 28.5, 30.0, 30.7]

def process(leftover):
    false = []
    for num in leftover:
        print('num:' , num)

        if 30 > num >= 20: false.append(num - 10) 
        elif num >= 30:            
            # (str(num[1]))
            result = str(num)
            #print('result:' , result)
            false.append('1' + result[1:])
            #
        else:
            false.append(num)
    return false 


def falsify(leftover):
    #Note  ## Your code here (replace with a single line) ###
    return process(leftover)

print('result', falsify(leftover1))

#print(falsify(leftover1))