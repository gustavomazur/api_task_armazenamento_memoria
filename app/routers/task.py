
from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from .. import models, schemas


router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate):

    new_task = task.model_dump()
    new_task["id"] = max(
        (task["id"] for task in models.my_task),
        default=0
    ) + 1

    models.my_task.append(new_task)

    return new_task

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.TaskResponse])
def get_tasks():
    return models.my_task


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.TaskResponse)
def get_task(id: int):

    task = next(
        (task for task in models.my_task if task["id"] == id),None)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task com esse id : {id} não existe ")
    return task

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):

    task = next(
    (task for task in models.my_task if task["id"] == id),None)


    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'task com esse id: {id} não existe')

    models.my_task.remove(task)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.TaskResponse)
def update_task(id: int, update_task: schemas.TaskAtulizacao,):

    task = next(
        (task for task in models.my_task if task["id"] == id), None)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'task com esse id: {id} não existe')

    update_task = update_task.model_dump(exclude_unset=True)
    task.update(update_task)

    return task

    