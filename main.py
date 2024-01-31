import os
import streamlit as st
from langchain_openai import ChatOpenAI

# 환경 변수 가져오기
api_key = os.getenv("OPEN_API_KEY")

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')

# API 키를 사용하여 ChatOpenAI 모델 인스턴스화
chat_model = ChatOpenAI(api_key=api_key)

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        response = chat_model.invoke(content + "에 대한 시를 써줘")
        # AIMessage 객체에서 텍스트를 추출하기 위해 적절한 속성을 사용합니다.
        response_text = response.content  # 예를 들어서 'content' 속성을 사용하는 경우입니다.
        # 시를 출력할 때 '\n'을 공백으로 대체하여 줄바꿈이 일어나도록 합니다.
        response_text = response_text.replace('\n', ' ')
        st.write(response_text)










#from langchain_openai import OpenAI

# OpenAI 객체 초기화
#llm = OpenAI(api_key=api_key)

# 예측 수행
#result = llm.invoke("내가 좋아하는 동물은")
#print(result)
