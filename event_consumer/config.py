import yaml
from dataclasses import dataclass

@dataclass
class ConsumerConfig:
    port: int
    database_url: str

    @classmethod
    def from_yaml(cls, file_path: str) -> "ConsumerConfig":
        with open(file_path, 'r') as f:
            config_data = yaml.safe_load(f)
            return cls(**config_data)