import sys
import keypoint.main_keypoint as mk
import motion.gui_motion as gm

def main():
    print("\n##### main.py #####\n")
    print("1. Keypoint")  # 유튜브 동영상 오디오 다운로드 후, 키포인트 테스트 케이스 생성
    print("2. Motion")  # 키포인트 데이터(.json)을 스켈레톤 애니메이션으로 변환
    print("?. Exit")

    # 번호 입력 예외 처리
    try:
        select = int(input("\nSelect the number: "))
    except:
        print("\n! Exit (Not Number)")
        sys.exit()

    # 번호 처리
    if select == 1:
        print("\n\tStart 1. Keypoint...")
        maink = mk.mainKeypoint()
        maink.excute()

    elif select == 2:
        print("\n\tStart 2. Motion...")
        guim = gm.GuiMotion()
        guim.show()

    else:
        print("\n! Exit (Number out of range)")
        sys.exit()

if __name__ == '__main__':
    main()