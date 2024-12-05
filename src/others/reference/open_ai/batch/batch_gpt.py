import time
from openai._client import OpenAI
import traceback
from jsonpickle.backend import json
import datetime
class GPTBatch:

    @staticmethod
    def wait_gpt_batch(batch_data):
        while True:
            try:
                client = OpenAI()
                print ("batch_data json-->", batch_data)
                status = client.batches.retrieve(batch_data.id)
                
                utc_dt = datetime.datetime.utcfromtimestamp(status.created_at)
# Add 8 hours to convert to GMT+8
                created_at = utc_dt + datetime.timedelta(hours=8)
                print("created at" , created_at , " Status-->" , status)
                output_file_id = status.output_file_id
                print("Output File ID:", output_file_id)
                if output_file_id is None:
                    print("Output File ID is None. Re-trying")
                    time.sleep(10)
                else:
                    print("Output File ID:", output_file_id)
                    utc_dt = datetime.datetime.utcfromtimestamp(status.completed_at)
# Add 8 hours to convert to GMT+8
                    completed_at = utc_dt + datetime.timedelta(hours=8)
                    print("completed_at" , completed_at)
                    return output_file_id
                    break
           
            except Exception as error:
                print("wait_gpt_batch exception occurred," , error)
                print(traceback.format_exc())
                time.sleep(1)
    
    @staticmethod
    def fetch_gpt_batch_file(output_file_id):
        try:
            client = OpenAI()

            file_response = client.files.content(output_file_id)
            print("result--->" , file_response.content)

            temp_file = open("_temp_result.txt", "wb")
    
            temp_file.write(file_response.content)

            temp_file.close()
        except Exception as error:
            print("fetch_gpt_batch_file exception occurred," , error)
            print(traceback.format_exc())

    @staticmethod
    def send_gpt_batch_file(input_file):
        #input_file = "batchinput.jsonl"
        client = OpenAI()
        batch_input_file = client.files.create(
            file=open(input_file, "rb"),
            purpose="batch"
            )

        batch_input_file_id = batch_input_file.id

        batch_object = client.batches.create(
            input_file_id=batch_input_file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": "nightly eval job"
        })
        return batch_object

if __name__ == '__main__':
    batch_object = GPTBatch.send_gpt_batch_file("batchinput.jsonl")
    output_file_id = GPTBatch.wait_gpt_batch(batch_object)
    #GPTBatch.fetch_gpt_batch_file(output_file_id)
    #GPTBatch.fetch_gpt_batch_file('file-JSl6TLG1kQGQoNgtf1VsJyOG')