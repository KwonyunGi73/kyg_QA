# scripts/generate_summary.py

import os
import sys
import requests
import json

# GitHub Actions에서 설정한 환경 변수에서 API 키와 diff 내용을 가져옵니다.
API_KEY = os.environ.get("GEMINI_API_KEY")
DIFF_CONTENT = os.environ.get("DIFF_CONTENT")

# 필수 환경 변수가 없는 경우 에러를 출력하고 종료합니다.
if not API_KEY:
    sys.exit("에러: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
# diff 내용이 비어있을 수도 있으므로, 이 부분은 에러보다는 경고로 처리하거나 그대로 진행할 수 있습니다.
# 여기서는 비어있으면 스크립트를 정상 종료하도록 처리합니다.
if not DIFF_CONTENT:
    print("변경 내용이 없어 리뷰를 건너뜁니다.")
    sys.exit(0)

# Gemini API에 전달할 프롬프트입니다.
# f-string 포맷은 이대로 사용하는 것이 맞습니다.
prompt = f"""
당신은 전문 코드 리뷰어입니다. 다음 git diff 내용을 분석해서 한국어로 내용을 요약해주세요.
어떤 코드가 추가/변경되었고, 주요 변경 목적이 무엇인지 마크다운 형식으로 설명해주세요.
제목은 '🤖 AI 코드 리뷰 요약'으로 시작해주세요.

```diff
{DIFF_CONTENT}