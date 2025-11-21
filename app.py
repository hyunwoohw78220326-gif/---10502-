import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="🎰나랑 로또 한판 안할래..?🕹️", layout="centered")

# --- CSS 및 폰트 설정 ---
# 모든 CSS 코드는 st.markdown의 문자열 블록 안에 있어야 합니다.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

.stApp {
    /* 앱 전체에 배달의민족 도현체 적용 */
    font-family: 'Do Hyeon', sans-serif;
}

/* 당첨 메시지: 'success' 클래스 정의 */
.success {
    color: #FF4C4C !important; /* 붉은색 계열 */
    font-weight: bold;
}

/* 낙첨/경고 메시지: 'warning' 클래스 정의 */
.warning {
    color: #FF7F50 !important; /* 주황색 계열 */
    font-weight: bold;
}

/* st.title에 적용되는 h1 태그에 커스텀 폰트 적용 */
h1 {
    font-family: 'Do Hyeon', sans-serif;
}

</style>
""", unsafe_allow_html=True)
# ------------------------

# 제목
st.title("🎰나랑 로또 하지 않을래?..🕹️")

st.write("1~45 숫자 6개를 입력하고, 결과를 확인하세요.")
st.write("MADE BY 10502강현우")

# 사용자 입력
PLAY_input = st.text_input("숫자 6개를 띄어쓰기로 입력:")

if PLAY_input:
    try:
        # 입력된 문자열을 정수 리스트로 변환
        PLAY = [int(x) for x in PLAY_input.split()]
        
        # --- 입력 값 검증 ---
        if len(PLAY) != 6:
            st.error("⚠ 숫자는 정확히 **6개** 입력해야 합니다.")
        elif any(n < 1 or n > 45 for n in PLAY):
            st.error("⚠ **1~45** 사이 숫자만 입력 가능합니다.")
        elif len(set(PLAY)) != 6:
            st.error("⚠ **중복된** 숫자는 안 됩니다.")
        else:
            PLAY.sort()
            
            # 로또 번호 생성 (6개 당첨 번호 + 1개 보너스 번호)
            nums = random.sample(range(1, 46), 7)
            LOTTO = sorted(nums[:6])
            bonus = nums[6]
            
            st.write(f"**로또 당첨 번호:** {LOTTO}, **보너스 번호:** {bonus}")
            st.write(f"**당신의 번호:** {PLAY}")

            # 맞춘 개수 계산
            맞춘_개수 = len(set(PLAY) & set(LOTTO)) # 집합 연산을 사용하여 중복 없이 계산
            
            st.write(f"**맞춘 번호 개수:** {맞춘_개수}개")

            # --- 등수 판단 ---
            
            # 로또 당첨 등수 기준: (6개 일치=1등, 5개+보너스 일치=2등, 5개 일치=3등, 4개 일치=4등, 3개 일치=5등)
            
            message = ""
            is_winner = False
            
            if 맞춘_개수 == 6:
                message = "당신은 로또 **1등**입니다! 💰"
                is_winner = True
            elif 맞춘_개수 == 5:
                if bonus in PLAY:
                    message = "당신은 로또 **2등**입니다! (보너스 번호 일치) 🥈"
                    is_winner = True
                else:
                    message = "당신은 로또 **3등**입니다! 🥉"
                    is_winner = True
            elif 맞춘_개수 == 4:
                message = "당신은 로또 **4등**입니다! (5만원) 🎉"
                is_winner = True
            elif 맞춘_개수 == 3:
                message = "당신은 로또 **5등**입니다! (5천원) 🎉"
                is_winner = True
            else:
                message = "아쉽지만 **낙첨**입니다. 다음 기회에! 😢"

            # 결과 출력 (커스텀 CSS 클래스 적용)
            if is_winner:
                st.markdown(f'<p class="success">{message}</p>', unsafe_allow_html=True)
            else:
                st.markdown(f'<p class="warning">{message}</p>', unsafe_allow_html=True)


    except ValueError:
        st.error("⚠ **숫자**와 **띄어쓰기**만 입력해주세요.")
    
    # 등수 계산 로직의 오류 가능성 제거 (기존 코드의 등수 배열 사용 방식은 복잡했음)
