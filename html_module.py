import streamlit as st

# title 함수


def title(text):
    html = f"""
        <h2 style='
            color:rgba(105,146,230,1);
            font-weight:bold;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
        '>
            {text}
        </h2>
    """
    return st.markdown(html, unsafe_allow_html=True)


# section 함수
def section(text, width=300):
    html = f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <br/>
        <div style="
            width:{width}px;
            background: rgb(220,172,255);
            background: linear-gradient(20deg, rgba(220,172,255,1) 0%, rgba(105,146,230,1) 100%);
            padding:7px;
            border:none;
            border-radius:10px;
            margin-bottom:10px;
            box-shadow: 1px 1px 2px 1px rgba(0, 0, 0, 0.125);
        ">
            <h5 style="padding:4px;color:white;cursor:default;">
                <i class="fa-solid fa-magnifying-glass"></i>
                &nbsp;{text}
            </h5>
        </div>
    """
    return st.markdown(html, unsafe_allow_html=True)


# callout text 함수
def callout(text_list):
    html = """
        <div style="
            background-color:#eff2ff;
            color:#666;
            padding: 20px;
            border-radius:3px;
            margin-top: 1px;
        ">
        """
    for text in text_list:
        html += f'<span>{text}</span><br/>'
    html += "</div>"
    return st.markdown(html, unsafe_allow_html=True)


# 줄 띄우기 함수
def line_break():
    return st.markdown("<br/>", unsafe_allow_html=True)
