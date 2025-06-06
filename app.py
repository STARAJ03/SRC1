# Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

from flask import Flask, request, jsonify
import logging
import os
from utils.func import get_user_data, save_user_data, is_premium_user
from utils.encrypt import encrypt_data, decrypt_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/user/<int:user_id>', methods=['GET'])
async def get_user(user_id):
    try:
        user_data = await get_user_data(user_id)
        if user_data:
            return jsonify({
                "status": "success",
                "data": user_data
            })
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/user/<int:user_id>', methods=['POST'])
async def update_user(user_id):
    try:
        data = request.json
        if not data:
            return jsonify({
                "status": "error",
                "message": "No data provided"
            }), 400
            
        success = await save_user_data(user_id, data)
        if success:
            return jsonify({
                "status": "success",
                "message": "User data updated"
            })
        return jsonify({
            "status": "error",
            "message": "Failed to update user data"
        }), 500
    except Exception as e:
        logger.error(f"Error updating user: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/premium/<int:user_id>', methods=['GET'])
async def check_premium(user_id):
    try:
        is_premium = await is_premium_user(user_id)
        return jsonify({
            "status": "success",
            "is_premium": is_premium
        })
    except Exception as e:
        logger.error(f"Error checking premium status: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({
                "status": "error",
                "message": "No data provided"
            }), 400
            
        encrypted_data = encrypt_data(data)
        if encrypted_data:
            return jsonify({
                "status": "success",
                "encrypted_data": encrypted_data
            })
        return jsonify({
            "status": "error",
            "message": "Encryption failed"
        }), 500
    except Exception as e:
        logger.error(f"Error encrypting data: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({
                "status": "error",
                "message": "No data provided"
            }), 400
            
        decrypted_data = decrypt_data(data)
        if decrypted_data:
            return jsonify({
                "status": "success",
                "decrypted_data": decrypted_data
            })
        return jsonify({
            "status": "error",
            "message": "Decryption failed"
        }), 500
    except Exception as e:
        logger.error(f"Error decrypting data: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)