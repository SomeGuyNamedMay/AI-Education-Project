"""
This module contains routes and functions related to exam management in the application.

It defines a Flask Blueprint for exam-related routes and includes functions for
handling exam operations such as listing exams and retrieving specific exam details.
"""

from flask import Blueprint

# Create a Blueprint named 'exam_bp'
exam_bp = Blueprint('exam_bp', __name__)

@exam_bp.route('/exams', methods=['GET'])
def list_exams():
    """
    Retrieve a list of all exams.

    This route handles GET requests to fetch a list of all available exams.

    Returns:
        str: A placeholder string indicating a list of exams.
        In the actual implementation, this should return a proper response
        containing the list of exams.
    """
    # This is a placeholder for the actual implementation
    return "List of exams"

@exam_bp.route('/exams/<int:exam_id>', methods=['GET'])
def get_exam(exam_id):
    """
    Retrieve details of a specific exam.

    This route handles GET requests to fetch details of a particular exam
    identified by its ID.

    Args:
        exam_id (int): The unique identifier of the exam.

    Returns:
        str: A placeholder string indicating details of the specified exam.
        In the actual implementation, this should return a proper response
        containing the exam details.
    """
    # This is a placeholder for the actual implementation
    return f"Details of exam {exam_id}"