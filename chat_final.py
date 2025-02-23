from langchain.llms import Ollama

# 모델 초기화 
exaone = Ollama(model="exaone3.5:7.8b", temperature=0.7)
deepseek = Ollama(model="deepseek-r1:7b", temperature=0.7)

TRANSLATE_TEMPLATE = """다음 한글 질문을 영어로 번역하세요:
{input}"""

ANSWER_TEMPLATE = """You are a helpful AI assistant. Please answer the following question:
{input}"""

SUMMARIZE_TEMPLATE = """다음 영어 답변을 한글로 요약/정리해서 답변하세요:
{input}"""

def get_response(user_input):
   try:
       # 엑사원이 한글->영어 번역
       eng_question = exaone.invoke(TRANSLATE_TEMPLATE.format(input=user_input))
       
       # Deepseek가 영어로 답변
       eng_answer = deepseek.invoke(ANSWER_TEMPLATE.format(input=eng_question))
       
       # 엑사원이 영어->한글 요약/정리
       final_answer = exaone.invoke(SUMMARIZE_TEMPLATE.format(input=eng_answer))
       
       return {
           "번역된 질문": eng_question,
           "영어 답변": eng_answer, 
           "최종 답변": final_answer
       }
   except Exception as e:
       print(f"오류 발생: {str(e)}")
       return None

if __name__ == "__main__":
   while True:
       user_input = input("\n질문을 입력하세요 (종료: q): ")
       if user_input.lower() == 'q':
           break
           
       response = get_response(user_input)
       if response:
           print("\n[디버그] 번역된 질문:", response["번역된 질문"])
           print("\n[디버그] 영어 답변:", response["영어 답변"]) 
           print("\n최종 답변:", response["최종 답변"])