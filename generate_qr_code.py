





import qrcode

def generate_qr_code(data, filename="qr_code.png"):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    sample_data = "https://www.example.com"
    generate_qr_code(sample_data)
