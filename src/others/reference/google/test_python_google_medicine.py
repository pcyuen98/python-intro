import requests
import os
import re
from bin.others.reference.draw.test_check_image import ImageUrlValidator
from bin.others.reference.draw.test_draw_image import ImageDownloader
from others.reference.draw.test_download_image_chrome import ChromeImageDownloader

google_api_key = os.environ.get('GOOGLE_API_KEY')

def google_search(api_key, cse_id, query, start=1):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'start': start
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def clean_text(text):

    text = text.replace(" ", "_")

  # Remove all non-alphanumeric characters except underscores
    cleaned_text = re.sub(r"[^\w_]", "", text)

    return cleaned_text + ".jpg"

def main():
    api_key = 'AIzaSyAzuH4xXqNC0Cs2D91nDU5L03DFJYFS0jE'
    cse_id = "725a3b584d2264662"  # Replace with your Custom Search Engine ID
    query = input("Enter your search query: ")

    # Loop through 10 pages (1000 results)
    for start in range(1, 101, 10):
        results = google_search(api_key, cse_id, query, start=start)
        try:
            if results:
                for item in results.get('items', []):
                    print ('item-->', item)
                    print(f"Title: {item['title']}")
                    print(f"Link: {item['link']}")
                    print(f"Snippet: {item['snippet']}\n")
                    link = item.get("link")
                    title = item.get("title")
                    snippet = item.get("snippet")
                    src = item.get("pagemap", {}).get("cse_image", [{}])[0].get("src")
                    #if ImageUrlValidator.is_image_url(src):
                    ChromeImageDownloader.download_image(src, clean_text(title))
                    print('src-->', src)
            else:
                print(f"Error fetching results for start position {start}.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()