# GrovynAI Chatbot

Production-ready AI-powered chatbot backend built with FastAPI, MongoDB, and Google Gemini API.

## Features

- **JWT-based Authentication** - Secure token-based auth with 30-minute expiration
- **Multi-user Support** - Isolated user sessions and conversations
- **Conversation Management** - Persistent session storage with MongoDB
- **Context-aware AI** - Smart context handling with Gemini LLM
- **Rate Limiting** - Request throttling for API protection
- **Error Handling** - Comprehensive error responses
- **Dockerized** - Container-ready deployment
- **Async Architecture** - Non-blocking I/O for high performance

## Architecture
```
Client → API Layer → Service Layer → Repository Layer → MongoDB
                          ↓
                     Gemini API
```

### Layers

- **API Layer**: Request validation, authentication, routing
- **Service Layer**: Business logic, context management, AI prompts
- **Repository Layer**: Database abstraction
- **Security Layer**: JWT tokens & password hashing
- **AI Integration**: Gemini API with timeout & fallback

## Database Schema

### Users
```json
{
  "_id": "ObjectId",
  "email": "string",
  "password_hash": "string",
  "created_at": "datetime"
}
```

### Sessions
```json
{
  "_id": "ObjectId",
  "user_id": "string",
  "title": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "messages": [
    {
      "role": "user | assistant",
      "content": "string",
      "timestamp": "datetime"
    }
  ]
}
```

## Prerequisites

- Python 3.10+
- Docker (optional)
- MongoDB
- [Gemini API Key](https://aistudio.google.com/app/)

## Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/GrovynAI-Chatbot.git
cd GrovynAI-Chatbot
```

### 2. Environment Configuration
```bash
cp .env.example .env
```

Edit `.env`:
```env
MONGO_URI=mongodb://admin:secretpassword@mongodb:27017/chatbot_db?authSource=admin
DB_NAME=chatbot_db
JWT_SECRET=your_secure_random_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
GEMINI_API_KEY=your_gemini_key
```

### 3. Run Application

#### Local Development
```bash
uvicorn app.main:app --reload
```

#### Docker
```bash
docker-compose up --build
```

Access API documentation: `http://localhost:8000/docs`

## API Endpoints

### Authentication
- `POST /auth/register` - Create new user
- `POST /auth/login` - Get JWT token

### Sessions
- `POST /sessions` - Create chat session
- `GET /sessions` - List user sessions
- `GET /sessions/{session_id}` - Get session details
- `DELETE /sessions/{session_id}` - Delete session

### Chat
- `POST /chat/{session_id}` - Send message

### User
- `DELETE /users/me` - Delete account

## Testing

1. Navigate to `http://localhost:8000/docs`
2. Register a new user
3. Login to get JWT token
4. Click **Authorize** button and enter `Bearer <your_token>`
5. Create a session
6. Send chat messages

## Scalability

- **Async FastAPI** - Non-blocking I/O
- **Stateless Auth** - Horizontal scaling ready
- **Connection Pooling** - Efficient database connections
- **Containerized** - Kubernetes/ECS ready

## Security

- Environment variables via `.gitignore`
- JWT secret management
- bcrypt password hashing
- Pydantic input validation
- Rate limiting

## Edge Cases Handled

- Invalid/expired JWT tokens
- Unauthorized session access
- Empty or oversized messages
- Invalid session IDs
- Gemini API timeouts
- API failures with fallbacks
- Rate limit exceeded
- Database connectivity issues
- Context overflow prevention



## License

For technical evaluation purposes.

## Contributing

Contributions welcome! Please open an issue first to discuss changes.

---

**Note**: Gemini API keys have daily limits. Generate new keys at [Google AI Studio](https://aistudio.google.com/app/).