import cv2, json, os
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

class getKeypoint:
    def getKeypointFromImages(self, download_path, video_name):
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
        images_path = download_path + "image_cropped/" + video_name + "/"
        ffile_list = os.listdir(images_path)
        file_list = []
        for ffile in ffile_list:
            file = int(ffile.split('.')[0])
            file_list.append(file)

        file_list.sort()

        # json 파일 생성
        json_path = download_path + "keypoint/" + video_name + ".json"
        with open(json_path, 'w') as f:
            pass

        # imread가 한글 경로를 인식하지 못해 대신 imencode 사용
        def imread2(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
            try:
                n = np.fromfile(filename, dtype)
                img = cv2.imdecode(n, flags)
                return img
            except Exception as e:
                print(e)
                return None

        # imwrite가 한글 경로를 인식하지 못해 대신 imencode 사용
        def imwrite2(filename, image, params=None):
            try:
                ext = os.path.splitext(filename)[1]
                result, n = cv2.imencode(ext, image, params)
                if result:
                    with open(filename, mode='w+b') as f:
                        n.tofile(f)
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                return False

        # 해당 비디오 파일의 이름으로 빈 디렉토리를 생성
        keypoint_path = download_path + "image_keypoint/" + video_name + "/"
        try:
            if not os.path.exists(keypoint_path):
                os.makedirs(keypoint_path)
            for file in os.scandir(keypoint_path):
                os.remove(file.path)
        except:
            print("\n! Error: Failed to create empty directory")

        with mp_holistic.Holistic(
            static_image_mode=True,
            min_detection_confidence=0.5,
            upper_body_only=True) as holistic:
            for idx, file in enumerate(file_list):
                image = imread2(images_path + str(file) + '.jpg')

                results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                frame = file

                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_holistic.UPPER_BODY_POSE_CONNECTIONS)

                imwrite2(keypoint_path + str(file) + ".jpg", image)
                print(keypoint_path + str(file) + ".jpg done...")

                if (results.pose_landmarks or results.left_hand_landmarks or results.right_hand_landmarks):
                    # json 파일 비어있는지 확인
                    with open(json_path) as f:
                        isEmpty = f.read().strip()

                    # json 파일이 있는 경우 추가
                    with open(json_path) as json_file:
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
                    with open(json_path, 'w') as outfile:
                        json.dump(file_data, outfile, indent='\t')

        print("\nGetting keypoints completed...")