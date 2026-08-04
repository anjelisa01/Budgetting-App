# PersonalFinanceApp
## Description: 
A rest-API backend for managing Personal Finance. Built using python FastAPI and PostgreSQL via neon. Entirely developed using github's Codespace.

## API documentation
swaggeruilinkhere.com

## Features:
- Secure user authentication with signup and login
- User profile management (view, update, and delete personal data)
- JWT-based authorization for protected API endpoints
- Financial resource management:
  - Accounts
  - Goals
  - Categories
  - Transactions
  - Budgets
- Full CRUD operations for all user-owned resources
- Protected routes accessible only to authenticated users

## Tech Stacks
- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy
- JWT Authentication

## Project Structure
``` 
PersonalFinanceApp/
|  backend/  
|     api/  
|     dependecies/  
|     core/  
|     models/  
|     schemas/  
|     services/  
|     tests/  
|     main.py  
```