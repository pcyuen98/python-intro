# Example  
# Advance condition usages
# How to make multiple conditions into single statement or single line from leftover.py

def falsify():
    leftover = [19.7, 20.0, 28.5, 30.0, 30.7]
    return [num - 10 if 30 > num >= 20 else ('1' + str(num)[1:]) if num >= 30 else num for num in leftover]

print('result', falsify())
