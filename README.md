# QR Code Generator for Biox Systems (Python Project)

## Overview

This project is a simple QR Code Generator developed using Python for **Biox Systems**. The application generates a QR code for the official Biox Systems website and saves it as an image file.

The QR code can be scanned using any mobile device or QR scanner to directly access the Biox Systems website.

---

## Features

* Generates QR code for Biox Systems website
* Saves QR code as PNG image
* Lightweight and simple Python implementation
* No user input required (static URL-based generation)

---

## Website Encoded in QR Code

The QR code represents the following URL:

https://www.bioxsystems.com/

When scanned, it redirects users to the official Biox Systems website.

---

## Technologies Used

* Python 3
* qrcode library
* Pillow (PIL)
* Visual Studio Code
* Git & GitHub

---

## Installation

### 1. Clone Repository

```bash id="g7m2aa"
git clone https://github.com/shresthabikash22/qrcodegenerator.git
```

### 2. Navigate to Project Directory

```bash id="k3p9vv"
cd qrcodegenerator
```

### 3. Create Virtual Environment

```bash id="t8x1nn"
python3 -m venv venv
```

### 4. Activate Virtual Environment

**Linux / macOS**

```bash id="a1d7qq"
source venv/bin/activate
```

**Windows**

```bash id="p5m2ss"
venv\Scripts\activate
```

### 5. Install Dependencies

```bash id="v9c4kk"
pip install qrcode[pil]
```

---

## Usage

Run the Python script:

```bash id="r2n8zz"
python qrcode-generator.py
```

The program will generate a QR code image for the Biox Systems website.

---

## Output

The generated QR code is saved as:

qrcode.png

Scanning this QR code opens:

https://www.bioxsystems.com/

---

## Project Structure
```text
qrcodegenerator/
│
├── qrcode-generator.py
├── requirements.txt
├── README.md
├── qrcode.png
└── .gitignore
```
---


