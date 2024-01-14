from pydantic import BaseModel, Field, Extra
from typing import Optional


class SectionStructure(BaseModel):
    title: Optional[int] = Field(None, ge=1, description="Number of title variants required")
    subtitle: Optional[int] = Field(None, ge=1, description="Number of subtitle variants required")
    description: Optional[int] = Field(None, ge=1, description="Number of description variants required")

    class Config:
        extra = Extra.forbid

    def cleanup(self):
        """Removes all fields that are None"""
        none_fields = {field for field in self.model_fields.keys() if getattr(self, field) is None}

        for field in none_fields:
            delattr(self, field)

        return None if len(none_fields) == len(self.model_fields) else self


class Sections(BaseModel):
    about: Optional[SectionStructure] = Field(None, description="Structure for the 'About' section")
    refunds: Optional[SectionStructure] = Field(None, description="Structure for the 'Refunds' section")
    hero: Optional[SectionStructure] = Field(None, description="Structure for the 'Hero' section")

    class Config:
        extra = Extra.forbid

    def cleanup(self):
        """Removes all fields that are None"""
        empty_sections = []

        for section_name, section in self.__dict__.items():
            if section is None or (section and section.cleanup() is None):
                empty_sections.append(section_name)

        for section_name in empty_sections:
            delattr(self, section_name)

        return self


class ContentGenerationRequest(BaseModel):
    description: str = Field(..., description="User business description")
    sections: Sections = Field(..., description="Sections required for the website with structure")

    class Config:
        extra = Extra.forbid
