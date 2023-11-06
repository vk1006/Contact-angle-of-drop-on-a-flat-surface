import cv2
import numpy as np

def line_gen(path):
    # Load the image

    image = cv2.imread(path)

    img = image.copy()

    # Convert the image to grayscale
    gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred1 = cv2.GaussianBlur(gray1, (5, 5), 0)

    # Perform edge detection using the Canny edge detector with adjusted parameters
    edges1 = cv2.Canny(blurred1, 30, 70)  # Adjust these thresholds as needed

    # Use the Hough Line Transform to detect lines
    lines = cv2.HoughLines(edges1, 1, np.pi / 180, threshold=100)

    c = None

    if lines is not None:
        # Initialize variables to keep track of the line with the largest distance from the top
        max_distance = -1
        top_line = None

        # Iterate through the detected lines
        for rho, theta in lines[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            
            # Calculate the distance from the top of the image to the line
            distance = y1

            # If this line has a greater distance, update the max_distance and top_line
            if distance > max_distance:
                max_distance = distance
                c = y1
                top_line = (x1, y1, x2, y2)

        if top_line is not None:
            # Draw the line with the largest distance on the original image
            x1, y1, x2, y2 = top_line
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Adjust color and thickness as needed
            cv2.imwrite("Line_image.jpg",img)
            return c

            # Display or save the image with the detected line
    #         cv2.imshow('Image with Top Line', img)
    #         cv2.waitKey(0)
    #         cv2.destroyAllWindows()
        else:
            print("No lines detected.")
    else:
        print("No lines detected.")
