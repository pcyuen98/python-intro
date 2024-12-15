import vertexai
from vertexai.preview.generative_models import GenerativeModel, Image

class ImageProcessor:
    @staticmethod
    def process_image(image_path):
        PROJECT_ID = "gemini-440706"
        REGION = "us-central1"
        api_key = "AIzaSyBBBa5MIIZYXW7Ipbeespb1htgCl9Y_bOI"
        vertexai.init(project=PROJECT_ID, location=REGION, api_key=api_key)

        image = Image.load_from_file(image_path)

        generative_multimodal_model = GenerativeModel("gemini-1.5-flash-002")
        response = generative_multimodal_model.generate_content(["What is shown in this image?", image])
        return response

def main():
    image_path = "C:\\Users\\User\\Downloads\\backup\\999.jpg"
    result = ImageProcessor.process_image(image_path)
    print(result)

if __name__ == "__main__":
    main()
    
