#requirement - pip3 install pillow
#Usage: python3 exif.py
#simple script that prints exif information for a user 
#prompted image name in the same directory as this script

from PIL import Image
from PIL.ExifTags import TAGS

#prompt user for name of image
imagename = input("Enter name of the image: ")

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")