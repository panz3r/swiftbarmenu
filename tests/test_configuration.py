
from src.swiftbarmenu import Configuration


def test_configuration_str():
    p = Configuration()

    assert p.__str__() == "Configuration(path='config.ini')"


def test_configuration_repr():
    p = Configuration()

    assert p.__repr__() == "Configuration(path='config.ini')"


def test_configuration_persist_empty(monkeypatch, tmp_path):
    # Arrange
    plugin_data_p = tmp_path / "test.1h.py"
    plugin_data_p.mkdir()

    monkeypatch.setenv('SWIFTBAR_PLUGIN_DATA_PATH', plugin_data_p.as_posix())
    monkeypatch.setenv('SWIFTBAR_PLUGIN_PATH', '/sbm/plugins/test.1h.py')

    # Act
    c = Configuration()
    c.persist()

    # Assert
    assert (plugin_data_p / 'config.ini').exists()
