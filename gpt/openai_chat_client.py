import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from gpt.openai_enums import GPTRole, GPTJsonModel, GPTResponseFormat
from models.openai_output_model import ChatResponse
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

load_dotenv()

openai_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
TIMEOUT_SECONDS = 30


class OpenAIChat:
    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
    async def chat_completion_with_backoff(self, system_description: str, messages: str) -> ChatResponse | None:
        try:
            response = await openai_client.chat.completions.create(
                messages=[
                    {"role": GPTRole.SYSTEM, "content": system_description},
                    {"role": GPTRole.USER, "content": messages},
                ],
                model=GPTJsonModel.GPT_4_1106_PREVIEW,
                response_format={"type": GPTResponseFormat.JSON},
                timeout=TIMEOUT_SECONDS,
            )
            return ChatResponse(**response.model_dump())
        except Exception as e:
            logging.error(f"GPT API call failed with error: {e}")
            return None
