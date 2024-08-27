# FastAPI GitHub OAuth Application

This is a FastAPI application that demonstrates GitHub OAuth authentication.

## Features

- GitHub OAuth login
- Fetch GitHub user information

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Setup

1. Update the `config.py` file with your GitHub OAuth credentials:
    ```python
    GITHUB_CLIENT_ID = 'your-client-id'
    GITHUB_CLIENT_SECRET = 'your-client-secret'
    ```

## Usage

1. Run the application:
    ```sh
    python run.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000`.

## Endpoints 📌

- `GET /` - Home endpoint 🏠
- `GET /github-login` - Redirects to GitHub OAuth login 🔗
- `GET /github-code` - Handles GitHub OAuth callback 🔄

## Example

1. Navigate to `http://127.0.0.1:8000/github-login` to initiate the GitHub OAuth login process.
2. After logging in, GitHub will redirect you back to `http://127.0.0.1:8000/github-code` with a code.
3. The application will exchange the code for an access token and fetch the GitHub user information.

## License

This project is licensed under the MIT License.