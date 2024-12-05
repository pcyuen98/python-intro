import requests

def get_x_frame_options_header(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    status: int = 400
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 404:
            status = 404
        
        x_frame_options_header = response.headers.get('X-Frame-Options')

        if x_frame_options_header is None:
            status = 200
        elif x_frame_options_header.lower() == 'sameorigin':
            status = 200
        else:
            status = 400
    except requests.exceptions.RequestException as e:
        status: int = 400
    print ('status-->', status)
    return status
# Example URL to test
url = "https://www.yelp.com/search?cflt=mamak&find_loc=Jln+Raja+Laut%2C+Kuala+Lumpur"

x_frame_options_header = get_x_frame_options_header(url)
print(f'X-Frame-Options Header: {x_frame_options_header}')