import cv2
import numpy as np
import sys

def deskew_image(image_path, output_path="deskewed_output.jpg"):
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Convert to binary using OTSU threshold
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Invert if background is white and text is black
    if np.mean(thresh) > 127:
        thresh = cv2.bitwise_not(thresh)
    
    # Get coordinates of non-zero pixels
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    
    # Correct angle
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    
    # Rotate image
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h),
                             flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    cv2.imwrite(output_path, rotated)
    print(f"Deskewed image saved as: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python deskew.py <image_path> [output_path]")
    else:
        image_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else "deskewed_output.jpg"
        deskew_image(image_path, output_path)
