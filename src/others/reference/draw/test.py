# iLibrary imports

# Importing PyTorch library, for building and training neural networks
import torch
import os
# Importing StableDiffusionPipeline to use pre-trained Stable Diffusion models
from diffusers import StableDiffusionPipeline
from diffusers import DiffusionPipeline
# Image is a class for the PIL module to visualize images in a Python Notebook
from PIL import Image

import time
import json
import traceback
# Creating pipeline 
# use torch.float32 for CPU, half floats (float16) not supported on Intel for this module
#pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
#                                                  torch_dtype=torch.float32)

#pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float32, use_safetensors=True)


pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5",
                                                  torch_dtype=torch.float32)
pipeline.to("cpu")
pipeline.unet.to(memory_format=torch.channels_last)
pipeline.unet = torch.compile(pipeline.unet, mode="reduce-overhead", fullgraph=True)
# only do 1 image for CPU let's not get too crazy

import pymysql as MySQLdb

class ProverbDrawTest:
    
    @staticmethod
    def get_random_pic(heritage_type, is_gospel):
        conn = MySQLdb.connect(host="219.93.129.18", user="super_user", passwd="Reindeer..7!", db="eyebot_agent")
        cursor = conn.cursor()
        gospel_sql = ""
        if is_gospel is False:
            gospel_sql = " and is_gospel = 0 "
        else:
            gospel_sql = " and is_gospel = 1"   
        sql = "SELECT h.heritage_name, h.en, h.history_en, h.heritage_type FROM heritage AS h  WHERE h.heritage_type = " + str(heritage_type) + str(gospel_sql) + " and is_approve is NULL ORDER BY RAND() LIMIT 1"
        print('sql->', sql)
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        myresult = cursor.fetchall()

        if not myresult:
            print("result is None")
            return '{}'

        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))

        heritage_json = json.dumps(json_data, indent=4, sort_keys=True, default=str)
        #print('json_str-->', heritage_json)
        return heritage_json

    @staticmethod
    def getAnimal():
        conn = MySQLdb.connect(host="219.93.129.18", user="super_user", passwd="Reindeer..7!", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "SELECT * from animal " # where animal_type = " + str(animal_type)
        #print('sql->', sql)
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        myresult = cursor.fetchall()

        if not myresult:
            print("result is None")
            return '{}'

        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))

        animal_json = json.dumps(json_data, indent=4, sort_keys=True, default=str)
        #print('json_str-->', animal_json)
        return animal_json

    @staticmethod
    def image_grid(imgs, rows, cols):
        assert len(imgs) == rows*cols
    
        w, h = imgs[0].size
        grid = Image.new('RGB', size = (cols*w,
                                   rows * w))
        grid_w, grid_h = grid.size
    
        for i, img in enumerate(imgs):
            grid.paste(img, box = (i%cols*w, i // cols*h))
        return grid

    @staticmethod
    def generateAnimal(animal_name, heritage_name ,desc, type):
        prompt_head = "A professional photo of " + animal_name + " in the middle of the picture." + desc
        animal_remove_space = animal_name.replace(' ', '_')
        heritage_name_remove_space = heritage_name.replace(' ', '_')
        file_name = animal_remove_space + "-" + heritage_name_remove_space + "-" + type
        ProverbDrawTest.generate(prompt_head, file_name)

    @staticmethod
    def generatePlain(heritage_name, desc, type):
        prompt_head = "A professional photo of " + heritage_name + "." + desc
        heritage_name_remove_space = heritage_name.replace(' ', '_')
        file_name = heritage_name_remove_space + "-" + type
        ProverbDrawTest.generate(prompt_head, file_name)
             
    @staticmethod
    def generate(prompt_head, file_name):
        n_images = 1 # Let's generate 6 images based on the prompt below
        
        print ("generating-->" + file_name)
        file_path = file_name + ".jpg"
        
        if os.path.exists(file_path):
            print(f"The file '{file_path}' exists. skipping")
        else:
            print(f"The file '{file_path}' does not exist.")
            prompt = [prompt_head] * n_images
     #   height = 256
     #   width = 256
     #   num_inference_steps = 20
     #   images = pipeline(prompt,height,width).images

            images = pipeline(prompt_head).images
            grid = ProverbDrawTest.image_grid(images, rows=1, cols=1)
            grid.save(file_name + ".jpg")
            
if __name__ == '__main__':

    animal_json = ProverbDrawTest.getAnimal()

    animal_obj = json.loads(animal_json)
    for animal_data in animal_obj:
        animal_name = animal_data["animal"]
        animal_type = animal_data["animal_type"]
        heritage_json = ProverbDrawTest.get_random_pic("1", False)
        heritage_obj = json.loads(heritage_json)
        en =  heritage_obj[0].get("en")
        history =  heritage_obj[0].get("history_en")
        heritage_name = heritage_obj[0].get("heritage_name")

        try:
            print ('heritage_name-->' , heritage_name)
            ProverbDrawTest.generatePlain("name=" + heritage_name , " with a group of birds flying ", "key=bird")
            ProverbDrawTest.generatePlain("name=" + heritage_name , " with a big sun ", "key=sun")
            ProverbDrawTest.generatePlain("name=" + heritage_name , " with a big moon ", "key=moon")
        except Exception as error:
            print("Loop error An exception occurred:", error)
            print(traceback.format_exc())
            #time.sleep(3)   


       #  ProverbDrawTest.generatePlain(heritage_name , history, "plain_history_add=rainbow")

        #ProverbDrawTest.generateAnimal(animal_name, heritage_name , "", "animal_")
        #ProverbDrawTest.generateAnimal(animal_name, heritage_name , en, "animal_en")
        #ProverbDrawTest.generateAnimal(animal_name, heritage_name , history, "animal_history")

        
        

       # ProverbDrawTest.generatePlain("name=" + heritage_name , ", a beautiful cat, raining. ", "plain_key=cat_beauty")

