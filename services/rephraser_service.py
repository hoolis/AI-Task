from gpt.openai_chat_client import OpenAIChat
from helpers.json_convert import convert_string_to_json
from gpt.system_descriptions import get_rephraser_system_description
from helpers.validate_response import is_gpt_rephraser_response_valid
from models.rephraser_model import RephraseRequest
from fastapi import HTTPException, status
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from typing import List


class InvalidResponseException(Exception):
    """Exception for invalid or incorrectly formatted GPT responses."""


@retry(wait=wait_fixed(1), stop=stop_after_attempt(2), retry=retry_if_exception_type(InvalidResponseException))
async def rephraser_service(request: RephraseRequest) -> List[str]:
    gpt_response = await OpenAIChat().chat_completion_with_backoff(
        get_rephraser_system_description(request.number_of_variants), request.text
    )

    if not gpt_response:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve a response from the GPT service.",
        )

    rephrased_content = convert_string_to_json(gpt_response.choices[0].message.content)
    if not rephrased_content:
        raise InvalidResponseException("The GPT service response is not valid JSON.")

    if not is_gpt_rephraser_response_valid(rephrased_content, request.number_of_variants):
        raise InvalidResponseException("The GPT service did not return a valid rephraser response.")

    return rephrased_content["variants"]
