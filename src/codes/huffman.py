
import heapq
from collections import Counter


# Node for Huffman Tree
class Node:
    def __init__(self, pixel, frequency):
        self.pixel = pixel
        self.frequency = frequency
        self.left = None
        self.right = None

    # Compare nodes based on frequency
    def __lt__(self, other):
        return self.frequency < other.frequency


# Build Huffman Tree
def build_huffman_tree(pixel_data):

    # Count frequency of each pixel
    frequency = Counter(pixel_data.flatten())

    # Create a priority queue
    heap = []

    # Create nodes for each pixel
    for pixel, count in frequency.items():
        node = Node(pixel, count)
        heapq.heappush(heap, node)

    # Combine nodes until one tree remains
    while len(heap) > 1:

        # Remove two nodes with lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new parent node
        merged = Node(None, left.frequency + right.frequency)

        merged.left = left
        merged.right = right

        # Insert parent node back into heap
        heapq.heappush(heap, merged)

    # Return the root of the tree
    return heap[0]

# Generate Huffman codes
def generate_codes(root):

    codes = {}

    def generate(node, current_code):

        # If node is a leaf, store its code
        if node.pixel is not None:
            codes[node.pixel] = current_code
            return

        # Traverse left with 0
        generate(node.left, current_code + "0")

        # Traverse right with 1
        generate(node.right, current_code + "1")

    generate(root, "")

    return codes

# Encode pixel data using Huffman codes
def encode_image(pixel_data, codes):

    encoded_data = ""

    # Convert each pixel into its Huffman code
    for pixel in pixel_data.flatten():
        encoded_data += codes[int(pixel)]

    return encoded_data


