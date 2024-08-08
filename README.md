# Image-Transfer

Image Transfer is a web application that allows users to upload an image and apply various transformations to it, such as blurring, sharpening, smoothing, converting to grayscale, rotating, resizing, or converting the image to PNG format. The application is built using Flask and Pillow (PIL) for image processing.

## Features

- **Image Upload**: Upload images in various formats for processing.
- **Transformation Options**: Apply different transformations like blur, sharpen, smooth, grayscale, rotate, resize, or convert to PNG.
- **Dynamic Form**: Additional fields appear based on the selected transformation (e.g., input fields for rotation degrees or image dimensions).
- **Processed Image Preview**: View the original and processed images side by side after uploading.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **Pillow (PIL)**: A powerful library for image processing in Python.
- **HTML/CSS**: For the frontend design of the web interface.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the repository:**

   ---bash
   git clone https://github.com/yourusername/image-transfer.git
   cd image-transfer

2. Install the required packages:

    ---bash
    pip install -r requirements.txt
    
3. Run the application:

    ---bash
    python image.py
  
4. Access the application:

   Open your web browser and navigate to http://127.0.0.1:5000/.

Usage
1. Upload an Image: On the homepage, choose an image file from your device.
2. Select a Transformation: Choose a transformation from the dropdown menu. If you select "Rotate" or "Resize," additional input fields will appear for specifying the rotation angle or new dimensions.
3. Submit the Form: Click the "Upload" button to process the image.
4. View the Result: The original and processed images will be displayed on a new page.

Project Structure
image-transfer/
│
├── image.py                   # Main Flask application file
├── templates/
│   ├── index.html             # HTML template for the image upload form
│   └── result.html            # HTML template for displaying the processed image
│
├── static/
│   ├── css/
│   │   └── style.css          # Stylesheet for the web interface
│   └── uploads/               # Directory for uploaded and processed images
│
└── requirements.txt           # Python dependencies file

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. Issues can also be submitted to suggest new features or report bugs.

Acknowledgments
Flask: Web framework for Python.
Pillow (PIL): Image processing library for Python.

This `README.md` provides a detailed overview of the project, including installation instructions, usage guidelines, and a description of the project's structure. Make sure to replace `"yourusername"` with your actual GitHub username if you plan to use the clone URL.
