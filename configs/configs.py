from dataclasses import dataclass
from configs.parser.configparser import *

@parse("configs/config.json","jwt")
@dataclass
class JWTConfig:
  jwt_expiry: int
  jwt_algorithm: str
  email_key: str
  expiry_key: str

jwtConfig = JWTConfig()

@parse("configs/config.json","hash")
@dataclass
class HashConfig:
  password_hash_algorithm: str
  hash_repetitions: int

hashConfig = HashConfig()
