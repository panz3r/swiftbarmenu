from __future__ import annotations

import os
from pathlib import Path


class Configuration:
    def __init__(self):
        """Initialize a Configuration."""

        self.file_path = Path(
            os.getenv('SWIFTBAR_PLUGIN_DATA_PATH', '.'),
            'config.ini'
        )

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f"Configuration(path='{self.file_path}')")
