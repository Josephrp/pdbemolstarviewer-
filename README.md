---
tags: [gradio-custom-component, File, pdb, molecule, chemistry, protein, visualization, bio, biopython, pdbe, molstar, gradio, tonic, viewer, structural, biology, medicine, research, dna, cell, 3D, dynamics, ligand, conformation, WebGL, binding, atom, chem, chemistry, med, sequence]
title: gradio_pdbemolstarviewer
short_description: renders protein structures from .pdb files using PDBe Molstar
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_pdbemolstarviewer`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.7%20-%20orange">  

renders protein structures from .pdb files using PDBe Molstar

## Installation

```bash
pip install gradio_pdbemolstarviewer
```

## Usage

```python
import gradio as gr
from pdbemolstarviewer import PDBeMolstarViewer

def render_protein(file):
    return file

demo = gr.Interface(
    render_protein,
    PDBeMolstarViewer(),
    PDBeMolstarViewer(),
    examples=[["example.pdb"]]
)

if __name__ == "__main__":
    demo.launch()
```

## `PDBeMolstarViewer`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
gradio.data_classes.FileData | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>
</tbody></table>




### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, the preprocessed input data sent to the user's function in the backend.


 ```python
 def predict(
     value: str | None
 ) -> str | None:
     return value
 ```
 
