import json

#data = '{"chinese": ["画蛇添足"], "chinese_explaination": ["Unnecessary actions complicate situations."], "chinese_pinyin": ["huà shé tiān zú"], "malay": ["menyulitkan diri sendiri"], "malay_explaination": ["Making things more complicated for oneself."]}'
data = '{"chinese": ["画蛇添足"], "chinese_explaination": ["Unnecessary actions complicate situations."], "chinese_pinyin": ["huà shé tiān zú"], "malay": ["menyulitkan diri sendiri"], "malay_explaination": ["Making things more complicated for oneself."]}'
json_dict = json.loads(data)
idiom = "AI Idiom"
idiom_cn = "AI 成语"
                    
cn_idiom = idiom_cn + ", " + json_dict["chinese"][0] + ", " + json_dict["chinese_pinyin"][0] + ", " + json_dict["chinese_explaination"][0]
malay_idiom = idiom + ", " + json_dict["malay"][0] + ", " + json_dict["malay_explaination"][0]
print(cn_idiom)
print(malay_idiom)

description_cn = "画蛇添足"
description_my = "malay"
description_cn = description_cn + cn_idiom 
description_my = str(description_my) + str(malay_idiom)