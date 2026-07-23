import qrcode
import os

def generate_qr_code(data, filename="qrcode.png", box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generates a QR Code for the given data and saves it as an image.
    
    Parameters:
    - data (str): The content to encode in the QR code (URL, text, etc.).
    - filename (str): The name of the output image file.
    - box_size (int): Size of each box (pixel height/width) in the QR code grid.
    - border (int): Thickness of the border (number of boxes).
    - fill_color (str): Color of the QR code itself.
    - back_color (str): Background color of the QR code.
    """
    try:
        # Create a QRCode object with customization options
        qr = qrcode.QRCode(
            version=1,  # controls the size of the QR Code (1 is 21x21 matrix, up to 40)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction (approx 30% or less errors corrected)
            box_size=box_size,
            border=border,
        )
        
        # Add data to the QR Code object
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save the image
        img.save(filename)
        print(f"Success! QR code saved as '{filename}'")
        
        # Return absolute path
        return os.path.abspath(filename)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print("--- Python QR Code Generator ---")
    data_to_encode = input("Enter the text or URL to encode: ").strip()
    if not data_to_encode:
        # Default fallback
        data_to_encode = "https://www.google.com"
        print(f"No input provided. Using default: {data_to_encode}")
        
    output_filename = input("Enter output file name (default: qrcode.png): ").strip()
    if not output_filename:
        output_filename = "qrcode.png"
        
    # Generate the QR Code
    filepath = generate_qr_code(data_to_encode, filename=output_filename)
    if filepath:
        print(f"QR code successfully generated at: {filepath}")
