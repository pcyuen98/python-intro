from jsonpickle.backend import json
from news.news_redis import News
json_data = '''{
    "title": "Tips for Exercise, Diet, and Mental Health",
    "link": "https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise/art-20048389",
    "image_url": "",
    "pubDate": "",
    "isPositive": true,
    "news_ai": "",
    "well_being_ai": "This article provides valuable information on exercise, diet, and mental health.",
    "description": "This article offers tips for exercise, diet, and mental health. It covers topics such as finding enjoyable physical activities, making healthy food choices, and managing stress.",
    "description_my": "Artikel ini menawarkan tip untuk senaman, diet, dan kesihatan mental. Ia meliputi topik seperti mencari aktiviti fizikal yang menyeronokkan, membuat pilihan makanan yang sihat, dan menguruskan tekanan.",
    "description_cn": "本文提供了有关运动、饮食和心理健康的建议。它涵盖了诸如寻找愉快的体力活动、做出健康的食物选择以及管理压力等主题。",
    "bible_ai": "",
    "bible_life": "",
    "bible_life_cn": "",
    "is_duplicate": false,
    "headline": "",
    "pinyin": ""
}'''

# Parse the JSON data
data = json.loads(json_data)

print("\n data.get('title')--->" , data.get('title'))
print ("\n data['title']-->", data['title'])
# print ("\n data['title']-->", data['title'])   --> error
print ("\n data.get('isPositive')-->", data.get('isPositive'))

news_instance = News.from_json_obj(data)
print ("casting from_json_obj-->" , news_instance.title)