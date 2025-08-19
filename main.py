import streamlit as st

# MBTI별 직업 추천 딕셔너리 예시
job_recommendations = {
    "INTJ": ["전략 컨설턴트", "데이터 사이언티스트", "연구원"],
    "ENTP": ["창업가", "마케팅 기획자", "PD"],
    "INFJ": ["심리상담사", "작가", "교사"],
    "ESTJ": ["경영 관리자", "군인", "프로젝트 매니저"],
    # 필요하면 더 추가
}

st.set_page_config(page_title="MBTI 직업 추천", layout="centered")

st.title("🎯 MBTI 기반 진로 추천 사이트")
st.write("자신의 MBTI 유형을 선택하면 어울리는 직업을 추천해드립니다.")

# MBTI 선택 박스
mbti = st.selectbox("MBTI를 선택하세요:", list(job_recommendations.keys()))

# 추천 결과 출력
if mbti:
    st.subheader(f"✅ {mbti} 유형 추천 직업")
    for job in job_recommendations[mbti]:
        st.write(f"- {job}")
