from PIL import Image

# Load the uploaded image
image_path = "/mnt/data/WhatsApp Image 2025-03-29 at 07.40.50_d86755ad.jpg"
image = Image.open(image_path)

# Display the image to verify
image.show()
