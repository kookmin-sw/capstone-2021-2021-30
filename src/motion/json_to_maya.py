import maya.cmds as cmds
import json, math, os

class jsonToMaya:
    # Rotation 값 저장할 리스트 46 + 46*3 (총 184)
    def __init__(self):
        #self.data_path = "../data/"
        self.data_path = "D:/Workspace/GitHub/capstone-2021-2021-30/data/"
        self.json_name = ""
        self.json_data = None
        self.frames = 0

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
        self.right_wrist = dict()
        self.right_thumb_cmc = dict()
        self.right_thumb_mcp = dict()
        self.right_thumb_ip = dict()
        self.right_thumb_tip = dict()
        self.right_index_finger_mcp = dict()
        self.right_index_finger_pip = dict()
        self.right_index_finger_dip = dict()
        self.right_index_finger_tip = dict()
        self.right_middle_finger_mcp = dict()
        self.right_middle_finger_pip = dict()
        self.right_middle_finger_dip = dict()
        self.right_middle_finger_tip = dict()
        self.right_ring_finger_mcp = dict()
        self.right_ring_finger_pip = dict()
        self.right_ring_finger_dip = dict()
        self.right_ring_finger_tip = dict()
        self.right_pinky_mcp = dict()
        self.right_pinky_pip = dict()
        self.right_pinky_dip = dict()
        self.right_pinky_tip = dict()

        self.left_shoulder_x = dict()
        self.left_elbow_x = dict()
        self.left_wrist_x = dict()
        self.left_thumb_cmc_x = dict()
        self.left_thumb_mcp_x = dict()
        self.left_thumb_ip_x = dict()
        self.left_thumb_tip_x = dict()
        self.left_index_finger_mcp_x = dict()
        self.left_index_finger_pip_x = dict()
        self.left_index_finger_dip_x = dict()
        self.left_index_finger_tip_x = dict()
        self.left_middle_finger_mcp_x = dict()
        self.left_middle_finger_pip_x = dict()
        self.left_middle_finger_dip_x = dict()
        self.left_middle_finger_tip_x = dict()
        self.left_ring_finger_mcp_x = dict()
        self.left_ring_finger_pip_x = dict()
        self.left_ring_finger_dip_x = dict()
        self.left_ring_finger_tip_x = dict()
        self.left_pinky_mcp_x = dict()
        self.left_pinky_pip_x = dict()
        self.left_pinky_dip_x = dict()
        self.left_pinky_tip_x = dict()
        self.right_shoulder_x = dict()
        self.right_elbow_x = dict()
        self.right_wrist_x = dict()
        self.right_thumb_cmc_x = dict()
        self.right_thumb_mcp_x = dict()
        self.right_thumb_ip_x = dict()
        self.right_thumb_tip_x = dict()
        self.right_index_finger_mcp_x = dict()
        self.right_index_finger_pip_x = dict()
        self.right_index_finger_dip_x = dict()
        self.right_index_finger_tip_x = dict()
        self.right_middle_finger_mcp_x = dict()
        self.right_middle_finger_pip_x = dict()
        self.right_middle_finger_dip_x = dict()
        self.right_middle_finger_tip_x = dict()
        self.right_ring_finger_mcp_x = dict()
        self.right_ring_finger_pip_x = dict()
        self.right_ring_finger_dip_x = dict()
        self.right_ring_finger_tip_x = dict()
        self.right_pinky_mcp_x = dict()
        self.right_pinky_pip_x = dict()
        self.right_pinky_dip_x = dict()
        self.right_pinky_tip_x = dict()

        self.left_shoulder_y = dict()
        self.left_elbow_y = dict()
        self.left_wrist_y = dict()
        self.left_thumb_cmc_y = dict()
        self.left_thumb_mcp_y = dict()
        self.left_thumb_ip_y = dict()
        self.left_thumb_tip_y = dict()
        self.left_index_finger_mcp_y = dict()
        self.left_index_finger_pip_y = dict()
        self.left_index_finger_dip_y = dict()
        self.left_index_finger_tip_y = dict()
        self.left_middle_finger_mcp_y = dict()
        self.left_middle_finger_pip_y = dict()
        self.left_middle_finger_dip_y = dict()
        self.left_middle_finger_tip_y = dict()
        self.left_ring_finger_mcp_y = dict()
        self.left_ring_finger_pip_y = dict()
        self.left_ring_finger_dip_y = dict()
        self.left_ring_finger_tip_y = dict()
        self.left_pinky_mcp_y = dict()
        self.left_pinky_pip_y = dict()
        self.left_pinky_dip_y = dict()
        self.left_pinky_tip_y = dict()
        self.right_shoulder_y = dict()
        self.right_elbow_y = dict()
        self.right_wrist_y = dict()
        self.right_thumb_cmc_y = dict()
        self.right_thumb_mcp_y = dict()
        self.right_thumb_ip_y = dict()
        self.right_thumb_tip_y = dict()
        self.right_index_finger_mcp_y = dict()
        self.right_index_finger_pip_y = dict()
        self.right_index_finger_dip_y = dict()
        self.right_index_finger_tip_y = dict()
        self.right_middle_finger_mcp_y = dict()
        self.right_middle_finger_pip_y = dict()
        self.right_middle_finger_dip_y = dict()
        self.right_middle_finger_tip_y = dict()
        self.right_ring_finger_mcp_y = dict()
        self.right_ring_finger_pip_y = dict()
        self.right_ring_finger_dip_y = dict()
        self.right_ring_finger_tip_y = dict()
        self.right_pinky_mcp_y = dict()
        self.right_pinky_pip_y = dict()
        self.right_pinky_dip_y = dict()
        self.right_pinky_tip_y = dict()

        self.left_shoulder_z = dict()
        self.left_elbow_z = dict()
        self.left_wrist_z = dict()
        self.left_thumb_cmc_z = dict()
        self.left_thumb_mcp_z = dict()
        self.left_thumb_ip_z = dict()
        self.left_thumb_tip_z = dict()
        self.left_index_finger_mcp_z = dict()
        self.left_index_finger_pip_z = dict()
        self.left_index_finger_dip_z = dict()
        self.left_index_finger_tip_z = dict()
        self.left_middle_finger_mcp_z = dict()
        self.left_middle_finger_pip_z = dict()
        self.left_middle_finger_dip_z = dict()
        self.left_middle_finger_tip_z = dict()
        self.left_ring_finger_mcp_z = dict()
        self.left_ring_finger_pip_z = dict()
        self.left_ring_finger_dip_z = dict()
        self.left_ring_finger_tip_z = dict()
        self.left_pinky_mcp_z = dict()
        self.left_pinky_pip_z = dict()
        self.left_pinky_dip_z = dict()
        self.left_pinky_tip_z = dict()
        self.right_shoulder_z = dict()
        self.right_elbow_z = dict()
        self.right_wrist_z = dict()
        self.right_thumb_cmc_z = dict()
        self.right_thumb_mcp_z = dict()
        self.right_thumb_ip_z = dict()
        self.right_thumb_tip_z = dict()
        self.right_index_finger_mcp_z = dict()
        self.right_index_finger_pip_z = dict()
        self.right_index_finger_dip_z = dict()
        self.right_index_finger_tip_z = dict()
        self.right_middle_finger_mcp_z = dict()
        self.right_middle_finger_pip_z = dict()
        self.right_middle_finger_dip_z = dict()
        self.right_middle_finger_tip_z = dict()
        self.right_ring_finger_mcp_z = dict()
        self.right_ring_finger_pip_z = dict()
        self.right_ring_finger_dip_z = dict()
        self.right_ring_finger_tip_z = dict()
        self.right_pinky_mcp_z = dict()
        self.right_pinky_pip_z = dict()
        self.right_pinky_dip_z = dict()
        self.right_pinky_tip_z = dict()

    # 클래스 실행 함수
    def excute(self):
        print("\n##### json_to_python.py #####\n")

        # keypoint 폴더에서 json 파일 선택
        json_list = os.listdir(self.data_path + "keypoint/")
        print("")
        for i, file in enumerate(json_list):
            print(i, '. ', file)
        try:
            json_num = int(input("\nSelect json file: "))
            self.json_name = json_list[json_num]
        except:
            print("\n! Error: Wrong select number")

        self.locToRot()  # json -> rotation

    # json 파일을 읽고, Rotation 값을 구한 뒤, 리스트에 저장
    def locToRot(self):
        # json 파일을 읽고
        with open(self.data_path + "keypoint/" + self.json_name, 'r') as f:
            self.json_data = json.load(f)

        # json 파일을 읽고 프레임별로 Rotaion 값 구한 뒤, 리스트에 저장
        self.frames = self.json_data['frames']
        for i in range(self.frames+1):
            # Left-x
            self.left_shoulder_x[i] = self.json_data['left_shoulder']['x'][str(i)]
            self.left_elbow_x[i] = self.json_data['left_elbow']['x'][str(i)] - \
                                   self.json_data['left_shoulder']['x'][str(i)]
            self.left_wrist_x[i] = self.json_data['left_wrist']['x'][str(i)] - \
                                   self.json_data['left_elbow']['x'][str(i)]

            self.left_thumb_cmc_x[i] = self.json_data['left_thumb_cmc']['x'][str(i)] - \
                                       self.json_data['left_wrist']['x'][str(i)]
            self.left_thumb_mcp_x[i] = self.json_data['left_thumb_mcp']['x'][str(i)] - \
                                       self.json_data['left_thumb_cmc']['x'][str(i)]
            self.left_thumb_ip_x[i] = self.json_data['left_thumb_ip']['x'][str(i)] - \
                                       self.json_data['left_thumb_mcp']['x'][str(i)]
            self.left_thumb_tip_x[i] = self.json_data['left_thumb_tip']['x'][str(i)] - \
                                       self.json_data['left_thumb_ip']['x'][str(i)]

            self.left_index_finger_mcp_x[i] = self.json_data['left_index_finger_mcp']['x'][str(i)] - \
                                       self.json_data['left_wrist']['x'][str(i)]
            self.left_index_finger_pip_x[i] = self.json_data['left_index_finger_pip']['x'][str(i)] - \
                                       self.json_data['left_index_finger_mcp']['x'][str(i)]
            self.left_index_finger_dip_x[i] = self.json_data['left_index_finger_dip']['x'][str(i)] - \
                                      self.json_data['left_index_finger_pip']['x'][str(i)]
            self.left_index_finger_tip_x[i] = self.json_data['left_index_finger_tip']['x'][str(i)] - \
                                       self.json_data['left_index_finger_dip']['x'][str(i)]

            self.left_middle_finger_mcp_x[i] = self.json_data['left_middle_finger_mcp']['x'][str(i)] - \
                                       self.json_data['left_wrist']['x'][str(i)]
            self.left_middle_finger_pip_x[i] = self.json_data['left_middle_finger_pip']['x'][str(i)] - \
                                       self.json_data['left_middle_finger_mcp']['x'][str(i)]
            self.left_middle_finger_dip_x[i] = self.json_data['left_middle_finger_dip']['x'][str(i)] - \
                                      self.json_data['left_middle_finger_pip']['x'][str(i)]
            self.left_middle_finger_tip_x[i] = self.json_data['left_middle_finger_tip']['x'][str(i)] - \
                                       self.json_data['left_middle_finger_dip']['x'][str(i)]

            self.left_ring_finger_mcp_x[i] = self.json_data['left_ring_finger_mcp']['x'][str(i)] - \
                                       self.json_data['left_wrist']['x'][str(i)]
            self.left_ring_finger_pip_x[i] = self.json_data['left_ring_finger_pip']['x'][str(i)] - \
                                       self.json_data['left_ring_finger_mcp']['x'][str(i)]
            self.left_ring_finger_dip_x[i] = self.json_data['left_ring_finger_dip']['x'][str(i)] - \
                                      self.json_data['left_ring_finger_pip']['x'][str(i)]
            self.left_ring_finger_tip_x[i] = self.json_data['left_ring_finger_tip']['x'][str(i)] - \
                                       self.json_data['left_ring_finger_dip']['x'][str(i)]

            self.left_pinky_mcp_x[i] = self.json_data['left_pinky_mcp']['x'][str(i)] - \
                                       self.json_data['left_wrist']['x'][str(i)]
            self.left_pinky_pip_x[i] = self.json_data['left_pinky_pip']['x'][str(i)] - \
                                       self.json_data['left_pinky_mcp']['x'][str(i)]
            self.left_pinky_dip_x[i] = self.json_data['left_pinky_dip']['x'][str(i)] - \
                                      self.json_data['left_pinky_pip']['x'][str(i)]
            self.left_pinky_tip_x[i] = self.json_data['left_pinky_tip']['x'][str(i)] - \
                                       self.json_data['left_pinky_dip']['x'][str(i)]

            # Right-x
            self.right_shoulder_x[i] = self.json_data['right_shoulder']['x'][str(i)]
            self.right_elbow_x[i] = self.json_data['right_elbow']['x'][str(i)] - \
                                   self.json_data['right_shoulder']['x'][str(i)]
            self.right_wrist_x[i] = self.json_data['right_wrist']['x'][str(i)] - \
                                   self.json_data['right_elbow']['x'][str(i)]

            self.right_thumb_cmc_x[i] = self.json_data['right_thumb_cmc']['x'][str(i)] - \
                                       self.json_data['right_wrist']['x'][str(i)]
            self.right_thumb_mcp_x[i] = self.json_data['right_thumb_mcp']['x'][str(i)] - \
                                       self.json_data['right_thumb_cmc']['x'][str(i)]
            self.right_thumb_ip_x[i] = self.json_data['right_thumb_ip']['x'][str(i)] - \
                                      self.json_data['right_thumb_mcp']['x'][str(i)]
            self.right_thumb_tip_x[i] = self.json_data['right_thumb_tip']['x'][str(i)] - \
                                       self.json_data['right_thumb_ip']['x'][str(i)]

            self.right_index_finger_mcp_x[i] = self.json_data['right_index_finger_mcp']['x'][str(i)] - \
                                              self.json_data['right_wrist']['x'][str(i)]
            self.right_index_finger_pip_x[i] = self.json_data['right_index_finger_pip']['x'][str(i)] - \
                                              self.json_data['right_index_finger_mcp']['x'][str(i)]
            self.right_index_finger_dip_x[i] = self.json_data['right_index_finger_dip']['x'][str(i)] - \
                                              self.json_data['right_index_finger_pip']['x'][str(i)]
            self.right_index_finger_tip_x[i] = self.json_data['right_index_finger_tip']['x'][str(i)] - \
                                              self.json_data['right_index_finger_dip']['x'][str(i)]

            self.right_middle_finger_mcp_x[i] = self.json_data['right_middle_finger_mcp']['x'][str(i)] - \
                                               self.json_data['right_wrist']['x'][str(i)]
            self.right_middle_finger_pip_x[i] = self.json_data['right_middle_finger_pip']['x'][str(i)] - \
                                               self.json_data['right_middle_finger_mcp']['x'][str(i)]
            self.right_middle_finger_dip_x[i] = self.json_data['right_middle_finger_dip']['x'][str(i)] - \
                                               self.json_data['right_middle_finger_pip']['x'][str(i)]
            self.right_middle_finger_tip_x[i] = self.json_data['right_middle_finger_tip']['x'][str(i)] - \
                                               self.json_data['right_middle_finger_dip']['x'][str(i)]

            self.right_ring_finger_mcp_x[i] = self.json_data['right_ring_finger_mcp']['x'][str(i)] - \
                                             self.json_data['right_wrist']['x'][str(i)]
            self.right_ring_finger_pip_x[i] = self.json_data['right_ring_finger_pip']['x'][str(i)] - \
                                             self.json_data['right_ring_finger_mcp']['x'][str(i)]
            self.right_ring_finger_dip_x[i] = self.json_data['right_ring_finger_dip']['x'][str(i)] - \
                                             self.json_data['right_ring_finger_pip']['x'][str(i)]
            self.right_ring_finger_tip_x[i] = self.json_data['right_ring_finger_tip']['x'][str(i)] - \
                                             self.json_data['right_ring_finger_dip']['x'][str(i)]

            self.right_pinky_mcp_x[i] = self.json_data['right_pinky_mcp']['x'][str(i)] - \
                                       self.json_data['right_wrist']['x'][str(i)]
            self.right_pinky_pip_x[i] = self.json_data['right_pinky_pip']['x'][str(i)] - \
                                       self.json_data['right_pinky_mcp']['x'][str(i)]
            self.right_pinky_dip_x[i] = self.json_data['right_pinky_dip']['x'][str(i)] - \
                                       self.json_data['right_pinky_pip']['x'][str(i)]
            self.right_pinky_tip_x[i] = self.json_data['right_pinky_tip']['x'][str(i)] - \
                                       self.json_data['right_pinky_dip']['x'][str(i)]

            # Left-y
            self.left_shoulder_y[i] = self.json_data['left_shoulder']['y'][str(i)]
            self.left_elbow_y[i] = self.json_data['left_elbow']['y'][str(i)] - \
                                   self.json_data['left_shoulder']['y'][str(i)]
            self.left_wrist_y[i] = self.json_data['left_wrist']['y'][str(i)] - \
                                   self.json_data['left_elbow']['y'][str(i)]

            self.left_thumb_cmc_y[i] = self.json_data['left_thumb_cmc']['y'][str(i)] - \
                                       self.json_data['left_wrist']['y'][str(i)]
            self.left_thumb_mcp_y[i] = self.json_data['left_thumb_mcp']['y'][str(i)] - \
                                       self.json_data['left_thumb_cmc']['y'][str(i)]
            self.left_thumb_ip_y[i] = self.json_data['left_thumb_ip']['y'][str(i)] - \
                                      self.json_data['left_thumb_mcp']['y'][str(i)]
            self.left_thumb_tip_y[i] = self.json_data['left_thumb_tip']['y'][str(i)] - \
                                       self.json_data['left_thumb_ip']['y'][str(i)]

            self.left_index_finger_mcp_y[i] = self.json_data['left_index_finger_mcp']['y'][str(i)] - \
                                              self.json_data['left_wrist']['y'][str(i)]
            self.left_index_finger_pip_y[i] = self.json_data['left_index_finger_pip']['y'][str(i)] - \
                                              self.json_data['left_index_finger_mcp']['y'][str(i)]
            self.left_index_finger_dip_y[i] = self.json_data['left_index_finger_dip']['y'][str(i)] - \
                                              self.json_data['left_index_finger_pip']['y'][str(i)]
            self.left_index_finger_tip_y[i] = self.json_data['left_index_finger_tip']['y'][str(i)] - \
                                              self.json_data['left_index_finger_dip']['y'][str(i)]

            self.left_middle_finger_mcp_y[i] = self.json_data['left_middle_finger_mcp']['y'][str(i)] - \
                                               self.json_data['left_wrist']['y'][str(i)]
            self.left_middle_finger_pip_y[i] = self.json_data['left_middle_finger_pip']['y'][str(i)] - \
                                               self.json_data['left_middle_finger_mcp']['y'][str(i)]
            self.left_middle_finger_dip_y[i] = self.json_data['left_middle_finger_dip']['y'][str(i)] - \
                                               self.json_data['left_middle_finger_pip']['y'][str(i)]
            self.left_middle_finger_tip_y[i] = self.json_data['left_middle_finger_tip']['y'][str(i)] - \
                                               self.json_data['left_middle_finger_dip']['y'][str(i)]

            self.left_ring_finger_mcp_y[i] = self.json_data['left_ring_finger_mcp']['y'][str(i)] - \
                                             self.json_data['left_wrist']['y'][str(i)]
            self.left_ring_finger_pip_y[i] = self.json_data['left_ring_finger_pip']['y'][str(i)] - \
                                             self.json_data['left_ring_finger_mcp']['y'][str(i)]
            self.left_ring_finger_dip_y[i] = self.json_data['left_ring_finger_dip']['y'][str(i)] - \
                                             self.json_data['left_ring_finger_pip']['y'][str(i)]
            self.left_ring_finger_tip_y[i] = self.json_data['left_ring_finger_tip']['y'][str(i)] - \
                                             self.json_data['left_ring_finger_dip']['y'][str(i)]

            self.left_pinky_mcp_y[i] = self.json_data['left_pinky_mcp']['y'][str(i)] - \
                                       self.json_data['left_wrist']['y'][str(i)]
            self.left_pinky_pip_y[i] = self.json_data['left_pinky_pip']['y'][str(i)] - \
                                       self.json_data['left_pinky_mcp']['y'][str(i)]
            self.left_pinky_dip_y[i] = self.json_data['left_pinky_dip']['y'][str(i)] - \
                                       self.json_data['left_pinky_pip']['y'][str(i)]
            self.left_pinky_tip_y[i] = self.json_data['left_pinky_tip']['y'][str(i)] - \
                                       self.json_data['left_pinky_dip']['y'][str(i)]

            # Right-y
            self.right_shoulder_y[i] = self.json_data['right_shoulder']['y'][str(i)]
            self.right_elbow_y[i] = self.json_data['right_elbow']['y'][str(i)] - \
                                   self.json_data['right_shoulder']['y'][str(i)]
            self.right_wrist_y[i] = self.json_data['right_wrist']['y'][str(i)] - \
                                   self.json_data['right_elbow']['y'][str(i)]

            self.right_thumb_cmc_y[i] = self.json_data['right_thumb_cmc']['y'][str(i)] - \
                                       self.json_data['right_wrist']['y'][str(i)]
            self.right_thumb_mcp_y[i] = self.json_data['right_thumb_mcp']['y'][str(i)] - \
                                       self.json_data['right_thumb_cmc']['y'][str(i)]
            self.right_thumb_ip_y[i] = self.json_data['right_thumb_ip']['y'][str(i)] - \
                                      self.json_data['right_thumb_mcp']['y'][str(i)]
            self.right_thumb_tip_y[i] = self.json_data['right_thumb_tip']['y'][str(i)] - \
                                       self.json_data['right_thumb_ip']['y'][str(i)]

            self.right_index_finger_mcp_y[i] = self.json_data['right_index_finger_mcp']['y'][str(i)] - \
                                              self.json_data['right_wrist']['y'][str(i)]
            self.right_index_finger_pip_y[i] = self.json_data['right_index_finger_pip']['y'][str(i)] - \
                                              self.json_data['right_index_finger_mcp']['y'][str(i)]
            self.right_index_finger_dip_y[i] = self.json_data['right_index_finger_dip']['y'][str(i)] - \
                                              self.json_data['right_index_finger_pip']['y'][str(i)]
            self.right_index_finger_tip_y[i] = self.json_data['right_index_finger_tip']['y'][str(i)] - \
                                              self.json_data['right_index_finger_dip']['y'][str(i)]

            self.right_middle_finger_mcp_y[i] = self.json_data['right_middle_finger_mcp']['y'][str(i)] - \
                                               self.json_data['right_wrist']['y'][str(i)]
            self.right_middle_finger_pip_y[i] = self.json_data['right_middle_finger_pip']['y'][str(i)] - \
                                               self.json_data['right_middle_finger_mcp']['y'][str(i)]
            self.right_middle_finger_dip_y[i] = self.json_data['right_middle_finger_dip']['y'][str(i)] - \
                                               self.json_data['right_middle_finger_pip']['y'][str(i)]
            self.right_middle_finger_tip_y[i] = self.json_data['right_middle_finger_tip']['y'][str(i)] - \
                                               self.json_data['right_middle_finger_dip']['y'][str(i)]

            self.right_ring_finger_mcp_y[i] = self.json_data['right_ring_finger_mcp']['y'][str(i)] - \
                                             self.json_data['right_wrist']['y'][str(i)]
            self.right_ring_finger_pip_y[i] = self.json_data['right_ring_finger_pip']['y'][str(i)] - \
                                             self.json_data['right_ring_finger_mcp']['y'][str(i)]
            self.right_ring_finger_dip_y[i] = self.json_data['right_ring_finger_dip']['y'][str(i)] - \
                                             self.json_data['right_ring_finger_pip']['y'][str(i)]
            self.right_ring_finger_tip_y[i] = self.json_data['right_ring_finger_tip']['y'][str(i)] - \
                                             self.json_data['right_ring_finger_dip']['y'][str(i)]

            self.right_pinky_mcp_y[i] = self.json_data['right_pinky_mcp']['y'][str(i)] - \
                                       self.json_data['right_wrist']['y'][str(i)]
            self.right_pinky_pip_y[i] = self.json_data['right_pinky_pip']['y'][str(i)] - \
                                       self.json_data['right_pinky_mcp']['y'][str(i)]
            self.right_pinky_dip_y[i] = self.json_data['right_pinky_dip']['y'][str(i)] - \
                                       self.json_data['right_pinky_pip']['y'][str(i)]
            self.right_pinky_tip_y[i] = self.json_data['right_pinky_tip']['y'][str(i)] - \
                                       self.json_data['right_pinky_dip']['y'][str(i)]

            # Left-z
            self.left_shoulder_z[i] = self.json_data['left_shoulder']['z'][str(i)]
            self.left_elbow_z[i] = self.json_data['left_elbow']['z'][str(i)] - \
                                   self.json_data['left_shoulder']['z'][str(i)]
            self.left_wrist_z[i] = self.json_data['left_wrist']['z'][str(i)] - \
                                   self.json_data['left_elbow']['z'][str(i)]

            self.left_thumb_cmc_z[i] = self.json_data['left_thumb_cmc']['z'][str(i)] - \
                                       self.json_data['left_wrist']['z'][str(i)]
            self.left_thumb_mcp_z[i] = self.json_data['left_thumb_mcp']['z'][str(i)] - \
                                       self.json_data['left_thumb_cmc']['z'][str(i)]
            self.left_thumb_ip_z[i] = self.json_data['left_thumb_ip']['z'][str(i)] - \
                                      self.json_data['left_thumb_mcp']['z'][str(i)]
            self.left_thumb_tip_z[i] = self.json_data['left_thumb_tip']['z'][str(i)] - \
                                       self.json_data['left_thumb_ip']['z'][str(i)]

            self.left_index_finger_mcp_z[i] = self.json_data['left_index_finger_mcp']['z'][str(i)] - \
                                              self.json_data['left_wrist']['z'][str(i)]
            self.left_index_finger_pip_z[i] = self.json_data['left_index_finger_pip']['z'][str(i)] - \
                                              self.json_data['left_index_finger_mcp']['z'][str(i)]
            self.left_index_finger_dip_z[i] = self.json_data['left_index_finger_dip']['z'][str(i)] - \
                                              self.json_data['left_index_finger_pip']['z'][str(i)]
            self.left_index_finger_tip_z[i] = self.json_data['left_index_finger_tip']['z'][str(i)] - \
                                              self.json_data['left_index_finger_dip']['z'][str(i)]

            self.left_middle_finger_mcp_z[i] = self.json_data['left_middle_finger_mcp']['z'][str(i)] - \
                                               self.json_data['left_wrist']['z'][str(i)]
            self.left_middle_finger_pip_z[i] = self.json_data['left_middle_finger_pip']['z'][str(i)] - \
                                               self.json_data['left_middle_finger_mcp']['z'][str(i)]
            self.left_middle_finger_dip_z[i] = self.json_data['left_middle_finger_dip']['z'][str(i)] - \
                                               self.json_data['left_middle_finger_pip']['z'][str(i)]
            self.left_middle_finger_tip_z[i] = self.json_data['left_middle_finger_tip']['z'][str(i)] - \
                                               self.json_data['left_middle_finger_dip']['z'][str(i)]

            self.left_ring_finger_mcp_z[i] = self.json_data['left_ring_finger_mcp']['z'][str(i)] - \
                                             self.json_data['left_wrist']['z'][str(i)]
            self.left_ring_finger_pip_z[i] = self.json_data['left_ring_finger_pip']['z'][str(i)] - \
                                             self.json_data['left_ring_finger_mcp']['z'][str(i)]
            self.left_ring_finger_dip_z[i] = self.json_data['left_ring_finger_dip']['z'][str(i)] - \
                                             self.json_data['left_ring_finger_pip']['z'][str(i)]
            self.left_ring_finger_tip_z[i] = self.json_data['left_ring_finger_tip']['z'][str(i)] - \
                                             self.json_data['left_ring_finger_dip']['z'][str(i)]

            self.left_pinky_mcp_z[i] = self.json_data['left_pinky_mcp']['z'][str(i)] - \
                                       self.json_data['left_wrist']['z'][str(i)]
            self.left_pinky_pip_z[i] = self.json_data['left_pinky_pip']['z'][str(i)] - \
                                       self.json_data['left_pinky_mcp']['z'][str(i)]
            self.left_pinky_dip_z[i] = self.json_data['left_pinky_dip']['z'][str(i)] - \
                                       self.json_data['left_pinky_pip']['z'][str(i)]
            self.left_pinky_tip_z[i] = self.json_data['left_pinky_tip']['z'][str(i)] - \
                                       self.json_data['left_pinky_dip']['z'][str(i)]

            # Right-z
            self.right_shoulder_z[i] = self.json_data['right_shoulder']['z'][str(i)]
            self.right_elbow_z[i] = self.json_data['right_elbow']['z'][str(i)] - \
                                   self.json_data['right_shoulder']['z'][str(i)]
            self.right_wrist_z[i] = self.json_data['right_wrist']['z'][str(i)] - \
                                   self.json_data['right_elbow']['z'][str(i)]

            self.right_thumb_cmc_z[i] = self.json_data['right_thumb_cmc']['z'][str(i)] - \
                                       self.json_data['right_wrist']['z'][str(i)]
            self.right_thumb_mcp_z[i] = self.json_data['right_thumb_mcp']['z'][str(i)] - \
                                       self.json_data['right_thumb_cmc']['z'][str(i)]
            self.right_thumb_ip_z[i] = self.json_data['right_thumb_ip']['z'][str(i)] - \
                                      self.json_data['right_thumb_mcp']['z'][str(i)]
            self.right_thumb_tip_z[i] = self.json_data['right_thumb_tip']['z'][str(i)] - \
                                       self.json_data['right_thumb_ip']['z'][str(i)]

            self.right_index_finger_mcp_z[i] = self.json_data['right_index_finger_mcp']['z'][str(i)] - \
                                              self.json_data['right_wrist']['z'][str(i)]
            self.right_index_finger_pip_z[i] = self.json_data['right_index_finger_pip']['z'][str(i)] - \
                                              self.json_data['right_index_finger_mcp']['z'][str(i)]
            self.right_index_finger_dip_z[i] = self.json_data['right_index_finger_dip']['z'][str(i)] - \
                                              self.json_data['right_index_finger_pip']['z'][str(i)]
            self.right_index_finger_tip_z[i] = self.json_data['right_index_finger_tip']['z'][str(i)] - \
                                              self.json_data['right_index_finger_dip']['z'][str(i)]

            self.right_middle_finger_mcp_z[i] = self.json_data['right_middle_finger_mcp']['z'][str(i)] - \
                                               self.json_data['right_wrist']['z'][str(i)]
            self.right_middle_finger_pip_z[i] = self.json_data['right_middle_finger_pip']['z'][str(i)] - \
                                               self.json_data['right_middle_finger_mcp']['z'][str(i)]
            self.right_middle_finger_dip_z[i] = self.json_data['right_middle_finger_dip']['z'][str(i)] - \
                                               self.json_data['right_middle_finger_pip']['z'][str(i)]
            self.right_middle_finger_tip_z[i] = self.json_data['right_middle_finger_tip']['z'][str(i)] - \
                                               self.json_data['right_middle_finger_dip']['z'][str(i)]

            self.right_ring_finger_mcp_z[i] = self.json_data['right_ring_finger_mcp']['z'][str(i)] - \
                                             self.json_data['right_wrist']['z'][str(i)]
            self.right_ring_finger_pip_z[i] = self.json_data['right_ring_finger_pip']['z'][str(i)] - \
                                             self.json_data['right_ring_finger_mcp']['z'][str(i)]
            self.right_ring_finger_dip_z[i] = self.json_data['right_ring_finger_dip']['z'][str(i)] - \
                                             self.json_data['right_ring_finger_pip']['z'][str(i)]
            self.right_ring_finger_tip_z[i] = self.json_data['right_ring_finger_tip']['z'][str(i)] - \
                                             self.json_data['right_ring_finger_dip']['z'][str(i)]

            self.right_pinky_mcp_z[i] = self.json_data['right_pinky_mcp']['z'][str(i)] - \
                                       self.json_data['right_wrist']['z'][str(i)]
            self.right_pinky_pip_z[i] = self.json_data['right_pinky_pip']['z'][str(i)] - \
                                       self.json_data['right_pinky_mcp']['z'][str(i)]
            self.right_pinky_dip_z[i] = self.json_data['right_pinky_dip']['z'][str(i)] - \
                                       self.json_data['right_pinky_pip']['z'][str(i)]
            self.right_pinky_tip_z[i] = self.json_data['right_pinky_tip']['z'][str(i)] - \
                                       self.json_data['right_pinky_dip']['z'][str(i)]

    # Rotation 값이 저장된 배열을 가지고 키프레임 생성
    def setKeyframes(self):
        objs = cmds.ls(selection=True)  # ['Character1_Reference', 'Character1_Hips', ...] 이런식으로 불러옴

        for obj in objs:
            alpha = 75
            falpha = 10
            trans = []
            rot = []
            frames = self.json_data['frames']

            if 'Character1' in obj:
                for frame in range(self.frames+1):
                    if 'Left' in obj:
                        if obj == 'Character1_LeftArm':

                            cmds.setKeyframe(obj + '.translateX', value=trans[0][0], time=frame * falpha)
                            cmds.setKeyframe(obj + '.translateY', value=trans[0][1], time=frame * falpha)
                            cmds.setKeyframe(obj + '.translateZ', value=trans[0][2], time=frame * falpha)
                        elif obj == 'Character1_LeftForeArm':
                            return
                        elif obj == 'Character1_LeftHand':
                            return
                        elif obj == 'Character1_LeftHandThumb1':
                            return
                        elif obj == 'Character1_LeftHandThumb2':
                            return
                        elif obj == 'Character1_LeftHandThumb3':
                            return
                        elif obj == 'Character1_LeftHandThumb4':
                            return
                        elif obj == 'Character1_LeftHandIndex1':
                            return
                        elif obj == 'Character1_LeftHandIndex2':
                            return
                        elif obj == 'Character1_LeftHandIndex3':
                            return
                        elif obj == 'Character1_LeftHandIndex4':
                            return
                        elif obj == 'Character1_LeftHandMiddle1':
                            return
                        elif obj == 'Character1_LeftHandMiddle2':
                            return
                        elif obj == 'Character1_LeftHandMiddle3':
                            return
                        elif obj == 'Character1_LeftHandMiddle4':
                            return
                        elif obj == 'Character1_LeftHandRing1':
                            return
                        elif obj == 'Character1_LeftHandRing2':
                            return
                        elif obj == 'Character1_LeftHandRing3':
                            return
                        elif obj == 'Character1_LeftHandRing4':
                            return
                        elif obj == 'Character1_LeftHandPinky1':
                            return
                        elif obj == 'Character1_LeftHandPinky2':
                            return
                        elif obj == 'Character1_LeftHandPinky3':
                            return
                        elif obj == 'Character1_LeftHandPinky4':
                            return

                    elif 'Right' in obj:
                        if obj == 'Character1_RightArm':
                            return
                        elif obj == 'Character1_RightForeArm':
                            return
                        elif obj == 'Character1_RightHand':
                            return
                        elif obj == 'Character1_RightHandThumb1':
                            return
                        elif obj == 'Character1_RightHandThumb2':
                            return
                        elif obj == 'Character1_RightHandThumb3':
                            return
                        elif obj == 'Character1_RightHandThumb4':
                            return
                        elif obj == 'Character1_RightHandIndex1':
                            return
                        elif obj == 'Character1_RightHandIndex2':
                            return
                        elif obj == 'Character1_RightHandIndex3':
                            return
                        elif obj == 'Character1_RightHandIndex4':
                            return
                        elif obj == 'Character1_RightHandMiddle1':
                            return
                        elif obj == 'Character1_RightHandMiddle2':
                            return
                        elif obj == 'Character1_RightHandMiddle3':
                            return
                        elif obj == 'Character1_RightHandMiddle4':
                            return
                        elif obj == 'Character1_RightHandRing1':
                            return
                        elif obj == 'Character1_RightHandRing2':
                            return
                        elif obj == 'Character1_RightHandRing3':
                            return
                        elif obj == 'Character1_RightHandRing4':
                            return
                        elif obj == 'Character1_RightHandPinky1':
                            return
                        elif obj == 'Character1_RightHandPinky2':
                            return
                        elif obj == 'Character1_RightHandPinky3':
                            return
                        elif obj == 'Character1_RightHandPinky4':
                            return

jtm = jsonToMaya()
jtm.excute()