
# ! user_data.py
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int
    role: str
    university:str
    course:str

# @dataclass
# class UserData:
#     name: str
#     age: int
#     role: str