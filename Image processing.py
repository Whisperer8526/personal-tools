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

def binarize_image(img, clip_limit=40, threshold=80, max_val=255, blur=False, bl=3):
    import cv2
    clahe = cv2.createCLAHE(clipLimit=clip_limit)
    
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)             # conversion to BW
    image = cv2.equalizeHist(image)                      # histogram equalization
    image = clahe.apply(image)
    ret, image = cv2.threshold(image, threshold, max_val,  cv2.THRESH_OTSU)
    ret, image = cv2.threshold(image,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # image binarizatiom
    if blur:
        image = cv2.medianBlur(image, bl)                 # applying blur
    
    return image
