import json
import jsonpickle

# Create a Python dictionary representing an object
data = {
   "id": "batch_req_AF19ZRxYIopvTtVxPlylF9U0",
   "custom_id": "request-3",
   "response": {
      "status_code": 200,
      "request_id": "638f9168b383a1dc178e9209554a4194",
      "body": {
         "id": "chatcmpl-A8RLsuz0MhwmYVwV34FMVku8QJLPU",
         "object": "chat.completion",
         "created": 1726575128,
         "model": "gpt-3.5-turbo-0125",
         "choices": [
            {
               "index": 0,
               "message": {
                  "role": "assistant",
                  "content": "",
                  "refusal": ""
               },
               "logprobs": "",
               "finish_reason": "stop"
            }
         ],
         "usage": {
            "prompt_tokens": 108,
            "completion_tokens": 302,
            "total_tokens": 410,
            "completion_tokens_details": {
               "reasoning_tokens": 0
            }
         },
         "system_fingerprint": ""
      },
      "error": ""
   }
}

content_value = { 
    "description_cn": "",  
    "bible_life_cn": "" ,
    "bible_life_pinyin": ""
}

# Convert content_value dictionary to a JSON string
content_value_json = json.dumps(content_value)

# Assign content_value_json to data["response"]["body"]["choices"][0]["message"]["content"]
data["response"]["body"]["choices"][0]["message"]["content"] = content_value_json

content_ques = "Today is great. Translate this to cn and pinyin in this json format"

# Convert the Python dictionary to a JSON string
json_string = json.dumps(data, indent=4)

# Print the JSON string
print(json_string)

# Output the concatenated string
print(content_ques + content_value_json)

# Output the content in UTF-8 encoding
utf8_content = data["response"]["body"]["choices"][0]["message"]["content"].encode('utf-8')
print("Content in UTF-8: ", utf8_content)

# Decode the UTF-8 content back to a string
decoded_content = json.loads(utf8_content.decode('utf-8'))

utf8_string = decoded_content["description_cn"].encode('utf-8')

# Print the UTF-8 encoded string
print("UTF-8 Encoded String:", utf8_string.decode('utf-8'))

data["response"]["body"]["choices"][0]["message"]["content"] = content_ques + content_value_json

print ("new json-->", json.dumps(data))

