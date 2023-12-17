from flask import Blueprint, jsonify


bp_health = Blueprint("health", __name__)


@bp_health.get("/")
def health():
    return jsonify({"status": "OK"}), 200
