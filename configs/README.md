# Configs
- All application configs should be set in the config.json file.
- Configs can be accessed by creating a data class in the config.py folder
- All config classes must add the decorator "@parse(filname,path) with filename being the name of the config file, e.g. "configs/config.json" and path is the "." deliminated path to the required config object in the config json file e.g. "application.password_confg". Example code:
  ```
  @parse("configs/config.json","jwt")
  @dataclass
  class JWTConfig:
    jwt_expiry: int
    jwt_algorithm: str
    email_key: str
    expiry_key: str
  ```
- An instance of each config class should then be creaed which can be accessed from other files. Example:
  ```
  jwtConfig = JWTConfig()
  ```

# Flask Config
- All flask app configs are set in the flask_config folder in classes. Configs must be set for local, testing and deployment. 
