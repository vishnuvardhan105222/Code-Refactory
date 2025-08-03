from flask import Flask, request, jsonify, redirect
#from models import url_store
from .util import generate_short_code, is_valid_url
from .models import url_store
 # Relative import (if in a package)
import sys
print(sys.path)

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "API is running"
    })

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    for _ in range(5):
        short_code = generate_short_code()
        if url_store.get_url(short_code) is None:
            break
    else:
        return jsonify({"error": "Failed to generate unique code"}), 500

    url_store.add_url(short_code, original_url)
    return jsonify({
        "short_code": short_code,
        "short_url": request.host_url + short_code
    }), 201

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = url_store.get_url(short_code)
    if url is None:
        return jsonify({"error": "Short URL not found"}), 404
    url_store.increment_click(short_code)
    return redirect(url, code=302)

@app.route('/api/analytics/<short_code>')
def analytics(short_code):
    metadata = url_store.get_metadata(short_code)
    if metadata is None:
        return jsonify({"error": "Short URL not found"}), 404
    return jsonify({
        "short_code": short_code,
        "original_url": metadata["original_url"],
        "clicks": metadata["clicks"],
        "created_at": metadata["created_at"].isoformat() + "Z"
    })

if __name__ == "__main__":
    app.run(debug=True)
