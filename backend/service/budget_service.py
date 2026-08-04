#import
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.budget import Budget
from models.category import Category
from schemas.budget import BudgetBase,BudgetUpdate
#util
from logger import logger
from exceptions import ResourceExistedError,ResourceNotFoundError

class BudgetService:
    def __init__(self,db: Session,user_id:int):
        self.db = db
        self.user_id=user_id
    def create(self,category_id:int,payload:BudgetBase):
        #find category
        category = (
            self.db.query(Category)
            .filter(
                Category.id == category_id,
                Category.user_id == self.user_id,
            )
            .first()
        )
        if category is None:
            raise ResourceNotFoundError("Category", category_id)
        #build budget data for the category
        budget=Budget(**payload.model_dump())
        budget.category_id=category.id
        #insert
        try:
            self.db.add(budget)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise 
        logger.info("Budget created, budget id=%s", budget.id)
        self.db.refresh(budget)
        return budget

    def read_one(self,category_id:int):
        #get category
        category = self.db.scalar(
            select(Category).where(
                Category.user_id==self.user_id,
                Category.id==category_id)
        )#raise Category have no budget, dont have to check for existence of budget in itself, because dont need too, if the category not found automatically the budget is not exist
        if category is None:
            raise ResourceNotFoundError("Category", category_id)        
        #get the budget for this category
        budget= self.db.scalar(
            select(Budget).where(
                Budget.category_id==category.id
            )
        )
        if budget is None:
            raise ResourceNotFoundError("Budget for Category", category_id)
        return budget

    def update(self,category_id:int,payload:BudgetBase):
        #find category
        category = self.db.scalar(
            select(Category).where(
                Category.user_id==self.user_id,
                Category.id==category_id)
        )
        if category is None:
            raise ResourceNotFoundError("Category", category_id)    
        # find budget 
        budget = self.db.scalar(
            select(Budget).where(
                Budget.category_id==category.id
            )
        ) 
        if budget is None:
            raise ResourceNotFoundError("Budget for Category", category_id) 
        #build update data
        update_data=payload.model_dump(exclude_unset=True)
        #update
        try:
            for field,value in update_data.items():
                setattr(budget,field,value)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        logger.info("Budget updated, category id =%s", category_id)
        self.db.refresh(budget)
        return budget
    def delete(self,category_id:int):
        #find category
        category = self.db.scalar(
            select(Category).where(
                Category.user_id==self.user_id,
                Category.id==category_id)
        )
        if category is None:
            raise ResourceNotFoundError("Category", category_id)       
        # find budget 
        budget = self.db.scalar(
            select(Budget).where(
                Budget.category_id==category.id
            )
        )
        if budget is None:
            raise ResourceNotFoundError("Budget for Category", category_id)
        #delete
        try:
            self.db.delete(budget)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        logger.info("Budget deleted.  category id=%s", category_id) 
        return{"message":"deleted"}
 