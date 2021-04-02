import maya.cmds as cmds
import json

def setKeyframes():
    objs = cmds.ls(selection=True)  # ['Character1_Reference'] 형식
    json_data = readJson('0.json')  # json 읽고
    
    # 선택한 오브젝트 중
    for obj in objs:
        #print(obj)
        
        # json에 있는 오브젝트일 경우
        if obj in json_data:
            frames = json_data['frames']
            for frame in range(1, frames+1):
                if str(frame) in json_data[obj]['x']:
                    if (obj == 'Character1_LeftArm') or (obj == 'Character1_RightArm'): 
                        xVal = json_data[obj]['x'][str(frame)]
                        yVal = json_data[obj]['y'][str(frame)]
                        zVal = json_data[obj]['z'][str(frame)]
                    else:
                        xVal = json_data[obj]['x'][str(frame)] * 500
                        yVal = json_data[obj]['y'][str(frame)] * 500
                        zVal = json_data[obj]['z'][str(frame)] * 500
                        
                    cmds.setKeyframe(obj + '.translateX', value=xVal, time=frame*10)
                    cmds.setKeyframe(obj + '.translateY', value=yVal, time=frame*10)
                    cmds.setKeyframe(obj + '.translateZ', value=zVal, time=frame*10)
     
def readJson(json_name):
    json_path = 'D:/Workspace/GitHub/capstone-2021-2021-30/capston_db/motion_data_file/' + json_name
    #json_path = '../motion_data_file/' + json_name
    
    with open(json_path, 'r') as f:
        json_data = json.load(f)
       
    return json_data
    
setKeyframes()