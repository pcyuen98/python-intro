import json

data1 = '''
[
    {
        "description_cn": "在北京参观故宫博物院，感受中国古代皇宫的壮丽。"
    }
]
'''

data2 = '''
[
    {
        "description_cn": "在杭州体验壮观的印象西湖表演。"
    }
]
'''

# Parse the JSON data into lists
data1_list = json.loads(data1)
data2_list = json.loads(data2)

# Append data1 into data2
data2_list.extend(data1_list)

# Print the merged list
print(data2_list)