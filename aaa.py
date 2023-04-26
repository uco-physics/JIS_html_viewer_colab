import gradio as gr
import requests
from bs4 import BeautifulSoup


def render_html(url):
    
    response = requests.get(url)
    html = response.content
    if 'iso-2023-jp' in response.headers['content-type']:
        html = html.decode('iso-2022-jp').encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return str(soup)

inputs = gr.inputs.Textbox(label="URL")
outputs = gr.outputs.HTML()

interface = gr.Interface(fn=render_html, inputs=inputs, outputs=outputs)



with gr.Blocks() as demo:
    gr.Markdown("html変換ツール"):
    with gr.Tab("Flip0"):
        with gr.Column():
            inp0 = gr.inputs.Textbox(label = "URL")
            button0 = gr.Button("表示")
            out0 = gr.outpurs.HTML()
    with gr.Tab("Flip1"):
        with gr.Column():
            inp1 = gr.inputs.Textbox(label = "URL")
            button1 = gr.Button("表示")
            out1 = gr.outpurs.HTML()
    with gr.Tab("Flip2"):
        with gr.Column():
            inp2 = gr.inputs.Textbox(label = "URL")
            button2 = gr.Button("表示")
            out2 = gr.outpurs.HTML()
    with gr.Tab("Flip3"):
        with gr.Column():
            inp3 = gr.inputs.Textbox(label = "URL")
            button3 = gr.Button("表示")
            out3 = gr.outpurs.HTML()

    button0.click(render_html, inputs=inp0, outputs=out0)
    button1.click(render_html, inputs=inp1, outputs=out1)
    button2.click(render_html, inputs=inp2, outputs=out2)
    button3.click(render_html, inputs=inp3, outputs=out3)

if __name__ == "__main__":
    demo.launch()
