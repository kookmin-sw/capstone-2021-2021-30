import cv2, json, os, time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

class MotionData:
    def __init__(self):
        self.file_data = dict()

        self.left_shoulder = dict()
        self.left_elbow = dict()
        self.left_wrist = dict()
        self.left_thumb_cmc = dict()
        self.left_thumb_mcp = dict()
        self.left_thumb_ip = dict()
        self.left_thumb_tip = dict()
        self.left_index_finger_mcp = dict()
        self.left_index_finger_pip = dict()
        self.left_index_finger_dip = dict()
        self.left_index_finger_tip = dict()
        self.left_middle_finger_mcp = dict()
        self.left_middle_finger_pip = dict()
        self.left_middle_finger_dip = dict()
        self.left_middle_finger_tip = dict()
        self.left_ring_finger_mcp = dict()
        self.left_ring_finger_pip = dict()
        self.left_ring_finger_dip = dict()
        self.left_ring_finger_tip = dict()
        self.left_pinky_mcp = dict()
        self.left_pinky_pip = dict()
        self.left_pinky_dip = dict()
        self.left_pinky_tip = dict()
        self.right_shoulder = dict()
        self.right_elbow = dict()
        right_wrist = dict()
        right_thumb_cmc = dict()
        right_thumb_mcp = dict()
        right_thumb_ip = dict()
        right_thumb_tip = dict()
        right_index_finger_mcp = dict()
        right_index_finger_pip = dict()
        right_index_finger_dip = dict()
        right_index_finger_tip = dict()
        right_middle_finger_mcp = dict()
        right_middle_finger_pip = dict()
        right_middle_finger_dip = dict()
        right_middle_finger_tip = dict()
        right_ring_finger_mcp = dict()
        right_ring_finger_pip = dict()
        right_ring_finger_dip = dict()
        right_ring_finger_tip = dict()
        right_pinky_mcp = dict()
        right_pinky_pip = dict()
        right_pinky_dip = dict()
        right_pinky_tip = dict()

        left_shoulder_x = dict()
        left_elbow_x = dict()
        left_wrist_x = dict()
        left_thumb_cmc_x = dict()
        left_thumb_mcp_x = dict()
        left_thumb_ip_x = dict()
        left_thumb_tip_x = dict()
        left_index_finger_mcp_x = dict()
        left_index_finger_pip_x = dict()
        left_index_finger_dip_x = dict()
        left_index_finger_tip_x = dict()
        left_middle_finger_mcp_x = dict()
        left_middle_finger_pip_x = dict()
        left_middle_finger_dip_x = dict()
        left_middle_finger_tip_x = dict()
        left_ring_finger_mcp_x = dict()
        left_ring_finger_pip_x = dict()
        left_ring_finger_dip_x = dict()
        left_ring_finger_tip_x = dict()
        left_pinky_mcp_x = dict()
        left_pinky_pip_x = dict()
        left_pinky_dip_x = dict()
        left_pinky_tip_x = dict()
        right_shoulder_x = dict()
        right_elbow_x = dict()
        right_wrist_x = dict()
        right_thumb_cmc_x = dict()
        right_thumb_mcp_x = dict()
        right_thumb_ip_x = dict()
        right_thumb_tip_x = dict()
        right_index_finger_mcp_x = dict()
        right_index_finger_pip_x = dict()
        right_index_finger_dip_x = dict()
        right_index_finger_tip_x = dict()
        right_middle_finger_mcp_x = dict()
        right_middle_finger_pip_x = dict()
        right_middle_finger_dip_x = dict()
        right_middle_finger_tip_x = dict()
        right_ring_finger_mcp_x = dict()
        right_ring_finger_pip_x = dict()
        right_ring_finger_dip_x = dict()
        right_ring_finger_tip_x = dict()
        right_pinky_mcp_x = dict()
        right_pinky_pip_x = dict()
        right_pinky_dip_x = dict()
        right_pinky_tip_x = dict()

        left_shoulder_y = dict()
        left_elbow_y = dict()
        left_wrist_y = dict()
        left_thumb_cmc_y = dict()
        left_thumb_mcp_y = dict()
        left_thumb_ip_y = dict()
        left_thumb_tip_y = dict()
        left_index_finger_mcp_y = dict()
        left_index_finger_pip_y = dict()
        left_index_finger_dip_y = dict()
        left_index_finger_tip_y = dict()
        left_middle_finger_mcp_y = dict()
        left_middle_finger_pip_y = dict()
        left_middle_finger_dip_y = dict()
        left_middle_finger_tip_y = dict()
        left_ring_finger_mcp_y = dict()
        left_ring_finger_pip_y = dict()
        left_ring_finger_dip_y = dict()
        left_ring_finger_tip_y = dict()
        left_pinky_mcp_y = dict()
        left_pinky_pip_y = dict()
        left_pinky_dip_y = dict()
        left_pinky_tip_y = dict()
        right_shoulder_y = dict()
        right_elbow_y = dict()
        right_wrist_y = dict()
        right_thumb_cmc_y = dict()
        right_thumb_mcp_y = dict()
        right_thumb_ip_y = dict()
        right_thumb_tip_y = dict()
        right_index_finger_mcp_y = dict()
        right_index_finger_pip_y = dict()
        right_index_finger_dip_y = dict()
        right_index_finger_tip_y = dict()
        right_middle_finger_mcp_y = dict()
        right_middle_finger_pip_y = dict()
        right_middle_finger_dip_y = dict()
        right_middle_finger_tip_y = dict()
        right_ring_finger_mcp_y = dict()
        right_ring_finger_pip_y = dict()
        right_ring_finger_dip_y = dict()
        right_ring_finger_tip_y = dict()
        right_pinky_mcp_y = dict()
        right_pinky_pip_y = dict()
        right_pinky_dip_y = dict()
        right_pinky_tip_y = dict()

        left_shoulder_z = dict()
        left_elbow_z = dict()
        left_wrist_z = dict()
        left_thumb_cmc_z = dict()
        left_thumb_mcp_z = dict()
        left_thumb_ip_z = dict()
        left_thumb_tip_z = dict()
        left_index_finger_mcp_z = dict()
        left_index_finger_pip_z = dict()
        left_index_finger_dip_z = dict()
        left_index_finger_tip_z = dict()
        left_middle_finger_mcp_z = dict()
        left_middle_finger_pip_z = dict()
        left_middle_finger_dip_z = dict()
        left_middle_finger_tip_z = dict()
        left_ring_finger_mcp_z = dict()
        left_ring_finger_pip_z = dict()
        left_ring_finger_dip_z = dict()
        left_ring_finger_tip_z = dict()
        left_pinky_mcp_z = dict()
        left_pinky_pip_z = dict()
        left_pinky_dip_z = dict()
        left_pinky_tip_z = dict()
        right_shoulder_z = dict()
        right_elbow_z = dict()
        right_wrist_z = dict()
        right_thumb_cmc_z = dict()
        right_thumb_mcp_z = dict()
        right_thumb_ip_z = dict()
        right_thumb_tip_z = dict()
        right_index_finger_mcp_z = dict()
        right_index_finger_pip_z = dict()
        right_index_finger_dip_z = dict()
        right_index_finger_tip_z = dict()
        right_middle_finger_mcp_z = dict()
        right_middle_finger_pip_z = dict()
        right_middle_finger_dip_z = dict()
        right_middle_finger_tip_z = dict()
        right_ring_finger_mcp_z = dict()
        right_ring_finger_pip_z = dict()
        right_ring_finger_dip_z = dict()
        right_ring_finger_tip_z = dict()
        right_pinky_mcp_z = dict()
        right_pinky_pip_z = dict()
        right_pinky_dip_z = dict()
        right_pinky_tip_z = dict()
        '''
        left_shoulder['x'] = left_shoulder_x
        left_elbow['x'] = left_elbow_x
        left_wrist['x'] = left_wrist_x
        left_thumb_cmc['x'] = left_thumb_cmc_x
        left_thumb_mcp['x'] = left_thumb_mcp_x
        left_thumb_ip['x'] = left_thumb_ip_x
        left_thumb_tip['x'] = left_thumb_tip_x
        left_index_finger_mcp['x'] = left_index_finger_mcp_x
        left_index_finger_pip['x'] = left_index_finger_pip_x
        left_index_finger_dip['x'] = left_index_finger_dip_x
        left_index_finger_tip['x'] = left_index_finger_tip_x
        left_middle_finger_mcp['x'] = left_middle_finger_mcp_x
        left_middle_finger_pip['x'] = left_middle_finger_pip_x
        left_middle_finger_dip['x'] = left_middle_finger_dip_x
        left_middle_finger_tip['x'] = left_middle_finger_tip_x
        left_ring_finger_mcp['x'] = left_ring_finger_mcp_x
        left_ring_finger_pip['x'] = left_ring_finger_pip_x
        left_ring_finger_dip['x'] = left_ring_finger_dip_x
        left_ring_finger_tip['x'] = left_ring_finger_tip_x
        left_pinky_mcp['x'] = left_pinky_mcp_x
        left_pinky_pip['x'] = left_pinky_pip_x
        left_pinky_dip['x'] = left_pinky_dip_x
        left_pinky_tip['x'] = left_pinky_tip_x
        right_shoulder['x'] = right_shoulder_x
        right_elbow['x'] = right_elbow_x
        right_wrist['x'] = right_wrist_x
        right_thumb_cmc['x'] = right_thumb_cmc_x
        right_thumb_mcp['x'] = right_thumb_mcp_x
        right_thumb_ip['x'] = right_thumb_ip_x
        right_thumb_tip['x'] = right_thumb_tip_x
        right_index_finger_mcp['x'] = right_index_finger_mcp_x
        right_index_finger_pip['x'] = right_index_finger_pip_x
        right_index_finger_dip['x'] = right_index_finger_dip_x
        right_index_finger_tip['x'] = right_index_finger_tip_x
        right_middle_finger_mcp['x'] = right_middle_finger_mcp_x
        right_middle_finger_pip['x'] = right_middle_finger_pip_x
        right_middle_finger_dip['x'] = right_middle_finger_dip_x
        right_middle_finger_tip['x'] = right_middle_finger_tip_x
        right_ring_finger_mcp['x'] = right_ring_finger_mcp_x
        right_ring_finger_pip['x'] = right_ring_finger_pip_x
        right_ring_finger_dip['x'] = right_ring_finger_dip_x
        right_ring_finger_tip['x'] = right_ring_finger_tip_x
        right_pinky_mcp['x'] = right_pinky_mcp_x
        right_pinky_pip['x'] = right_pinky_pip_x
        right_pinky_dip['x'] = right_pinky_dip_x
        right_pinky_tip['x'] = right_pinky_tip_x

        left_shoulder['y'] = left_shoulder_y
        left_elbow['y'] = left_elbow_y
        left_wrist['y'] = left_wrist_y
        left_thumb_cmc['y'] = left_thumb_cmc_y
        left_thumb_mcp['y'] = left_thumb_mcp_y
        left_thumb_ip['y'] = left_thumb_ip_y
        left_thumb_tip['y'] = left_thumb_tip_y
        left_index_finger_mcp['y'] = left_index_finger_mcp_y
        left_index_finger_pip['y'] = left_index_finger_pip_y
        left_index_finger_dip['y'] = left_index_finger_dip_y
        left_index_finger_tip['y'] = left_index_finger_tip_y
        left_middle_finger_mcp['y'] = left_middle_finger_mcp_y
        left_middle_finger_pip['y'] = left_middle_finger_pip_y
        left_middle_finger_dip['y'] = left_middle_finger_dip_y
        left_middle_finger_tip['y'] = left_middle_finger_tip_y
        left_ring_finger_mcp['y'] = left_ring_finger_mcp_y
        left_ring_finger_pip['y'] = left_ring_finger_pip_y
        left_ring_finger_dip['y'] = left_ring_finger_dip_y
        left_ring_finger_tip['y'] = left_ring_finger_tip_y
        left_pinky_mcp['y'] = left_pinky_mcp_y
        left_pinky_pip['y'] = left_pinky_pip_y
        left_pinky_dip['y'] = left_pinky_dip_y
        left_pinky_tip['y'] = left_pinky_tip_y
        right_shoulder['y'] = right_shoulder_y
        right_elbow['y'] = right_elbow_y
        right_wrist['y'] = right_wrist_y
        right_thumb_cmc['y'] = right_thumb_cmc_y
        right_thumb_mcp['y'] = right_thumb_mcp_y
        right_thumb_ip['y'] = right_thumb_ip_y
        right_thumb_tip['y'] = right_thumb_tip_y
        right_index_finger_mcp['y'] = right_index_finger_mcp_y
        right_index_finger_pip['y'] = right_index_finger_pip_y
        right_index_finger_dip['y'] = right_index_finger_dip_y
        right_index_finger_tip['y'] = right_index_finger_tip_y
        right_middle_finger_mcp['y'] = right_middle_finger_mcp_y
        right_middle_finger_pip['y'] = right_middle_finger_pip_y
        right_middle_finger_dip['y'] = right_middle_finger_dip_y
        right_middle_finger_tip['y'] = right_middle_finger_tip_y
        right_ring_finger_mcp['y'] = right_ring_finger_mcp_y
        right_ring_finger_pip['y'] = right_ring_finger_pip_y
        right_ring_finger_dip['y'] = right_ring_finger_dip_y
        right_ring_finger_tip['y'] = right_ring_finger_tip_y
        right_pinky_mcp['y'] = right_pinky_mcp_y
        right_pinky_pip['y'] = right_pinky_pip_y
        right_pinky_dip['y'] = right_pinky_dip_y
        right_pinky_tip['y'] = right_pinky_tip_y

        left_shoulder['z'] = left_shoulder_z
        left_elbow['z'] = left_elbow_z
        left_wrist['z'] = left_wrist_z
        left_thumb_cmc['z'] = left_thumb_cmc_z
        left_thumb_mcp['z'] = left_thumb_mcp_z
        left_thumb_ip['z'] = left_thumb_ip_z
        left_thumb_tip['z'] = left_thumb_tip_z
        left_index_finger_mcp['z'] = left_index_finger_mcp_z
        left_index_finger_pip['z'] = left_index_finger_pip_z
        left_index_finger_dip['z'] = left_index_finger_dip_z
        left_index_finger_tip['z'] = left_index_finger_tip_z
        left_middle_finger_mcp['z'] = left_middle_finger_mcp_z
        left_middle_finger_pip['z'] = left_middle_finger_pip_z
        left_middle_finger_dip['z'] = left_middle_finger_dip_z
        left_middle_finger_tip['z'] = left_middle_finger_tip_z
        left_ring_finger_mcp['z'] = left_ring_finger_mcp_z
        left_ring_finger_pip['z'] = left_ring_finger_pip_z
        left_ring_finger_dip['z'] = left_ring_finger_dip_z
        left_ring_finger_tip['z'] = left_ring_finger_tip_z
        left_pinky_mcp['z'] = left_pinky_mcp_z
        left_pinky_pip['z'] = left_pinky_pip_z
        left_pinky_dip['z'] = left_pinky_dip_z
        left_pinky_tip['z'] = left_pinky_tip_z
        right_shoulder['z'] = right_shoulder_z
        right_elbow['z'] = right_elbow_z
        right_wrist['z'] = right_wrist_z
        right_thumb_cmc['z'] = right_thumb_cmc_z
        right_thumb_mcp['z'] = right_thumb_mcp_z
        right_thumb_ip['z'] = right_thumb_ip_z
        right_thumb_tip['z'] = right_thumb_tip_z
        right_index_finger_mcp['z'] = right_index_finger_mcp_z
        right_index_finger_pip['z'] = right_index_finger_pip_z
        right_index_finger_dip['z'] = right_index_finger_dip_z
        right_index_finger_tip['z'] = right_index_finger_tip_z
        right_middle_finger_mcp['z'] = right_middle_finger_mcp_z
        right_middle_finger_pip['z'] = right_middle_finger_pip_z
        right_middle_finger_dip['z'] = right_middle_finger_dip_z
        right_middle_finger_tip['z'] = right_middle_finger_tip_z
        right_ring_finger_mcp['z'] = right_ring_finger_mcp_z
        right_ring_finger_pip['z'] = right_ring_finger_pip_z
        right_ring_finger_dip['z'] = right_ring_finger_dip_z
        right_ring_finger_tip['z'] = right_ring_finger_tip_z
        right_pinky_mcp['z'] = right_pinky_mcp_z
        right_pinky_pip['z'] = right_pinky_pip_z
        right_pinky_dip['z'] = right_pinky_dip_z
        right_pinky_tip['z'] = right_pinky_tip_z
        '''
    # 손(손가락) + 포즈 + 얼굴 트래킹
    def getHolisticData(self, file_path):
        # 캡쳐 횟수 조절
        prev_time = 0
        fps = 5
        frame = 0

        # 파일 경로 설정
        file_name = file_path.split('/')[2]
        save_path = '../data/motion/' + file_name.replace('.avi', '')
        print(save_path)

        # OpenCV로 읽고 json 파일 생성
        cap = cv2.VideoCapture(file_path)
        with open(save_path + '.json', 'w') as f:
            pass

        # 비디오의 너비, 높이
        width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 간단한 비디오 정보
        print("\n# Video Information")
        print("Sign Language Name: " + file_name)
        print("Video Path : " + file_path)
        print("Video Width: " + str(width))
        print("Video Height: " + str(height) + '\n')

        # 비디오 재생하는 동안 반복되는 부분
        with mp_holistic.Holistic(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5,
                upper_body_only=True) as holistic:
            while cap.isOpened():
                success, image = cap.read()

                # 시간 관리
                time_rate = time.time() - prev_time

                if not success:
                    print("\nIgnoring empty camera frame")
                    break

                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # 성능을 높이기 위해 API reference에서 요구하는 부분
                image.flags.writeable = False
                results = holistic.process(image)

                # 영상에 어노테이션을 그리는 부분
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_holistic.UPPER_BODY_POSE_CONNECTIONS)

                #
                if time_rate > 1. / fps:
                    prev_time = time.time()
                    frame += 1

                    # json 파일 비어있는지 확인
                    with open(save_path + '.json') as f:
                        isEmpty = f.read().strip()

                    # json 파일이 있는 경우 추가
                    with open(save_path + '.json') as json_file:
                        if isEmpty:
                            file_data = json.load(json_file)

                    # 포즈 데이터
                    if results.pose_landmarks:
                        print()

    def getDataFromImages(self, download_path):
        if True:
            file_data = dict()

            left_shoulder = dict()
            left_elbow = dict()
            left_wrist = dict()
            left_thumb_cmc = dict()
            left_thumb_mcp = dict()
            left_thumb_ip = dict()
            left_thumb_tip = dict()
            left_index_finger_mcp = dict()
            left_index_finger_pip = dict()
            left_index_finger_dip = dict()
            left_index_finger_tip = dict()
            left_middle_finger_mcp = dict()
            left_middle_finger_pip = dict()
            left_middle_finger_dip = dict()
            left_middle_finger_tip = dict()
            left_ring_finger_mcp = dict()
            left_ring_finger_pip = dict()
            left_ring_finger_dip = dict()
            left_ring_finger_tip = dict()
            left_pinky_mcp = dict()
            left_pinky_pip = dict()
            left_pinky_dip = dict()
            left_pinky_tip = dict()
            right_shoulder = dict()
            right_elbow = dict()
            right_wrist = dict()
            right_thumb_cmc = dict()
            right_thumb_mcp = dict()
            right_thumb_ip = dict()
            right_thumb_tip = dict()
            right_index_finger_mcp = dict()
            right_index_finger_pip = dict()
            right_index_finger_dip = dict()
            right_index_finger_tip = dict()
            right_middle_finger_mcp = dict()
            right_middle_finger_pip = dict()
            right_middle_finger_dip = dict()
            right_middle_finger_tip = dict()
            right_ring_finger_mcp = dict()
            right_ring_finger_pip = dict()
            right_ring_finger_dip = dict()
            right_ring_finger_tip = dict()
            right_pinky_mcp = dict()
            right_pinky_pip = dict()
            right_pinky_dip = dict()
            right_pinky_tip = dict()

            left_shoulder_x = dict()
            left_elbow_x = dict()
            left_wrist_x = dict()
            left_thumb_cmc_x = dict()
            left_thumb_mcp_x = dict()
            left_thumb_ip_x = dict()
            left_thumb_tip_x = dict()
            left_index_finger_mcp_x = dict()
            left_index_finger_pip_x = dict()
            left_index_finger_dip_x = dict()
            left_index_finger_tip_x = dict()
            left_middle_finger_mcp_x = dict()
            left_middle_finger_pip_x = dict()
            left_middle_finger_dip_x = dict()
            left_middle_finger_tip_x = dict()
            left_ring_finger_mcp_x = dict()
            left_ring_finger_pip_x= dict()
            left_ring_finger_dip_x = dict()
            left_ring_finger_tip_x = dict()
            left_pinky_mcp_x = dict()
            left_pinky_pip_x = dict()
            left_pinky_dip_x = dict()
            left_pinky_tip_x = dict()
            right_shoulder_x = dict()
            right_elbow_x = dict()
            right_wrist_x = dict()
            right_thumb_cmc_x = dict()
            right_thumb_mcp_x = dict()
            right_thumb_ip_x = dict()
            right_thumb_tip_x = dict()
            right_index_finger_mcp_x = dict()
            right_index_finger_pip_x = dict()
            right_index_finger_dip_x = dict()
            right_index_finger_tip_x = dict()
            right_middle_finger_mcp_x = dict()
            right_middle_finger_pip_x = dict()
            right_middle_finger_dip_x = dict()
            right_middle_finger_tip_x = dict()
            right_ring_finger_mcp_x = dict()
            right_ring_finger_pip_x = dict()
            right_ring_finger_dip_x = dict()
            right_ring_finger_tip_x = dict()
            right_pinky_mcp_x = dict()
            right_pinky_pip_x = dict()
            right_pinky_dip_x = dict()
            right_pinky_tip_x = dict()

            left_shoulder_y = dict()
            left_elbow_y = dict()
            left_wrist_y = dict()
            left_thumb_cmc_y = dict()
            left_thumb_mcp_y = dict()
            left_thumb_ip_y = dict()
            left_thumb_tip_y = dict()
            left_index_finger_mcp_y = dict()
            left_index_finger_pip_y = dict()
            left_index_finger_dip_y = dict()
            left_index_finger_tip_y = dict()
            left_middle_finger_mcp_y = dict()
            left_middle_finger_pip_y = dict()
            left_middle_finger_dip_y = dict()
            left_middle_finger_tip_y = dict()
            left_ring_finger_mcp_y = dict()
            left_ring_finger_pip_y = dict()
            left_ring_finger_dip_y = dict()
            left_ring_finger_tip_y = dict()
            left_pinky_mcp_y = dict()
            left_pinky_pip_y = dict()
            left_pinky_dip_y = dict()
            left_pinky_tip_y = dict()
            right_shoulder_y = dict()
            right_elbow_y = dict()
            right_wrist_y = dict()
            right_thumb_cmc_y = dict()
            right_thumb_mcp_y = dict()
            right_thumb_ip_y = dict()
            right_thumb_tip_y = dict()
            right_index_finger_mcp_y = dict()
            right_index_finger_pip_y = dict()
            right_index_finger_dip_y = dict()
            right_index_finger_tip_y = dict()
            right_middle_finger_mcp_y = dict()
            right_middle_finger_pip_y = dict()
            right_middle_finger_dip_y = dict()
            right_middle_finger_tip_y = dict()
            right_ring_finger_mcp_y = dict()
            right_ring_finger_pip_y = dict()
            right_ring_finger_dip_y = dict()
            right_ring_finger_tip_y = dict()
            right_pinky_mcp_y = dict()
            right_pinky_pip_y = dict()
            right_pinky_dip_y = dict()
            right_pinky_tip_y = dict()

            left_shoulder_z = dict()
            left_elbow_z = dict()
            left_wrist_z =dict()
            left_thumb_cmc_z =dict()
            left_thumb_mcp_z =dict()
            left_thumb_ip_z =dict()
            left_thumb_tip_z =dict()
            left_index_finger_mcp_z =dict()
            left_index_finger_pip_z =dict()
            left_index_finger_dip_z =dict()
            left_index_finger_tip_z =dict()
            left_middle_finger_mcp_z =dict()
            left_middle_finger_pip_z =dict()
            left_middle_finger_dip_z =dict()
            left_middle_finger_tip_z =dict()
            left_ring_finger_mcp_z =dict()
            left_ring_finger_pip_z =dict()
            left_ring_finger_dip_z =dict()
            left_ring_finger_tip_z =dict()
            left_pinky_mcp_z =dict()
            left_pinky_pip_z =dict()
            left_pinky_dip_z =dict()
            left_pinky_tip_z =dict()
            right_shoulder_z =dict()
            right_elbow_z =dict()
            right_wrist_z =dict()
            right_thumb_cmc_z =dict()
            right_thumb_mcp_z =dict()
            right_thumb_ip_z =dict()
            right_thumb_tip_z =dict()
            right_index_finger_mcp_z =dict()
            right_index_finger_pip_z =dict()
            right_index_finger_dip_z =dict()
            right_index_finger_tip_z =dict()
            right_middle_finger_mcp_z =dict()
            right_middle_finger_pip_z =dict()
            right_middle_finger_dip_z =dict()
            right_middle_finger_tip_z =dict()
            right_ring_finger_mcp_z =dict()
            right_ring_finger_pip_z =dict()
            right_ring_finger_dip_z =dict()
            right_ring_finger_tip_z =dict()
            right_pinky_mcp_z =dict()
            right_pinky_pip_z =dict()
            right_pinky_dip_z =dict()
            right_pinky_tip_z =dict()

            left_shoulder['x'] = left_shoulder_x
            left_elbow['x'] = left_elbow_x
            left_wrist['x'] = left_wrist_x
            left_thumb_cmc['x'] = left_thumb_cmc_x
            left_thumb_mcp['x'] = left_thumb_mcp_x
            left_thumb_ip['x'] = left_thumb_ip_x
            left_thumb_tip['x'] = left_thumb_tip_x
            left_index_finger_mcp['x'] = left_index_finger_mcp_x
            left_index_finger_pip['x'] =left_index_finger_pip_x
            left_index_finger_dip['x'] =left_index_finger_dip_x
            left_index_finger_tip['x'] =left_index_finger_tip_x
            left_middle_finger_mcp['x'] =left_middle_finger_mcp_x
            left_middle_finger_pip['x'] =left_middle_finger_pip_x
            left_middle_finger_dip['x'] =left_middle_finger_dip_x
            left_middle_finger_tip['x'] =left_middle_finger_tip_x
            left_ring_finger_mcp['x'] =left_ring_finger_mcp_x
            left_ring_finger_pip['x'] =left_ring_finger_pip_x
            left_ring_finger_dip['x'] =left_ring_finger_dip_x
            left_ring_finger_tip['x'] =left_ring_finger_tip_x
            left_pinky_mcp['x'] =left_pinky_mcp_x
            left_pinky_pip['x'] =left_pinky_pip_x
            left_pinky_dip['x'] =left_pinky_dip_x
            left_pinky_tip['x'] =left_pinky_tip_x
            right_shoulder['x'] =right_shoulder_x
            right_elbow['x'] =right_elbow_x
            right_wrist['x'] =right_wrist_x
            right_thumb_cmc['x'] =right_thumb_cmc_x
            right_thumb_mcp['x'] =right_thumb_mcp_x
            right_thumb_ip['x'] =right_thumb_ip_x
            right_thumb_tip['x'] =right_thumb_tip_x
            right_index_finger_mcp['x'] =right_index_finger_mcp_x
            right_index_finger_pip['x'] =right_index_finger_pip_x
            right_index_finger_dip['x'] =right_index_finger_dip_x
            right_index_finger_tip['x'] =right_index_finger_tip_x
            right_middle_finger_mcp['x'] =right_middle_finger_mcp_x
            right_middle_finger_pip['x'] =right_middle_finger_pip_x
            right_middle_finger_dip['x'] =right_middle_finger_dip_x
            right_middle_finger_tip['x'] =right_middle_finger_tip_x
            right_ring_finger_mcp['x'] =right_ring_finger_mcp_x
            right_ring_finger_pip['x'] =right_ring_finger_pip_x
            right_ring_finger_dip['x'] =right_ring_finger_dip_x
            right_ring_finger_tip['x'] =right_ring_finger_tip_x
            right_pinky_mcp['x'] =right_pinky_mcp_x
            right_pinky_pip['x'] =right_pinky_pip_x
            right_pinky_dip['x'] =right_pinky_dip_x
            right_pinky_tip['x'] =right_pinky_tip_x

            left_shoulder['y'] =left_shoulder_y
            left_elbow['y'] =left_elbow_y
            left_wrist['y'] =left_wrist_y
            left_thumb_cmc['y'] =left_thumb_cmc_y
            left_thumb_mcp['y'] =left_thumb_mcp_y
            left_thumb_ip['y'] =left_thumb_ip_y
            left_thumb_tip['y'] =left_thumb_tip_y
            left_index_finger_mcp['y'] =left_index_finger_mcp_y
            left_index_finger_pip['y'] =left_index_finger_pip_y
            left_index_finger_dip['y'] =left_index_finger_dip_y
            left_index_finger_tip['y'] =left_index_finger_tip_y
            left_middle_finger_mcp['y'] =left_middle_finger_mcp_y
            left_middle_finger_pip['y'] =left_middle_finger_pip_y
            left_middle_finger_dip['y'] =left_middle_finger_dip_y
            left_middle_finger_tip['y'] =left_middle_finger_tip_y
            left_ring_finger_mcp['y'] =left_ring_finger_mcp_y
            left_ring_finger_pip['y'] =left_ring_finger_pip_y
            left_ring_finger_dip['y'] =left_ring_finger_dip_y
            left_ring_finger_tip['y'] =left_ring_finger_tip_y
            left_pinky_mcp['y'] =left_pinky_mcp_y
            left_pinky_pip['y'] =left_pinky_pip_y
            left_pinky_dip['y'] =left_pinky_dip_y
            left_pinky_tip['y'] =left_pinky_tip_y
            right_shoulder['y'] =right_shoulder_y
            right_elbow['y'] =right_elbow_y
            right_wrist['y'] =right_wrist_y
            right_thumb_cmc['y'] =right_thumb_cmc_y
            right_thumb_mcp['y'] =right_thumb_mcp_y
            right_thumb_ip['y'] =right_thumb_ip_y
            right_thumb_tip['y'] =right_thumb_tip_y
            right_index_finger_mcp['y'] =right_index_finger_mcp_y
            right_index_finger_pip['y'] =right_index_finger_pip_y
            right_index_finger_dip['y'] =right_index_finger_dip_y
            right_index_finger_tip['y'] =right_index_finger_tip_y
            right_middle_finger_mcp['y'] =right_middle_finger_mcp_y
            right_middle_finger_pip['y'] =right_middle_finger_pip_y
            right_middle_finger_dip['y'] =right_middle_finger_dip_y
            right_middle_finger_tip['y'] =right_middle_finger_tip_y
            right_ring_finger_mcp['y'] =right_ring_finger_mcp_y
            right_ring_finger_pip['y'] =right_ring_finger_pip_y
            right_ring_finger_dip['y'] =right_ring_finger_dip_y
            right_ring_finger_tip['y'] =right_ring_finger_tip_y
            right_pinky_mcp['y'] =right_pinky_mcp_y
            right_pinky_pip['y'] =right_pinky_pip_y
            right_pinky_dip['y'] =right_pinky_dip_y
            right_pinky_tip['y'] =right_pinky_tip_y

            left_shoulder['z'] = left_shoulder_z
            left_elbow['z'] = left_elbow_z
            left_wrist['z'] = left_wrist_z
            left_thumb_cmc['z'] = left_thumb_cmc_z
            left_thumb_mcp['z'] = left_thumb_mcp_z
            left_thumb_ip['z'] = left_thumb_ip_z
            left_thumb_tip['z'] = left_thumb_tip_z
            left_index_finger_mcp['z'] = left_index_finger_mcp_z
            left_index_finger_pip['z'] = left_index_finger_pip_z
            left_index_finger_dip['z'] = left_index_finger_dip_z
            left_index_finger_tip['z'] = left_index_finger_tip_z
            left_middle_finger_mcp['z'] = left_middle_finger_mcp_z
            left_middle_finger_pip['z'] = left_middle_finger_pip_z
            left_middle_finger_dip['z'] = left_middle_finger_dip_z
            left_middle_finger_tip['z'] = left_middle_finger_tip_z
            left_ring_finger_mcp['z'] = left_ring_finger_mcp_z
            left_ring_finger_pip['z'] = left_ring_finger_pip_z
            left_ring_finger_dip['z'] = left_ring_finger_dip_z
            left_ring_finger_tip['z'] = left_ring_finger_tip_z
            left_pinky_mcp['z'] = left_pinky_mcp_z
            left_pinky_pip['z'] = left_pinky_pip_z
            left_pinky_dip['z'] = left_pinky_dip_z
            left_pinky_tip['z'] = left_pinky_tip_z
            right_shoulder['z'] = right_shoulder_z
            right_elbow['z'] = right_elbow_z
            right_wrist['z'] = right_wrist_z
            right_thumb_cmc['z'] = right_thumb_cmc_z
            right_thumb_mcp['z'] = right_thumb_mcp_z
            right_thumb_ip['z'] = right_thumb_ip_z
            right_thumb_tip['z'] = right_thumb_tip_z
            right_index_finger_mcp['z'] = right_index_finger_mcp_z
            right_index_finger_pip['z'] = right_index_finger_pip_z
            right_index_finger_dip['z'] = right_index_finger_dip_z
            right_index_finger_tip['z'] = right_index_finger_tip_z
            right_middle_finger_mcp['z'] = right_middle_finger_mcp_z
            right_middle_finger_pip['z'] = right_middle_finger_pip_z
            right_middle_finger_dip['z'] = right_middle_finger_dip_z
            right_middle_finger_tip['z'] = right_middle_finger_tip_z
            right_ring_finger_mcp['z'] = right_ring_finger_mcp_z
            right_ring_finger_pip['z'] = right_ring_finger_pip_z
            right_ring_finger_dip['z'] = right_ring_finger_dip_z
            right_ring_finger_tip['z'] = right_ring_finger_tip_z
            right_pinky_mcp['z'] = right_pinky_mcp_z
            right_pinky_pip['z'] = right_pinky_pip_z
            right_pinky_dip['z'] = right_pinky_dip_z
            right_pinky_tip['z'] = right_pinky_tip_z

        # 프레임 순서 정렬을 위해 문자열을 숫자로 변환 후 저장
        directory_path = download_path + "crop_images/"
        ffile_list = os.listdir(directory_path)
        file_list = []
        for ffile in ffile_list:
            file = int(ffile.split('.')[0])
            file_list.append(file)

        file_list.sort()

        # json 파일 생성

        with open(download_path + 'json/keypoint.json', 'w') as f:
            pass

        with mp_holistic.Holistic(
            static_image_mode=True,
            min_detection_confidence=0.5,
            upper_body_only=True) as holistic:
            for idx, file in enumerate(file_list):
                image = cv2.imread(directory_path+str(file)+'.jpg')

                results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

                frame = file

                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_holistic.UPPER_BODY_POSE_CONNECTIONS)

                cv2.imwrite(download_path+'annnotated_images/'+str(file)+'.jpg', image)

                if (results.pose_landmarks or results.left_hand_landmarks or results.right_hand_landmarks):
                    # json 파일 비어있는지 확인
                    with open(download_path + 'json/keypoint.json') as f:
                        isEmpty = f.read().strip()

                    # json 파일이 있는 경우 추가
                    with open(download_path + 'json/keypoint.json') as json_file:
                        if isEmpty:
                            file_data = json.load(json_file)

                    if results.pose_landmarks:
                        # 어깨는 움직이지 않는다고 가정(상대 좌표 구하는 것이 불가능)
                        left_shoulder_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
                        left_elbow_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x
                        left_wrist_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x
                        right_shoulder_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
                        right_elbow_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x
                        right_wrist_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x

                        left_shoulder_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
                        left_elbow_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
                        left_wrist_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
                        right_shoulder_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
                        right_elbow_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
                        right_wrist_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y

                        left_shoulder_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].z
                        left_elbow_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].z
                        left_wrist_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].z
                        right_shoulder_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].z
                        right_elbow_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].z
                        right_wrist_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z

                    else:
                        left_shoulder_x[frame] = -9999
                        left_elbow_x[frame] = -9999
                        left_wrist_x[frame] = -9999
                        right_shoulder_x[frame] = -9999
                        right_elbow_x[frame] = -9999
                        right_wrist_x[frame] = -9999

                        left_shoulder_y[frame] = -9999
                        left_elbow_y[frame] = -9999
                        left_wrist_y[frame] = -9999
                        right_shoulder_y[frame] = -9999
                        right_elbow_y[frame] = -9999
                        right_wrist_y[frame] = -9999

                        left_shoulder_z[frame] = -9999
                        left_elbow_z[frame] = -9999
                        left_wrist_z[frame] = -9999
                        right_shoulder_z[frame] = -9999
                        right_elbow_z[frame] = -9999
                        right_wrist_z[frame] = -9999

                    file_data['left_shoulder'] = left_shoulder
                    file_data['left_elbow'] = left_elbow
                    file_data['right_shoulder'] = right_shoulder
                    file_data['right_elbow'] = right_elbow

                    # 왼손 데이터
                    if results.left_hand_landmarks:
                        #left_wrist_x[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_thumb_cmc_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_CMC].x
                        left_thumb_mcp_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_MCP].x
                        left_thumb_ip_x[frame] = results.left_hand_landmarks.landmark[
                                                     mp_hands.HandLandmark.THUMB_IP].x
                        left_thumb_tip_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_TIP].x
                        left_index_finger_mcp_x[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_MCP].x
                        left_index_finger_pip_x[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                        left_index_finger_dip_x[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_DIP].x
                        left_index_finger_tip_x[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                        left_middle_finger_mcp_x[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                        left_middle_finger_pip_x[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                        left_middle_finger_dip_x[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
                        left_middle_finger_tip_x[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                        left_ring_finger_mcp_x[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_MCP].x
                        left_ring_finger_pip_x[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_PIP].x
                        left_ring_finger_dip_x[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_DIP].x
                        left_ring_finger_tip_x[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_TIP].x
                        left_pinky_mcp_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_MCP].x
                        left_pinky_pip_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_PIP].x
                        left_pinky_dip_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_DIP].x
                        left_pinky_tip_x[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_TIP].x

                        #left_wrist_y[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        left_thumb_cmc_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_CMC].y
                        left_thumb_mcp_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_MCP].y
                        left_thumb_ip_y[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
                        left_thumb_tip_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_TIP].y
                        left_index_finger_mcp_y[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                        left_index_finger_pip_y[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_PIP].y
                        left_index_finger_dip_y[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_DIP].y
                        left_index_finger_tip_y[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        left_middle_finger_mcp_y[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                        left_middle_finger_pip_y[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                        left_middle_finger_dip_y[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                        left_middle_finger_tip_y[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                        left_ring_finger_mcp_y[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_MCP].y
                        left_ring_finger_pip_y[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_PIP].y
                        left_ring_finger_dip_y[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_DIP].y
                        left_ring_finger_tip_y[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_TIP].y
                        left_pinky_mcp_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_MCP].y
                        left_pinky_pip_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_PIP].y
                        left_pinky_dip_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_DIP].y
                        left_pinky_tip_y[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_TIP].y

                        #left_wrist_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_thumb_cmc_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_CMC].z
                        left_thumb_mcp_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_MCP].z
                        left_thumb_ip_z[frame] = results.left_hand_landmarks.landmark[
                                                     mp_hands.HandLandmark.THUMB_IP].z
                        left_thumb_tip_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_TIP].z
                        left_index_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_MCP].z
                        left_index_finger_pip_z[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_PIP].z
                        left_index_finger_dip_z[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_DIP].z
                        left_index_finger_tip_z[frame] = results.left_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.INDEX_FINGER_TIP].z
                        left_middle_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
                        left_middle_finger_pip_z[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
                        left_middle_finger_dip_z[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
                        left_middle_finger_tip_z[frame] = results.left_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z
                        left_ring_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_MCP].z
                        left_ring_finger_pip_z[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_PIP].z
                        left_ring_finger_dip_z[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_DIP].z
                        left_ring_finger_tip_z[frame] = results.left_hand_landmarks.landmark[
                                                            mp_hands.HandLandmark.RING_FINGER_TIP].z
                        left_pinky_mcp_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_MCP].z
                        left_pinky_pip_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_PIP].z
                        left_pinky_dip_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_DIP].z
                        left_pinky_tip_z[frame] = results.left_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.PINKY_TIP].z

                    else:
                        #left_wrist_x[frame] = -9999
                        left_thumb_cmc_x[frame] = -9999
                        left_thumb_mcp_x[frame] = -9999
                        left_thumb_ip_x[frame] = -9999
                        left_thumb_tip_x[frame] = -9999
                        left_index_finger_mcp_x[frame] = -9999
                        left_index_finger_pip_x[frame] = -9999
                        left_index_finger_dip_x[frame] = -9999
                        left_index_finger_tip[frame] = -9999
                        left_middle_finger_mcp_x[frame] = -9999
                        left_middle_finger_pip_x[frame] = -9999
                        left_middle_finger_dip_x[frame] = -9999
                        left_middle_finger_tip_x[frame] = -9999
                        left_ring_finger_mcp_x[frame] = -9999
                        left_ring_finger_pip_x[frame] = -9999
                        left_ring_finger_dip_x[frame] = -9999
                        left_ring_finger_tip_x[frame] = -9999
                        left_pinky_mcp_x[frame] = -9999
                        left_pinky_pip_x[frame] = -9999
                        left_pinky_dip_x[frame] = -9999
                        left_pinky_tip_x[frame] = -9999

                        #left_wrist_y[frame] = -9999
                        left_thumb_cmc_y[frame] = -9999
                        left_thumb_mcp_y[frame] = -9999
                        left_thumb_ip_y[frame] = -9999
                        left_thumb_tip_y[frame] = -9999
                        left_index_finger_mcp_y[frame] = -9999
                        left_index_finger_pip_y[frame] = -9999
                        left_index_finger_dip_y[frame] = -9999
                        left_index_finger_tip_y[frame] = -9999
                        left_middle_finger_mcp_y[frame] = -9999
                        left_middle_finger_pip_y[frame] = -9999
                        left_middle_finger_dip_y[frame] = -9999
                        left_middle_finger_tip_y[frame] = -9999
                        left_ring_finger_mcp_y[frame] = -9999
                        left_ring_finger_pip_y[frame] = -9999
                        left_ring_finger_dip_y[frame] = -9999
                        left_ring_finger_tip_y[frame] = -9999
                        left_pinky_mcp_y[frame] = -9999
                        left_pinky_pip_y[frame] = -9999
                        left_pinky_dip_y[frame] = -9999
                        left_pinky_tip_y[frame] = -9999

                        #left_wrist_z[frame] = -9999
                        left_thumb_cmc_z[frame] = -9999
                        left_thumb_mcp_z[frame] = -9999
                        left_thumb_ip_z[frame] = -9999
                        left_thumb_tip_z[frame] = -9999
                        left_index_finger_mcp_z[frame] = -9999
                        left_index_finger_pip_z[frame] = -9999
                        left_index_finger_dip_z[frame] = -9999
                        left_index_finger_tip_z[frame] = -9999
                        left_middle_finger_mcp_z[frame] = -9999
                        left_middle_finger_pip_z[frame] = -9999
                        left_middle_finger_dip_z[frame] = -9999
                        left_middle_finger_tip_z[frame] = -9999
                        left_ring_finger_mcp_z[frame] = -9999
                        left_ring_finger_pip_z[frame] = -9999
                        left_ring_finger_dip_z[frame] = -9999
                        left_ring_finger_tip_z[frame] = -9999
                        left_pinky_mcp_z[frame] = -9999
                        left_pinky_pip_z[frame] = -9999
                        left_pinky_dip_z[frame] = -9999
                        left_pinky_tip_z[frame] = -9999

                    file_data['left_wrist'] = left_wrist
                    file_data['left_thumb_cmc'] = left_thumb_cmc
                    file_data['left_thumb_mcp'] = left_thumb_mcp
                    file_data['left_thumb_ip'] = left_thumb_ip
                    file_data['left_thumb_tip'] = left_thumb_tip
                    file_data['left_index_finger_mcp'] = left_index_finger_mcp
                    file_data['left_index_finger_pip'] = left_index_finger_pip
                    file_data['left_index_finger_dip'] = left_index_finger_dip
                    file_data['left_index_finger_tip'] = left_index_finger_tip
                    file_data['left_middle_finger_mcp'] = left_middle_finger_mcp
                    file_data['left_middle_finger_pip'] = left_middle_finger_pip
                    file_data['left_middle_finger_dip'] = left_middle_finger_dip
                    file_data['left_middle_finger_tip'] = left_middle_finger_tip
                    file_data['left_ring_finger_mcp'] = left_ring_finger_mcp
                    file_data['left_ring_finger_pip'] = left_ring_finger_pip
                    file_data['left_ring_finger_dip'] = left_ring_finger_dip
                    file_data['left_ring_finger_tip'] = left_ring_finger_tip
                    file_data['left_pinky_mcp'] = left_pinky_mcp
                    file_data['left_pinky_pip'] = left_pinky_pip
                    file_data['left_pinky_dip'] = left_pinky_dip
                    file_data['left_pinky_tip'] = left_pinky_tip

                    # 오른손 데이터
                    if results.right_hand_landmarks:
                        #right_wrist_x[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_thumb_cmc_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_CMC].x
                        right_thumb_mcp_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_MCP].x
                        right_thumb_ip_x[frame] = results.right_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_IP].x
                        right_thumb_tip_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_TIP].x
                        right_index_finger_mcp_x[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_MCP].x
                        right_index_finger_pip_x[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                        right_index_finger_dip_x[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_DIP].x
                        right_index_finger_tip_x[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                        right_middle_finger_mcp_x[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                        right_middle_finger_pip_x[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                        right_middle_finger_dip_x[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
                        right_middle_finger_tip_x[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                        right_ring_finger_mcp_x[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_MCP].x
                        right_ring_finger_pip_x[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_PIP].x
                        right_ring_finger_dip_x[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_DIP].x
                        right_ring_finger_tip_x[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_TIP].x
                        right_pinky_mcp_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_MCP].x
                        right_pinky_pip_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_PIP].x
                        right_pinky_dip_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_DIP].x
                        right_pinky_tip_x[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_TIP].x

                        #right_wrist_y[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        right_thumb_cmc_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_CMC].y
                        right_thumb_mcp_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_MCP].y
                        right_thumb_ip_y[frame] = results.right_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_IP].y
                        right_thumb_tip_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_TIP].y
                        right_index_finger_mcp_y[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                        right_index_finger_pip_y[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_PIP].y
                        right_index_finger_dip_y[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_DIP].y
                        right_index_finger_tip_y[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        right_middle_finger_mcp_y[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                        right_middle_finger_pip_y[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                        right_middle_finger_dip_y[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                        right_middle_finger_tip_y[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                        right_ring_finger_mcp_y[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_MCP].y
                        right_ring_finger_pip_y[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_PIP].y
                        right_ring_finger_dip_y[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_DIP].y
                        right_ring_finger_tip_y[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_TIP].y
                        right_pinky_mcp_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_MCP].y
                        right_pinky_pip_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_PIP].y
                        right_pinky_dip_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_DIP].y
                        right_pinky_tip_y[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_TIP].y

                        #right_wrist_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_thumb_cmc_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_CMC].z
                        right_thumb_mcp_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_MCP].z
                        right_thumb_ip_z[frame] = results.right_hand_landmarks.landmark[
                                                      mp_hands.HandLandmark.THUMB_IP].z
                        right_thumb_tip_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.THUMB_TIP].z
                        right_index_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_MCP].z
                        right_index_finger_pip_z[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_PIP].z
                        right_index_finger_dip_z[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_DIP].z
                        right_index_finger_tip_z[frame] = results.right_hand_landmarks.landmark[
                                                              mp_hands.HandLandmark.INDEX_FINGER_TIP].z
                        right_middle_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
                        right_middle_finger_pip_z[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
                        right_middle_finger_dip_z[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
                        right_middle_finger_tip_z[frame] = results.right_hand_landmarks.landmark[
                                                               mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z
                        right_ring_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_MCP].z
                        right_ring_finger_pip_z[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_PIP].z
                        right_ring_finger_dip_z[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_DIP].z
                        right_ring_finger_tip_z[frame] = results.right_hand_landmarks.landmark[
                                                             mp_hands.HandLandmark.RING_FINGER_TIP].z
                        right_pinky_mcp_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_MCP].z
                        right_pinky_pip_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_PIP].z
                        right_pinky_dip_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_DIP].z
                        right_pinky_tip_z[frame] = results.right_hand_landmarks.landmark[
                                                       mp_hands.HandLandmark.PINKY_TIP].z

                    else:
                        #right_wrist_x[frame] = -9999
                        right_thumb_cmc_x[frame] = -9999
                        right_thumb_mcp_x[frame] = -9999
                        right_thumb_ip_x[frame] = -9999
                        right_thumb_tip_x[frame] = -9999
                        right_index_finger_mcp_x[frame] = -9999
                        right_index_finger_pip_x[frame] = -9999
                        right_index_finger_dip_x[frame] = -9999
                        right_index_finger_tip[frame] = -9999
                        right_middle_finger_mcp_x[frame] = -9999
                        right_middle_finger_pip_x[frame] = -9999
                        right_middle_finger_dip_x[frame] = -9999
                        right_middle_finger_tip_x[frame] = -9999
                        right_ring_finger_mcp_x[frame] = -9999
                        right_ring_finger_pip_x[frame] = -9999
                        right_ring_finger_dip_x[frame] = -9999
                        right_ring_finger_tip_x[frame] = -9999
                        right_pinky_mcp_x[frame] = -9999
                        right_pinky_pip_x[frame] = -9999
                        right_pinky_dip_x[frame] = -9999
                        right_pinky_tip_x[frame] = -9999

                        #right_wrist_y[frame] = -9999
                        right_thumb_cmc_y[frame] = -9999
                        right_thumb_mcp_y[frame] = -9999
                        right_thumb_ip_y[frame] = -9999
                        right_thumb_tip_y[frame] = -9999
                        right_index_finger_mcp_y[frame] = -9999
                        right_index_finger_pip_y[frame] = -9999
                        right_index_finger_dip_y[frame] = -9999
                        right_index_finger_tip_y[frame] = -9999
                        right_middle_finger_mcp_y[frame] = -9999
                        right_middle_finger_pip_y[frame] = -9999
                        right_middle_finger_dip_y[frame] = -9999
                        right_middle_finger_tip_y[frame] = -9999
                        right_ring_finger_mcp_y[frame] = -9999
                        right_ring_finger_pip_y[frame] = -9999
                        right_ring_finger_dip_y[frame] = -9999
                        right_ring_finger_tip_y[frame] = -9999
                        right_pinky_mcp_y[frame] = -9999
                        right_pinky_pip_y[frame] = -9999
                        right_pinky_dip_y[frame] = -9999
                        right_pinky_tip_y[frame] = -9999

                        #right_wrist_z[frame] = -9999
                        right_thumb_cmc_z[frame] = -9999
                        right_thumb_mcp_z[frame] = -9999
                        right_thumb_ip_z[frame] = -9999
                        right_thumb_tip_z[frame] = -9999
                        right_index_finger_mcp_z[frame] = -9999
                        right_index_finger_pip_z[frame] = -9999
                        right_index_finger_dip_z[frame] = -9999
                        right_index_finger_tip_z[frame] = -9999
                        right_middle_finger_mcp_z[frame] = -9999
                        right_middle_finger_pip_z[frame] = -9999
                        right_middle_finger_dip_z[frame] = -9999
                        right_middle_finger_tip_z[frame] = -9999
                        right_ring_finger_mcp_z[frame] = -9999
                        right_ring_finger_pip_z[frame] = -9999
                        right_ring_finger_dip_z[frame] = -9999
                        right_ring_finger_tip_z[frame] = -9999
                        right_pinky_mcp_z[frame] = -9999
                        right_pinky_pip_z[frame] = -9999
                        right_pinky_dip_z[frame] = -9999
                        right_pinky_tip_z[frame] = -9999

                    file_data['right_wrist'] = right_wrist
                    file_data['right_thumb_cmc'] = right_thumb_cmc
                    file_data['right_thumb_mcp'] = right_thumb_mcp
                    file_data['right_thumb_ip'] = right_thumb_ip
                    file_data['right_thumb_tip'] = right_thumb_tip
                    file_data['right_index_finger_mcp'] = right_index_finger_mcp
                    file_data['right_index_finger_pip'] = right_index_finger_pip
                    file_data['right_index_finger_dip'] = right_index_finger_dip
                    file_data['right_index_finger_tip'] = right_index_finger_tip
                    file_data['right_middle_finger_mcp'] = right_middle_finger_mcp
                    file_data['right_middle_finger_pip'] = right_middle_finger_pip
                    file_data['right_middle_finger_dip'] = right_middle_finger_dip
                    file_data['right_middle_finger_tip'] = right_middle_finger_tip
                    file_data['right_ring_finger_mcp'] = right_ring_finger_mcp
                    file_data['right_ring_finger_pip'] = right_ring_finger_pip
                    file_data['right_ring_finger_dip'] = right_ring_finger_dip
                    file_data['right_ring_finger_tip'] = right_ring_finger_tip
                    file_data['right_pinky_mcp'] = right_pinky_mcp
                    file_data['right_pinky_pip'] = right_pinky_pip
                    file_data['right_pinky_dip'] = right_pinky_dip
                    file_data['right_pinky_tip'] = right_pinky_tip

                    file_data["frames"] = frame

                    # json 파일에 쓰기
                    with open(download_path + 'json/keypoint.json', 'w') as outfile:
                        json.dump(file_data, outfile, indent='\t')

        print("getting keypoints completed...")