import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate


model = ChatOpenAI(
    model = 'gpt-4.1-2025-04-14',
    temperature=0.5,
)


system_prompt = """
당신은 취업 준비생입니다. 아래 입력값을 참고하여 500자 자기소개서를 작성해주세요.
자소서의 첫 부분에는 해당 질문에 대한 자기소개서의 제목을 []안에 넣어주세요.
"""


user_promt = """
대학교: {univ}
동아리: {circle}
봉사활동: {helper}
성격: {type}
인턴 : {intern}
수상경험 : {prize}
경력 : {carreer}
프로젝트 경험 : {project}
"""


prompt = ChatPromptTemplate.from_messages(
    [
       ("system", system_prompt),
       ("human", user_promt)
    ]
)
# print(prompt)


col1, col2, col3, col4 = st.columns(4)
with col1:
    univ = st.text_input("대학교명", placeholder= ' ')
    circle = st.text_input("동아리", placeholder= ' ')
with col2:
    helper = st.text_input("봉사활동", placeholder= ' ')
    type_ = st.text_input("성격", placeholder= ' ')    
with col3:
    intern = st.text_input("인턴", placeholder= ' ')
    prize = st.text_input("수상경험", placeholder= ' ')   

with col4:
    carreer = st.text_input("경력", placeholder= ' ')
    project = st.text_input("프로젝트", placeholder= ' ')   

print("-----------")
print(univ, circle, helper, type_)


if st.button("자소서 생성"):
    msgs = prompt.format_messages(
        univ = univ,
        circle = circle,
        helper = helper,
        type = type_,
        prize=prize,
        carreer=carreer,
        project=project,
        intern=intern
    )
    print(msgs)


    with st.spinner("자소서 생성중..."):
        response = model.invoke(msgs)
   
    st.success("생성 완료")


    st.text_area(label='결과', value=response.content, height=300)

