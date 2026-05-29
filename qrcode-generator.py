import qrcode


# Generate QR code
img = qrcode.make("https://www.bioxsystems.com/")

# Save image
img.save("qrcode.png")

print("QR code generated successfully and saved as 'qrcode.png'.")