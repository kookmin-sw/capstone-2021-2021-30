import sys
import keypoint.main_keypoint as mk

def main():
    print("\n##### main.py #####\n")
    print("1. Keypoint")  # 유튜브 동영상 오디오 다운로드 후, 키포인트 테스트 케이스 생성
    # 마야 파이썬 스크립팅은 마야 프로그램 내에서만 가능
    #print("2. Motion")  # 키포인트 데이터(.json)을 스켈레톤 애니메이션으로 변환
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

    else:
        print("\n! Exit (Number out of range)")
        sys.exit()

if __name__ == '__main__':
    main()