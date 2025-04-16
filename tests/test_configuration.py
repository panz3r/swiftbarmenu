
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


def test_configuration_set_str():
    # Act
    c = Configuration()
    c.set("test", "test")

    # Assert
    assert c.get("test") == "test"


def test_configuration_set_int():
    # Act
    c = Configuration()
    c.set("test", 1)

    # Assert
    assert c.get("test", type="int") == 1


def test_configuration_set_float():
    # Act
    c = Configuration()
    c.set("test", 2.3)

    # Assert
    assert c.get("test", type="float") == 2.3


def test_configuration_set_boolean():
    # Act
    c = Configuration()
    c.set("test", True)

    # Assert
    assert c.get("test", type="bool") is True


def test_configuration_set_multiple():
    # Act
    c = Configuration()
    c.set("test1", "test2").set("test2", 2).set(
        "test3", 3.4).set("test4", False)

    # Assert
    assert c.get("test1") == "test2"
    assert c.get("test2", type="int") == 2
    assert c.get("test3", type="float") == 3.4
    assert c.get("test4", type="bool") is False
