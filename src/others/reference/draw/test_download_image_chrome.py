from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

class ChromeImageDownloader:

    @staticmethod
    def download_image(url, filename):
        """Downloads an image from the given URL using Selenium WebDriver.

        Args:
          url: The URL of the image.
        """

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        try:
            # Find the image element
            image_element = driver.find_element(By.TAG_NAME, "img")

            # Get the image source URL
            image_src = image_element.get_attribute("src")

            # Download the image
            response = requests.get(image_src, stream=True)
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Image downloaded successfully:", filename)
        except Exception as e:
            print(f"Error downloading image: {e}")
        finally:
            driver.quit()

if __name__ == "__main__":
    url = "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1436189330079564"  # Replace with the actual image URL
    ChromeImageDownloader.download_image(url)