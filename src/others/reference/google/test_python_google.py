import requests
import os

google_api_key = os.environ.get('GOOGLE_API_KEY')

def google_search(api_key, cse_id, query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    api_key = 'AIzaSyBBBa5MIIZYXW7Ipbeespb1htgCl9Y_bOI'
    cse_id = "YOUR_CSE_ID"  # Replace with your Custom Search Engine ID
    query = input("Enter your search query: ")
    
    results = google_search(api_key, cse_id, query)
    
    if results:
        for item in results.get('items', []):
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print(f"Snippet: {item['snippet']}\n")
    else:
        print("Error fetching results.")

if __name__ == "__main__":
    main()