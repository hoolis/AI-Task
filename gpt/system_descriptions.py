def get_rephraser_system_description(number_of_variants) -> str:
    return (
        f"You have to rephrase the given text in the same langauge. "
        f"You must respond in JSON format and provide {number_of_variants} "
        f"variants of differently rephrased text. Your response must be as in an example below:"
        f'"number_of_variants": {number_of_variants}, "variants": ["rephrased_text"]}}'
    )


def get_content_generation_system_description(sections) -> str:
    return (
        f"You will receive a description about users website. "
        f"You are required and must generate content for each given section of a website, but no extra. "
        f"Each section has a corresponding count/number, how many variants of that type you need to generate. "
        f"Your response should be in the same language as provided description from user. "
        f"Your response should be formatted in JSON, the same way as this following dictionary: "
        f"{sections}"
    )
