import cv2, time, json
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

class MotionData:
    # 손(손가락) + 포즈 + 얼굴 트래킹
    def getHolisticData(self, file_path):
        # 캡쳐 횟수 조절
        prev_time = 0
        fps = 5
        count = 0

        # 파일 경로 설정
        file_name = file_path.split('/')[2]
        save_path = './motion_data_file/' + file_name.replace('.avi', '')
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
                ''' 얼굴을 그리는 부분
                mp_drawing.draw_landmarks(
                    image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
                '''
                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_holistic.UPPER_BODY_POSE_CONNECTIONS)

                # 랜드마크의 x,y 값 출력
                current_time = time.time() - prev_time
                file_data = {}

                # 일정 시간(fps)마다 랜드마크 데이터가 하나라도 있을 때, 그 데이터를 가져와 저장
                if (results.pose_landmarks or results.left_hand_landmarks or results.right_hand_landmarks) and (current_time > 1./fps):
                    prev_time = time.time()
                    count += 1

                    # json 파일 비어있는지 확인
                    with open(save_path + '.json') as f:
                        isEmpty = f.read().strip()

                    # json 파일이 있는 경우 추가
                    with open(save_path + '.json') as json_file:
                        if isEmpty:
                            file_data = json.load(json_file)

                    file_data[str(count)] = []

                    # 포즈 데이터
                    pose_data = {}
                    pose_data['pose'] = []
                    if results.pose_landmarks:
                        pose_data['pose'].append({
                            'left_shoulder[0]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                            'left_shoulder[1]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y,
                            'left_elbow[0]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                            'left_elbow[1]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y,
                            'right_shoulder[0]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                            'right_shoulder[1]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y,
                            'right_elbow[0]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
                            'right_elbow[1]':results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
                        })
                        file_data[str(count)].append(pose_data)
                    else:
                        pose_data['pose'].append({
                            'left_shoulder[0]':0, 'left_shoulder[1]':0, 'left_elbow[0]':0, 'left_elbow[1]':0,
                            'right_shoulder[0]':0, 'right_shoulder[1]':0, 'right_elbow[0]':0, 'right_elbow[1]':0
                        })
                        file_data[str(count)].append(pose_data)

                    # 오른손 데이터
                    right_hand_data = {}
                    right_hand_data['right_hand'] = []
                    if results.right_hand_landmarks:
                        right_hand_data['right_hand'].append({
                            'wrist[0]': results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,
                            'wrist[1]': results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,
                        })
                        file_data[str(count)].append(right_hand_data)
                    else:
                        right_hand_data['right_hand'].append({
                            'wrist[0]':0, 'wrist[1]':0
                        })
                        file_data[str(count)].append(right_hand_data)

                    # 왼손 데이터
                    left_hand_data = {}
                    left_hand_data['left_hand'] = []
                    if results.left_hand_landmarks:
                        left_hand_data['left_hand'].append({
                            'wrist[0]': results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,
                            'wrist[1]': results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,
                        })
                        file_data[str(count)].append(left_hand_data)
                    else:
                        left_hand_data['left_hand'].append({
                            'wrist[0]': 0, 'wrist[1]': 0
                        })
                        file_data[str(count)].append(left_hand_data)

                    # json 파일에 쓰기
                    with open(save_path + '.json', "w") as outfile:
                        json.dump(file_data, outfile, indent='\t')

                # 결과물 표시
                cv2.imshow('Holistic', image)

                # 종료 키 받는 부분
                if cv2.waitKey(5) & 0xFF == 27:
                    break

            cap.release()

    # 절대 좌표
    def getHolisticData2(self, file_path):
        # 키포인트 딕셔너리
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

        # 캡쳐 횟수 조절
        prev_time = 0
        fps = 5
        frame = 0

        # 파일 경로 설정
        file_name = file_path.split('/')[2]
        save_path = '../motion_data_file/' + file_name.replace('.avi', '')

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
                ''' 얼굴을 그리는 부분
                mp_drawing.draw_landmarks(
                    image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
                '''
                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_holistic.UPPER_BODY_POSE_CONNECTIONS)

                # 랜드마크의 x,y 값 출력
                current_time = time.time() - prev_time
                #file_data = dict()  # 최종 저장할 json 딕셔너리

                # 일정 시간(fps)마다 랜드마크 데이터가 하나라도 있을 때, 그 데이터를 가져와 저장
                if (results.pose_landmarks or results.left_hand_landmarks or results.right_hand_landmarks) and (
                        current_time > 1. / fps):
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
                        left_shoulder_x[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
                        left_elbow_x[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x
                        right_shoulder_x[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
                        right_elbow_x[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x

                        left_shoulder_y[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
                        left_elbow_y[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
                        right_shoulder_y[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
                        right_elbow_y[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y

                        left_shoulder_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].z
                        left_elbow_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].z
                        right_shoulder_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].z
                        right_elbow_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].z

                        file_data['Character1_LeftArm'] = left_shoulder
                        file_data['Character1_LeftForeArm'] = left_elbow
                        file_data['Character1_RightArm'] = right_shoulder
                        file_data['Character1_RightForeArm'] = right_elbow

                    # 왼손 데이터
                    if results.left_hand_landmarks:
                        left_wrist_x[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_thumb_cmc_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x
                        left_thumb_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
                        left_thumb_ip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
                        left_thumb_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                        left_index_finger_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
                        left_index_finger_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                        left_index_finger_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
                        left_index_finger_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                        left_middle_finger_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                        left_middle_finger_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                        left_middle_finger_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
                        left_middle_finger_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                        left_ring_finger_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
                        left_ring_finger_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
                        left_ring_finger_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
                        left_ring_finger_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
                        left_pinky_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
                        left_pinky_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
                        left_pinky_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x
                        left_pinky_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x

                        left_wrist_y[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        left_thumb_cmc_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
                        left_thumb_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
                        left_thumb_ip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
                        left_thumb_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                        left_index_finger_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                        left_index_finger_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
                        left_index_finger_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
                        left_index_finger_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        left_middle_finger_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                        left_middle_finger_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                        left_middle_finger_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                        left_middle_finger_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                        left_ring_finger_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
                        left_ring_finger_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
                        left_ring_finger_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
                        left_ring_finger_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                        left_pinky_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
                        left_pinky_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
                        left_pinky_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
                        left_pinky_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                        left_wrist_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_thumb_cmc_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z
                        left_thumb_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z
                        left_thumb_ip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z
                        left_thumb_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z
                        left_index_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z
                        left_index_finger_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z
                        left_index_finger_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z
                        left_index_finger_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
                        left_middle_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
                        left_middle_finger_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
                        left_middle_finger_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
                        left_middle_finger_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z
                        left_ring_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z
                        left_ring_finger_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z
                        left_ring_finger_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z
                        left_ring_finger_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z
                        left_pinky_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z
                        left_pinky_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z
                        left_pinky_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z
                        left_pinky_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z

                        file_data['Character1_LeftHand'] =left_wrist
                        file_data['Character1_LeftHandThumb1'] =left_thumb_cmc
                        file_data['Character1_LeftHandThumb2'] =left_thumb_mcp
                        file_data['Character1_LeftHandThumb3'] =left_thumb_ip
                        file_data['Character1_LeftHandThumb4'] =left_thumb_tip
                        file_data['Character1_LeftHandIndex1'] =left_index_finger_mcp
                        file_data['Character1_LeftHandIndex2'] =left_index_finger_pip
                        file_data['Character1_LeftHandIndex3'] =left_index_finger_dip
                        file_data['Character1_LeftHandIndex4'] =left_index_finger_tip
                        file_data['Character1_LeftHandMiddle1'] =left_middle_finger_mcp
                        file_data['Character1_LeftHandMiddle2'] =left_middle_finger_pip
                        file_data['Character1_LeftHandMiddle3'] =left_middle_finger_dip
                        file_data['Character1_LeftHandMiddle4'] =left_middle_finger_tip
                        file_data['Character1_LeftHandRing1'] =left_ring_finger_mcp
                        file_data['Character1_LeftHandRing2'] =left_ring_finger_pip
                        file_data['Character1_LeftHandRing3'] =left_ring_finger_dip
                        file_data['Character1_LeftHandRing4'] =left_ring_finger_tip
                        file_data['Character1_LeftHandPinky1'] =left_pinky_mcp
                        file_data['Character1_LeftHandPinky2'] =left_pinky_pip
                        file_data['Character1_LeftHandPinky3'] =left_pinky_dip
                        file_data['Character1_LeftHandPinky4'] =left_pinky_tip

                    # 오른손 데이터
                    if results.right_hand_landmarks:
                        right_wrist_x[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_thumb_cmc_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x
                        right_thumb_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
                        right_thumb_ip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
                        right_thumb_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                        right_index_finger_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
                        right_index_finger_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                        right_index_finger_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
                        right_index_finger_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                        right_middle_finger_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                        right_middle_finger_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                        right_middle_finger_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
                        right_middle_finger_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                        right_ring_finger_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
                        right_ring_finger_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
                        right_ring_finger_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
                        right_ring_finger_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
                        right_pinky_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
                        right_pinky_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
                        right_pinky_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x
                        right_pinky_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x

                        right_wrist_y[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        right_thumb_cmc_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
                        right_thumb_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
                        right_thumb_ip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
                        right_thumb_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                        right_index_finger_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                        right_index_finger_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
                        right_index_finger_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
                        right_index_finger_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        right_middle_finger_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                        right_middle_finger_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                        right_middle_finger_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                        right_middle_finger_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                        right_ring_finger_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
                        right_ring_finger_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
                        right_ring_finger_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
                        right_ring_finger_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                        right_pinky_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
                        right_pinky_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
                        right_pinky_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
                        right_pinky_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                        right_wrist_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_thumb_cmc_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z
                        right_thumb_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z
                        right_thumb_ip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z
                        right_thumb_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z
                        right_index_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z
                        right_index_finger_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z
                        right_index_finger_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z
                        right_index_finger_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
                        right_middle_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
                        right_middle_finger_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
                        right_middle_finger_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
                        right_middle_finger_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z
                        right_ring_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z
                        right_ring_finger_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z
                        right_ring_finger_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z
                        right_ring_finger_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z
                        right_pinky_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z
                        right_pinky_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z
                        right_pinky_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z
                        right_pinky_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z

                        file_data['Character1_RightHand'] =right_wrist
                        file_data['Character1_RightHandThumb1'] =right_thumb_cmc
                        file_data['Character1_RightHandThumb2'] =right_thumb_mcp
                        file_data['Character1_RightHandThumb3'] =right_thumb_ip
                        file_data['Character1_RightHandThumb4'] =right_thumb_tip
                        file_data['Character1_RightHandIndex1'] =right_index_finger_mcp
                        file_data['Character1_RightHandIndex2'] =right_index_finger_pip
                        file_data['Character1_RightHandIndex3'] =right_index_finger_dip
                        file_data['Character1_RightHandIndex4'] =right_index_finger_tip
                        file_data['Character1_RightHandMiddle1'] =right_middle_finger_mcp
                        file_data['Character1_RightHandMiddle2'] =right_middle_finger_pip
                        file_data['Character1_RightHandMiddle3'] =right_middle_finger_dip
                        file_data['Character1_RightHandMiddle4'] =right_middle_finger_tip
                        file_data['Character1_RightHandRing1'] =right_ring_finger_mcp
                        file_data['Character1_RightHandRing2'] =right_ring_finger_pip
                        file_data['Character1_RightHandRing3'] =right_ring_finger_dip
                        file_data['Character1_RightHandRing4'] =right_ring_finger_tip
                        file_data['Character1_RightHandPinky1'] =right_pinky_mcp
                        file_data['Character1_RightHandPinky2'] =right_pinky_pip
                        file_data['Character1_RightHandPinky3'] =right_pinky_dip
                        file_data['Character1_RightHandPinky4'] =right_pinky_tip

                    file_data["frames"] = frame

                    # json 파일에 쓰기
                    with open(save_path + '.json', "w") as outfile:
                        json.dump(file_data, outfile, indent='\t')

                # 결과물 표시
                cv2.imshow('Holistic', image)

                # 종료 키 받는 부분
                if cv2.waitKey(5) & 0xFF == 27:
                    break

            cap.release()

    # 상대 좌표
    def getHolisticData3(self, file_path):
        # 키포인트 딕셔너리(상위46 + 하위46*3(xyz))
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

        # 캡쳐 횟수 조절
        prev_time = 0
        fps = 5
        frame = 0

        # 파일 경로 설정
        file_name = file_path.split('/')[2]
        save_path = '../motion_data_file/' + file_name.replace('.avi', '')

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
                ''' 얼굴을 그리는 부분
                mp_drawing.draw_landmarks(
                    image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
                '''
                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_holistic.UPPER_BODY_POSE_CONNECTIONS)

                # 랜드마크의 x,y 값 출력
                current_time = time.time() - prev_time

                # 일정 시간(fps)마다 랜드마크 데이터가 하나라도 있을 때, 그 데이터를 가져와 저장
                if (results.pose_landmarks or results.left_hand_landmarks or results.right_hand_landmarks) and (
                        current_time > 1. / fps):
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
                        # 어깨는 움직이지 않는다고 가정(상대 좌표 구하는 것이 불가능)
                        left_shoulder_x[frame] =10.707
                        left_elbow_x[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x - \
                                             results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
                        left_wrist_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x
                        right_shoulder_x[frame] =-10.707
                        right_elbow_x[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x - \
                                              results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
                        right_wrist_x[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x

                        left_shoulder_y[frame] =-0
                        left_elbow_y[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y - \
                                             results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
                        left_wrist_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
                        right_shoulder_y[frame] =0
                        right_elbow_y[frame] =results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y - \
                                              results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
                        right_wrist_y[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y

                        left_shoulder_z[frame] = 0
                        left_elbow_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].z - \
                                              results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].z
                        left_wrist_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].z
                        right_shoulder_z[frame] =0
                        right_elbow_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].z - \
                                               results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].z
                        right_wrist_z[frame] = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].z

                        file_data['Character1_LeftArm'] = left_shoulder
                        file_data['Character1_LeftForeArm'] = left_elbow
                        file_data['Character1_RightArm'] = right_shoulder
                        file_data['Character1_RightForeArm'] = right_elbow

                    # 왼손 데이터
                    if results.left_hand_landmarks:
                        left_wrist_x[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x - left_wrist_x[frame]
                        left_thumb_cmc_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_thumb_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]
                        left_thumb_ip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
                        left_thumb_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
                        left_index_finger_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_index_finger_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
                        left_index_finger_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                        left_index_finger_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
                        left_middle_finger_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_middle_finger_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                        left_middle_finger_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                        left_middle_finger_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
                        left_ring_finger_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_ring_finger_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
                        left_ring_finger_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
                        left_ring_finger_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
                        left_pinky_mcp_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        left_pinky_pip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
                        left_pinky_dip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
                        left_pinky_tip_x[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x

                        left_wrist_y[frame] -= results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        left_thumb_cmc_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
                        left_thumb_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
                        left_thumb_ip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y - \
                                                results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
                        left_thumb_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                        left_index_finger_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                        left_index_finger_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
                        left_index_finger_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
                        left_index_finger_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        left_middle_finger_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                        left_middle_finger_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                        left_middle_finger_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                        left_middle_finger_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                        left_ring_finger_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
                        left_ring_finger_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
                        left_ring_finger_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
                        left_ring_finger_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y - \
                                                       results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                        left_pinky_mcp_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
                        left_pinky_pip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
                        left_pinky_dip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
                        left_pinky_tip_y[frame] =results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                        left_wrist_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z - left_wrist_z[frame]
                        left_thumb_cmc_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_thumb_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z
                        left_thumb_ip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z - \
                                                 results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z
                        left_thumb_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z
                        left_index_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_index_finger_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z
                        left_index_finger_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z
                        left_index_finger_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z - \
                                                         results.left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z
                        left_middle_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z - \
                                                          results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_middle_finger_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z - \
                                                          results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
                        left_middle_finger_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z - \
                                                          results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
                        left_middle_finger_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z - \
                                                          results.left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
                        left_ring_finger_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_ring_finger_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z
                        left_ring_finger_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z
                        left_ring_finger_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z - \
                                                        results.left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z
                        left_pinky_mcp_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        left_pinky_pip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z
                        left_pinky_dip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z
                        left_pinky_tip_z[frame] = results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z - \
                                                  results.left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z

                        file_data['Character1_LeftHand'] =left_wrist
                        file_data['Character1_LeftHandThumb1'] =left_thumb_cmc
                        file_data['Character1_LeftHandThumb2'] =left_thumb_mcp
                        file_data['Character1_LeftHandThumb3'] =left_thumb_ip
                        file_data['Character1_LeftHandThumb4'] =left_thumb_tip
                        file_data['Character1_LeftHandIndex1'] =left_index_finger_mcp
                        file_data['Character1_LeftHandIndex2'] =left_index_finger_pip
                        file_data['Character1_LeftHandIndex3'] =left_index_finger_dip
                        file_data['Character1_LeftHandIndex4'] =left_index_finger_tip
                        file_data['Character1_LeftHandMiddle1'] =left_middle_finger_mcp
                        file_data['Character1_LeftHandMiddle2'] =left_middle_finger_pip
                        file_data['Character1_LeftHandMiddle3'] =left_middle_finger_dip
                        file_data['Character1_LeftHandMiddle4'] =left_middle_finger_tip
                        file_data['Character1_LeftHandRing1'] =left_ring_finger_mcp
                        file_data['Character1_LeftHandRing2'] =left_ring_finger_pip
                        file_data['Character1_LeftHandRing3'] =left_ring_finger_dip
                        file_data['Character1_LeftHandRing4'] =left_ring_finger_tip
                        file_data['Character1_LeftHandPinky1'] =left_pinky_mcp
                        file_data['Character1_LeftHandPinky2'] =left_pinky_pip
                        file_data['Character1_LeftHandPinky3'] =left_pinky_dip
                        file_data['Character1_LeftHandPinky4'] =left_pinky_tip

                    # 오른손 데이터
                    if results.right_hand_landmarks:
                        right_wrist_x[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x - right_wrist_x[frame]
                        right_thumb_cmc_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_thumb_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x
                        right_thumb_ip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x - \
                                                 results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
                        right_thumb_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
                        right_index_finger_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_index_finger_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
                        right_index_finger_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
                        right_index_finger_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
                        right_middle_finger_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_middle_finger_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                        right_middle_finger_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
                        right_middle_finger_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
                        right_ring_finger_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_ring_finger_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
                        right_ring_finger_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
                        right_ring_finger_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
                        right_pinky_mcp_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                        right_pinky_pip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
                        right_pinky_dip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
                        right_pinky_tip_x[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x

                        right_wrist_y[frame] -=results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                        right_thumb_cmc_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
                        right_thumb_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
                        right_thumb_ip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y - \
                                                 results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
                        right_thumb_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                        right_index_finger_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                        right_index_finger_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
                        right_index_finger_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
                        right_index_finger_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                        right_middle_finger_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                        right_middle_finger_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
                        right_middle_finger_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                        right_middle_finger_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                        right_ring_finger_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
                        right_ring_finger_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
                        right_ring_finger_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
                        right_ring_finger_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y - \
                                                        results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                        right_pinky_mcp_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
                        right_pinky_pip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
                        right_pinky_dip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
                        right_pinky_tip_y[frame] =results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                        right_wrist_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z - right_wrist_z[frame]
                        right_thumb_cmc_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_thumb_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z
                        right_thumb_ip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z - \
                                                  results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z
                        right_thumb_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z
                        right_index_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_index_finger_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z
                        right_index_finger_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z
                        right_index_finger_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z - \
                                                          results.right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z
                        right_middle_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z - \
                                                           results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_middle_finger_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z - \
                                                           results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
                        right_middle_finger_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z - \
                                                           results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
                        right_middle_finger_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z - \
                                                           results.right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
                        right_ring_finger_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_ring_finger_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].z
                        right_ring_finger_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z
                        right_ring_finger_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z - \
                                                         results.right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z
                        right_pinky_mcp_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
                        right_pinky_pip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z
                        right_pinky_dip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z
                        right_pinky_tip_z[frame] = results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z - \
                                                   results.right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z

                        file_data['Character1_RightHand'] =right_wrist
                        file_data['Character1_RightHandThumb1'] =right_thumb_cmc
                        file_data['Character1_RightHandThumb2'] =right_thumb_mcp
                        file_data['Character1_RightHandThumb3'] =right_thumb_ip
                        file_data['Character1_RightHandThumb4'] =right_thumb_tip
                        file_data['Character1_RightHandIndex1'] =right_index_finger_mcp
                        file_data['Character1_RightHandIndex2'] =right_index_finger_pip
                        file_data['Character1_RightHandIndex3'] =right_index_finger_dip
                        file_data['Character1_RightHandIndex4'] =right_index_finger_tip
                        file_data['Character1_RightHandMiddle1'] =right_middle_finger_mcp
                        file_data['Character1_RightHandMiddle2'] =right_middle_finger_pip
                        file_data['Character1_RightHandMiddle3'] =right_middle_finger_dip
                        file_data['Character1_RightHandMiddle4'] =right_middle_finger_tip
                        file_data['Character1_RightHandRing1'] =right_ring_finger_mcp
                        file_data['Character1_RightHandRing2'] =right_ring_finger_pip
                        file_data['Character1_RightHandRing3'] =right_ring_finger_dip
                        file_data['Character1_RightHandRing4'] =right_ring_finger_tip
                        file_data['Character1_RightHandPinky1'] =right_pinky_mcp
                        file_data['Character1_RightHandPinky2'] =right_pinky_pip
                        file_data['Character1_RightHandPinky3'] =right_pinky_dip
                        file_data['Character1_RightHandPinky4'] =right_pinky_tip

                    file_data["frames"] = frame

                    # json 파일에 쓰기
                    with open(save_path + '.json', "w") as outfile:
                        json.dump(file_data, outfile, indent='\t')

                # 결과물 표시
                cv2.imshow('Holistic', image)

                # 종료 키 받는 부분
                if cv2.waitKey(5) & 0xFF == 27:
                    break

            cap.release()