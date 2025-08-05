from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class MathAnswer:
    question:str
    answer:str
    steps:list[str]
    
class NextJSHelp(BaseModel):
    topic: str
    explanation: str
    code_sample: str