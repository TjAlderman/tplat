# QR

This module seeks to create a QR code using the PyPi package qrcode (e.g. **Figure 1**).

<div align="center">
  <img src="data/qr_code.png" alt="Example QR code" width="50%">
  <p><em><strong>Figure 1:</strong> An example QR code created using the PyPi qrcode package.</em></p>
</div>

## API

## Usage

The following code was used to create the QR Code seen in **Figure 1**.

```python
from qrcode import QRCode, constants

# Create a QR code object with a larger size and higher error correction
qr = QRCode(version=3, box_size=20, border=10, error_correction=constants.ERROR_CORRECT_H)

# Define the data to be encoded in the QR code
data = "https://www.cameo.com/recipient/65b0cf9120691a9dc777450a?from_share_sheet=1&utm_campaign=video_share_to_copy"

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("projects/qr/docs/data/qr_code.png")
```