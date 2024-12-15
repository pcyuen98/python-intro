import requests
from urllib.parse import urlparse


class ImageUrlValidator:
    """Class for validating URLs."""

    @staticmethod
    def is_image_url(url):
        """Checks if a given URL is an image URL.

        Args:
            url: The URL to check.

        Returns:
            True if the URL is an image URL, False otherwise.
        """

        try:
            response = requests.head(url)
            content_type = response.headers['Content-Type']
            return content_type.startswith('image/')
        except requests.exceptions.RequestException:
            # Handle exceptions, e.g., network errors, timeouts
            return False


# Main method for testing
def main():
    url = "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100064515558896"
    if ImageUrlValidator.is_image_url(url):
        print("It's an image URL!")
    else:
        print("It's not an image URL.")


if __name__ == "__main__":
    main()