import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="🎰나랑 로또 한판 안할래..?🕹️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

.stApp {
    /* 앱 전체에 배달의민족 도현체 적용 */
    font-family: 'Do Hyeon', sans-serif;
}
</style>
""", unsafe_allow_html=True)

/* 당첨 메시지 */
.success {
    color: #FF4C4C !important;
    font-weight: bold;
}

/* 낙첨/경고 메시지 */
.warning {
    color: #FF7F50 !important;
    font-weight: bold;
}


# 제목
st.title("🎰나랑 로또 하지 않을래?..🕹️")

st.write("1~45 숫자 6개를 입력하고, 결과를 확인하세요.")
st.write("MADE BY 10502강현우")

# 사용자 입력
PLAY_input = st.text_input("숫자 6개를 띄어쓰기로 입력:")

if PLAY_input:
    try:
        PLAY = [int(x) for x in PLAY_input.split()]
        
        # 입력 체크
        if len(PLAY) != 6:
            st.error("⚠ 숫자는 정확히 6개 입력해야 합니다.")
        elif any(n < 1 or n > 45 for n in PLAY):
            st.error("⚠ 1~45 사이 숫자만 입력 가능")
        elif len(set(PLAY)) != 6:
            st.error("⚠ 중복된 숫자는 안 됩니다.")
        else:
            PLAY.sort()
            개수 = 0
            등수 = [6,5,4,3,2,1]

            # 로또 번호 생성 (중복 없이 6개 + 보너스 1개)
            nums = random.sample(range(1,46),7)
            fi, se, th, fo, fif, si = nums[:6]
            bonus = nums[6]
            LOTTO = [fi, se, th, fo, fif, si]
            LOTTO.sort()

            # 결과 출력
            st.write(f"진행자 : 로또 번호는 {LOTTO}, 보너스 번호는 {bonus}입니다.")
            st.write(f"입력한 번호: {PLAY}")

            # 맞춘 개수 계산
            for i in range(6):
                if PLAY[i] in LOTTO:
                    개수 += 1

            st.write(f"맞춘 개수는 {개수}개 입니다")

            # 등수 판단 (보너스 포함)
            if 개수 < 3:
                st.warning("낙첨입니다")
            else:
                if 개수 == 5 and bonus in PLAY:
                    st.success("당신은 로또 2등 입니다! (보너스 번호 일치)")
                else:
                    for q in range(6):
                        if 개수 == 등수[q]:
                            st.success(f"당신은 로또 {q+1}등 입니다")
                            break
                        
    except ValueError:
        st.error("⚠ 숫자만 입력해주세요")
