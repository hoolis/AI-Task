import json
import logging


def convert_string_to_json(content_string) -> dict | None:
    try:
        return json.loads(content_string)
    except json.JSONDecodeError:
        logging.error("Failed to convert GPT response to JSON.")
        return None
