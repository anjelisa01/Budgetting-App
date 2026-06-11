import pytest
from fastapi.testclient import TestClient
from main import app

from dotenv import load_dotenv
import os
load_dotenv()
AUTHENTICATED_USER=os.getenv("AUTHENTICATED_USER_TOKEN")

@pytest.fixture
def authenticated_client():
    client=TestClient(app)

    client.headers.update({
        "Authorization":f"Bearer {AUTHENTICATED_USER}"
    })
    return client
        


# #kalo mau pake db asli, comment all of this file

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# TEST_DATABASE_URL="sqlite:///./test.db"

# test_engine=create_engine(
#     TEST_DATABASE_URL,
#     connect_args={"check_same_thread":False}
# )

# TestingSessionLocal=sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=test_engine
# )


# from main import app
# from database import Base
# from dependency import get_db

# Base.metadata.create_all(bind=test_engine)

# def override_get_db():
#     db=TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db]=override_get_db