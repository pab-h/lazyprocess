from dataclasses import dataclass

@dataclass()
class Edit(object): 
    origin: str
    destiny: str
    versions: list[str]
