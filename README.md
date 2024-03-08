# Setting Up Development Environment

This guide outlines how to set up a development environment for this Django project.

**Prerequisites:**

- Python 3.x (https://www.python.org/downloads/)
- pip (package manager for Python, usually comes with Python installation)

**Steps:**

1. **Create a virtual environment:**

    - Open a command prompt or terminal and navigate to your project directory.
    - Run the following command:

      ```bash
      python -m venv venv
      ```

      Replace `venv` with your desired environment name.

2. **Activate the virtual environment:**

    - **Windows:**
      ```bash
      .\venv\Scripts\activate
      ```

    - **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

3. **Install required packages:**

    ```bash
    pip install Django django-crispy-forms  # Install core dependencies
    pip install Pillow  # Optional, for image processing
    pip install crispy-bootstrap4  # Optional, for Bootstrap 4 integration
    ```

4. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

    This will typically start the server at `http://127.0.0.1:8000/`. You can access your Django application in your web browser at that URL.

**Additional Notes:**

- Consider using a code editor or IDE with Django support for a more streamlined development experience.
- For production deployment, you'll need to configure a web server (e.g., Apache, Nginx) and a database. Refer to Django documentation for deployment guidance.

**Screenshots:**

![image](https://github.com/kzehra/Bidding/assets/82747649/e5c576a3-137d-4281-b990-0a81337371cd)

![image](https://github.com/kzehra/Bidding/assets/82747649/f8d10593-e641-4eab-b3fc-8f51d9650158)
