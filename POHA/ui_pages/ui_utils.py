import base64
import streamlit as st



def show_logo(width, padding, margin):
    with open('images/poha_icon.png', 'rb') as f:
        data = f.read()
    link = 'https://harshityadav.in'
    padding_top, padding_right, padding_bottom, padding_left = padding
    margin_top, margin_right, margin_bottom, margin_left = margin

    bin_str = base64.b64encode(data).decode()
    html_code = f'''
                <a href="{link}" target = _blank>
                    <img src="data:image/png;base64,{bin_str}"
                    style="
                     margin: auto;
                     width: {width}%;
                     margin-top: {margin_top}px;
                     margin-right: {margin_right}px;
                     margin-bottom: {margin_bottom}px;
                     margin-left: {margin_left}%;
                     padding-top: {margin_top}px;
                     padding-right: {padding_right}px;
                     padding-bottom: {padding_bottom}px;
                     padding-left: {padding_left}%;
                     "/>
                 </a>
                '''
    return html_code



def show_poha_logo(width, padding, margin):
    padding_top, padding_right, padding_bottom, padding_left = padding
    margin_top, margin_right, margin_bottom, margin_left = margin

    link = 'https://harshityadav.in'

    #sidebar image
    with open('images/poha_logo_transparent.png', 'rb') as f:
        data = f.read()

    bin_str = base64.b64encode(data).decode()
    html_code = f'''
                <img src="data:image/png;base64,{bin_str}"
                style="
                     margin: auto;
                     width: {width}%;
                     margin-top: {margin_top}px;
                     margin-right: {margin_right}px;
                     margin-bottom: {margin_bottom}px;
                     margin-left: {margin_left}%;
                     padding-top: {margin_top}px;
                     padding-right: {padding_right}px;
                     padding-bottom: {padding_bottom}px;
                     padding-left: {padding_left}%;
                     "/>
                '''

    return html_code
