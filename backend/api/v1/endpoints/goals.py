from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schemas.goal import GoalBase,GoalUpdate,GoalResponse
# services
# from service.goal import create_goal,read_one_goal,read_all_goals,update_goal,delete_goal
#dependencies
from service.goal_service import GoalService
from dependencies.services import get_goal_service

#Add new account
router=APIRouter(tags=["goals"])

@router.post("/",response_model=GoalResponse)
def add_goal(payload:GoalBase,service:GoalService=Depends(get_goal_service)):
    return service.create(payload)

@router.get("/",response_model=list[GoalResponse])   
def get_all_goals(service:GoalService=Depends(get_goal_service)):
    return service.read_all()

@router.get("/{goal_id}",response_model=GoalResponse)
def get_one_goal(goal_id:int,service:GoalService=Depends(get_goal_service)):  
    return service.read_one(goal_id)

#Update 
@router.patch("/{goal_id}",response_model=GoalResponse)
def edit_goal(goal_id:int,payload:GoalUpdate,service:GoalService=Depends(get_goal_service)):
    return service.update(goal_id,payload)

#delete 
@router.delete("/{goal_id}")  
def remove_goal(goal_id:int,service:GoalService=Depends(get_goal_service)):
    return service.delete(goal_id)