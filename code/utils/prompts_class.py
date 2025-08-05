from pydantic import BaseModel, Field

from typing import Optional, List

class UserMessage(BaseModel):
        # rut: str = Field(description="User's identification number.")
        question: str = Field(description="User's question.")

# {format_instructions}  usar si se usa ChatPromptTemplate para obtener la relevancia de los documentos
# Document is used to store the document and its score
class DocumentScore(BaseModel):
        score: float = Field(description="Score between 0 and 1 indicating the document's relevance")

# ValidQuestion is used to validate the question based on programming language topics
class ValidQuestion(BaseModel):
        language_related: bool = Field(
                description="Indicates if the query is related with programming language topics",
                default=False
        )
        python_related: bool = Field(
                description="Indicates whether the query is related to topics related to the ""Python"" programming language.",
                default=False,
        )
        question: str = Field(
                description = "The last question of the user based on the history"
        )
        resason: Optional[str] = Field(
                default="",
                description="The reason why the question is not valid with the allowed topics"
        )   

# ValidLanguage is used to validate the Python language of the question
class ValidLanguage(BaseModel):
        valid: bool = Field(
                description="Indicates whether the question is valid. It is valid when the question is answered. Only one of these fields is required, and it will be ""True."".",
        )
        name: Optional[str] = Field(
                description="Indicate the question.",
                default="",
        )
        languaje: Optional[str] = Field(
                default="",
                description="Programming language topics"
        )
        reason: Optional[str] = Field(
                default="",
                description="The reason why the question is not valid."
        )        

