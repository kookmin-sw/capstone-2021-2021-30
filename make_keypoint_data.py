import json
import numpy as np
import math
def make_keypoint_data():
    motions = ["left_shoulder", "left_elbow", "right_shoulder", "right_elbow", "left_wrist", "left_thumb_cmc",
               "left_thumb_mcp", "left_thumb_ip", "left_thumb_tip", "left_index_finger_mcp", "left_index_finger_pip",
               "left_index_finger_dip", "left_index_finger_tip", "left_middle_finger_mcp", "left_middle_finger_pip",
               "left_middle_finger_dip", "left_middle_finger_tip", "left_ring_finger_mcp", "left_ring_finger_pip",
               "left_ring_finger_dip", "left_ring_finger_tip", "left_pinky_mcp", "left_pinky_pip", "left_pinky_dip",
               "left_pinky_tip", "right_wrist", "right_thumb_cmc", "right_thumb_mcp", "right_thumb_ip", "right_thumb_tip",
               "right_index_finger_mcp", "right_index_finger_pip", "right_index_finger_dip", "right_index_finger_tip",
               "right_middle_finger_mcp", "right_middle_finger_pip", "right_middle_finger_dip", "right_middle_finger_tip",
               "right_ring_finger_mcp", "right_ring_finger_pip", "right_ring_finger_dip", "right_ring_finger_tip",
               "right_pinky_mcp", "right_pinky_pip", "right_pinky_dip", "right_pinky_tip"]

    with open("keypoint(20frame).json") as f:
        datas = json.load(f)

    res = [[] for _ in range(1697)]
    #res = [[]for _ in range(423)]
    i = 0
    for lst in res:
        for motion in motions:
            idx = str(i)
            if idx not in datas[motion]["x"]: datas[motion]["x"][idx] = 0
            if idx not in datas[motion]["y"]: datas[motion]["y"][idx] = 0
            if idx not in datas[motion]["z"]: datas[motion]["z"][idx] = 0
            if datas[motion]["x"][idx] == -9999: datas[motion]["x"][idx] = 0
            if datas[motion]["y"][idx] == -9999: datas[motion]["y"][idx] = 0
            if datas[motion]["z"][idx] == -9999: datas[motion]["z"][idx] = 0
            # lst.append(round(datas[motion]["x"][idx],13))
            # lst.append(round(datas[motion]["y"][idx],13))
            # lst.append(round(datas[motion]["z"][idx],13))
            lst.append(int(round(datas[motion]["x"][idx],1)*10))
            lst.append(int(round(datas[motion]["y"][idx],1)*10))
            lst.append(int(round(datas[motion]["z"][idx],1)*10))
        i+=1
    labels = []
    for lst in res:
      labels.extend(lst)
    
    return labels
