import streamlit as st
import openai
import time
import json


# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a header
st.header("欢迎使用 GPT 3.5!")

# Add some text
st.write("Powered by Johnny Tao")

# Add a sidebar
option = st.sidebar.selectbox("选择模型", ("GPT 3.5", "Davici-003"))

# Add a text input
text_input = st.text_input("Human:", "")

# Add a submit button
bnt = st.button("发送", use_container_width=True)
bnt2 = st.button("清空输入框", use_container_width=True)
bnt3 = st.button("清空对话记录", use_container_width=True)


API_KEY = st.secrets["openai_api_key"]
openai.api_key = API_KEY

while bnt2:
    text_input.value = ""

while bnt3:
    msg = []
    with open('msg.json', 'w') as f:
        json.dump(msg, f)
    
    st.write("历史对话记录已清空")
    bnt2 = False    

while bnt:
    with open('msg.json', 'r') as f:
        msg = json.load(f)  
    
    new_input_msg = text_input
    new_input = {"role": "user", "content": new_input_msg}
    msg.append(new_input)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=msg
    )

    new_output = completion.choices[0].message.to_dict()
    msg.append(new_output)
    
    with open('msg.json', 'w') as f:
        json.dump(msg, f)
    
    st.write("GPT 3.5:")
    st.write(new_output["content"])

    bnt = False
