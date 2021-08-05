from dataclasses import dataclass
from flask_tools.configparser import parse

@parse("configs/config.json","jwt")
@dataclass
class JWTConfig:
  jwt_expiry: int
  jwt_algorithm: str
  jwt_header_key: str

jwtConfig = JWTConfig()

@parse("configs/config.json","token_type")
@dataclass
class TokensConfig:
  auth_token: str
  email_confirm: str
  password_change: str

tokensConfig = TokensConfig()

