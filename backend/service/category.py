from sqlalchemy.orm import Session
from sqlalchemy import select

from models.category import Category
from schemas.category import CategoryBase

from logger import logger

def create_category(user_id:int,db:Session,category:CategoryBase):
    db_category=Category(**category.model_dump())
    db_category.user_id=user_id
    db.add(db_category)
    db.commit()
    logger.info("Category Added, category =%s",db_category.category_name)

    db.refresh(db_category)
    return db_category

def read_one_category(user_id:int,category_id:int,db:Session):
    db_category=db.scalar(
        select(Category).where(
            Category.user_id==user_id,
            Category.id==category_id)
    )
    return db_category


def read_all_categories(user_id:int,db:Session):
    #read all transaction from current user
    return db.scalars(
        select(Category).where(Category.user_id == user_id)
    ).all()

def update_category(user_id:int,category_id:int,db:Session,payload:AccountBase):
    stmt=select(Category).where(
        Category.user_id==user_id,
        Category.id==category_id)
    category=db.scalar(stmt)
    update_data=payload.model_dump(exclude_unset=True)
    
    for field,value in update_data.items():
        setattr(category,field,value)

    db.commit()
    logger.info("Category updated, category name changes to =%s", category_id)

    db.refresh(category)

    return category

def delete_category(user_id:int,category_id:int,db:Session):
    stmt=select(Category).where(
        Category.user_id==user_id,
        Category.id==category_id)
    category=db.scalar(stmt)
    db.delete(category)
    db.commit()
    logger.info("Category deleted.  user_id=%s", category_id)
    return{"message":"deleted"}
    
# def create_many_categories(user_id:int,db:Session,category:list[CategoryAdd]):
#     pass #a list, each value become a new row in a database.
