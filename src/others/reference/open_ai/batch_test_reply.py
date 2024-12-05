from openai import OpenAI
client = OpenAI()

status = client.batches.retrieve("batch_66f3724442ec8190a69608a08d2295cd")

print("Status-->" , status)

file_response = client.files.content("file-Z3alyijaGt11tQLGzjn2KxDE")
print("result--->" , file_response.content)

temp_file = open("_temp_result.txt", "wb")
    
temp_file.write(file_response.content)

temp_file.close()