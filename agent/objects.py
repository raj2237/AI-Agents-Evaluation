from pydantic import BaseModel, Field 

class ConversationStatus(BaseModel):
    conversation: bool = Field(
        description="Whether the assistant needs another user reply to continue the refund request"
    )

class PurchaseItem(BaseModel):
    name: str = Field(description="name of the item puchased")

    