"""
This module initializes and collects all the Flask blueprints for the application.

It imports the blueprints from their respective modules and creates a list
of all blueprints for easy registration in the main application factory.
"""

from .user_routes import user_bp
from .ai_routes import ai_bp
from .course_routes import course_bp
from .exam_routes import exam_bp
from .main_routes import main_bp


# Define a list of all blueprints for easy registration
all_blueprints = [user_bp, ai_bp, course_bp, exam_bp, main_bp]