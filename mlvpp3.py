import cv2
import os

# Define paths
INPUT_DIR = 'C:/Users/asus/Desktop/python/p3/'
OUTPUT_DIR = 'C:/Users/asus/Desktop/python/p3/outputs/'

# Check if input directory exists
if not os.path.exists(INPUT_DIR):
    print(f"Error: Directory '{INPUT_DIR}' does not exist.")
    exit(1)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process each image in the input directory
for image_name in os.listdir(INPUT_DIR):
    if image_name.endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(INPUT_DIR, image_name)

        # Load original image
        original = cv2.imread(image_path)
        if original is None:
            print(f"Could not load image: {image_name}")
            continue

        # Resize to uniform size
        original = cv2.resize(original, (400, 400))

        # === Level 1: Thumbnail version (Unrelated User) ===
        thumbnail = cv2.resize(original, (50, 50))
        thumbnail = cv2.resize(thumbnail, (400, 400), interpolation=cv2.INTER_NEAREST)

        # === Level 2: Partial Blur (Semi-related User) ===
        partial_blur = original.copy()
        (h, w) = partial_blur.shape[:2]
        partial_blur[0:h // 2, :] = cv2.GaussianBlur(partial_blur[0:h // 2, :], (31, 31), 0)

        # === Level 3: Full image (Fully-related User) ===
        full_view = original.copy()

        # Save outputs
        base_name = os.path.splitext(image_name)[0]
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base_name}_unrelated.jpg"), thumbnail)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base_name}_semi_related.jpg"), partial_blur)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"{base_name}_fully_related.jpg"), full_view)

        print(f"Processed: {image_name}")

print("Images generated for all three privacy levels in the 'outputs' folder.")
