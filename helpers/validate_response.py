import logging


def is_gpt_rephraser_response_valid(gpt_response, number_of_variants):
    try:
        if (
            gpt_response.get("number_of_variants", 0) == number_of_variants
            and len(gpt_response.get("variants", [])) == number_of_variants
        ):
            return True
        return False
    except Exception as e:
        logging.error(f"Failed to validate GPT response: {gpt_response} - error: {e}")
        return False


def is_gpt_content_generation_response_valid(gpt_response, expected_structure):
    try:
        expected_structure_dict = expected_structure.dict(exclude_none=True)

        for section_name, section_structure in expected_structure_dict.items():
            if not is_section_present(gpt_response, section_name):
                return False

            gpt_section = gpt_response[section_name]

            for attr, expected_count in section_structure.items():
                if not is_attribute_valid(gpt_section, attr, expected_count):
                    return False

        return True

    except Exception as e:
        logging.error(f"Failed to validate GPT content generation response: {e}")
        return False


def is_section_present(gpt_response, section_name):
    if section_name not in gpt_response:
        logging.error(f"Missing section: {section_name}")
        return False
    return True


def is_attribute_valid(gpt_section, attribute_name, expected_count):
    if attribute_name not in gpt_section:
        logging.error(f"Missing attribute '{attribute_name}'")
        return False

    if len(gpt_section[attribute_name]) != expected_count:
        logging.error(f"Incorrect number of '{attribute_name}' variants, expected {expected_count}")
        return False

    return True
