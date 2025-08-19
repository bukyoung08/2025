import streamlit as st

# --- 데이터 정의 ---
job_recommendations = {
    "INTJ 🧠": ["데이터 사이언티스트 📊", "전략 컨설턴트 🕴️", "연구원 🔬", "엔지니어 ⚙️"],
    "INTP 💡": ["철학자 📖", "개발자 👨‍💻", "분석가 🔎", "과학자 🔭"],
    "ENTJ 🚀": ["CEO 👑", "경영 컨설턴트 📈", "변호사 ⚖️", "정치가 🎤"],
    "ENTP 🎭": ["창업가 💼", "마케팅 기획자 📢", "PD 🎬", "광고 전문가 📰"],

    "INFJ 🌱": ["심리상담사 🧑‍⚕️", "작가 ✍️", "교사 📚", "환경운동가 🌍"],
    "INFP 🎨": ["예술가 🎨", "작곡가 🎼", "사회복지사 🤝", "문학가 📜"],
    "ENFJ 🌟": ["강사 🎤", "HR 전문가 🧑‍💼", "교육자 📘", "커뮤니티 리더 👥"],
    "ENFP 🔥": ["디자이너 🎨", "여행작가 ✈️", "홍보 담당자 📣", "배우 🎭"],

    "ISTJ 📏": ["회계사 🧾", "법률가 ⚖️", "군인 🎖️", "은행원 🏦"],
    "ISFJ 🫶": ["간호사 🏥", "교사 📘", "사회복지사 🤲", "비서 🗂️"],
    "ESTJ 📊": ["프로젝트 매니저 📋", "군 간부 🪖", "기업 관리자 🏢", "판사 ⚖️"],
    "ESFJ 🤗": ["간호사 🧑‍⚕️", "초등교사 📚", "인사 담당자 🧑‍💼", "상담사 💬"],

    "ISTP 🛠️": ["기계공 🛠️", "파일럿 ✈️", "수리공 🔧", "운동선수 🏋️"],
    "ISFP 🎶": ["음악가 🎵", "패션 디자이너 👗", "사진작가 📸", "댄서 💃"],
    "ESTP ⚡": ["기업가 💼", "스포츠 코치 🏀", "소방관 🚒", "경찰 👮"],
    "ESFP 🎉": ["배우 🎭", "가수 🎤", "여행 가이드 🧳", "이벤트 플래너 🎪"],
}

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 직업 추천", layout="wide")

# --- CSS 꾸미기 ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #e0c3fc, #8ec5fc);
        }
        .stSelectbox label {
            font-size:20px !important;
            font-weight: bold;
            color: #4B0082;
        }
        .job-card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
            margin-bottom: 15px;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 앱 UI ---
st.title("✨ MBTI 기반 진로 추천 사이트 ✨")
st.subheader("당신의 MBTI를 선택하고, 어울리는 직업을 확인해보세요! 💼")

# 선택 박스
mbti = st.selectbox("👉 MBTI 유형을 선택하세요", list(job_recommendations.keys()))

# 결과 출력
if mbti:
    st.markdown(f"## ✅ {mbti} 추천 직업")
    for job in job_recommendations[mbti]:
        st.markdown(f"<div class='job-card'> {job} </div>", unsafe_allow_html=True)
