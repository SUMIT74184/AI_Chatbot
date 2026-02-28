# GrovynAI Chatbot

This is a FastAPI-powered AI chatbot application.

## Prerequisites

- Python 3.10+
- Docker (for running with Docker)
- MongoDB

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/GrovynAI-Chatbot.git
   cd GrovynAI-Chatbot
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file by copying the `.env.example` file:

   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with your MongoDB connection string and other settings.

## Running the Application

### Locally

1. **Start the FastAPI application:**

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

### With Docker

1. **Build and run the Docker containers:**

   ```bash
   docker-compose up -d --build
   ```

   This will start the FastAPI application and a MongoDB container. The application will be accessible at `http://localhost:8000`.

## API Documentation

Once the application is running, you can access the API documentation at `http://localhost:8000/docs`.
