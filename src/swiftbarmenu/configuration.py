from __future__ import annotations

from configparser import ConfigParser
import os
from pathlib import Path
from typing import Any


class Configuration:
    def __init__(self):
        """Initialize a Configuration."""

        self.file_path = Path(
            os.getenv('SWIFTBAR_PLUGIN_DATA_PATH', '.'),
            'config.ini'
        )
        self.config = ConfigParser()

    def set(self, key: str, value: Any) -> Configuration:
        """
        Set a configuration string value for a given key.

        Args:
            key (str): The key for the configuration value.
            value (Any): The value to set for the given key.

        Returns:
            Configuration: This instance of Configuration for method chaining.
        """

        self.config.set("DEFAULT", key, str(value))

        return self

    def get(self, key: str, default: Any = None, type: str = "str") -> Any:
        """
        Get a configuration value for a given key.

        Args:
            key (str): The key for the configuration value.
            default (any, optional): The default value to return if the key is not found. Defaults to `None`.
            type (str, optional): The type of the configuration value. Defaults to "str".

        Returns:
            Any: The configuration value for the given key, or the default value if not found.
        """

        if type == "int":
            default_v = int(default) if default else None
            return self.config.getint("DEFAULT", key, fallback=default_v)
        elif type == "float":
            default_v = float(default) if default else None
            return self.config.getfloat("DEFAULT", key, fallback=default_v)
        elif type == "bool":
            default_v = bool(default) if default else None
            return self.config.getboolean("DEFAULT", key, fallback=default_v)
        else:
            return self.config.get("DEFAULT", key, fallback=default)

    def persist(self) -> Configuration:
        """Persist Configuration to a file."""

        with self.file_path.open('w') as config_file:
            self.config.write(config_file)

        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f"Configuration(path='{self.file_path}')")
