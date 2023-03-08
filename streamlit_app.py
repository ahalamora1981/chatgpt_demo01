import streamlit as st
from streamlit.hashing import _CodeHasher
import openai
import time
import json


def get_state():
    # Create a hash of the current script code
    state = _CodeHasher().transform(__name__)
    # Initialize session state if it doesn't exist
    if state not in st.session_state:
        st.session_state[state] = {
            'msg': []
        }
    return st.session_state[state]

state = get_state()

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a header
st.header("欢迎使用 GPT 3.5!")

# Add some text
st.write("Powered by Johnny Tao")

# Add a sidebar
option = st.sidebar.selectbox("选择模型", ("GPT 3.5", "Davici-003"))

# Add a text input
text_input = st.text_input("Human:")

# Add a submit button
bnt = st.button("发送", use_container_width=True)
bnt2 = st.button("清空对话记录", use_container_width=True)


API_KEY = st.secrets["openai_api_key"]
openai.api_key = API_KEY

while bnt2:
#     msg = []
#     with open('msg.json', 'w') as f:
#         json.dump(msg, f)
    
    state = get_state()
    
    st.write("历史对话记录已清空")
    bnt2 = False    

while bnt:
#     with open('msg.json', 'r') as f:
#         msg = json.load(f)  
    
    new_input_msg = text_input
    new_input = {"role": "user", "content": new_input_msg}
    state["msg"].append(new_input)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=state["msg"]
    )

    new_output = completion.choices[0].message.to_dict()
    state["msg"].append(new_output)
    
#     with open('msg.json', 'w') as f:
#         json.dump(msg, f)
    
    st.write("GPT 3.5:")
    st.write(new_output["content"])

    bnt = False
