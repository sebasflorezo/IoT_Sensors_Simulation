from dataclasses import dataclass


@dataclass
class Valor:
    value: float
    unit: str

    def __str__(self) -> str:
        return f"{self.value}{self.unit}"

    def __repr__(self) -> str:
        return f"Valor(value={self.value!r}, unit={self.unit!r})"
