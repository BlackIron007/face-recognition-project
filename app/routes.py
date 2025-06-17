from flask import Blueprint, request, jsonify, render_template
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def live():
    return render_template('live.html')

@main_bp.route('/api/recognize', methods=['POST'])
def recognize():
    return jsonify([])  # placeholder

@main_bp.route('/api/mark_attendance', methods=['POST'])
def mark_attendance():
    return jsonify({'success': True})
