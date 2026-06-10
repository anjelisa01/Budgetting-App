#if making changes in the sqlalchemy models level, i have to also change on the posgresql level
#changing in sqlalchemyy level doesnt automatically change the db 

#Because SQLAlchemy is NOT an ORM that syncs schema automatically 
#(unless you explicitly use migration tools or drop/create tables).

from sqlalchemy import select, ForeignKey,func,String
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database import Base

# (User-Transaction) - one to many
# i want the transactions to have one user

#Table User
class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(255))
    email:Mapped[str]=mapped_column(String(255))
    hashed_password:Mapped[str]=mapped_column(String(255))

    #defining relationship:
    transactions:Mapped[list["Transaction"]]=relationship(
        back_populates="user"
        #about back populates:
        #biderctional relationship, so changes in user.transactions automaticalley updates transaction.user
        #so the relationship synchronized in python
    )
    #so atribut of class User name 'transaction' is defining a 
    #relationship, where 'transaction' contains a liist of 
    #Transaction objects
    #AND this relationship corresponding to the class Transaction atribut call 'user'

#so back_populates needed both table that connected to defined that they are conncted 

#one row of thable 'users'
#so one object instance is one row 
# user = User(    
#     name="John",
#     email="john@gmail.com"
# )



#Table transactions
class Transaction(Base):
    __tablename__="transactions"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]
    amount:Mapped[float]
    note:Mapped[str]
    created_at:Mapped[datetime]=mapped_column(
        server_default=func.now() #this is fill created_at at the database level
    )

    user_id:Mapped[int]=mapped_column(
        ForeignKey("users.id") #
    )

    user:Mapped["User"]=relationship(
        back_populates="transactions" 
    )


#one row of 'transactions' table
# t1 = Transaction(
#     title="Bought Book",
#     note="Python book",
#     created_at="2025-06-03",
#     user_id=1
# )

# t2 = Transaction(
#     title="Bought Coffee",
#     note="Latte",
#     created_at="2025-06-03",
#     user_id=1
# )
