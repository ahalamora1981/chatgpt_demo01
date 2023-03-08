import streamlit as st
import openai
import time
import json


def clear_text():
    st.session_state["text"] = ""

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a header
st.header("欢迎使用 GPT 3.5!")

# Add some text
st.write("Powered by Johnny Tao")

# Add a sidebar
option = st.sidebar.selectbox("选择模型", ("GPT 3.5", "Davici-003"))

# Add a text input
text_input = st.text_input("You:", key="text")

# Add a submit button
bnt = st.button("发送", use_container_width=True)
bnt2 = st.button("清空输入框", use_container_width=True, on_click=clear_text)
bnt3 = st.button("清空对话记录(即上下文重置)", use_container_width=True)


API_KEY = st.secrets["openai_api_key"]
openai.api_key = API_KEY

while bnt3:
#     msg = []
#     with open('msg.json', 'w') as f:
#         json.dump(msg, f)
        
    st.session_state["msg"] = []
    
    st.write("历史对话记录已清空")
    bnt3 = False    

while bnt:
#     with open('msg.json', 'r') as f:
#         msg = json.load(f)  

    if "msg" not in st.session_state:
        st.session_state["msg"] = []
    
    new_input_msg = text_input
    new_input = {"role": "user", "content": new_input_msg}
    st.session_state["msg"].append(new_input)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=st.session_state["msg"]
    )

    new_output = completion.choices[0].message.to_dict()
    st.session_state["msg"].append(new_output)
    
#     with open('msg.json', 'w') as f:
#         json.dump(msg, f)
    
    for msg in st.session_state["msg"][::-1]:
        if msg["role"] == "user":
            speaker = "YOU"
        elif msg["role"] == "assistant":
            speaker = "GPT"
        else:
            speaker = msg["role"]
            
        st.write(speaker + ": " + msg["content"])

    bnt = False
