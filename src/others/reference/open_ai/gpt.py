from _datetime import date
import json
import os
import time
import traceback

import jsonpickle
import openai
import requests


ai_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = ai_key

class GPT:
    @staticmethod
    def askGPT(str):
        while True:
            try:        
                ques = str + " .Is this a positive, not politic related and important news? Answer yes or no and explain in less than 15 words";
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
           
                messages=[
                    {"role": "user", "content": ques}
                    ],)
                time.sleep(1)
                break
            except Exception as error:
                print("askGPT_well_being An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)   
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_well_being(str):
        while True:
            try:
                ques = str + " .How is this news impact well being if reading too much. Explain in less than 15 words";
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": ques}
                        ],)
                time.sleep(1)
                break
            except Exception as error:
                print("askGPT_well_being An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)   
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_way_of_life(str):
        while True:
            try:
                ques = str + " .explain this in psychology way of life view without name or bible verse in 30 words";
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": ques}
                        ],)
                time.sleep(1)
                break 
            except Exception as error:
                print("askGPT_way_of_life An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)   
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content
    
    @staticmethod
    def askGPT_badminton():
        r = requests.get("https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVTFaR2dKTldTZ0FQAQ?hl=en-MY&gl=MY&ceid=MY:en")
        trim_str = r.text[0:2000]
        print ("trim_str-->" + trim_str)
        ques = trim_str + " . Give me sport comments summary in 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": ques}
                ],)
       
        result = completion.choices[0].message.content
        print(result)
       
        #summary = result + " .Provide a score result and some sport comments"
        #completion = openai.chat.completions.create(
        #    model="gpt-4o",
        #    messages=[
        #        {"role": "user", "content": summary}
        #        ],)
        #result = completion.choices[0].message.content
        #print(result)      
        return completion.choices[0].message.content
   
    @staticmethod
    def askGPT_bible(str):
        while True:
            try:
                ques = str + " Map this news to Bible verse in less than 20 words";
                completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": ques}
                    ],)
                time.sleep(1)
                break 
            except Exception as error:
                print("askGPT_bible An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)   
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_bible_life(str):
        while True:
            try:
                ques = str + " . Give a Bible life example in less than 50 words";
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": ques}
                        ],)
                time.sleep(1)
                break 
            except Exception as error:
                print("askGPT_bible_life An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)   
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_description(str):
        while True:
            try:
                ques = str + " . Summarize this in less than 50 words";
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    # response_format= {"type": "json_object"},
                    messages=[
                        {"role": "user", "content": ques}
                        ],)
                time.sleep(1)
                break
            except Exception as error:
                print("askGPT_description An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)        
        print("askGPT_description-->", completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_translate_my(str):
        while True:
            try:
                ques = str + " . Translate this into Bahasa Melayu.";
                completion = openai.chat.completions.create(
                model="gpt-4o-mini",
            # response_format= {"type": "json_object"},
                messages=[
                    {"role": "user", "content": ques}
                    ],)
                time.sleep(1)
                break    
            except Exception as error:
                print("askGPT_translate_my An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)
        print("askGPT_description-->", completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_translate_cn(str):
        while True:
            try:
                format_json = '{"description_cn": [""], "bible_life_cn": [""], "bible_life_pinyin": [""]}'
                ques = str + " . translate this into chinese and pinyin in this format " + format_json + " only  "  
        
                print ("ques askGPT_translate_cn-->" + ques)
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    # response_format= {"type": "json_object"},
                    messages=[
                        {"role": "user", "content": ques}
                        ],)
                time.sleep(1)
                break    
            except Exception as error:
                print("askGPT_translate_cn An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_idiom(str):
        while True:
            try:
                format_json = '{"chinese": [""], "chinese_explaination": [""], , "chinese_pinyin": [""], "malay": [""] "malay_explaination": [""]}'
                ques = str + " . Give a positive idiom in chinese and pinyin and malay positive idiom based on above without religion but explaination only in less than 15 words and without quotation mark or “ or ” in this format " + format_json + " only "  
        
                print ("ques askGPT_idiom-->" + ques)
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    # response_format= {"type": "json_object"},
                    messages=[
                        {"role": "user", "content": ques}
                        ],)
                time.sleep(1)
                break    
            except Exception as error:
                print("askGPT_idiom An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)
        return completion.choices[0].message.content
    
    @staticmethod
    def askGPT_translate(str):
        while True:
            try:
                ques = str + " . Translate this into Chinese and Malay in less than 5 words in JSON string only";
                completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                response_format= {"type": "json_object"},
                messages=[
                    {"role": "user", "content": ques}
                    ],)
                break 
                time.sleep(1)
            except Exception as error:
                print("askGPT_idiom An exception occurred:", error)
                print(traceback.format_exc())
                time.sleep(3)
        print(completion.choices[0].message.content.encode("utf-8"))
        return completion.choices[0].message.content
           
    @staticmethod
    def askGPTDummyYes(str):
        return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."

    @staticmethod
    def askGPTDummyWellBeing(str):
        return "Excessive exposure to corruption news can heighten stress and erode trust in institutions."

    @staticmethod
    def askGPTDummyNo(str):
        return "No, it reflects divisive rhetoric, which can intensify political tensions."      
   
    @staticmethod
    def process_cn_malay(news_src_json):
        return "No, it reflects divisive rhetoric, which can intensify political tensions."
   
    #GPT.askGPT("Over 142,000 individuals released from bankruptcy under Second Chance Policy, says PM.")

    @staticmethod
    def translateUTF8(str):
        #answer = GPT.askGPT_badminton()
        answer = "what is this"
        news_src_list=[]
        malay_chinese = GPT.askGPT_translate(answer)
        malay_chinese = malay_chinese.encode('utf-8')
        #print ('malay_chinese encode-->' , malay_chinese)
        #print (malay_chinese.decode('utf-8'))
# String containing the escape sequence
        news_src_list.append(malay_chinese.decode('utf-8'))
        news_src_json = jsonpickle.encode(news_src_list)
        redis_file = open("malay_chinese.txt", "w", encoding="utf-8")
        redis_file.write(news_src_json)
        redis_file.close()

        redis_file = open("malay_chinese.txt", "r+", encoding="utf-8")
        news_redis_json = redis_file.read()

        json_obj = jsonpickle.decode(news_redis_json)
        #json_obj = jsonpickle.encode(json_obj)
        print ("json_obj==>" , json_obj)
        #data = json.loads(json_obj[0])
        json_str = json_obj[0].strip()

# Load the JSON-like string as JSON data
        data = json.loads(json_str)

# Print the value associated with the "Malay" key
        malay_value = data["Malay"]
        print(malay_value)

        redis_file.close()  
        return json_obj

    @staticmethod
    def readDummyEncoded():

        redis_file = open("2024-07-31_redis_news.txt", "r+", encoding="utf-8")
        news_redis_json = redis_file.read()
        redis_file.close()  
        return news_redis_json

if __name__ == '__main__':
    #print (GPT.readDummyEncoded())
    #print (GPT.translateUTF8('test'))
    print (GPT.askGPT_idiom('When Nehemiah set out to rebuild Jerusalem wall, he prayed and committed his plans to God (Nehemiah 1:4-11). Despite opposition, his faith and dedication led to the successful completion of the wall, illustrating that committing our endeavors to the Lord brings success.'))
