import yaml
from dataclasses import dataclass

@dataclass
class PropagatorConfig:
    interval_seconds: int
    api_endpoint: str
    events_file: str

    @classmethod
    def from_yaml(cls, file_path: str) -> "PropagatorConfig":
        with open(file_path, 'r') as f:
            config_data = yaml.safe_load(f)
            return cls(**config_data)