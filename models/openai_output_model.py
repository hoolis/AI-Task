from pydantic import BaseModel
from typing import Optional, List, Dict


class Message(BaseModel):
    content: str
    role: str
    function_call: Optional[str] = None
    tool_calls: Optional[str] = None


class Choice(BaseModel):
    finish_reason: str
    index: int
    logprobs: Optional[Dict]
    message: Message


class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class ChatResponse(BaseModel):
    id: str
    choices: List[Choice]
    created: int
    model: str
    object: str
    system_fingerprint: str
    usage: Usage
