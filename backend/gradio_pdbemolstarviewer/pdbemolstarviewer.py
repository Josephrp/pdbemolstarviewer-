import tempfile
from pathlib import Path
from typing import Any, Dict

import gradio as gr
from gradio.components import Component
from gradio.data_classes import FileData

class PDBeMolstarViewer(Component):
    EVENTS = []

    def __init__(
        self,
        value: FileData | None = None,
        *,
        label: str | None = None,
        every: float | None = None,
        show_label: bool = True,
        interactive: bool = True,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        **kwargs,
    ):
        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            **kwargs,
        )

    def preprocess(self, x: FileData | None) -> str | None:
        if x is None:
            return None
        return x.path
    
    def postprocess(self, y: str | None) -> FileData | None:
        if y is None:
            return None
        return FileData(path=y, orig_name=Path(y).name)

    def example_inputs(self) -> Dict[str, Any]:
        return {
            "value": FileData(path="example.pdb", orig_name="example.pdb"),
        }