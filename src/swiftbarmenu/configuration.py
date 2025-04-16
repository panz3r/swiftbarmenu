from __future__ import annotations

from configparser import ConfigParser
import os
from pathlib import Path


class Configuration:
    def __init__(self):
        """Initialize a Configuration."""

        self.file_path = Path(
            os.getenv('SWIFTBAR_PLUGIN_DATA_PATH', '.'),
            'config.ini'
        )
        self.config = ConfigParser()

    def persist(self) -> Configuration:
        """Persist Configuration to a file."""

        with self.file_path.open('w') as config_file:
            self.config.write(config_file)

        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f"Configuration(path='{self.file_path}')")
