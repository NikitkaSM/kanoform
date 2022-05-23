from typing import List
from pydantic import BaseModel


class QualificationQuestion(BaseModel):
    question: str
    is_multiple: str
    answer_variants: list
    questionary: int

    class Config:
        orm_mode = True


class FeatureQuestion(BaseModel):
    questionary: int
    feature_name: str
    feature_description: str

    class Config:
        orm_mode = True


class Questionary(BaseModel):
    name: str
    user: int
    feature_questions: List[FeatureQuestion]
    qualification_questions: List[QualificationQuestion]
