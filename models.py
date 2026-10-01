from pydantic import BaseModel, Field

class MedicineInfo(BaseModel):

    medicine_name: str = Field(
        description="Name of the medicine."
    )

    indications: list[str] = Field(
        description="Approved indications."
    )

    mechanism_of_action: str = Field(
        description="How the medicine works."
    )

    common_side_effects: list[str] = Field(
        description="Common side effects."
    )

    contraindications: list[str] = Field(
        description="Contraindications."
    )