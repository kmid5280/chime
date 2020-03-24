"""Initializes the  dash html
"""
from typing import List

from dash.development.base_component import ComponentMeta

from chime_dash.app.utils.templates import read_localization_markdown
from dash_core_components import Markdown


LOCALIZATION_FILE = "definitions.md"


def setup(language: str) -> List[ComponentMeta]:
    """Initializes the header dash html
    """
    content = read_localization_markdown(LOCALIZATION_FILE, language)

    return [Markdown(content)]
