import os

draft_path = os.environ.get('IMAGE_DRAFT_PATH')

# List all files in the directory
files_list = os.listdir(draft_path)

# Iterate through the files in the directory
for filename in files_list:
    #print (filename , "is file-->", os.path.isfile(filename))
    if not filename.startswith("name=") :
        print (filename)
        # Construct the new filename by removing the prefix "name="
        #new_filename = filename.replace("name=", "")
        
        # Rename the file
        #os.rename(os.path.join(draft_path, filename), os.path.join(draft_path, "name=" + filename))
        #print(f"Renamed {filename} to {new_filename}")