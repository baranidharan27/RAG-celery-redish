
# FastAPI and Celery Integration with Redis 

This project demonstrates how to integrate FastAPI with Celery and Redis. It includes three different tasks managed by Celery workers and exposes an endpoint through FastAPI to enqueue these tasks.

## Table of Contents
1. [Description](#description)
2. [Installation](#installation) 
3. [Usage](#usage) 
4. [Endpoints](#endpoints)
5. [Contributing](#contributing) 



## Description 
This project uses FastAPI as the web framework and Celery as the task queue, with Redis as the message broker and result backend. It includes three tasks: 1. Convert uppercase string to lowercase. 2. Compute the square of a number. 3. Calculate the sum of three numbers.
 The tasks are defined in `celery_app.py` and exposed via an endpoint in `main.py`.

 ## Installation 
 ### Prerequisites 
 - Python 3.8+ 
 - Redis server 
 - FastAPI 
 - Celery



  ### Steps 
  1. **Clone the repository:**
  
  ```git clone https://github.com/baranidharan27/RAG-celery-redish.git cd RAG-celery-redish ``` 


  2. **Create and activate a virtual environment:** 
  
  ``` python -m venv venv source venv/bin/activate # On Windows use `venv\Scripts\activate` ``` 

  3. **Install the required packages:** 
  
  ```pip install -r requirements.txt ``` 

  4. **Start the Redis server:** 
  
  ```docker run --rm --name some-redis -p 6379:6379 redis:latest``` 
  
  5. **Start the Celery worker:** 
  
  ``` celery -A celery_app worker --loglevel=info ``` 

  6. **Run the FastAPI application:**

   ```uvicorn main:app --reload ``` 


   ## Usage 
   
   After starting the FastAPI server, you can enqueue tasks via the `/process_input` endpoint. 
   
   ### Example Request 
   To enqueue tasks, send a GET request to the `/process_input` endpoint with appropriate query parameters:
   
    ```sh curl -X GET "http://127.0.0.1:8000/process_input?input_data=HELLO" ``` 


### Example Response  

     ```json { "task_one_id": "hello", 
               "task_two_id": 49, 
               "task_three_id": 60 } ``` 
               


   ## Endpoints 

   ### Process Input

 **URL:** `/process_input`

 **Method:** `GET` 

 **Description:** Enqueues three tasks with the provided input data. 

 **Query Parameters:** `input_data`: The input data for the tasks (string).
 
 
 
  ## Contributing 
  
  Contributions are welcome! Please follow these steps: 
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`). 
3. Commit your changes (`git commit -m 'Add some feature'`). 
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request             
