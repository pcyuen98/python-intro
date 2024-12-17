import requests

def download_jpg(url, filename="image.jpg"):
  """Downloads a JPG image from the given URL and saves it with the specified filename.

  Args:
    url: The URL of the image.
    filename: The desired filename for the downloaded image (default: "image.jpg").
  """

  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception for unsuccessful requests

    # Check for JPG content type before downloading
    if response.headers['Content-Type'].startswith('image/jpeg'):
      with open(filename, 'wb') as f:
        for chunk in response.iter_content(1024):
          f.write(chunk)
      print(f"Image downloaded successfully: {filename}")
    else:
      print(f"URL doesn't point to a JPG image: {url}")

  except requests.exceptions.RequestException as e:
    print(f"Error downloading image: {e}")

# Example usage
image_url = "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=881849880777192"
download_jpg(image_url)