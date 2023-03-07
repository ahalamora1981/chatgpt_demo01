import streamlit as st
import openai
import time


# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a header
st.header("Welcome to my ChatGPT 3.5!")

# Add some text
st.write("This is some sample text.")

# Add a sidebar
option = st.sidebar.selectbox("Select an option", ("one", "two", "three"))

# Add a text input
text_input = st.text_input("Enter some text")

# Add a submit button
bnt = st.button("Submit")


API_KEY = "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"
openai.api_key = API_KEY

msg = []

while bnt:

    new_input_msg = text_input
    new_input = {"role": "user", "content": new_input_msg}
    msg.append(new_input)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=msg
    )

    new_output = completion.choices[0].message.to_dict()
    msg.append(new_output)
    text_output = st.text_input("AI Repsposne: ", value=new_output)
    print(new_output)

    time.sleep(500)