def load_image(img, resize=False, bw=False, img_size=256):
    import cv2
    
    image = cv2.imread(img)
    
    if resize:
        image = cv2.resize(image, (img_size, img_size))
    if bw:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image 

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
