# Example  
# Using pipe and dictionary append to merge dictionary

# Example output
#dict 1-> {'modelA': [92.3, 92.4, 92.5], 'modelB': [87.3, 87.4, 87.5]}
#dict 2-> {'modelA': [91.6], 'modelB': [87.0]}
#dict 3-> {'modelA': [91.7, 91.6], 'modelB': [87.9, 87.4]}
#replaced value in dictionary: {'modelA': [91.7, 91.6], 'modelB': [87.9, 87.4]}
#appended value in dictionary: {'modelA': [92.3, 92.4, 92.5, [91.6]], 'modelB': [87.3, 87.4, 87.5, [87.0]]}

def replaceDict (run8, run9, run10):
    return run8 | run9 | run10

def appendDict (merged_dic, dic):
    for entry in dic:
        if entry in merged_dic:
            merged_dic[entry].append(dic[entry])
        else:
            merged_dic[entry] = dic[entry]
    return merged_dic

dict1 = {'modelA': [92.3, 92.4, 92.5], 'modelB': [87.3, 87.4, 87.5]}
dict2 = {'modelA': [91.6], 'modelB': [87.0]}
dict3 = {'modelA': [91.7, 91.6], 'modelB': [87.9, 87.4]}

print ('dict 1->', dict1)
print ('dict 2->', dict2)
print ('dict 3->', dict3)

print ('replaced value in dictionary:' , replaceDict(dict1, dict2, dict3))

merged_dic = {}
appendDict(merged_dic, dict1)
appendDict(merged_dic, dict2)
       
print ('appended value in dictionary:' , merged_dic )
