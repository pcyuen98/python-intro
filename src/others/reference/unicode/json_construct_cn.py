import json
import jsonpickle

content_value = { 
    "description_cn": "",  # "大卫和拖" in Chinese
    "bible_life_cn": "" , # "大" in Chinese
    "bible_life_pinyin": ""  # "大" in Chinese
}

# Convert content_value dictionary to a JSON string
content_value_json = json.dumps(content_value)

content_ques = "Today is great. Translate this to cn and pinyin in this json format"

# Output the concatenated string
print(content_ques + content_value_json)

