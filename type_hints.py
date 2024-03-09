from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    account_id: int


user = User(name="12", email="m", account_id=1)
print(user)
