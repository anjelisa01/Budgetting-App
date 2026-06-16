# Budgetting-App


# how to test
1. sign up 
    make sure using new email
    pytest -m signup
2. login 
    make sure existing user credential
    pytest -m login
3. full crud 
    make sure existing user credential
    pytest -m user_crud_flow

#where to log
log only important event

app startup,
endpoints calls
errors




#IN crud the functions name follow pattern "create,read,update,delete-prefix"


#note on production flow
##Real production workflow (standard practice):

The correct long-term workflow is:
Models define intent → Migrations apply changes → DB evolves

So the real source of truth becomes:
Migrations (not models alone)

Flow:
Models → Alembic migration → PostgreSQL schema