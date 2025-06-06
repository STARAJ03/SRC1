# Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import base64
import logging
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from config import MASTER_KEY, IV_KEY

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_key():
    """Generate encryption key from master key"""
    try:
        salt = IV_KEY.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(MASTER_KEY.encode()))
        return key
    except Exception as e:
        logger.error(f"Error generating key: {e}")
        return None

def encrypt_data(data):
    """Encrypt data using Fernet"""
    try:
        if not isinstance(data, str):
            data = str(data)
            
        key = generate_key()
        if not key:
            return None
            
        f = Fernet(key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data.decode()
    except Exception as e:
        logger.error(f"Error encrypting data: {e}")
        return None

def decrypt_data(encrypted_data):
    """Decrypt data using Fernet"""
    try:
        key = generate_key()
        if not key:
            return None
            
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data.encode())
        return decrypted_data.decode()
    except Exception as e:
        logger.error(f"Error decrypting data: {e}")
        return None

def encrypt_file(file_path):
    """Encrypt file content"""
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            
        key = generate_key()
        if not key:
            return None
            
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
        
        encrypted_file_path = f"{file_path}.encrypted"
        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted_data)
            
        return encrypted_file_path
    except Exception as e:
        logger.error(f"Error encrypting file: {e}")
        return None

def decrypt_file(encrypted_file_path):
    """Decrypt file content"""
    try:
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()
            
        key = generate_key()
        if not key:
            return None
            
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        
        decrypted_file_path = encrypted_file_path.replace('.encrypted', '')
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data)
            
        return decrypted_file_path
    except Exception as e:
        logger.error(f"Error decrypting file: {e}")
        return None
