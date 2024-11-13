import streamlit as st
from openai import OpenAI

# Session state에 API key가 없으면 입력받도록 설정
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.session_state.api_key = st.text_input("OpenAI API Key", type='password', value=st.session_state.api_key)

# OpenAI client 생성
client = OpenAI(api_key=st.session_state.api_key)

# Prompt 입력란
prompt = st.text_area("Prompt")
messages = [
    {"role": "user", "content": prompt}
]

answer = ''

# Generate 버튼이 클릭되면 응답 생성
if st.button("Generate"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    answer = response.choices[0].message.content

st.text(answer)

# 이미지 생성 버튼과 이미지 표시
image_url = ''

if st.button("Image"):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url

if image_url:
    st.markdown(f"![{prompt}]({image_url})")
