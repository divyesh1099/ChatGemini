# Chat Gemini: Flutter and Flask Chat Application

Chat Gemini is a simple chat application built with Flutter for the frontend and Flask for the backend. This README provides step-by-step instructions on how to create and deploy this project.

## Features

- Real-time chat with Gemini, an AI chatbot.
- Support for Markdown rendering in chat messages.
- Responsive design for different screen sizes.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Flutter](https://flutter.dev/docs/get-started/install)
- [Python](https://www.python.org/downloads/)
- [PythonAnywhere](https://www.pythonanywhere.com/) account (for deployment)

## Getting Started

Follow these steps to set up and run the Chat Gemini project locally:

### Frontend (Flutter)

1. Clone the repository:

   ```bash
   git clone https://github.com/divyesh1099/ChatGemini.git
   ```

2. Navigate to the `flutter_frontend` directory:

   ```bash
   cd ChatGemini/flutter_frontend
   ```

3. Run the Flutter app:

   ```bash
   flutter run
   ```

   This will start the Flutter app on your local machine.

### Backend (Flask)

1. Navigate to the `flask_backend` directory:

   ```bash
   cd ChatGemini/flask_backend
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   flask run
   ```

   The Flask app will start serving at `http://127.0.0.1:5000/`.

## Deployment on PythonAnywhere

To deploy the Flask backend on PythonAnywhere, follow these steps:

1. Sign in to your PythonAnywhere account or create one if you don't have it.

2. Upload your Flask project to PythonAnywhere.

3. Create a virtual environment:

   ```bash
   mkvirtualenv --python=/usr/bin/python3.8 myenvname
   ```

4. Install the required packages using the virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure the WSGI file (e.g., `motiedivya_pythonanywhere_com_wsgi.py`) to point to your Flask app.

   ```python
   from chatAPI import app as application  # Replace with your Flask app name
   ```

6. Reload your PythonAnywhere web app to apply the changes.

## Usage

- Access the Flutter app by running it on your local machine.
- Send messages to interact with Gemini, the chatbot.
- Enjoy real-time chat and Markdown rendering!

## Screenshots

![Screenshot (116)](https://github.com/divyesh1099/ChatGemini/assets/65925922/382abbf0-c8e2-41e0-ae18-2648d9bf8d1f)

## Installation

You can download and install the application for different platforms from the "releases" section. Choose the appropriate platform below:

### Android

- Navigate to the [Android Releases](releases/Android) folder.
- Download the APK file for Android.
- Transfer the APK file to your Android device.
- Install the app on your Android device and start using it.

### Google Chrome

- Access the web version of the application by visiting [Application on Google Chrome](releases/Google%20Chrome).
- Use the web app directly in your Google Chrome browser without any installation.

### Windows

- Go to the [Windows Releases](releases/Windows) folder.
- Download the Windows installer.
- Run the installer and follow the installation instructions.
- Once installed, launch the app on your Windows computer.

Please note that these releases are for testing and may not be officially deployed. If you encounter any issues or have feedback, feel free to [report them](https://github.com/divyesh1099/ChatGemini/issues).

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Google AI](https://ai.google/) for providing the AI chatbot API.
- Inspired by the [Flutter](https://flutter.dev/) and [Flask](https://flask.palletsprojects.com/) communities.
- The article that taught me about Gemini API and how to configure it [How to Access and Use Google Gemini API Key (with Examples)](https://beebom.com/how-use-google-gemini-api-key/amp/). 

## Contact

For any questions or issues, please contact [Divyesh Nandlal Vishwakarma](https://github.com/divyesh1099).
