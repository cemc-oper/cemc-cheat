# coding=utf-8
import os
from textual.app import App, ComposeResult
from textual.widgets import Markdown, Footer


class MarkdownViewer(App):
    """A Textual app to display Markdown cheat sheets."""

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("t", "toggle_theme", "Toggle Theme"),
    ]

    CSS = """
    Markdown { margin: 1 2; }
    """

    def __init__(self, content: str, **kwargs):
        self.content = content
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield Markdown(self.content)
        yield Footer()

    def on_mount(self) -> None:
        """Detect terminal background and set initial theme."""
        colorfgbg = os.environ.get("COLORFGBG")
        if colorfgbg:
            try:
                bg = int(colorfgbg.split(";")[-1])
                # Background 0-7 are generally dark, 8-15 are light
                if bg >= 8:
                    self.theme = "textual-light"
                else:
                    self.theme = "textual-dark"
                return
            except ValueError:
                pass
        # Default to light when detection fails or is unavailable
        self.theme = "textual-light"

    def action_toggle_theme(self) -> None:
        """Toggle between light and dark themes."""
        self.theme = (
            "textual-light" if self.current_theme.dark else "textual-dark"
        )
