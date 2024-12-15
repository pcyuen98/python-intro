import requests

class ImageDownloader:
    @staticmethod
    def download_image(url, save_path):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_path, 'wb') as file:
                    file.write(response.content)
                print("Image downloaded successfully!")
            else:
                print("Failed to download image. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error downloading the image:", e)

    @staticmethod
    def main():
        # URL of the image you want to download
        #image_url = "https://eyebot.name.my/pic/heritage/draft/name%3DTe_Ana_Maori_Rock_Art_Site%2C_Christchurch%2C_New_Zealand-key%3Dmoon.jpg"
        image_url = 'https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100063681397762'
        # Path where you want to save the downloaded image
        save_path = "downloaded_image.jpg"

        # Call the static method to download the image
        ImageDownloader.download_image(image_url, save_path)

if __name__ == '__main__':
# Call the main method of the ImageDownloader class
    ImageDownloader.main()