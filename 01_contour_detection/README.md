# Contour Detection with OpenCV

This simple OpenCV project demonstrates how to detect and draw contours from an image.

## 📌 What the script does

1. **Load an image** from disk.
2. **Convert it to grayscale** for easier processing.
3. **Apply binary thresholding** to simplify the image into black and white.
4. **Detect contours** using `cv2.findContours`.
5. **Draw all detected contours** over the original image using red lines.

## 🧠 Concepts used

- `cv2.imread()`: Load an image from disk.
- `cv2.cvtColor()`: Convert between color spaces (BGR ↔ grayscale).
- `cv2.threshold()`: Create a binary version of the grayscale image.
- `cv2.findContours()`: Detect edges and shapes in the binary image.
- `cv2.drawContours()`: Draw the found contours onto the image.

## 🖼️ Example

If the input image looks like this:

[images.jpeg]

The output will highlight the edges of all shapes in **red**.

## 💡 Notes

- You can change the threshold level (`127`) to see how it affects contour detection.
- Use other retrieval modes like `cv2.RETR_EXTERNAL` or approximation modes like `cv2.CHAIN_APPROX_NONE` to experiment further.

## ✅ Requirements

- Python
- OpenCV (`pip install opencv-python`)


