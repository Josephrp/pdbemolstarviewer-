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