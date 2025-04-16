
from src.swiftbarmenu import Configuration


def test_configuration_str():
    p = Configuration()

    assert p.__str__() == "Configuration(path='config.ini')"


def test_configuration_repr():
    p = Configuration()

    assert p.__repr__() == "Configuration(path='config.ini')"
