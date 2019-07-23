from PIL import Image
from urllib.request import urlopen

user = {
        'profile_img': 'image'
        }

url = f"https://test-bucket-xd.s3.us-east-2.amazonaws.com/images/{user['profile_img']}"

img = Image.open(urlopen(url))
img.show()
