import cv2
from PIL import Image

hereid_path = 'hereid.jpg'
cat_path = 'cat.jpg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
hereid_image = cv2.imread(hereid_path)
cat_image = cv2.imread(cat_path)
hereid_face = cat_face_cascade.detectMultiScale(hereid_image)
cat_face = cat_face_cascade.detectMultiScale(cat_image)

hereid = Image.open(hereid_path)
cat = Image.open(cat_path)
glasses = Image.open('glasses.png')
hereid = hereid.convert("RGBA")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for(x,y,w,h) in hereid_face:
    glasses = glasses.resize((w, int(h/3)))
    hereid.paste(glasses, (x, int(y + h/4)), glasses)
    hereid.save("hereid_with_glasses.png")
    print("Hereid with glasses saved")
for(x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y/1.7 + h/3)), glasses)
    cat.save("cat_with_glasses.png")
    print("Cat with glasses saved")