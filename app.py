import os
from flask import Flask, render_template, jsonify
import config
from image_metadata import IMAGE_METADATA, TOKEN_MAPPING, TOKEN_METADATA

app = Flask(__name__)
app.config.from_object(config)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class GalleryImage:
    """Class to represent an image in the gallery with comprehensive metadata"""
    def __init__(self, filename, title=None, description=None, type=None, text_box=None, artist=None, color=None, region=None, flippable=None):
        self.filename = filename
        self.title = title or self._generate_title_from_filename(filename)
        self.description = description or ""
        self.type = type or ""
        self.text_box = text_box or ""
        self.artist = artist or ""
        self.color = color or []
        self.region = region or []
        self.flippable = flippable if flippable is not None else False
        self.url = f"static/uploads/{filename}"
        # Generate back image URL if flippable
        self.back_url = self._get_back_filename(filename) if self.flippable else None
        # Get token information
        self.tokens = self._get_token_urls(filename)
    
    def _generate_title_from_filename(self, filename):
        """Generate a title from filename by removing extension and formatting"""
        name = os.path.splitext(filename)[0]
        # Replace underscores and hyphens with spaces, capitalize words
        return ' '.join(word.capitalize() for word in name.replace('_', ' ').replace('-', ' ').split())
    
    def _get_back_filename(self, filename):
        """Generate back filename by adding '_back' before the extension"""
        name, ext = os.path.splitext(filename)
        return f"static/card_backs/{name}_back{ext}"
    
    def _get_token_urls(self, filename):
        """Get token URLs and metadata for this card"""
        token_filenames = TOKEN_MAPPING.get(filename, [])
        tokens = []
        for token_filename in token_filenames:
            token_data = {
                'url': f"static/tokens/{token_filename}",
                'filename': token_filename
            }
            # Add metadata if available
            if token_filename in TOKEN_METADATA:
                token_data.update(TOKEN_METADATA[token_filename])
            tokens.append(token_data)
        return tokens
    
    def to_dict(self):
        """Convert image object to dictionary for JSON serialization"""
        return {
            'filename': self.filename,
            'title': self.title,
            'description': self.description,
            'type': self.type,
            'text_box': self.text_box,
            'artist': self.artist,
            'color': self.color,
            'region': self.region,
            'url': self.url,
            'flippable': self.flippable,
            'back_url': self.back_url,
            'tokens': self.tokens
        }

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_gallery_images():
    """Get list of all images in the upload folder with their metadata"""
    images = []
    upload_folder = app.config['UPLOAD_FOLDER']
    
    if os.path.exists(upload_folder):
        for filename in os.listdir(upload_folder):
            if allowed_file(filename) and not filename.startswith('.'):
                metadata = IMAGE_METADATA.get(filename, {})
                image = GalleryImage(
                    filename=filename,
                    title=metadata.get('title'),
                    description=metadata.get('description', ''),
                    type=metadata.get('type'),
                    text_box=metadata.get('text_box'),
                    artist=metadata.get('artist'),
                    color=metadata.get('color'),
                    region=metadata.get('region'),
                    flippable=metadata.get('flippable', False)
                )
                images.append(image)
    
    return sorted(images, key=lambda x: x.title)

@app.route('/')
def index():
    images = get_gallery_images()
    return render_template('index.html', images=images)

@app.route('/api/images')
def api_images():
    """API endpoint to get current images list with metadata"""
    images = get_gallery_images()
    return jsonify({'images': [img.to_dict() for img in images]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
