# Example  
# Using dictionary double loop to swap key and value 

# Sample output
# original value=> {'New York': ['A', 'B'], 'California': ['A'], 'Chicago': ['A', 'C', 'B']}

# state_switched=> {'A': ['New York', 'California', 'Chicago'], 'B': ['New York', 'Chicago'], 'C': ['Chicago']}

def appendDict (key, value_in_list, state_as_key):
    for entry in value_in_list:
        if entry in state_as_key:
            state_as_key[entry].append(key)
        else:
            keyList = []
            keyList.append(key)
            state_as_key[entry] = keyList
    return state_as_key

def inverse_dict(my_dict):
    updated_dict = {}
  
    for key,value in my_dict.items():
        appendDict(key, value, updated_dict)       

    return updated_dict

state_as_key = {
 'New York': ['A', 'B'],
 'California': ['A'],
 'Chicago': ['A', 'C', 'B']
}

print ('original value=>', state_as_key)

print("state_switched=>" , inverse_dict(state_as_key))

