# Flask GitHub Pull Requests Viewer

This project is a simple Flask web app that fetches and displays pull requests from a GitHub repository using the GitHub API.

## Features

- Flask backend serving pull requests data  
- Jinja2 template to render PRs as clickable links  
- Unit tests covering API interaction  
- Fully Dockerized for easy deployment

## How It Works

1. **Flask App**  
   The app defines routes to fetch pull requests (`open` or `closed`) from a specified GitHub repo, using a personal access token for authentication. Pull requests are shown in a styled HTML page.

2. **Jinja2 Template**  
   Uses Jinja2 to render the pull requests list dynamically, showing PR titles, numbers, and links to GitHub.

3. **Unit Tests**  
   Tests are implemented with `pytest` and `unittest.mock` to mock GitHub API responses, ensuring stable and isolated testing without real network calls.

4. **Dockerization**  
   The app is containerized with a `Dockerfile` and managed via `docker-compose.yml`. Environment variables (like the GitHub token) are securely injected using a `.env` file. The Flask server is configured to listen on all interfaces (`0.0.0.0`) and the container exposes port 5000 mapped to a host port.

## Setup & Run

1. Clone the repo  
2. Create a `.env` file with your GitHub token:  
   ```bash
   TOKEN=your_github_personal_access_token

3. Build and run the container:
    `./build.sh`
    `docker compose up`

4. Open your browser at http://localhost:5000 (or your mapped port) to see the pull requests.
