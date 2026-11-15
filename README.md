# Fundamentals of Image Processing (FIP)

## Image Compression using Huffman Coding and Edge Detection

## Project Overview

This project demonstrates two fundamental techniques in image processing:

- **Image Compression:** Huffman Coding for lossless image compression.
- **Edge Detection:** Sobel, Prewitt, and Laplacian operators for identifying edges in grayscale images.

The project uses the `cameraman.tif` grayscale image with dimensions of 256 × 256 pixels.

## Objectives

- Implement Huffman Coding for lossless image compression.
- Reduce image storage size using variable-length encoding.
- Perform edge detection using Sobel, Prewitt, and Laplacian operators.
- Compare the results of different edge detection techniques.
- Analyze compression performance using quantitative metrics.

## Technologies Used

- Python
- NumPy
- OpenCV
- Matplotlib
- VS Code IDE

## 📂 Project Structure

```text
FIP-Project/
│
├── README.md
├── cameraman.tif
├── main.py
├── huffman.py
├── decompression.py
├── edge_detection.py
│
├── results/
│   ├── huffman_recontructed.png
│   ├── sobel_edges.png
│   ├── prewitt_edges.png
│   └── laplacian_edges.png
│
└── report/
    └── FIP_Project_Report.pdf
```
## Execution
    python main.py
## Part A: Huffman Coding

Huffman Coding is a lossless compression technique that assigns variable-length binary codes to pixel values based on their frequencies.

### Working Steps

1. Read the grayscale image.
2. Calculate the frequency of each unique pixel value.
3. Construct the Huffman tree.
4. Generate binary codes for each pixel value.
5. Encode the image data.
6. Decode the compressed data.
7. Verify that the reconstructed image is identical to the original.

### Results

| Metric              |        Value |
| ------------------- | -----------: |
| Image Dimensions    |    256 × 256 |
| Unique Pixel Values |          247 |
| Original Size       | 524,288 bits |
| Encoded Size       | 461,689 bits |
| Compression Ratio   |       1.14:1 |
| Space Saved         |       11.94% |
| Coding Efficiency   |        99.5% |
| Decompression       |   Successful |
| Reconstruction      |     Lossless |

## Part B: Edge Detection

Edge detection identifies boundaries and changes in intensity within an image.

### 1. Sobel Operator

The Sobel operator uses horizontal and vertical gradient kernels to detect edges. It provides clear edge detection and incorporates smoothing to reduce some noise.

### 2. Prewitt Operator

The Prewitt operator uses simple horizontal and vertical kernels to detect intensity changes. Its output is similar to Sobel.

### 3. Laplacian Operator

The Laplacian operator uses the second derivative to identify rapid intensity changes. It detects edges in multiple directions but is more sensitive to noise.

### Edge Detection Comparison

| Operator  | Principle               | Characteristics                     |
| --------- | ----------------------- | ----------------------------------- |
| Sobel     | First-order gradient    | Clear and smooth edges              |
| Prewitt   | First-order gradient    | Simple edge detection               |
| Laplacian | Second-order derivative | Detects fine edges; noise-sensitive |

### Sobel vs Prewitt Quantitative Comparison

| Metric                   | Result |
| ------------------------ | -----: |
| Mean Pixel Difference    | 1.4389 |
| Maximum Pixel Difference |     56 |

The Sobel and Prewitt outputs are visually similar, but small pixel-level differences exist.

## Project Outcomes

- Successfully implemented Huffman Coding.
- Achieved lossless reconstruction of the original image.
- Obtained a compression ratio of 1.14:1.
- Successfully detected edges using Sobel, Prewitt, and Laplacian operators.
- Compared the visual and quantitative performance of edge detection techniques.

## Future Scope

- Test Huffman Coding on different image formats and sizes.
- Explore advanced compression techniques.
- Apply edge detection to medical images, including knee images.
- Compare additional edge detection algorithms.
- Improve noise reduction before edge detection.

## Team Members

Mohammed Ardaan Ansar

Venkateshwara UD

Aman D Silva

Akmar Hussain K

## Academic Project

Fundamentals of Image Processing (FIP)

BTech Computer Science and Engineering

St Aloysius (Deemed to be University), Mangaluru
