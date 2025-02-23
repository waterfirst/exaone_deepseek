# ExaSeek 설치 가이드

## 1. Ollama 설치
### Windows
1. [ollama.ai/download](https://ollama.ai/download) 방문
2. Windows 설치 파일 다운로드 및 실행
3. 설치 완료 후 Windows 시스템 트레이에서 Ollama 실행 확인

### Mac
1. [ollama.ai/download](https://ollama.ai/download) 방문
2. Mac 설치 파일 다운로드 및 실행
3. 터미널에서 `ollama` 명령어로 실행 확인

### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

## 2. 모델 다운로드
터미널/CMD에서:
```bash
ollama pull exaone3.5:7.8b
ollama pull deepseek-r1:7b
```
각 모델 약 4-5GB, 총 10GB 저장공간 필요

## 3. Python 환경 설정
```bash
git clone https://github.com/your-username/exaseek
cd exaseek
pip install -r requirements.txt
```

## 4. 실행
```bash
streamlit run app.py
```
기본 브라우저에서 자동으로 http://localhost:8501 열림

## 문제해결
- Ollama 실행 확인: `ollama list` 
- GPU 메모리 부족: 에러 발생시 `app.py`의 temperature 값 낮춤
- 모델 로딩 오류: Ollama 서비스 재시작




# ExaSeek - EXAONE & DeepSeek Collaboration AI

오픈소스 LLM 모델인 EXAONE과 DeepSeek를 결합한 로컬 AI 대화 시스템입니다.

## 주요 기능
- EXAONE (한글 번역/이해) + DeepSeek (영어 답변 생성) 협업
- 100% 로컬 실행 - 인터넷 연결 불필요
- Streamlit 기반 직관적 UI
- 단계별 처리 현황 표시

## 설치 방법

1. Ollama 설치
```bash
# Windows/Mac 설치: https://ollama.ai/download
# Linux:
curl -fsSL https://ollama.ai/install.sh | sh
```

2. 필요 모델 다운로드
```bash
ollama pull exaone3.5:7.8b
ollama pull deepseek-r1:7b
```

3. Python 패키지 설치
```bash
pip install -r requirements.txt
```

4. 실행
```bash
streamlit run app.py
```

## 시스템 요구사항
- Python 3.8+
- RAM: 최소 16GB (권장 32GB)
- NVIDIA GPU: 최소 8GB VRAM

## 라이선스
MIT License

## 데모
https://exaseek.streamlit.app
```

```txt
# requirements.txt

streamlit>=1.30.0
langchain>=0.1.0 
ollama>=0.1.4
python-dotenv>=1.0.0
```
