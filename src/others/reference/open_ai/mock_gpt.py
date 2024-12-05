from unittest import mock
import openai
import os
import json
import traceback
import time

ai_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = ai_key

def call_chatgpt(prompt):
    while True:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            time.sleep(1)
            break   
        except Exception as error:
            print(prompt, ". A GPT query exception occurred:", error)
            print(traceback.format_exc())
            time.sleep(3)
    return response['choices'][0]['message']['content']

def call_chatgpt_multiple(prompt,prompt2):
    while True:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt},
                    {"role": "user", "content": prompt2}
                ]
            )
            time.sleep(1)
            break   
        except Exception as error:
            print(prompt, ". A GPT query exception occurred:", error)
            print(traceback.format_exc())
            time.sleep(3)
    print ("Multiple response-->", response)
    return response['choices'][0]['message']['content']

def test_call_chatgpt():
    mock_response = {
        'choices': [
            {'message': {'content': 'Hello, world!'}}
        ]
    }
    
    with mock.patch('openai.chat.completions.create', return_value=mock_response) as mock_create:
        result = call_chatgpt("Say something")

        mock_create.assert_called_once_with(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Say something"}
            ]
        )

        assert result == 'Hello, world!'

def askGPT_idiom(str):
    
    mock_response_idiom = {
        'choices': [
            {
                'message': {
                    'content': json.dumps({
                        "chinese": ["和衷共济"],
                        "chinese_explaination": ["各抒己见，共同应对困难"],
                        "chinese_pinyin": ["Hé zhōng gòng jì"],
                        "malay": ["Bersatu kita teguh"],
                        "malay_explaination": ["Bersatu padu kita teguh"]
                    })
                }
            }
        ]
    }
    
    while True:
        try:
            format_json = '{"chinese": [""], "chinese_explaination": [""], "chinese_pinyin": [""], "malay": [""] "malay_explaination": [""]}'
            ques = str + " . Give a positive idiom in chinese and pinyin and malay positive idiom based on above without religion but explaination only in less than 15 words and without quotation mark or “ or ” in this format " + format_json + " only "  
        
            print("ques askGPT_idiom-->" + ques)
            
            with mock.patch('openai.chat.completions.create', return_value=mock_response_idiom) as mock_create:
                result = call_chatgpt(ques)

                mock_create.assert_called_once_with(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": ques}
                    ]
                )

                time.sleep(1)
                break    
        except Exception as error:
            print("askGPT_idiom An exception occurred:", error)
            print(traceback.format_exc())
            time.sleep(3)

    print ("return_str-->", result)
    return result
    
if __name__ == '__main__':
    #print ('result askGPT-->' , askGPT("Say something today"))
    #print('result-->', test_call_chatgpt())
    #askGPT_idiom("Today is a good day")
    call_chatgpt_multiple("What day is today", "tell anything about sport")
    #print("Test passed!")