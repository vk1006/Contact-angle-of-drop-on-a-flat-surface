import cv2
import numpy as np

def ellipse_gen(path,path2,c,threshold = 20):

    # Example preprocessing steps
    img = cv2.imread(path2  )
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)


    # In[13]:


    # Example thresholding
    _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key=cv2.contourArea)
    contours = [largest_contour]


    # In[34]:
    height,width,_ = image.shape

    # Define the distance threshold
    # Adjust this as needed

    # Create an empty list to store the updated contours

    updated_contours = []

    for contour in contours:
        updated_contour = []  # Initialize the updated contour for this segment

        for point in contour:
            x, y = point[0]

            # Calculate the vertical distance from the point to the line y = c
            distance = abs(y - c)

            # Check if the distance is greater than the threshold_distance
            if distance > threshold and x>threshold and x<width-threshold and y>threshold :
                updated_contour.append([[x, y]])  # Keep this point

        if updated_contour:
            updated_contours.append(np.array(updated_contour))
            


    # In[35]:


    temp  = img.copy()

    cv2.drawContours(temp, updated_contours, -1, (0, 0, 255), 2)

    # cv2.imwrite("Contoured_image.jpg",temp)
    # cv2.imshow('Image with contours', temp)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # In[17]:


    image_with_ellipse = image.copy()
    ellipse = cv2.fitEllipse(updated_contours[0])

    # Draw the fitted ellipse on the image
    cv2.ellipse(img, ellipse, (0, 0, 255), 2)  # You can adjust the color and thickness

    cv2.imwrite("Ellipse_fitted_on_image.jpg",img)

    # cv2.imshow('Image with Ellipse', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return [ellipse[0][0],ellipse[0][1],ellipse[1][0]/2,ellipse[1][1]/2]
#{xc,yc,a,b}