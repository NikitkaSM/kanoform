from typing import List
from pydantic import BaseModel


class QualificationQuestion(BaseModel):
    is_multiple: str
    answer_variants: list
    questionary: int


class FeatureQuestion(BaseModel):
    feature_name: str
    feature_description: str


class Questionary(BaseModel):
    name: str
    user: int
    feature_questions: List[FeatureQuestion]
    qualification_questions: List[QualificationQuestion]
