import os

class Config:
    # Secret key for session management and flash messages
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    
    # Upload configuration
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Allowed file extensions for image uploads
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp', 'tiff'}
    
    # Gallery configuration
    IMAGES_PER_ROW = 10
    IMAGE_ASPECT_RATIO = '5:7'  # Width:Height ratio

# Export configuration
SECRET_KEY = Config.SECRET_KEY
UPLOAD_FOLDER = Config.UPLOAD_FOLDER
MAX_CONTENT_LENGTH = Config.MAX_CONTENT_LENGTH
ALLOWED_EXTENSIONS = Config.ALLOWED_EXTENSIONS
IMAGES_PER_ROW = Config.IMAGES_PER_ROW
IMAGE_ASPECT_RATIO = Config.IMAGE_ASPECT_RATIO
