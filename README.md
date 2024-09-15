# ACM Education Platform

This is a Flask-based web application for managing courses, exams, and providing AI-powered feedback on student assessments. The platform allows professors to administer college assessments and students to take these assessments, receiving AI-generated evaluations on how and where they need to improve.

## Features

- User management (students and teachers)
- Course management
- Exam creation and management
- AI-powered evaluation of student answers

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following variables:
   ```
   DB_USERNAME=your_db_username
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_NAME=acm_education_db
   ```

5. Run the application:
   ```
   python run.py
   ```

The application will be available at `http://localhost:5000`.

## Project Structure

- `run.py`: Main entry point for running the application
- `app/`: Main application package
  - `__init__.py`: Application factory and initialization
  - `config.py`: Configuration settings
  - `models.py`: Database models
  - `routes/`: Blueprint route definitions
    - `main_routes.py`: Main routes for the application
    - `course_routes.py`: Routes related to course management
    - `exam_routes.py`: Routes related to exam management
    - `user_routes.py`: Routes related to user management
    - `ai_routes.py`: Routes related to AI processing
  - `langchain/`: LangChain integration for AI-powered features
  - `utils/`: Utility functions and helpers

## API Endpoints

- `/`: Home page, returns a welcome message
- `/api/courses`: Returns a list of courses
- `/api/exams`: Returns a list of exams
- `/api/users/register`: Register a new user
- `/api/ai/process`: Process data using AI techniques


## Logging

Logs are stored in the `logs/` directory. The application uses rotating file handlers to manage log files.

## Contributing

This is a SUNY Brockport ACM team project. Please refer to the project guidelines for contribution instructions.

## License
