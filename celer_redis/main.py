# from fastapi import FastAPI
# from celery_app import task_one, task_two, task_three

# app = FastAPI()

# # Example endpoint to enqueue tasks
# @app.get("/tasks")
# async def run_tasks():
#     # Enqueue tasks asynchronously
#     result_one = task_one.delay(10, 5)
#     result_two = task_two.delay(7, 3)
#     result_three = task_three.delay(15, 8)
   
#     return {
#         "task_one_id": result_one.id,
#         "task_two_id": result_two.id,
#         "task_three_id": result_three.id
#     }

from fastapi import FastAPI
from celery_app import task_one, task_two, task_three

app = FastAPI()

@app.get("/process_input")
async def process_input(input_data: str):


    # Example inputs
    uppercase_input = "HELLO"
    number_input = "7"
    three_numbers = ["10", "20", "30"]
   
    # Enqueue tasks asynchronously
    result_task_one = task_one.delay(input_data)
    result_task_two = task_two.delay(number_input)
    result_task_three = task_three.delay(three_numbers)
   
    return {
        "task_one_id": result_task_one.result,
        "task_two_id": result_task_two.result,
        "task_three_id": result_task_three.result
    }