# HackerNews Top Stories App

## Overview
The project consists of a FastAPI backend and a React frontend that together fetch and display the top 10 stories from HackerNews. 

## Backend Setup 

### Prerequisites
- Python 3.11 or higher 

### Installation
1. Clone the repository:
   ```bash 
   git clone https://github.com/hackernews
   cd hackernews-backend
   ```
   
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
4. Run the FastAPI server: 
    ```bash 
    uvicorn main:app --reload
    ```

Run the FastAPI development server inside app/: 
    ```bash 
    fastapi dev main.py 
    ```

The server will be running at http://127.0.0.1:8000.

## Frontend Setup (React.js)
### Prerequisites
- Node.js (v14 or later)
- npm or yarn
### Installation
1. Navigate to the frontend directory:
    ```bash
    cd hackernews-frontend
    ```

2. Install the dependencies:
    ```bash
    npm install # or yarn install
    ```

3. Start the React app:
    ```bash
    npm start # or yarn start
    ```

The frontend will be running at http://localhost:3000.

## Testing
### Backend
1. Navigate to the backend directory:
    ```bash
    cd hackernews-backend
    ```

2. Run the tests:
    ```bash
    pytest
    ```


## Environment Variables
Create a .env file in the backend directory with the following content: 

```bash
HACKERNEWS_API_URL=https://hacker-news.firebaseio.com/v0/
```
