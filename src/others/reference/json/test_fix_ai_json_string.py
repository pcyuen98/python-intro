import re
import json

class YelpDataExtractor:
    @staticmethod
    def fix_json_incomplete(data):

        # Use a regular expression to find all objects in curly braces
        objects = re.findall(r'\{[^}]*\}', data)

        # Join the extracted objects into a single string separated by commas
        result = ', '.join(obj.strip() for obj in objects)

        # Wrap the result in square brackets to make it a valid JSON array
        result = "[" + result + "]"

        # Parse the JSON string and dump it back as a formatted JSON string
        json_obj = json.loads(result)
        json_dumps = json.dumps(json_obj, indent=4)

        return json_dumps

# JSON with incomplete bracket
data = '''[  {
    "title": "NS Al-Falah",

    "pros_cons_my": "Kelebihan: Ayam Biryani adalah hidangan India yang lazat dan popular. Kelemahan: Ayam Biryani tinggi karbohidrat dan boleh menyebabkan lonjakan gula dalam darah.",
    "food_related_or_others": "food",
    "image_type": 9
  },{
    "title": "NS Al-Falah",

    "pros_cons_my": "Kelebihan: Ayam Biryani adalah hidangan India yang lazat dan popular. Kelemahan: Ayam Biryani tinggi karbohidrat dan boleh menyebabkan lonjakan gula dalam darah.",
    "food_related_or_others": "food",
    "image_type": 9
  },
  {
    "title": "Ali, Muthu & Ah Hock",
    "link": "https://www.yelp.com/search?cflt=mamak&find_loc=Jln+Raja+Laut%2C+Kuala+Lumpur",
    "image_url": "https://s3-media0.fl.yelpcdn.com/assets/srv0/yelp_large_assets/a8d26394324f/assets/img/seo_metadata/yelp_og_image.png",
    "description": "Best mamak in Kuala Lumpur - Restoran SK Corner, Nasi Kandar Pelita, Alor Food Corner, FS Nasi Kandar, RSMY, NS Al-Falah, Ali, Muthu & Ah Hock, WonderMama,\u00a0...",
    "description_my": "Mamak terbaik di
'''

json_data = YelpDataExtractor.fix_json_incomplete(data)
print(json_data)