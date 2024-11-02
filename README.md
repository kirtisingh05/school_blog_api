# School Blog API

This is a School Blog API built with FastAPI and MongoDB (using Motor), designed for managing blog posts and related operations in a school setting. It includes data validation with Pydantic for structured and secure data handling.

## Features

- **Create, read, update, and delete** (CRUD) blog posts
- **MongoDB** database integration using Motor (async driver for MongoDB)
- **Data validation** using Pydantic models
- **Structured API documentation** with Swagger (available at `/docs`)

## Technologies

- **Backend**: FastAPI
- **Database**: MongoDB
- **ORM**: Motor
- **Validation**: Pydantic

## Getting Started

### Prerequisites

Make sure you have the following installed:

- **Python** (version 3.7 or higher)
- **MongoDB** (self-hosted or MongoDB Atlas)
- **Git** (for version control)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/school_blog_api.git
   cd school_blog_api
   ```

2. **Set up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB**

   - Set up a MongoDB database and obtain the connection string.
   - Create a `.env` file in the root directory with the following contents:

     ```env
     MONGO_URI="your_mongodb_connection_string"
     ```

5. **Run the Application**

   Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

### Project Structure

```
school_blog_api/
│
├── app/
│   ├── main.py           # FastAPI entry point
│   ├── routes/           # Route definitions
│   │   └── blog_routes.py
│   ├── models/           # Pydantic models
│   │   └── blog_model.py
│   ├── database/         # Database connection and setup
│       └── mongodb.py
├── .env                  # Environment variables
├── requirements.txt      # Project dependencies
└── README.md             # Project README file
```

## Usage

- **Create a blog post**: Send a POST request to `/api/blog` with JSON payload like:
  
  ```json
  {
    "title": "My First Blog",
    "content": "This is the content of the blog post.",
    "author": "Jane Doe"
  }
  ```

- **Retrieve all blog posts**: Send a GET request to `/api/blogs`.

Check the interactive documentation at `http://127.0.0.1:8000/docs` for more API operations.
