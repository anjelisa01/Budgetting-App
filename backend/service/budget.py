from sqlalchemy.orm import Session
from sqlalchemy import select

from models.budget import Budget
from models.category import Category
from schemas.budget import BudgetBase,BudgetUpdate

from logger import logger

'''
from a category, we create budget for it.
'''

def create_budget(
    user_id:int,
    category_id:int,
    db:Session,
    budget:BudgetBase):
    '''find the user, find the category, create budget for that category
    need to claim ownership since budget HAVE to belong to a category'''
    
    #query category: (this is authentication check)
    # to check the category_id belong to authenticated user 
    category = (
        db.query(Category)
        .filter(
            Category.id == category_id,
            Category.user_id == user_id,
        )
        .first()
    )

    #build budget 
    db_budget=Budget(**budget.model_dump())
    db_budget.category_id=category_id

    db.add(db_budget)
    db.commit()
    logger.info("New budget Added for category_id =%s",category.category_name)

    db.refresh(db_budget)
    return db_budget

#one budget for one category
#so this is read that budget
def read_one_budget(
    user_id:int,
    category_id:int,
    db:Session):

    #auth check usign Category
    category = db.scalar(
        select(Category).where(
            Category.user_id==user_id,
            Category.id==category_id)
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    #data retrival from Budget table. 
    #theres no budget id for filtering because one category have one budget.
    budget = db.scalar(
        select(Budget).where(
            Budget.category_id==category.id
        )
    )
    if not budget:
        raise HTTPException(
            status_code=404,
            detail="Budget not found"
        )
    return budget


def update_budget(user_id:int,
    category_id:int,
    db:Session,
    payload:BudgetUpdate):
    #auth check, category
    #auth check usign Category
    category = db.scalar(
        select(Category).where(
            Category.user_id==user_id,
            Category.id==category_id)
    )
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    #find budget
    budget = db.scalar(
        select(Budget).where(
            Budget.category_id==category.id
        )
    )
    if not budget:
        raise HTTPException(
            status_code=404,
            detail="Budget not found"
        )

    #update
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(budget,field,value)

    db.commit()
    logger.info("Budget updated on category name=%s", category.category_name)

    db.refresh(budget)

    return budget

def delete_budget(user_id:int,
    category_id:int,
    db:Session):
    #auth check
    #auth check usign Category
    category = db.scalar(
        select(Category).where(
            Category.user_id==user_id,
            Category.id==category_id)
    )
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    #find budget
    budget = db.scalar(
        select(Budget).where(
            Budget.category_id==category.id
        )
    )
    if not budget:
        raise HTTPException(
            status_code=404,
            detail="Budget not found"
        )
    #delete
    db.delete(budget)
    db.commit()
    logger.info("Budget deleted. for category=%s", category.category_name)
    return{"message":"deleted"}