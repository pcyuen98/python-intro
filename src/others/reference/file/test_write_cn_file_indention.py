import json

# Objective - Write a file with chinese content and 4 spaces indention

json_data = '''
[
    {
        "description_cn": "在杭州体验壮观的印象西湖表演，这是一场大型戏剧表演，展示了标志性西湖的美丽和历史。在 Pelago 上以最佳价格获取您的门票。"
    }
]
'''

# Specify the file path
file_path = "output.json"

# Writing the JSON data to a file with 4-space indentation
with open(file_path, "w", encoding="utf-8") as file:
    file.write(json.dumps(json.loads(json_data), ensure_ascii=False, indent=4))

print(f"Data has been written to '{file_path}' with 4-space indentation.")

# Reading the JSON data back from the file and printing it
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Data read from the file:")
print(json.dumps(data))