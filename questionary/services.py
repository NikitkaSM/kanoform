from pydantic import BaseModel
from typing import List


class QualificationQuestionBaseModel(BaseModel):
    question: str
    is_multiple: str
    answer_variants: list
    questionary: int


class QualificationQuestionsBaseModel(BaseModel):
    questions: List[QualificationQuestionBaseModel]
