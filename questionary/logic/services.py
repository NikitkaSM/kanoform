from pydantic import BaseModel


class QualificationQuestionBaseModel(BaseModel):
    question: str
    is_multiple: str
    answer_variants: list
