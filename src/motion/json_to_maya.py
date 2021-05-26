import maya.cmds as cmds
import json, math, os, time

class jsonToMaya:
    # Translation 값 저장할 딕셔너리 (Translation > 키포인트(48개) > x, y, z)
    def __init__(self):
        #self.data_path = "../data/"
        self.data_path = "D:/Workspace/GitHub/capstone-2021-2021-30/data/"  # 마야 파이썬 스크립팅에서 상대 경로 사용 불가
        self.json_name = ""
        self.json_data = None
        self.frames = 0
        self.annotations = ['Character1_LeftShoulder', 'Character1_LeftArm', 'Character1_LeftForeArm', 'Character1_LeftHand',
                            'Character1_LeftHandThumb1', 'Character1_LeftHandThumb2', 'Character1_LeftHandThumb3', 'Character1_LeftHandThumb4',
                            'Character1_LeftHandIndex1', 'Character1_LeftHandIndex2', 'Character1_LeftHandIndex3', 'Character1_LeftHandIndex4',
                            'Character1_LeftHandMiddle1', 'Character1_LeftHandMiddle2', 'Character1_LeftHandMiddle3', 'Character1_LeftHandMiddle4',
                            'Character1_LeftHandRing1', 'Character1_LeftHandRing2', 'Character1_LeftHandRing3', 'Character1_LeftHandRing4',
                            'Character1_LeftHandPinky1', 'Character1_LeftHandPinky2', 'Character1_LeftHandPinky3', 'Character1_LeftHandPinky4',
                            'Character1_RightShoulder', 'Character1_RightArm', 'Character1_RightForeArm', 'Character1_RightHand',
                            'Character1_RightHandThumb1', 'Character1_RightHandThumb2', 'Character1_RightHandThumb3', 'Character1_RightHandThumb4',
                            'Character1_RightHandIndex1', 'Character1_RightHandIndex2', 'Character1_RightHandIndex3', 'Character1_RightHandIndex4',
                            'Character1_RightHandMiddle1', 'Character1_RightHandMiddle2', 'Character1_RightHandMiddle3', 'Character1_RightHandMiddle4',
                            'Character1_RightHandRing1', 'Character1_RightHandRing2', 'Character1_RightHandRing3', 'Character1_RightHandRing4',
                            'Character1_RightHandPinky1', 'Character1_RightHandPinky2', 'Character1_RightHandPinky3', 'Character1_RightHandPinky4'
                            ]
        # 최종 Translation 값 저장할 딕셔너리
        self.trans = dict()

        # 키포인트
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

        # x
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

        # y
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

        # z
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

        # 키포인트 > x
        self.left_shoulder["x"] = self.left_shoulder_x
        self.left_elbow["x"] = self.left_elbow_x
        self.left_wrist["x"] = self.left_wrist_x
        self.left_thumb_cmc["x"] = self.left_thumb_cmc_x
        self.left_thumb_mcp["x"] = self.left_thumb_mcp_x
        self.left_thumb_ip["x"] = self.left_thumb_ip_x
        self.left_thumb_tip["x"] = self.left_thumb_tip_x
        self.left_index_finger_mcp["x"] = self.left_index_finger_mcp_x
        self.left_index_finger_pip["x"] = self.left_index_finger_pip_x
        self.left_index_finger_dip["x"] = self.left_index_finger_dip_x
        self.left_index_finger_tip["x"] = self.left_index_finger_tip_x
        self.left_middle_finger_mcp["x"] = self.left_middle_finger_mcp_x
        self.left_middle_finger_pip["x"] = self.left_middle_finger_pip_x
        self.left_middle_finger_dip["x"] = self.left_middle_finger_dip_x
        self.left_middle_finger_tip["x"] = self.left_middle_finger_tip_x
        self.left_ring_finger_mcp["x"] = self.left_ring_finger_mcp_x
        self.left_ring_finger_pip["x"] = self.left_ring_finger_pip_x
        self.left_ring_finger_dip["x"] = self.left_ring_finger_dip_x
        self.left_ring_finger_tip["x"] = self.left_ring_finger_tip_x
        self.left_pinky_mcp["x"] = self.left_pinky_mcp_x
        self.left_pinky_pip["x"] = self.left_pinky_pip_x
        self.left_pinky_dip["x"] = self.left_pinky_dip_x
        self.left_pinky_tip["x"] = self.left_pinky_tip_x
        self.right_shoulder["x"] = self.right_shoulder_x
        self.right_elbow["x"] = self.right_elbow_x
        self.right_wrist["x"] = self.right_wrist_x
        self.right_thumb_cmc["x"] = self.right_thumb_cmc_x
        self.right_thumb_mcp["x"] = self.right_thumb_mcp_x
        self.right_thumb_ip["x"] = self.right_thumb_ip_x
        self.right_thumb_tip["x"] = self.right_thumb_tip_x
        self.right_index_finger_mcp["x"] = self.right_index_finger_mcp_x
        self.right_index_finger_pip["x"] = self.right_index_finger_pip_x
        self.right_index_finger_dip["x"] = self.right_index_finger_dip_x
        self.right_index_finger_tip["x"] = self.right_index_finger_tip_x
        self.right_middle_finger_mcp["x"] = self.right_middle_finger_mcp_x
        self.right_middle_finger_pip["x"] = self.right_middle_finger_pip_x
        self.right_middle_finger_dip["x"] = self.right_middle_finger_dip_x
        self.right_middle_finger_tip["x"] = self.right_middle_finger_tip_x
        self.right_ring_finger_mcp["x"] = self.right_ring_finger_mcp_x
        self.right_ring_finger_pip["x"] = self.right_ring_finger_pip_x
        self.right_ring_finger_dip["x"] = self.right_ring_finger_dip_x
        self.right_ring_finger_tip["x"] = self.right_ring_finger_tip_x
        self.right_pinky_mcp["x"] = self.right_pinky_mcp_x
        self.right_pinky_pip["x"] = self.right_pinky_pip_x
        self.right_pinky_dip["x"] = self.right_pinky_dip_x
        self.right_pinky_tip["x"] = self.right_pinky_tip_x

        # 키포인트 > y
        self.left_shoulder["y"] = self.left_shoulder_y
        self.left_elbow["y"] = self.left_elbow_y
        self.left_wrist["y"] = self.left_wrist_y
        self.left_thumb_cmc["y"] = self.left_thumb_cmc_y
        self.left_thumb_mcp["y"] = self.left_thumb_mcp_y
        self.left_thumb_ip["y"] = self.left_thumb_ip_y
        self.left_thumb_tip["y"] = self.left_thumb_tip_y
        self.left_index_finger_mcp["y"] = self.left_index_finger_mcp_y
        self.left_index_finger_pip["y"] = self.left_index_finger_pip_y
        self.left_index_finger_dip["y"] = self.left_index_finger_dip_y
        self.left_index_finger_tip["y"] = self.left_index_finger_tip_y
        self.left_middle_finger_mcp["y"] = self.left_middle_finger_mcp_y
        self.left_middle_finger_pip["y"] = self.left_middle_finger_pip_y
        self.left_middle_finger_dip["y"] = self.left_middle_finger_dip_y
        self.left_middle_finger_tip["y"] = self.left_middle_finger_tip_y
        self.left_ring_finger_mcp["y"] = self.left_ring_finger_mcp_y
        self.left_ring_finger_pip["y"] = self.left_ring_finger_pip_y
        self.left_ring_finger_dip["y"] = self.left_ring_finger_dip_y
        self.left_ring_finger_tip["y"] = self.left_ring_finger_tip_y
        self.left_pinky_mcp["y"] = self.left_pinky_mcp_y
        self.left_pinky_pip["y"] = self.left_pinky_pip_y
        self.left_pinky_dip["y"] = self.left_pinky_dip_y
        self.left_pinky_tip["y"] = self.left_pinky_tip_y
        self.right_shoulder["y"] = self.right_shoulder_y
        self.right_elbow["y"] = self.right_elbow_y
        self.right_wrist["y"] = self.right_wrist_y
        self.right_thumb_cmc["y"] = self.right_thumb_cmc_y
        self.right_thumb_mcp["y"] = self.right_thumb_mcp_y
        self.right_thumb_ip["y"] = self.right_thumb_ip_y
        self.right_thumb_tip["y"] = self.right_thumb_tip_y
        self.right_index_finger_mcp["y"] = self.right_index_finger_mcp_y
        self.right_index_finger_pip["y"] = self.right_index_finger_pip_y
        self.right_index_finger_dip["y"] = self.right_index_finger_dip_y
        self.right_index_finger_tip["y"] = self.right_index_finger_tip_y
        self.right_middle_finger_mcp["y"] = self.right_middle_finger_mcp_y
        self.right_middle_finger_pip["y"] = self.right_middle_finger_pip_y
        self.right_middle_finger_dip["y"] = self.right_middle_finger_dip_y
        self.right_middle_finger_tip["y"] = self.right_middle_finger_tip_y
        self.right_ring_finger_mcp["y"] = self.right_ring_finger_mcp_y
        self.right_ring_finger_pip["y"] = self.right_ring_finger_pip_y
        self.right_ring_finger_dip["y"] = self.right_ring_finger_dip_y
        self.right_ring_finger_tip["y"] = self.right_ring_finger_tip_y
        self.right_pinky_mcp["y"] = self.right_pinky_mcp_y
        self.right_pinky_pip["y"] = self.right_pinky_pip_y
        self.right_pinky_dip["y"] = self.right_pinky_dip_y
        self.right_pinky_tip["y"] = self.right_pinky_tip_y

        # 키포인트 > z
        self.left_shoulder["z"] = self.left_shoulder_z
        self.left_elbow["z"] = self.left_elbow_z
        self.left_wrist["z"] = self.left_wrist_z
        self.left_thumb_cmc["z"] = self.left_thumb_cmc_z
        self.left_thumb_mcp["z"] = self.left_thumb_mcp_z
        self.left_thumb_ip["z"] = self.left_thumb_ip_z
        self.left_thumb_tip["z"] = self.left_thumb_tip_z
        self.left_index_finger_mcp["z"] = self.left_index_finger_mcp_z
        self.left_index_finger_pip["z"] = self.left_index_finger_pip_z
        self.left_index_finger_dip["z"] = self.left_index_finger_dip_z
        self.left_index_finger_tip["z"] = self.left_index_finger_tip_z
        self.left_middle_finger_mcp["z"] = self.left_middle_finger_mcp_z
        self.left_middle_finger_pip["z"] = self.left_middle_finger_pip_z
        self.left_middle_finger_dip["z"] = self.left_middle_finger_dip_z
        self.left_middle_finger_tip["z"] = self.left_middle_finger_tip_z
        self.left_ring_finger_mcp["z"] = self.left_ring_finger_mcp_z
        self.left_ring_finger_pip["z"] = self.left_ring_finger_pip_z
        self.left_ring_finger_dip["z"] = self.left_ring_finger_dip_z
        self.left_ring_finger_tip["z"] = self.left_ring_finger_tip_z
        self.left_pinky_mcp["z"] = self.left_pinky_mcp_z
        self.left_pinky_pip["z"] = self.left_pinky_pip_z
        self.left_pinky_dip["z"] = self.left_pinky_dip_z
        self.left_pinky_tip["z"] = self.left_pinky_tip_z
        self.right_shoulder["z"] = self.right_shoulder_z
        self.right_elbow["z"] = self.right_elbow_z
        self.right_wrist["z"] = self.right_wrist_z
        self.right_thumb_cmc["z"] = self.right_thumb_cmc_z
        self.right_thumb_mcp["z"] = self.right_thumb_mcp_z
        self.right_thumb_ip["z"] = self.right_thumb_ip_z
        self.right_thumb_tip["z"] = self.right_thumb_tip_z
        self.right_index_finger_mcp["z"] = self.right_index_finger_mcp_z
        self.right_index_finger_pip["z"] = self.right_index_finger_pip_z
        self.right_index_finger_dip["z"] = self.right_index_finger_dip_z
        self.right_index_finger_tip["z"] = self.right_index_finger_tip_z
        self.right_middle_finger_mcp["z"] = self.right_middle_finger_mcp_z
        self.right_middle_finger_pip["z"] = self.right_middle_finger_pip_z
        self.right_middle_finger_dip["z"] = self.right_middle_finger_dip_z
        self.right_middle_finger_tip["z"] = self.right_middle_finger_tip_z
        self.right_ring_finger_mcp["z"] = self.right_ring_finger_mcp_z
        self.right_ring_finger_pip["z"] = self.right_ring_finger_pip_z
        self.right_ring_finger_dip["z"] = self.right_ring_finger_dip_z
        self.right_ring_finger_tip["z"] = self.right_ring_finger_tip_z
        self.right_pinky_mcp["z"] = self.right_pinky_mcp_z
        self.right_pinky_pip["z"] = self.right_pinky_pip_z
        self.right_pinky_dip["z"] = self.right_pinky_dip_z
        self.right_pinky_tip["z"] = self.right_pinky_tip_z

        # Translation > 키포인트
        self.trans["Character1_LeftArm"] = self.left_shoulder
        self.trans["Character1_LeftForeArm"] = self.left_elbow
        self.trans["Character1_LeftHand"] = self.left_wrist
        self.trans["Character1_LeftHandThumb1"] = self.left_thumb_cmc
        self.trans["Character1_LeftHandThumb2"] = self.left_thumb_mcp
        self.trans["Character1_LeftHandThumb3"] = self.left_thumb_ip
        self.trans["Character1_LeftHandThumb4"] = self.left_thumb_tip
        self.trans["Character1_LeftHandIndex1"] = self.left_index_finger_mcp
        self.trans["Character1_LeftHandIndex2"] = self.left_index_finger_pip
        self.trans["Character1_LeftHandIndex3"] = self.left_index_finger_dip
        self.trans["Character1_LeftHandIndex4"] = self.left_index_finger_tip
        self.trans["Character1_LeftHandMiddle1"] = self.left_middle_finger_mcp
        self.trans["Character1_LeftHandMiddle2"] = self.left_middle_finger_pip
        self.trans["Character1_LeftHandMiddle3"] = self.left_middle_finger_dip
        self.trans["Character1_LeftHandMiddle4"] = self.left_middle_finger_tip
        self.trans["Character1_LeftHandRing1"] = self.left_ring_finger_mcp
        self.trans["Character1_LeftHandRing2"] = self.left_ring_finger_pip
        self.trans["Character1_LeftHandRing3"] = self.left_ring_finger_dip
        self.trans["Character1_LeftHandRing4"] = self.left_ring_finger_tip
        self.trans["Character1_LeftHandPinky1"] = self.left_pinky_mcp
        self.trans["Character1_LeftHandPinky2"] = self.left_pinky_pip
        self.trans["Character1_LeftHandPinky3"] = self.left_pinky_dip
        self.trans["Character1_LeftHandPinky4"] = self.left_pinky_tip
        self.trans["Character1_RightArm"] = self.right_shoulder
        self.trans["Character1_RightForeArm"] = self.right_elbow
        self.trans["Character1_RightHand"] = self.right_wrist
        self.trans["Character1_RightHandThumb1"] = self.right_thumb_cmc
        self.trans["Character1_RightHandThumb2"] = self.right_thumb_mcp
        self.trans["Character1_RightHandThumb3"] = self.right_thumb_ip
        self.trans["Character1_RightHandThumb4"] = self.right_thumb_tip
        self.trans["Character1_RightHandIndex1"] = self.right_index_finger_mcp
        self.trans["Character1_RightHandIndex2"] = self.right_index_finger_pip
        self.trans["Character1_RightHandIndex3"] = self.right_index_finger_dip
        self.trans["Character1_RightHandIndex4"] = self.right_index_finger_tip
        self.trans["Character1_RightHandMiddle1"] = self.right_middle_finger_mcp
        self.trans["Character1_RightHandMiddle2"] = self.right_middle_finger_pip
        self.trans["Character1_RightHandMiddle3"] = self.right_middle_finger_dip
        self.trans["Character1_RightHandMiddle4"] = self.right_middle_finger_tip
        self.trans["Character1_RightHandRing1"] = self.right_ring_finger_mcp
        self.trans["Character1_RightHandRing2"] = self.right_ring_finger_pip
        self.trans["Character1_RightHandRing3"] = self.right_ring_finger_dip
        self.trans["Character1_RightHandRing4"] = self.right_ring_finger_tip
        self.trans["Character1_RightHandPinky1"] = self.right_pinky_mcp
        self.trans["Character1_RightHandPinky2"] = self.right_pinky_pip
        self.trans["Character1_RightHandPinky3"] = self.right_pinky_dip
        self.trans["Character1_RightHandPinky4"] = self.right_pinky_tip

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
        print("\n'locToRot()' Done...")

        self.setKeyframes()  # rotation -> keyframe animation
        print("'setKeyframes()' Done...")

    # json 파일을 읽고, Rotation 값을 구한 뒤, 리스트에 저장
    def locToRot(self):
        # json 파일을 읽고
        with open(self.data_path + "keypoint/" + self.json_name, 'r') as f:
            self.json_data = json.load(f)

        # json 파일을 읽고 프레임별로 Rotaion 값 구한 뒤, 리스트에 저장
        self.frames = self.json_data['frames']
        for i in range(self.frames+1):
            # Left-x
            #self.left_shoulder_x[i] = self.json_data['left_shoulder']['x'][str(i)]
            self.left_shoulder_x[i] = self.json_data['left_shoulder']['x'][str(i)] - \
                                      self.json_data['right_shoulder']['x'][str(i)]
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
            #self.right_shoulder_x[i] = self.json_data['right_shoulder']['x'][str(i)]
            self.right_shoulder_x[i] = self.json_data['right_shoulder']['x'][str(i)] - \
                                       self.json_data['left_shoulder']['x'][str(i)]
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
            #self.left_shoulder_y[i] = self.json_data['left_shoulder']['y'][str(i)]
            self.left_shoulder_y[i] = self.json_data['left_shoulder']['y'][str(i)] -\
                                      self.json_data['right_shoulder']['y'][str(i)]
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
            #self.right_shoulder_y[i] = self.json_data['right_shoulder']['y'][str(i)]
            self.right_shoulder_y[i] = self.json_data['right_shoulder']['y'][str(i)] -\
                                       self.json_data['left_shoulder']['y'][str(i)]
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
            #self.left_shoulder_z[i] = self.json_data['left_shoulder']['z'][str(i)]
            self.left_shoulder_z[i] = self.json_data['left_shoulder']['z'][str(i)] - \
                                      self.json_data['right_shoulder']['z'][str(i)]
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
            #self.right_shoulder_z[i] = self.json_data['right_shoulder']['z'][str(i)]
            self.right_shoulder_z[i] = self.json_data['right_shoulder']['z'][str(i)] - \
                                       self.json_data['left_shoulder']['z'][str(i)]
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

        # 범위를 넘는 값이 있을 경우 -9999값으로 통일
        for key in self.trans.keys():
            for loc in self.trans[key].keys():
                for j in range(self.frames+1):
                    if (self.trans[key][loc][j] > 1) or (self.trans[key][loc][j] < -1):
                        self.trans[key][loc][j] = -9999

    # Rotation 값이 저장된 배열을 가지고 키프레임 생성
    def setKeyframes(self):
        objs = cmds.ls(selection=True)  # ['Character1_Reference', 'Character1_Hips', ...] 이런식으로 불러옴

        # 마야 내의 오브젝트들 중에서
        for obj in objs:
            # normalized value -> proper value
            xalpha = 50
            yalpha = 49
            zalpha = 10
            falpha = 1  # frame alpha value

            # Translation의 키값과 일치하는 것이 있으면
            if obj in self.trans.keys():
                num = self.annotations.index(obj)

                # Translate 1
                if obj == 'Character1_LeftArm':
                    continue
                elif obj == 'Character1_RightArm':
                    continue
                elif obj == 'Character1_LeftHand' or obj == 'Character1_RightHand':
                    for frame in range(self.frames+1):
                        if (self.trans[obj]['x'][frame] == -9999) or (self.trans[obj]['y'][frame] == -9999) or (self.trans[obj]['z'][frame] == -9999):
                            continue
                        else:
                            cmds.setKeyframe(obj + '.translateX', value=self.trans[obj]['x'][frame]*xalpha, time=frame*falpha)
                            cmds.setKeyframe(obj + '.translateY', value=-self.trans[obj]['y'][frame]*yalpha, time=frame*falpha)
                            cmds.setKeyframe(obj + '.translateZ', value=-self.trans[obj]['z'][frame]*zalpha, time=frame*falpha)
                            #print(obj, "[", frame, "]: (",
                            #      self.trans[obj]['x'][frame]*xalpha, ", ",
                            #      -self.trans[obj]['y'][frame] * yalpha, ", ",
                            #      -self.trans[obj]['z'][frame] * zalpha, ")")
                else:
                    for frame in range(self.frames+1):
                        if (self.trans[obj]['x'][frame] == -9999) or (self.trans[obj]['y'][frame] == -9999) or (self.trans[obj]['z'][frame] == -9999):
                            continue
                        else:
                            cmds.setKeyframe(obj + '.translateX', value=self.trans[obj]['x'][frame]*xalpha, time=frame*falpha)
                            cmds.setKeyframe(obj + '.translateY', value=-self.trans[obj]['y'][frame]*yalpha, time=frame*falpha)
                            cmds.setKeyframe(obj + '.translateZ', value=self.trans[obj]['z'][frame]*zalpha, time=frame*falpha)
                            #print(obj, "[", frame, "]: (",
                            #      self.trans[obj]['x'][frame] * xalpha, ", ",
                            #      -self.trans[obj]['y'][frame] * yalpha, ", ",
                            #      self.trans[obj]['z'][frame] * zalpha, ")")

                '''
                # Rotate 1
                if 'RightArm' in obj:
                    for frame in range(30):
                        #self.frames+1:
                        if (self.trans[obj]['x'][frame] == -9999) or (self.trans[obj]['y'][frame] == -9999) or (self.trans[obj]['z'][frame] == -9999):
                            continue
                        else:
                            rotX = math.degrees(math.atan2(-self.trans[obj]['y'][frame]*yalpha , self.trans[obj]['z'][frame]*zalpha))
                            rotY = math.degrees(math.atan2(-self.trans[obj]['z'][frame]*zalpha , self.trans[obj]['x'][frame]*xalpha))
                            rotZ = math.degrees(math.atan2(-self.trans[obj]['x'][frame]*xalpha , self.trans[obj]['y'][frame]*yalpha))
                            cmds.setKeyframe(obj + '.rotateX', value=rotX, time=frame*falpha)
                            cmds.setKeyframe(obj + '.rotateY', value=rotY, time=frame*falpha)
                            cmds.setKeyframe(obj + '.rotateZ', value=-rotZ, time=frame*falpha)
                else:
                    for frame in range(30):
                        #self.frames+1:
                        if (self.trans[obj]['x'][frame] == -9999) or (self.trans[obj]['y'][frame] == -9999) or (self.trans[obj]['z'][frame] == -9999):
                            continue
                        else:
                            rotX = math.degrees(math.atan2(-self.trans[obj]['y'][frame]*yalpha , self.trans[obj]['z'][frame]*zalpha))
                            rotY = math.degrees(math.atan2(-self.trans[obj]['z'][frame]*zalpha , self.trans[obj]['x'][frame]*xalpha))
                            rotZ = math.degrees(math.atan2(-self.trans[obj]['x'][frame]*xalpha , self.trans[obj]['y'][frame]*yalpha))
                            cmds.setKeyframe(obj + '.rotateX', value=rotX, time=frame*falpha)
                            cmds.setKeyframe(obj + '.rotateY', value=rotY, time=frame*falpha)
                            cmds.setKeyframe(obj + '.rotateZ', value=rotZ, time=frame*falpha)
                '''
                '''
                # Rotate 2
                if obj == 'Character1_LeftArm':
                    continue
                elif obj == 'Character1_RightArm':
                    continue
                elif 'Thumb1' in obj or 'Index1' in obj or 'Middle1' in obj or 'Ring1' in obj or 'Pinky1' in obj:
                    continue
                else:
                    if 'Left' in obj:
                        for frame in range(self.frames+1):
                            if (self.trans[obj]['x'][frame] == -9999) or (self.trans[obj]['y'][frame] == -9999) or (self.trans[obj]['z'][frame] == -9999):
                                continue
                            else:
                                rotZ = math.atan2(-self.trans[obj]['x'][frame]*xalpha, self.trans[obj]['y'][frame]*yalpha)
                                rotZ = (rotZ*180)/math.pi
                                cmds.setKeyframe(self.annotations[num-1] + '.rotateZ', value=rotZ, time=frame*falpha)
                                #print(self.annotations[num-1], " [", frame, "] : ", rotZ)
                                #rotX = math.degrees(math.atan(self.trans[obj]['y'][frame] * yalpha))
                                #rotY = math.degrees(math.atan(self.trans[obj]['x'][frame] * xalpha))
                                #rotX = math.degrees(math.atan2(self.trans[obj]['y'][frame] * yalpha, -self.trans[obj]['z'][frame] * zalpha))
                                #rotY = math.degrees(math.atan2(self.trans[obj]['z'][frame] * zalpha, self.trans[obj]['x'][frame] * xalpha))
                                #rotZ = math.degrees(math.atan2(-self.trans[obj]['x'][frame] * xalpha, -self.trans[obj]['y'][frame] * yalpha))
                                #cmds.setKeyframe(self.annotations[num-1] + '.rotateX', value=rotX, time=frame * falpha)
                                #cmds.setKeyframe(self.annotations[num-1] + '.rotateY', value=rotY, time=frame * falpha)
                                #cmds.setKeyframe(self.annotations[num-1] + '.rotateZ', value=rotZ, time=frame * falpha)

                                #print(self.annotations[num-1], " [", frame, "] : ", rotX, ", ", rotY)#, ", ", rotZ)
                    else:
                        # self.frames+1
                        for frame in range(self.frames+1):
                            if (self.trans[obj]['x'][frame] == -9999) or (self.trans[obj]['y'][frame] == -9999) or (self.trans[obj]['z'][frame] == -9999):
                                continue
                            else:
                                rotZ = math.atan2(-self.trans[obj]['x'][frame] * xalpha, self.trans[obj]['y'][frame] * yalpha)
                                rotZ = (rotZ * 180) / math.pi
                                cmds.setKeyframe(self.annotations[num-1] + '.rotateZ', value=rotZ, time=frame * falpha)
                                #print(self.annotations[num - 1], " [", frame, "] : ", rotZ)
                                #rotX = math.degrees(math.atan(self.trans[obj]['y'][frame] * yalpha))
                                #rotY = math.degrees(math.atan(self.trans[obj]['x'][frame] * xalpha))
                                #rotX = math.degrees(math.atan2(self.trans[obj]['y'][frame] * yalpha, self.trans[obj]['z'][frame] * zalpha))
                                #rotY = math.degrees(math.atan2(-self.trans[obj]['z'][frame] * zalpha, self.trans[obj]['x'][frame] * xalpha))
                                #rotZ = math.degrees(math.atan2(-self.trans[obj]['x'][frame] * xalpha, -self.trans[obj]['y'][frame] * yalpha))
                                #cmds.setKeyframe(self.annotations[num-1] + '.rotateX', value=rotX, time=frame * falpha)
                                #cmds.setKeyframe(self.annotations[num-1] + '.rotateY', value=rotY, time=frame * falpha)
                                #cmds.setKeyframe(self.annotations[num-1] + '.rotateZ', value=-rotZ, time=frame * falpha)

                                #print(self.annotations[num-1], " [", frame, "] : ", rotX, ", ", rotY)#, ", ", rotZ)
                '''

start_time = time.time()
jtm = jsonToMaya()
jtm.excute()
end_time = time.time()
print("total_time: ", end_time - start_time, " sec")
