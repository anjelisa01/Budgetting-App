from sqlalchemy.orm import Session
from sqlalchemy import select

from models.goal import Goal
from schemas.goal import GoalBase,GoalUpdate

from logger import logger

def create_goal(user_id:int,db:Session,goal:GoalBase):
    #add user_id to the data to insert to db
    db_goal=Goal(**goal.model_dump())
    db_goal.user_id=user_id
    db.add(db_goal)
    db.commit()
    logger.info("New Goal created, Goal name=%s",db_goal.goal_name)

    db.refresh(db_goal)
    return db_goal

def read_one_goal(user_id:int,goal_id:int,db:Session):
    db_goal=db.scalar(
        select(Goal).where(
            Goal.user_id==user_id,
            Goal.id==goal_id)
    )
    return db_goal

def read_all_goals(user_id:int,db:Session):
    return db.scalars(
        select(Goal).where(Goal.user_id == user_id)
    ).all()

def update_goal(user_id:int,goal_id:int,db:Session,payload:GoalUpdate):
    stmt=select(Goal).where(
        Goal.user_id==user_id,
        Goal.id==goal_id)
    goal=db.scalar(stmt)
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(goal,field,value)

    db.commit()
    logger.info("Goal updated, transaction name changes to =%s", goal_id)

    db.refresh(goal)

    return goal

def delete_goal(user_id:int,goal_id:int,db:Session):
    stmt=select(Goal).where(
        Goal.user_id==user_id,
        Goal.id==goal_id)
    goal=db.scalar(stmt)
    db.delete(goal)
    db.commit()
    logger.info("Goal deleted.  Goal name=%s", goal.goal_name) #supposed to be account_id
    return{"message":"deleted"}

