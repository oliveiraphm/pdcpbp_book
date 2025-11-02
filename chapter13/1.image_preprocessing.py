from PIL import Image
import numpy as np
import cv2
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def show_image(image, title="Image"):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

image_url = "https://images.unsplash.com/photo-1593642532871-8b12e02d091c"
image = load_image_from_url(image_url)

print("Loaded Image from URL")
show_image(image, "Original Image")

def resize_and_crop(image, target_size):
    image = image.resize((target_size, target_size), Image.LANCZOS)
    return image

target_size = 256
processed_image = resize_and_crop(image, target_size)
show_image(processed_image, "Resized and Cropped Image")

def normalize(image):
    image_array = np.array(image)
    normalized_array = image_array / 255.0
    return normalized_array

def standardize(image):
    image_array = np.array(image)
    mean = np.mean(image_array, axis=(0,1), keepdims=True)
    std = np.std(image_array, axis=(0,1), keepdims=True)
    standardized_array = (image_array - mean) / std
    return standardized_array

normalized_image = normalize(processed_image)

show_image(normalized_image, "Normalized Image")

standardized_image = standardize(processed_image)

show_image(standardized_image, "Standardized Image")

mean_after = np.mean(standardized_image)
std_after = np.std(standardized_image)
print(f"Mean after standardization: {mean_after}")
print(f"Standar deviation after standardization: {std_after}")

assert np.isclose(mean_after, 0, atol=1e-6)
assert np.isclose(std_after, 1, atol=1e-6)
print("Standardization completed successfully.")

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

def augment_image(image):
    image = np.expand_dims(image, axis=0)
    augmented_iter = datagen.flow(image, batch_size=1)
    augmented_image = next(augmented_iter)[0]
    return augmented_image

augmented_image = augment_image(normalized_image)

show_image(augmented_image, "Augmented Image")

tensor_image = tf.convert_to_tensor(augmented_image, dtype=tf.float32)

def tensor_to_image(tensor):
    tensor = tensor.numpy()
    tensor = np.clip(tensor, 0, 1)
    return tensor

def add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy_image = np.copy(image)
    num_salt = np.ceil(salt_prob * image.size)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 0

    return noisy_image

use_salt_and_pepper_noise = False

if use_salt_and_pepper_noise:
    noisy_image = add_salt_and_pepper_noise(tensor_to_image(tensor_image))
    show_image(noisy_image, "Salt-and-Pepper Noisy Image")

else:
    noisy_image = tensor_to_image(tensor_image)
    show_image(noisy_image, "Original Image (No Noise)")

def gaussian_blur(image):
    blurred_image = cv2.GaussianBlur(image, (5,5), 0)
    return blurred_image

def median_blur(image):
    image_uint8 = (image * 255).astype(np.uint8)
    blurred_image = cv2.medianBlur(image_uint8, 5)
    blurred_image = blurred_image / 255.0
    return blurred_image

def bilateral_filter(image):
    image_uint8 = (image * 255).astype(np.uint8)
    filtered_image = cv2.bilateralFilter(image_uint8, 9, 75, 75)
    filtered_image = filtered_image / 255.0
    return filtered_image

def remove_noise(image):
    image_uint8 = (image * 255).astype(np.uint8)
    denoised_image = cv2.fastNlMeansDenoisingColored(image_uint8, None, h=10, templateWindowSize=7, searchWindowSize=21)
    denoised_image = denoised_image / 255.0
    return denoised_image

blurred_image = gaussian_blur(noisy_image)
show_image(blurred_image, "Gaussian Blur")

median_blurred_image = median_blur(noisy_image)
show_image(median_blurred_image, "Median Blur")

bilateral_filtered_image = bilateral_filter(noisy_image)
show_image(bilateral_filtered_image, "Bilateral Filter")

denoised_image = remove_noise(noisy_image)
show_image(denoised_image, "Non-Local Means Denoising")