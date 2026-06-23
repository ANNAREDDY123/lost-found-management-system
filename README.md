# lost-found-management-system
FastAPI Lost &amp; Found Management System with Lost Items, Found Items, Claim Requests, Matching System, JWT Authentication, SQLAlchemy ORM, Background Tasks, Pagination, and Docker Support.
# Lost & Found Management System

## Features

- JWT Authentication
- Lost Item Management
- Found Item Management
- Claim Requests
- Item Matching
- Reports Dashboard
- Background Tasks
- SQLAlchemy ORM
- SQLite Database
- Docker Support

## APIs

### Authentication
POST /auth/register
POST /auth/login

### Lost Items
POST /lost-items
GET /lost-items
GET /lost-items/{id}
PUT /lost-items/{id}
DELETE /lost-items/{id}

### Found Items
POST /found-items
GET /found-items
GET /found-items/{id}

### Claims
POST /claims/{found_item_id}
GET /claims
PUT /claims/{claim_id}/approve
PUT /claims/{claim_id}/reject

### Reports
GET /reports/total-lost-items
GET /reports/total-found-items
GET /reports/successful-claims
GET /reports/matches
