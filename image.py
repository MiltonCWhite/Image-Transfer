from flask import Flask, request, render_template
from PIL import Image, ImageFilter, ImageOps
import os

app = Flask(__name__)

# Ensure the static directory exists for uploads
STATIC_FOLDER = 'static/uploads'
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded.'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file.'
    
    original_file_path = os.path.join(STATIC_FOLDER, file.filename)
    file.save(original_file_path)

    option = request.form.get('option')
    degrees = request.form.get('degrees', type=int)
    width = request.form.get('width', type=int)
    height = request.form.get('height', type=int)
    img = Image.open(original_file_path)

    # Process the image based on the selected option
    if option == 'blur':
        img = img.filter(ImageFilter.BLUR)
    elif option == 'sharpen':
        img = img.filter(ImageFilter.SHARPEN)
    elif option == 'smooth':
        img = img.filter(ImageFilter.SMOOTH)
    elif option == 'greyscale':
        img = ImageOps.grayscale(img)
    elif option == 'rotate' and degrees:
        img = img.rotate(degrees, expand=True)
    elif option == 'resize' and width and height:
        img = img.resize((width, height))
    elif option == 'convert_to_png':
        file.filename = os.path.splitext(file.filename)[0] + '.png'
        original_file_path = os.path.join(STATIC_FOLDER, file.filename)

    processed_file_path = os.path.join(STATIC_FOLDER, f'processed_{file.filename}')
    img.save(processed_file_path)

    return render_template('result.html', original=file.filename, processed=f'processed_{file.filename}')

if __name__ == '__main__':
    app.run(debug=True)
