import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/student_tasks'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    # Arduino CLI configuration
    ARDUINO_CLI_PATH = 'arduino-cli'
    DEFAULT_FQBN = 'arduino:avr:uno'
    
    # Groq AI configuration for code validation
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY') or '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'