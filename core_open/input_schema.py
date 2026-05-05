from dataclasses import dataclass

VALID_ARCH = {"low", "medium", "high"}
VALID_INSTEP = {"none", "mild", "moderate", "high"}
VALID_USE_CASE = {"daily_walking", "standing", "indoor", "light_activity"}
VALID_SPACE_PREF = {"thin", "medium", "thick"}


@dataclass
class InsoleInput:
    left_foot_length_mm: float
    right_foot_length_mm: float
    left_forefoot_width_mm: float
    right_forefoot_width_mm: float
    arch_height_level: str
    instep_pressure_level: str
    use_case: str
    in_shoe_space_preference: str

    @classmethod
    def from_dict(cls, data: dict) -> "InsoleInput":
        obj = cls(**data)
        obj.validate()
        return obj

    def validate(self) -> None:
        for name in [
            "left_foot_length_mm",
            "right_foot_length_mm",
            "left_forefoot_width_mm",
            "right_forefoot_width_mm",
        ]:
            val = getattr(self, name)
            if not isinstance(val, (int, float)):
                raise ValueError(f"{name} must be numeric")
            if val <= 0:
                raise ValueError(f"{name} must be > 0")

        if self.arch_height_level not in VALID_ARCH:
            raise ValueError("arch_height_level must be one of: low, medium, high")
        if self.instep_pressure_level not in VALID_INSTEP:
            raise ValueError("instep_pressure_level must be one of: none, mild, moderate, high")
        if self.use_case not in VALID_USE_CASE:
            raise ValueError("use_case must be one of: daily_walking, standing, indoor, light_activity")
        if self.in_shoe_space_preference not in VALID_SPACE_PREF:
            raise ValueError("in_shoe_space_preference must be one of: thin, medium, thick")
