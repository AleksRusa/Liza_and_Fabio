votes = {"option1": 0, "option2": 0}


from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    @property
    def google_auth(self):
        config_auth = {
            "GOOGLE_CLIENT_ID": self.GOOGLE_CLIENT_ID,
            "GOOGLE_CLIENT_SECRET": self.GOOGLE_CLIENT_SECRET,
            "GOOGLE_REDIRECT_URI" : self.GOOGLE_REDIRECT_URI
        }
        return config_auth
    
    model_config = SettingsConfigDict(env_file=".env")

# Экземпляр настроек
settings = Settings() 