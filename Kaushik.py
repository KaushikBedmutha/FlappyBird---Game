import Opencv


img = cv2.imread('meter_cabin.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to separate the meters from the background
thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)[1]

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize counters for rows and columns
row_count = 0
col_count = 0

# Loop through the contours and count the number of meters row-wise and column-wise
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if h > w:
        row_count += 1
    else:
        col_count += 1

# Print the row and column counts
print(f"Row count: {row_count}")
print(f"Column count: {col_count}")
