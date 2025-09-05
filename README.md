# Backend README

```markdown
# Todo API Backend

A FastAPI-based RESTful API for managing todo items with advanced features.

## 🌐 Live API

**API Base URL:** [https://todos-backend-eta.vercel.app](https://todos-backend-eta.vercel.app)

**API Documentation:** [https://todos-backend-eta.vercel.app/docs](https://todos-backend-eta.vercel.app/docs)

## 🚀 Features

- **RESTful API:** Full CRUD operations for todo management
- **CORS Support:** Configured for cross-origin requests
- **Data Validation:** Pydantic models for request/response validation
- **Search Functionality:** Search todos by task content
- **Statistics Endpoint:** Get overview statistics of todos
- **Priority System:** Support for task prioritization (1-5)
- **Due Dates:** Optional due dates for tasks
- **Automatic Documentation:** Interactive API docs with Swagger UI

## 🛠️ Tech Stack

- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server for running FastAPI
- **Python 3.8+** - Programming language
- **Vercel** - Deployment platform with serverless functions

## 📦 Installation

1. Clone the repository:
```
git clone <your-repo-url>
cd backend
```
2. Create virtual environment:

```python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate```

3. Install dependencies:

```pip install -r requirements.txt```

4. Run locally:

```uvicorn main:app --reload```

The API will be available at http://localhost:8000

## 🔧 API Endpoints
Base URL: https://todos-backend-eta.vercel.app  
Method	Endpoint	Description  
GET	/	API status check  
GET	/todos	Get all todos (optional completed filter)  
GET	/todos/{id}	Get specific todo by ID  
POST	/todos	Create new todo  
PUT	/todos/{id}	Update existing todo  
DELETE	/todos/{id}	Delete todo  
GET	/todos/search/{query}	Search todos by text  
GET	/stats	Get todo statistics  

## 📁 Project Structure  
text  
backend/  
├── api/  
│   └── __init__.py  
├── main.py              # Main application file  
├── requirements.txt     # Python dependencies  
├── vercel.json          # Vercel deployment configuration  
└── README.md            # This file  

## 🚀 Deployment  
### Deploy to Vercel
Install Vercel CLI:

```npm install -g vercel```
Login to Vercel:

```vercel login```
Deploy:

```vercel --prod```
## Manual Setup
Ensure vercel.json is configured correctly

Make sure requirements.txt includes all dependencies

Deploy using Vercel CLI or connect GitHub repository

## 📊 API Usage Examples
### Create a Todo

```curl -X POST "https://todos-backend-eta.vercel.app/todos" \
  -H "Content-Type: application/json" \
  -d '{"task": "Buy groceries", "priority": 3}'
Get All Todos```

```curl "https://todos-backend-eta.vercel.app/todos"
Get Completed Todos```

```curl "https://todos-backend-eta.vercel.app/todos?completed=true"
Update a Todo```

```curl -X PUT "https://todos-backend-eta.vercel.app/todos/{id}" \
  -H "Content-Type: application/json" \
  -d '{"completed": true, "priority": 2}'```
Get Statistics

```curl "https://todos-backend-eta.vercel.app/stats"```

## 🔒 CORS Configuration
The API is configured to allow requests from:

https://todos-eight-eta.vercel.app

http://localhost:3000 (for development)

## 📝 Data Models
TodoCreate
```json
{
  "task": "string",
  "priority": 1,
  "due_date": "2023-12-31T23:59:59"
}```
TodoItem
```json
{
  "id": "uuid-string",
  "task": "string",
  "completed": false,
  "priority": 1,
  "due_date": "2023-12-31T23:59:59",
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00"
}```
## ⚠️ Limitations
In-memory storage: Data is not persisted between deployments

No authentication: API is open to public requests

No rate limiting: Consider implementing for production use

For production use, consider adding:

Database persistence (PostgreSQL, MongoDB)

User authentication (JWT, OAuth)

Rate limiting

Input sanitization

## API key authentication

## 📄 License
This project is open source and available under the MIT License.

## 🔗 Interactive Documentation
Visit https://todos-backend-eta.vercel.app/docs for interactive API documentation with Swagger UI.

## 📞 Support
For issues or questions:

Check the API documentation at /docs

Review the error responses in the console

Ensure CORS is properly configured for your frontend domain

## 🚀 Future Enhancements
Database integration for data persistence

User authentication and authorization

File attachments for tasks

Task categories and tags

Email notifications for due tasks

Task sharing and collaboration