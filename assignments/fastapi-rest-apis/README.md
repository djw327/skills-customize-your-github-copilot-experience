# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework in Python, including endpoints for retrieving and creating data.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project

#### Description

Install FastAPI and create a basic application structure with a root endpoint that returns a welcome message.

#### Requirements

Completed program should:

- Install FastAPI and Uvicorn
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Run the server and verify the endpoint works

### 🛠️ Create Data Retrieval Endpoints

#### Description

Implement GET endpoints to retrieve a list of items and a specific item by ID.

#### Requirements

Completed program should:

- Define a GET endpoint at "/items" that returns a list of sample items in JSON format
- Define a GET endpoint at "/items/{item_id}" that returns a specific item by ID
- Handle cases where the item ID does not exist (return 404 status)

### 🛠️ Add Data Creation Endpoint

#### Description

Implement a POST endpoint to create new items with request body validation.

#### Requirements

Completed program should:

- Define a POST endpoint at "/items" that accepts JSON data for a new item
- Use Pydantic models for request and response validation
- Add the new item to the list and return the created item with a 201 status
- Ensure proper error handling for invalid data

### 🛠️ Implement Query Parameters

#### Description

Add query parameters to filter and limit the results from the items endpoint.

#### Requirements

Completed program should:

- Modify the "/items" GET endpoint to accept optional query parameters (e.g., limit, category)
- Filter the items based on the query parameters
- Return the filtered list in JSON format</content>
<parameter name="filePath">/workspaces/skills-customize-your-github-copilot-experience/assignments/fastapi-rest-apis/README.md