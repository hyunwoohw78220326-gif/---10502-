import streamlit as st
import random
st.set_page_config(page_title="⭐🎰 나랑 로또 게임 해볼래..? 🎰 ⭐", page_icon="🎯", layout="centered")


st.title("🎰 10502 강현우 작품 🎰")
st.markdown(" **1부터 45까지 숫자** 중에서 **메인 6개 + 보너스 1개** 번호를 뽑습니다. 행운을 빌어요 🍀")
PLAY_input = st.text_input("로또 6개 숫자를 입력:")

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
            등수 = [6,5,4,3,2,1]  # 기존 코드 기준

            # 로또 번호 생성 (중복 없이 6개 + 보너스 1개)
            nums = random.sample(range(1,46),7)
            fi, se, th, fo, fif, si = nums[:6]
            bonus = nums[6]
            LOTTO = [fi, se, th, fo, fif, si]
            LOTTO.sort()  # 번호 정렬

            # 결과 출력
            st.write(f"진행자 : 로또 번호는 {LOTTO}, 보너스 번호는 {bonus}입니다.")
            st.write(f"입력한 번호: {PLAY}")

            # 맞춘 개수 계산
            for i in range(6):
                if PLAY[i] in LOTTO:
                    개수 += 1

            st.write(f"맞춘 개수는 {개수}개 입니다")

            # 등수 판단 (기존 코드 기준)
            if 개수 < 3:
                st.warning("낙첨입니다")
            else:
                # 보너스 체크 포함
                if 개수 == 5 and bonus in PLAY:
                    st.success("당신은 로또 2등 입니다! (보너스 번호 일치)")
                else:
                    for q in range(6):
                        if 개수 == 등수[q]:
                            st.success(f"당신은 로또 {q+1}등 입니다")
                            break
                        
    except ValueError:
        st.error("숫자만 입력해주세요")
