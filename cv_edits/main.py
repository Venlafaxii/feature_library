import cv2
import numpy as np
from pathlib import Path

base_dir = Path(__file__).resolve().parent
image_path = base_dir / "3.jpg"

image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

# 2. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# 3. Adjust Light / Brightness
bright_image = cv2.convertScaleAbs(image, alpha=1.0, beta=50)

# 4. Add a Radial Light Source / Spotlight effect
rows, cols, _ = image.shape
mask = np.zeros((rows, cols), dtype=np.uint8)
cv2.circle(mask, (cols // 2, rows // 2), min(rows, cols) // 3, 255, -1)
mask_blur = cv2.GaussianBlur(mask, (101, 101), 0) / 255.0

light_spotlight = np.zeros_like(image)
for i in range(3):
    light_spotlight[:, :, i] = np.clip(image[:, :, i] * mask_blur + 30, 0, 255).astype(np.uint8)

# 5. Motion Blur
kernel_size = 15
kernel_motion = np.zeros((kernel_size, kernel_size))
kernel_motion[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
kernel_motion = kernel_motion / kernel_size
motion_blur = cv2.filter2D(image, -1, kernel_motion)

# Save the results
cv2.imwrite(str(base_dir / "gaussian_blur.jpg"), gaussian_blur)
cv2.imwrite(str(base_dir / "bright_image.jpg"), bright_image)
cv2.imwrite(str(base_dir / "light_spotlight.jpg"), light_spotlight)
cv2.imwrite(str(base_dir / "motion_blur.jpg"), motion_blur)