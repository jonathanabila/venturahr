from dataclasses import dataclass


@dataclass
class UserStub:
    username: str

    first_name: str
    last_name: str
    email: str

    password1: str
    password2: str


@dataclass
class UserWithCompanyStub(UserStub):
    company: str
