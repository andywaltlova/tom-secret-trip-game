from PIL import Image
import piexif

message = "FLAG-3: ZXJsb2cu"

im = Image.open("mystery_trip/static/panda_detective.jpg")
if "exif" in im.info:
    exif_dict = piexif.load(im.info["exif"])
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = message
    exif_bytes = piexif.dump(exif_dict)
else:
    exif_bytes = piexif.dump({"0th":{piexif.ImageIFD.ImageDescription:message}})

im.save("mystery_trip/static/panda_detective_secret.jpg", exif=exif_bytes)