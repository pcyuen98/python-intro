# Assume student will have some knowledge of basic installation of python and basic usages
# get your api key from tutuorial here https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

import openai

def askQUes(ques):
    openai.api_key = 'refer to the tutorial link above'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": ques }]
        )
    return completion.choices[0].message.content

ques = ''

while ques != 'quit':
    # Ask the user for a name.
    ques = input("Ask a question, or enter 'quit': ")
    print(askQUes(ques))
