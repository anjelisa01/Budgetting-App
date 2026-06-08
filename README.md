# Budgetting-App

#IN crud the functions name follow pattern "create,read,update,delete-prefix"


#note on production flow
##Real production workflow (standard practice):

The correct long-term workflow is:
Models define intent → Migrations apply changes → DB evolves

So the real source of truth becomes:
Migrations (not models alone)

Flow:
Models → Alembic migration → PostgreSQL schema