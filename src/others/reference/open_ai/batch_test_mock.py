# Define the batch data as a dictionary
import traceback
import time
import json
import jsonpickle
import codecs
batch_data = {
    'id': 'batch_LunAvcYn4RGXvp59fWOxse0s',
    'completion_window': '24h',
    'created_at': 1726575125,
    'endpoint': '/v1/chat/completions',
    'input_file_id': 'file-416zCVB58AUZkdeIrcXbKu9q',
    'object': 'batch',
    'status': 'validating',
    'cancelled_at': None,
    'cancelling_at': None,
    'completed_at': None,
    'error_file_id': None,
    'errors': None,
    'expired_at': None,
    'expires_at': 1726661525,
    'failed_at': None,
    'finalizing_at': None,
    'in_progress_at': None,
    'metadata': {'description': 'nightly eval job'},
    'output_file_id': "test",
    'request_counts': {
        'completed': 0,
        'failed': 0,
        'total': 0
    }
}

while True:
    try:
        batch_data['output_file_id']
        print("Output File ID:", batch_data['output_file_id'])
        if batch_data['output_file_id'] is None:
            print("Output File ID is None. Re-trying")
            time.sleep(1)
        else:
            print("Output File ID:", batch_data['output_file_id'])
            break
           
    except Exception as error:
        print("An exception occurred," , error)
        print(traceback.format_exc())
        
