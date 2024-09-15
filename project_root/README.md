# ACM Education Platform

This is a Flask-based web application for managing courses, exams, and AI-assisted evaluations.

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
   OPENAI_API_KEY=your_openai_api_key
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
  - `utils/`: Utility functions and helpers

## Contributing



## License

