# Example  
# Method or def usages 
# How to make code cleaner from the sample

# -- Original dirty code -- 
#def falsify(leftover):
    #Note   ## Your code here (replace with a single line) ###
     
# def falsify(leftover):
#    false = []
#    for num in leftover:
#        if 30 > num > 20:
#            false.append(num - 10)
#        elif num >= 30:
#            false.append('1' + (str(num[1:])))
#        else:
#            false.append(num)
#     return false
 

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
