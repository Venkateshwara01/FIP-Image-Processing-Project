import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# Sobel Edge Detection
def sobel_edge_detection(image):

    # Sobel kernels
    Gx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    Gy = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ])

    # Convert image to NumPy array
    image = np.array(image, dtype=float)

    # Create output arrays
    height, width = image.shape
    gradient_x = np.zeros((height, width))
    gradient_y = np.zeros((height, width))

    # Apply Sobel kernels
    for i in range(1, height - 1):
        for j in range(1, width - 1):

            region = image[i-1:i+2, j-1:j+2]

            gradient_x[i, j] = np.sum(region * Gx)
            gradient_y[i, j] = np.sum(region * Gy)

    # Calculate edge strength
    edges = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalize values to 0-255
    edges = edges / edges.max() * 255

    return edges.astype(np.uint8)

# Prewitt Edge Detection
def prewitt_edge_detection(image):

    # Prewitt kernels
    Gx = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])

    Gy = np.array([
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ])

    # Convert image to NumPy array
    image = np.array(image, dtype=float)

    # Get image dimensions
    height, width = image.shape

    # Create output arrays
    gradient_x = np.zeros((height, width))
    gradient_y = np.zeros((height, width))

    # Apply Prewitt kernels
    for i in range(1, height - 1):
        for j in range(1, width - 1):

            region = image[i-1:i+2, j-1:j+2]

            gradient_x[i, j] = np.sum(region * Gx)
            gradient_y[i, j] = np.sum(region * Gy)

    # Calculate edge strength
    edges = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalize to 0-255
    if edges.max() > 0:
        edges = edges / edges.max() * 255

    return edges.astype(np.uint8)

# Laplacian Edge Detection
def laplacian_edge_detection(image):

    # Laplacian kernel
    kernel = np.array([
        [ 0,  1,  0],
        [ 1, -4,  1],
        [ 0,  1,  0]
    ])

    # Convert image to NumPy array
    image = np.array(image, dtype=float)

    # Get image dimensions
    height, width = image.shape

    # Create output array
    edges = np.zeros((height, width))

    # Apply Laplacian kernel
    for i in range(1, height - 1):
        for j in range(1, width - 1):

            region = image[i-1:i+2, j-1:j+2]

            edges[i, j] = np.sum(region * kernel)

    # Take absolute values
    edges = np.abs(edges)

    # Normalize to 0-255
    if edges.max() > 0:
        edges = edges / edges.max() * 255

    return edges.astype(np.uint8)