# The byte string provided
byte_string = b'{"id": "batch_req_LnghmiCZwKM2vA5Xga1rXGnO", "custom_id": "request-1", "response": {"status_code": 200, "request_id": "a6ce4ecd1904d2fd7ef85e668567f29d", "body": {"id": "chatcmpl-A8RMqmVqrm2Ni505AaWK4mN1i8KMD", "object": "chat.completion", "created": 1726575188, "model": "gpt-3.5-turbo-0125", "choices": [{"index": 0, "message": {"role": "assistant", "content": "No", "refusal": null}, "logprobs": null, "finish_reason": "stop"}], "usage": {"prompt_tokens": 61, "completion_tokens": 1, "total_tokens": 62, "completion_tokens_details": {"reasoning_tokens": 0}}, "system_fingerprint": null}}, "error": null}\n{"id": "batch_req_T8UtWxgP5iTKWLigOi11zS2b", "custom_id": "request-2", "response": {"status_code": 200, "request_id": "321de174ec5b86b16374bd3653247789", "body": {"id": "chatcmpl-A8RLs9N7rGll75vuxzqElhIAYy5o9", "object": "chat.completion", "created": 1726575128, "model": "gpt-3.5-turbo-0125", "choices": [{"index": 0, "message": {"role": "assistant", "content": "From a psychological perspective, the passing of Raja Petra can be viewed through the lens of the stages of grief and loss. When a person dies, those who were close to them may experience a range of emotions including denial, anger, bargaining, depression, and eventually acceptance. This process of grieving is a natural response to loss and helps individuals to come to terms with the reality of death.\\n\\nAdditionally, the news of Raja Petra\'s passing may evoke feelings of sadness and nostalgia in those who knew him or were familiar with his work. This can also trigger thoughts about mortality and the impermanence of life, prompting individuals to reflect on their own lives and relationships.\\n\\nOverall, the passing of Raja Petra serves as a reminder of the inevitable nature of death and encourages individuals to cherish their loved ones and make the most of their time on this earth. It also highlights the importance of processing and coping with grief in a healthy way, as part of the human experience.", "refusal": null}, "logprobs": null, "finish_reason": "stop"}], "usage": {"prompt_tokens": 52, "completion_tokens": 193, "total_tokens": 245, "completion_tokens_details": {"reasoning_tokens": 0}}, "system_fingerprint": null}}, "error": null}\n{"id": "batch_req_AF19ZRxYIopvTtVxPlylF9U0", "custom_id": "request-3", "response": {"status_code": 200, "request_id": "638f9168b383a1dc178e9209554a4194", "body": {"id": "chatcmpl-A8RLsuz0MhwmYVwV34FMVku8QJLPU", "object": "chat.completion", "created": 1726575128, "model": "gpt-3.5-turbo-0125", "choices": [{"index": 0, "message": {"role": "assistant", "content": "{\\"description_cn\\": [\\"\\u5927\\u536b\\u548c\\u62d4\\u793a\\u5df4\\u7684\\u6545\\u4e8b\\u4e2d\\uff0c\\u5927\\u536b\\u56fd\\u738b\\u7684\\u7f6a\\u6700\\u521d\\u88ab\\u9690\\u85cf\\u8d77\\u6765\\u3002\\u7136\\u800c\\uff0c\\u5148\\u77e5\\u62ff\\u5355\\u9762\\u5bf9\\u4ed6\\uff0c\\u63ed\\u793a\\u4e86\\u4ed6\\u7684\\u8fc7\\u5931\\u3002\\u5927\\u536b\\u7684\\u61ca\\u6094\\u8868\\u660e\\uff0c\\u5373\\u4f7f\\u9690\\u85cf\\u7684\\u7f6a\\u884c\\u4e5f\\u4f1a\\u88ab\\u63ed\\u9732\\uff0c\\u5728\\u4e0a\\u5e1d\\u773c\\u4e2d\\uff0c\\u516c\\u5e73\\u4e0e\\u95ee\\u8d23\\u6700\\u7ec8\\u4f1a\\u80dc\\u5229\\u3002\\"], \\"bible_life_cn\\": [\\"\\"], \\"bible_life_pinyin\\": [\\"d\\u00e0 w\\u00e8i h\\u00e9 b\\u00e1 sh\\u00ec b\\u0101 de g\\u00f9 sh\\u00ec zh\\u014dng, d\\u00e0 w\\u00e8i gu\\u00f3 w\\u00e1ng de zu\\u00ec zu\\u00ec ch\\u016b b\\u00e8i y\\u01d0n c\\u00e1ng q\\u01d0 l\\u00e1i. r\\u00e1n \\u00e9r, xi\\u0101n zh\\u012b n\\u00e1 d\\u0101n mi\\u00e0n du\\u00e0i t\\u0101, ji\\u0113 sh\\u00ec le t\\u0101 de gu\\u00f2 sh\\u012b. d\\u00e0 w\\u00e8i de \\u00e0o hu\\u01d0 bi\\u01ceo m\\u00edng, j\\u00ed sh\\u01d0 y\\u01d0n c\\u00e1ng de zu\\u00ec x\\u00edng y\\u011b hu\\u00ec b\\u00e8i ji\\u0113 l\\u00f9, z\\u00e0i sh\\u00e0ng d\\u00ec y\\u01cen zh\\u014dng, g\\u014dng p\\u00edng y\\u01d4 w\\u00e8n z\\u00e9 zu\\u00ei zh\\u014dng hu\\u00ec sh\\u00e8ng l\\u00ec.\\"]}", "refusal": null}, "logprobs": null, "finish_reason": "stop"}], "usage": {"prompt_tokens": 108, "completion_tokens": 302, "total_tokens": 410, "completion_tokens_details": {"reasoning_tokens": 0}}, "system_fingerprint": null}}, "error": null}\n'

# Decode the byte string and split into individual JSON objects
decoded_string = byte_string.decode('utf-8')
json_strings = decoded_string.strip().split('\n')
# Parse each JSON string into a dictionary

# Print the resulting list
for item in json_strings:
    # Parse the JSON string into a dictionary
    
    #json_object = json.loads(item)
    json_data = json.dumps(item, ensure_ascii=False)
    json_data = json_data.replace('\\"', '"')
    json_data = json_data.replace('\\"', '"')
    json_data = json_data.replace('\"', '"')
    json_data = json_data.replace('{\"', '"')
    print ("\njson_data1-->", json_data)
    #print (json_data)
    # Access the content value
    json_data = json_data.replace('"{', '{')
    json_data = json_data.replace('}"', '}')
    
    print ("json_data2-->", json_data)
    data_dict = json.loads(json_data)
    print ("data_dict-->", data_dict)
# Extract the value of the 'content' key
    content_value = data_dict['response']['body']['choices'][0]['message']['content']

    print(content_value)