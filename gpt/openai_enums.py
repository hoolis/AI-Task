from enum import StrEnum, Enum


class GPTRole(StrEnum):
    SYSTEM = "system"
    USER = "user"


class GPTJsonModel(StrEnum):
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_35_TURBO_1106 = "gpt-3.5-turbo-1106"


class GPTResponseFormat(StrEnum):
    JSON = "json_object"
    TEXT = "text"
