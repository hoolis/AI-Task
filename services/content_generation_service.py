from gpt.openai_chat_client import OpenAIChat
from helpers.json_convert import convert_string_to_json
from gpt.system_descriptions import get_content_generation_system_description
from helpers.validate_response import is_gpt_rephraser_response_valid, is_gpt_content_generation_response_valid
from models.content_generation_model import ContentGenerationRequest
from fastapi import HTTPException, status
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type


class InvalidResponseException(Exception):
    """Exception for invalid or incorrectly formatted GPT responses."""


@retry(wait=wait_fixed(1), stop=stop_after_attempt(2), retry=retry_if_exception_type(InvalidResponseException))
async def content_generation_service(request: ContentGenerationRequest):
    cleaned_model = request.sections.cleanup()

    gpt_response = await OpenAIChat().chat_completion_with_backoff(
        get_content_generation_system_description(cleaned_model), request.description
    )

    if not gpt_response:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve a response from the GPT service.",
        )

    generated_content = convert_string_to_json(gpt_response.choices[0].message.content)
    if not generated_content:
        raise InvalidResponseException("The GPT service response is not valid JSON.")

    if not is_gpt_content_generation_response_valid(generated_content, cleaned_model):
        raise InvalidResponseException("The GPT service did not return a valid content generation response.")

    return generated_content
