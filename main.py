from edge_detection import (
    sobel_edge_detection,
    prewitt_edge_detection,
    laplacian_edge_detection
)
from huffman import build_huffman_tree, generate_codes, encode_image
from decompression import decode_image

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = Image.open("cameraman.tif")

# Convert to grayscale
gray_image = image.convert("L")

# Convert image into a NumPy array
pixel_data = np.array(gray_image)

# Display image
plt.imshow(pixel_data, cmap="gray")
plt.title("Cameraman Grayscale Image")
plt.axis("off")
plt.savefig("outputs/original_image.png")
plt.show()

# Print image dimensions
print("Image dimensions:", pixel_data.shape)

# Print pixel values
print("Pixel values:")
print(pixel_data[:5, :5])

# Calculate frequency of each pixel value
unique_values, counts = np.unique(pixel_data, return_counts=True)

print("\nPixel Frequency:")
for value, count in zip(unique_values, counts):
    print(f"Pixel value {value}: {count} times")

print("\nTotal unique pixel values:", len(unique_values))

# Build Huffman Tree
root = build_huffman_tree(pixel_data)

# Generate Huffman codes
codes = generate_codes(root)

# Encode the image
encoded_data = encode_image(pixel_data, codes)

print("\n--- Huffman Compression Results ---")
print("Number of Huffman codes:", len(codes))
print("Encoded data length:", len(encoded_data), "bits")

# Decode the encoded data
decoded_pixels = decode_image(encoded_data, root)

# Convert decoded pixels into original image dimensions
decoded_image = np.array(decoded_pixels).reshape(pixel_data.shape)
Image.fromarray(decoded_image.astype(np.uint8)).save("outputs/huffman_reconstructed.png")

# Verify image reconstruction
if np.array_equal(pixel_data, decoded_image):
    print("Decompression successful!")
    print("Original and decoded images are identical.")
else:
    print("Decompression failed!")

# Calculate original image size in bits
original_size = pixel_data.size * 8

# Calculate compressed size in bits
compressed_size = len(encoded_data)

# Calculate compression ratio
compression_ratio = original_size / compressed_size

# Calculate percentage of space saved
space_saved = ((original_size - compressed_size) / original_size) * 100
# Calculate Image Entropy
probabilities = counts / pixel_data.size

entropy = -np.sum(probabilities * np.log2(probabilities))

# Calculate Average Huffman Code Length
average_code_length = sum(
    probabilities[i] * len(codes[value])
    for i, value in enumerate(unique_values)
)
# Calculate Coding Efficiency
coding_efficiency = (entropy / average_code_length) * 100

print("\n--- Compression Performance ---")
print("Original size:", original_size, "bits")
print("Compressed size:", compressed_size, "bits")
print("Compression ratio:", round(compression_ratio, 2))
print("Space saved:", round(space_saved, 2), "%")
print("Huffman Coding Efficiency:", round(coding_efficiency, 2), "%")

# Apply Sobel operator
sobel_result = sobel_edge_detection(gray_image)

# Display Sobel result
plt.imshow(sobel_result, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")
plt.savefig("outputs/sobel_edges.png")
plt.show()

# Prewitt Edge Detection
prewitt_result = prewitt_edge_detection(gray_image)

plt.imshow(prewitt_result, cmap="gray")
plt.title("Prewitt Edge Detection")
plt.axis("off")
plt.savefig("outputs/prewitt_edges.png")
plt.show()

# Laplacian Edge Detection
laplacian_result = laplacian_edge_detection(gray_image)

plt.imshow(laplacian_result, cmap="gray")
plt.title("Laplacian Edge Detection")
plt.axis("off")
plt.savefig("outputs/laplacian_edges.png")
plt.show()

# Compare Edge Detection Methods

plt.figure(figsize=(12, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Sobel result
plt.subplot(2, 2, 2)
plt.imshow(sobel_result, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")
plt.savefig("outputs/sobel_edges.png")

# Prewitt result
plt.subplot(2, 2, 3)
plt.imshow(prewitt_result, cmap="gray")
plt.title("Prewitt Edge Detection")
plt.axis("off")
plt.savefig("outputs/prewitt_edges.png")
# Laplacian result
plt.subplot(2, 2, 4)
plt.imshow(laplacian_result, cmap="gray")
plt.title("Laplacian Edge Detection")
plt.axis("off")
plt.savefig("outputs/laplacian_edges.png")

# Display all images together
plt.tight_layout()
plt.savefig("outputs/edge_detection_comparison.png", dpi=300, bbox_inches="tight")
plt.show()

difference = np.abs(sobel_result.astype(int) - prewitt_result.astype(int))

print("\n--- Sobel vs Prewitt Comparison ---")
print("Mean pixel difference:", np.mean(difference))
print("Maximum pixel difference:", np.max(difference))

# TWO FINAL GRAPHS FOR FIP REPORT
import matplotlib.pyplot as plt
import numpy as np

# Create output figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

fig.suptitle(
    "Huffman Compression Results",
    fontsize=16,
    fontweight="bold"
)

# GRAPH 1: GRAYSCALE IMAGE HISTOGRAM
axes[0].hist(
    pixel_data.flatten(),
    bins=256,
    range=(0, 256),
    color="gray",
    edgecolor="black",
    linewidth=0.3
)

axes[0].set_title("Grayscale Image Histogram")
axes[0].set_xlabel("Pixel Intensity")
axes[0].set_ylabel("Frequency")

axes[0].grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# GRAPH 2: ORIGINAL VS COMPRESSED SIZE
sizes_kb = [
    original_size / 8192,
    compressed_size / 8192
]

labels = ["Original Image", "Compressed Image"]

axes[1].bar(
    labels,
    sizes_kb,
    width=0.197,  # Approximately 0.5 cm
    color=["steelblue", "seagreen"]
)

axes[1].set_title("Original vs Compressed Image Size")
axes[1].set_ylabel("Size (KB)")

axes[1].grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add value labels
for i, value in enumerate(sizes_kb):
    axes[1].text(
        i,
        value,
        f"{value:.2f} KB",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "outputs/combined_graphs.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Two graphs generated successfully!")
print("Saved at outputs/combined_graphs.png")

