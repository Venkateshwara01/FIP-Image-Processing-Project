
# Decode Huffman encoded data
def decode_image(encoded_data, root):

    decoded_pixels = []

    current = root

    # Read each bit
    for bit in encoded_data:

        # Move left for 0
        if bit == "0":
            current = current.left

        # Move right for 1
        else:
            current = current.right

        # If leaf node is reached
        if current.pixel is not None:

            # Store original pixel value
            decoded_pixels.append(current.pixel)

            # Return to root
            current = root

    return decoded_pixels
