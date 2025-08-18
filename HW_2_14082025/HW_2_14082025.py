from flask import Flask
from pydantic import BaseModel, EmailStr, field_validator, Field, ValidationError, model_validator

json_input = """{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""

# json_input = """{
#     "name": "John Doe",
#     "age": 70,
#     "email": "john.doe@example.com",
#     "is_employed": true,
#     "address": {
#         "city": "New York",
#         "street": "5th Avenue",
#         "house_number": 123
#     }
# }"""

class Address(BaseModel):
    city: str = Field(..., min_length=2, description="City must have minimal 2 chair") #строка, минимум    2    символа.
    street: str = Field(..., min_length=3, description="Street must have minimal 3 chair") #строка, минимум    3    символа.
    house_number: int = Field(..., gt=0, description="House_number must be positive and numeric") #число, должно    быть    положительным.


class User(BaseModel):
    name: str = Field(...,min_length=2, pattern=r'^[A-Za-z\s]+$', description="Name must have minimal 2 chair and only alfabet") #строка, должна быть только из букв, минимум 2 символа.
    age: int = Field(...,ge=0, le=120, description="Age must be more than 0 and less than 120")#число, должно быть между 0 и 120.
    email: EmailStr = Field(..., description="Email must be email format") #строка, должна соответствовать формату email.
    is_employed: bool=Field(default=True) #булево значение, статус занятости пользователя.
    address: Address

    @model_validator(mode="after")# У меня установлена версия 2 pydantic, в нем есть model_validator, вместо field_validator
    def validate_age(cls,values):
        #is_employed=values.data.get("is_employed")
        if values.is_employed and not (18 <= values.age <= 65):
            raise ValueError("If you are working, your age must be between 18 and 65")
        return values

def user_json(json_data:str):
    try:
        user=User.model_validate_json(json_data)
        return user.model_dump_json(indent=4)
    except ValidationError as e:
        return e.json(indent=4)

user=user_json(json_input)
print(user)








