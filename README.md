# Flask Model Deployment Documentation

This documentation provides guidelines for deploying a machine learning model using Flask, a lightweight Python web framework. Flask enables you to create a web application to expose your machine learning model as an API endpoint.

#### Prerequisites

Before proceeding with deploying your model using Flask, ensure you have the following:

- Python installed on your system.
- Necessary Python packages installed, including Flask (`pip install flask`) and any packages required for your machine learning model.
- A trained machine learning model saved in a format compatible with your chosen library (e.g., scikit-learn, TensorFlow, PyTorch).

#### Setup

1. **Create a Flask App**: Start by creating a new directory for your project. Within this directory, create a Python file (e.g., `app.py`) where you'll define your Flask application.
2. **Import Dependencies**: In your Python file, import necessary dependencies, including Flask and your machine learning libraries.
3. **Load Model**: Load your pre-trained machine learning model using appropriate methods from your machine learning library. For example, if you're using scikit-learn, you can load a model using `joblib`.
4. **Define Flask App**: Initialize your Flask application.
5. **Create Simple Interface**: Create an interface using html and css or you can use bootstrap.
6. **Running the Application**: Run command in your terminal 'python main.py'


Your Flask application will start running, and you can access it through `http://localhost:5000`.
