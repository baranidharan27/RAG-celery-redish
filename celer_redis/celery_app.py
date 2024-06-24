# from celery import Celery
# import os

# redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

# app = Celery(
#     "tasks",
#     broker=redis_url,
#     backend=redis_url
# )

# # Define tasks
# @app.task
# def task_one(x, y):
#     return x + y

# @app.task
# def task_two(x, y):
#     return x * y

# @app.task
# def task_three(x, y):
#     return x - y


from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

# Define Celery app
app = Celery(
    "tasks",
    broker=redis_url,
    backend=redis_url
)

# Task definitions

@app.task
def task_one(input_data):
    # Task 1: Convert uppercase to lowercase
    if isinstance(input_data, str) and input_data.isupper():
        return input_data.lower()
    else:
        return "Input is not uppercase or not a string"

@app.task
def task_two(input_data):
    # Task 2: Square of a number
    try:
        num = int(input_data)
        return num ** 2
    except ValueError:
        return "Input is not a valid number"

@app.task
def task_three(inputs):
    # Task 3: Calculate sum of three numbers
    if len(inputs) == 3:
        try:
            num1 = int(inputs[0])
            num2 = int(inputs[1])
            num3 = int(inputs[2])
            total_sum = num1 + num2 + num3
            return total_sum
        except ValueError:
            return "All inputs must be valid numbers"
    else:
        return "Input should be a list of exactly three numbers"


