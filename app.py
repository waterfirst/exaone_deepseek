import streamlit as st
import time

from langchain.llms import Ollama

st.set_page_config(page_title="ExaSeek - AI Collaboration", page_icon="🤝", layout="wide")

st.title("🤝 ExaSeek - EXAONE & DeepSeek의 협업 AI")
st.markdown("---")

@st.cache_resource
def init_models():
   exaone = Ollama(model="exaone3.5:7.8b", temperature=0.7)
   deepseek = Ollama(model="deepseek-r1:7b", temperature=0.7)
   return exaone, deepseek

exaone, deepseek = init_models()

TRANSLATE_TEMPLATE = """다음 한글 질문을 영어로 번역하세요: {input}"""
ANSWER_TEMPLATE = """You are a helpful AI assistant. Please answer the following question: {input}"""
SUMMARIZE_TEMPLATE = """다음 영어 답변을 한글로 요약/정리해서 답변하세요: {input}"""

def get_response(user_input):
   with st.status("AI가 답변을 생성하고 있습니다...") as status:
       progress_bar = st.progress(0)
       
       # 번역 단계
       status.update(label="EXAONE이 질문을 영어로 번역중...")
       progress_bar.progress(25)
       eng_question = exaone.invoke(TRANSLATE_TEMPLATE.format(input=user_input))
       time.sleep(0.5)
       
       # DeepSeek 답변
       status.update(label="DeepSeek가 답변 생성중...")
       progress_bar.progress(50)
       eng_answer = deepseek.invoke(ANSWER_TEMPLATE.format(input=eng_question))
       time.sleep(0.5)
       
       # 최종 요약
       status.update(label="EXAONE이 답변을 한글로 정리중...")
       progress_bar.progress(75)
       final_answer = exaone.invoke(SUMMARIZE_TEMPLATE.format(input=eng_answer))
       time.sleep(0.5)
       
       progress_bar.progress(100)
       status.update(label="답변 생성 완료!", state="complete")
       
       return {
           "번역된 질문": eng_question,
           "영어 답변": eng_answer,
           "최종 답변": final_answer
       }

# 사이드바 설명
with st.sidebar:
   st.title("🔍 ExaSeek 소개")
   st.write("""
   ExaSeek은 EXAONE과 DeepSeek 모델의 장점을 결합한 협업 AI 시스템입니다:
   - EXAONE: 뛰어난 한글 이해력과 번역 능력
   - DeepSeek: 정교한 영어 답변 생성 능력
   """)
   
   st.markdown("---")
   st.write("Made with ❤️ by EXAONE & DeepSeek")

# 메인 UI
user_input = st.text_area("질문을 입력하세요:", height=100)

if st.button("답변 생성", type="primary"):
   if user_input:
       response = get_response(user_input)
       
       # 결과 표시
       with st.expander("🔍 처리 과정 보기"):
           st.write("번역된 질문:", response["번역된 질문"])
           st.write("DeepSeek 영어 답변:", response["영어 답변"])
           
       st.markdown("### 🤖 AI 답변")
       st.markdown(response["최종 답변"])
   else:
       st.warning("질문을 입력해주세요.")