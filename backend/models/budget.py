#impors
from sqlalchemy import select, ForeignKey,func,String
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database import Base
'''
INFORMATION:
Budget have fk on user_id
budget - user: many to one
category-budget: one to one
category-transactions: one to many
'''

class Budget(Base):
    __tablename__="budget"

    #fields
    id:Mapped[int]=mapped_column(primary_key=True)
    limit:Mapped[float]
    period:Mapped[str] #buat enum
    
    #fk
    category_id:Mapped[int]=mapped_column(
        ForeignKey("category.id"), 
        unique=True 
    )

    #relationship
    category:Mapped["Category"]=relationship(
        back_populates="budget" 
    )
