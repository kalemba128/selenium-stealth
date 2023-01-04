from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def with_utils(driver: Driver, utils_path: Path = None, **kwargs) -> None:
    def get_path() -> Path:
        if utils_path is not None:
            return utils_path
        return Path(__file__).parent.joinpath("js/utils.js")

    evaluateOnNewDocument(
        driver, get_path().read_text()
    )
