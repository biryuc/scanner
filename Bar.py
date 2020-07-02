import cv2
import numpy as np
import sys
import time

if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    inputImage = cv2.imread("qrcode.jpg")

# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    cv2.imshow("Results", im)

# Create a qrCodeDetector Object
qrDecoder = cv2.QRCodeDetector()

# Detect and decode the qrcode
t = time.time()
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
print("Time Taken for Detect and Decode : {:.3f} seconds".format(time.time() - t))
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)
cv2.imwrite("output.jpg",inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Display results
#
# cv2.imshow("Results", im)
#
# ## [imports]
# ## [imread]
# img = cv.imread(cv.samples.findFile("vm3.jpg"))
# ## [imread]
# ## [empty]
# if img is None:
#     sys.exit("Could not read the image.")
# ## [empty]
# ## [imshow]
# cv.imshow("Display window", img)
# k = cv.waitKey(0)
# ## [imshow]
# ## [imsave]
# if k == ord("s"):
#     cv.imwrite("vm3.jpg", img)
# ## [imsave]