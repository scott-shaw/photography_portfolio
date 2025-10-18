from PIL import Image
import os
import argparse
from tqdm import tqdm


def reduce_image_size(image_path, output_path, max_size_kb, quality=85):
    """
    Reduces the size of an image if it exceeds a specified limit.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the processed image.
        max_size_kb (int): Maximum desired file size in kilobytes.
        quality (int): Initial JPEG quality (0-100).
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Convert to RGB if not already (important for saving as JPEG)
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        # Get initial file size
        initial_size_bytes = os.path.getsize(image_path)
        initial_size_kb = initial_size_bytes / 1024

        if initial_size_kb <= max_size_kb:
            print(
                f"Image '{
                    os.path.basename(image_path)
                }' is already within the size limit ({initial_size_kb:.2f} KB)."
            )
            # Optionally, copy the original to output_path if it's not the same
            if image_path != output_path:
                img.save(output_path)
            return

        print(
            f"Reducing size of '{os.path.basename(image_path)}' (Initial: {
                initial_size_kb:.2f} KB)..."
        )

        # Iteratively reduce quality until size limit is met
        current_quality = quality
        while True:
            # Save with current quality and optimize
            img.save(output_path, "JPEG", quality=current_quality, optimize=True)
            processed_size_bytes = os.path.getsize(output_path)
            processed_size_kb = processed_size_bytes / 1024

            if processed_size_kb <= max_size_kb or current_quality <= 10:
                print(
                    f"Reduced to {processed_size_kb:.2f} KB with quality {
                        current_quality
                    }."
                )
                break

            # Reduce quality for next iteration
            current_quality -= 5
            if current_quality < 0:  # Ensure quality doesn't go below 0
                current_quality = 0

    except FileNotFoundError:
        print(f"Error: Image not found at '{image_path}'")
    except Exception as e:
        print(f"An error occurred while processing '{image_path}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reduce image file sizes.")
    parser.add_argument("dir", type=str, help="The path to the input files.")
    parser.add_argument("max_size", type=int, help="Max image size in KB.")
    args = parser.parse_args()

    for filename in tqdm(os.listdir(args.dir), desc=f"Processing {args.dir}"):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            file_path = os.path.join(args.dir, filename)
            reduce_image_size(file_path, file_path, args.max_size)
