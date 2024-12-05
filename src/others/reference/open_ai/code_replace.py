import json

# JSON data with properly escaped backslashes
json_data = """
{
  "custom_id": "request-3",
  "method": "POST",
  "url": "/v1/chat/completions",
  "body": {
    "model": "gpt-3.5-turbo-0125",
    "messages": [
      {
        "role": "user",
        "content": " test {\"description_cn\": [\" \\u5927\\u536b\\u548c\\u62d4 \"]} "
      }
    ],
    "max_tokens": 1000
  }
}
"""

# Load JSON data
data = json.loads(json_data)

# Extract and print description_cn in UTF-8
description_cn = data["body"]["messages"][0]["content"].split('\"description_cn\": [\"')[1].split('\"')[0]
print(description_cn.encode().decode('unicode-escape'))