import cv2
import os

image_path = "C:/Users/asus/Desktop/python/project/p2/input_image.jpg"

# Load original image
original = cv2.imread(image_path)

if original is None:
    raise ValueError("Could not load image!")

# Resize to uniform size
original = cv2.resize(original, (400, 400))

# === Level 1: Thumbnail version (Unrelated User) ===
thumbnail = cv2.resize(original, (50, 50))
thumbnail = cv2.resize(thumbnail, (400, 400), interpolation=cv2.INTER_NEAREST)

# === Level 2: Partial Blur (Semi-related User) ===
partial_blur = original.copy()
(h, w) = partial_blur.shape[:2]
partial_blur[0:h//2, :] = cv2.GaussianBlur(partial_blur[0:h//2, :], (31, 31), 0)

# === Level 3: Full image (Full-related User) ===
full_view = original.copy()

# Save outputs
os.makedirs('outputs', exist_ok=True)
cv2.imwrite('outputs/level1_unrelated.jpg', thumbnail)
cv2.imwrite('outputs/level2_semi_related.jpg', partial_blur)
cv2.imwrite('outputs/level3_full_related.jpg', full_view)

print("Images generated for all three privacy levels in the 'outputs' folder.")


