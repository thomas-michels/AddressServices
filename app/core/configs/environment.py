"""
Module to load all Environment variables
"""

from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    """
    Environment, add the variable and its type here matching the .env file
    """

    # APPLICATION
    APPLICATION_HOST: str
    APPLICATION_PORT: int

    # DATABASE
    DATABASE_URL: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    ENVIRONMENT: str
    DATABASE_MIN_CONNECTIONS: int
    DATABASE_MAX_CONNECTIONS: int

    # REDIS
    REDIS_HOST: str
    REDIS_PORT: str
    TIMED_CACHE: int

    class Config:
        """Load config file"""

        env_file = ".env"
        extra='ignore'
