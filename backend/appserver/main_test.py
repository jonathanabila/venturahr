import pytest

from appserver.main import main


class TestMain:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        self.sut = main

    def test_main(self) -> None:
        assert main() is True
