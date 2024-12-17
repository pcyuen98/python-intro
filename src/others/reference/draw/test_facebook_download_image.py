import requests

def download_facebook_photos(access_token):
    url = "https://graph.facebook.com/v13.0/me/photos"
    params = {
        "access_token": access_token
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "data" in data:
            for photo in data["data"]:
                image_url = photo["source"]
                save_path = f"photo_{photo['id']}.jpg"
                download_image(image_url, save_path)
        else:
            print("No photos found.")
    except requests.exceptions.RequestException as e:
        print("Error downloading photos:", e)

def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded successfully: {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error downloading the image:", e)

# Replace 'YOUR_ACCESS_TOKEN' with a valid user access token
access_token = '8f086fa5efa88b3cd22ccc634234b438'
download_facebook_photos(access_token)