from flask import Blueprint, request, jsonify, redirect, current_app
from .utils import generate_short_code
from .models import insert_url, find_original_url, find_existing_short_code

url_shortener_routes = Blueprint('url_shortener', __name__)

@url_shortener_routes.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    db = current_app.db
    existing_code = find_existing_short_code(db, original_url)

    if existing_code:
        short_url = f"{current_app.config['BASE_URL']}/{existing_code}"
        return jsonify({"short_url": short_url}), 200

    short_code = generate_short_code(original_url)
    insert_url(db, original_url, short_code)

    short_url = f"{current_app.config['BASE_URL']}/{short_code}"
    return jsonify({"short_url": short_url}), 201

@url_shortener_routes.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    db = current_app.db
    original_url = find_original_url(db, short_code)

    if original_url:
        return redirect(original_url)
    return jsonify({"error": "URL not found"}), 404

