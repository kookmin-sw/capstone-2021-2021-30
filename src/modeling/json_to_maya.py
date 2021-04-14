import maya.cmds as cmds
import json, math

def setKeyframes():
    objs = cmds.ls(selection=True)  # ['Character1_Reference'] 형식
    json_data = readJson('0.json')  # json 읽고
    
    # 선택한 오브젝트 중
    for obj in objs:
        alpha = 75
        falpha = 10
        trans = []
        rot = []
        frames = json_data['frames']

        if obj in json_data:
            for frame in range(1, frames+1):
                if str(frame) in json_data[obj]['x']:
                    xVal = json_data[obj]['x'][str(frame)]
                    yVal = json_data[obj]['y'][str(frame)]
                    zVal = json_data[obj]['z'][str(frame)]
                    
                    # 양 어깨는 그 전의 좌표를 통해 translation을 구할 수 없음
                    if obj == 'Character1_LeftArm':
                        xVal = 10.707
                        yVal = 0
                        zVal = 0
                        xRot = -13.77
                        yRot = 16.044
                        zRot = 5.257
                        cmds.setKeyframe(obj + '.translateX', value=xVal, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateY', value=yVal, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateZ', value=zVal, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateX', value=xRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateY', value=yRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateZ', value=zRot, time=frame*falpha) 
                    elif obj == 'Character1_RightArm':
                        xVal = -10.707
                        yVal = 0
                        zVal = 0
                        xRot = 13.77
                        yRot = 16.044
                        zRot = 5.257
                        cmds.setKeyframe(obj + '.translateX', value=xVal, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateY', value=yVal, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateZ', value=zVal, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateX', value=xRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateY', value=yRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateZ', value=zRot, time=frame*falpha)
                    
                    # 팔꿈치 기본 방향    
                    elif obj == 'Character1_LeftForeArm':
                        xRot = -17.5
                        yRot = 4.75
                        zRot = 48.5
                        cmds.setKeyframe(obj + '.rotateX', value=xRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateY', value=yRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateZ', value=zRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateX', value=xVal*alpha, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateY', value=yVal*alpha, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateZ', value=-zVal*alpha, time=frame*falpha)
                    elif obj == 'Character1_RightForeArm':
                        xRot = 17.5
                        yRot = -4.75
                        zRot = -48.5
                        cmds.setKeyframe(obj + '.rotateX', value=xRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateY', value=yRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.rotateZ', value=zRot, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateX', value=xVal*alpha, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateY', value=yVal*alpha, time=frame*falpha)
                        cmds.setKeyframe(obj + '.translateZ', value=-zVal*alpha, time=frame*falpha)
                        
                    # 손이 안보이는 경우 밑으로 향하게
                    elif obj == 'Character1_LeftHand':
                        if xVal == 1234:
                            xRot = 28 #16
                            cmds.setKeyframe(obj + '.rotateX', value=xRot, time=frame*falpha)
                        else:
                            cmds.setKeyframe(obj + '.translateX', value=-xVal*alpha, time=frame*falpha)
                        if yVal == 1234:
                            yRot = -20.5 #4.5
                            cmds.setKeyframe(obj + '.rotateY', value=yRot, time=frame*falpha)
                        else:
                            cmds.setKeyframe(obj + '.translateY', value=yVal*alpha, time=frame*falpha)
                        if zVal == 1234:
                            zRot = -37.5 #-100
                            cmds.setKeyframe(obj + '.rotateZ', value=zRot, time=frame*falpha)
                        else:
                            cmds.setKeyframe(obj + '.translateZ', value=zVal*alpha, time=frame*falpha)
                    elif obj == 'Character1_RightHand':
                        if xVal == 1234:
                            xRot = -28 #-16
                            cmds.setKeyframe(obj + '.rotateX', value=xRot, time=frame*falpha)
                        else:
                            cmds.setKeyframe(obj + '.translateX', value=-xVal*alpha, time=frame*falpha)
                        if yVal == 1234:
                            yRot = 20.5 #-4.5
                            cmds.setKeyframe(obj + '.rotateY', value=yRot, time=frame*falpha)
                        else:
                            cmds.setKeyframe(obj + '.translateY', value=yVal*alpha, time=frame*falpha)
                        if zVal == 1234:
                            zRot = 37.5 #100
                            cmds.setKeyframe(obj + '.rotateZ', value=zRot, time=frame*falpha)
                        else:
                            cmds.setKeyframe(obj + '.translateZ', value=zVal*alpha, time=frame*falpha)
                            
                    else:
                        if xVal != 1234:
                            cmds.setKeyframe(obj + '.translateX', value=xVal*alpha, time=frame*falpha)
                        if yVal != 1234:
                            cmds.setKeyframe(obj + '.translateY', value=yVal*alpha, time=frame*falpha)
                        if zVal != 1234:
                            cmds.setKeyframe(obj + '.translateZ', value=-zVal*alpha, time=frame*falpha)
          
        else:
            for frame in range(1, frames + 1):
                trans = cmds.getAttr(obj + '.translate')
                rot = cmds.getAttr(obj + '.rotate')

                cmds.setKeyframe(obj + '.translateX', value=trans[0][0], time=frame*falpha)
                cmds.setKeyframe(obj + '.translateY', value=trans[0][1], time=frame*falpha)
                cmds.setKeyframe(obj + '.translateZ', value=trans[0][2], time=frame*falpha)
                cmds.setKeyframe(obj + '.rotateX', value=rot[0][0], time=frame*falpha)
                cmds.setKeyframe(obj + '.rotateY', value=rot[0][1], time=frame*falpha)
                cmds.setKeyframe(obj + '.rotateZ', value=rot[0][2], time=frame*falpha)

def initPosition():
    '''
    cmds.setKeyframe("Character1_LeftArm.translateX", value=10.707, time=0)
    cmds.setKeyframe("Character1_LeftArm.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftArm.translateZ", value=0, time=0)
    cmds.setKeyframe("Character1_LeftArm.rotateX", value=0, time=0)
    cmds.setKeyframe("Character1_LeftArm.rotateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftArm.rotateZ", value=0, time=0)

    cmds.setKeyframe("Character1_RightArm.translateX", value=-10.707, time=0)
    cmds.setKeyframe("Character1_RightArm.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_RightArm.translateZ", value=-0, time=0)
    cmds.setKeyframe("Character1_RightArm.rotateX", value=0, time=0)
    cmds.setKeyframe("Character1_RightArm.rotateY", value=0, time=0)
    cmds.setKeyframe("Character1_RightArm.rotateZ", value=0, time=0)
    '''
    cmds.setKeyframe("Character1_LeftArm.translateX", value=10.707, time=0)
    cmds.setKeyframe("Character1_LeftArm.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftArm.translateZ", value=0, time=0)
    #cmds.setKeyframe("Character1_LeftArm.rotate", 10, -6, -75)
    cmds.setKeyframe("Character1_LeftForeArm.translateX", value=27.305, time=0)
    cmds.setKeyframe("Character1_LeftForeArm.translateY", value=0.001, time=0)
    cmds.setKeyframe("Character1_LeftForeArm.translateZ", value=0, time=0)

    cmds.setKeyframe("Character1_LeftHand.translateX", value=26.697, time=0)
    cmds.setKeyframe("Character1_LeftHand.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftHand.translateZ", value=0, time=0)

    cmds.setKeyframe("Character1_LeftHandThumb1.translateX", value=4.349, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb1.translateY", value=-0.799, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb1.translateZ", value=4.282, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb2.translateX", value=2.513, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb2.translateY", value=-0.536, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb2.translateZ", value=0.707, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb3.translateX", value=2.543, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb3.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb3.translateZ", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb4.translateX", value=2.677, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb4.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftHandThumb4.translateZ", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex1.translateX", value=8.822, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex1.translateY", value=0.2, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex1.translateZ", value=3.472, time=0)

    #cmds.setKeyframe("Character1_LeftHandIndex1.rotate", 0, -2, -0)
    cmds.setKeyframe("Character1_LeftHandIndex2.translateX", value=4.225, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex2.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex2.translateZ", value=-0, time=0)
    #cmds.setKeyframe("Character1_LeftHandIndex2.rotate", 0, -2, -0)
    cmds.setKeyframe("Character1_LeftHandIndex3.translateX", value=2.647, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex3.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex3.translateZ", value=0.185, time=0)
    #cmds.setKeyframe("Character1_LeftHandIndex3.rotate", 0, -2, -0)
    cmds.setKeyframe("Character1_LeftHandIndex4.translateX", value=1.957, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex4.translateY", value=-0, time=0)
    cmds.setKeyframe("Character1_LeftHandIndex4.translateZ", value=0.068, time=0)
    #cmds.setKeyframe("Character1_LeftHandIndex4.rotate", 0, -2, -0)
    cmds.setKeyframe("Character1_LeftHandMiddle1.translateX", value=8.81, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle1.translateY", value=0.501, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle1.translateZ", value=1.305, time=0)

    #cmds.setKeyframe("Character1_LeftHandMiddle1.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandMiddle2.translateX", value=4.863, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle2.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle2.translateZ", value=0, time=0)
    #cmds.setKeyframe("Character1_LeftHandMiddle2.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandMiddle3.translateX", value=2.7650, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle3.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle3.translateZ", value=0, time=0)
    #cmds.setKeyframe("Character1_LeftHandMiddle3.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandMiddle4.translateX", value=2.006, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle4.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandMiddle4.translateZ", value=0, time=0)

    #cmds.setKeyframe("Character1_LeftHandMiddle4.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandRing1.translateX", value=8.894, time=0)
    cmds.setKeyframe("Character1_LeftHandRing1.translateY", value=0.38, time=0)
    cmds.setKeyframe("Character1_LeftHandRing1.translateZ", value=-0.793, time=0)
    #cmds.setKeyframe("Character1_LeftHandRing1.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandRing2.translateX", value=4.538, time=0)
    cmds.setKeyframe("Character1_LeftHandRing2.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandRing2.translateZ", value=-0, time=0)
    #cmds.setKeyframe("Character1_LeftHandRing2.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandRing3.translateX", value=2.305, time=0)
    cmds.setKeyframe("Character1_LeftHandRing3.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandRing3.translateZ", value=0, time=0)

    #cmds.setKeyframe("Character1_LeftHandRing3.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandRing4.translateX", value=1.923, time=0)
    cmds.setKeyframe("Character1_LeftHandRing4.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandRing4.translateZ", value=-0, time=0)
    #cmds.setKeyframe("Character1_LeftHandRing4.rotate", 0, -0.004, -0)
    cmds.setKeyframe("Character1_LeftHandPinky1.translateX", value=8.882, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky1.translateY", value=-0.313, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky1.translateZ", value=-2.49, time=0)
    #cmds.setKeyframe("Character1_LeftHandPinky1.rotate", 0, 0, 0.001)
    cmds.setKeyframe("Character1_LeftHandPinky2.translateX", value=3.044, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky2.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky2.translateZ", value=0, time=0)
    #cmds.setKeyframe("Character1_LeftHandPinky2.rotate", 0, 0, 0.001)
    cmds.setKeyframe("Character1_LeftHandPinky3.translateX", value=1.975, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky3.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky3.translateZ", value=-0, time=0)
    #cmds.setKeyframe("Character1_LeftHandPinky3.rotate", 0, 0, 0.001)
    cmds.setKeyframe("Character1_LeftHandPinky4.translateX", value=1.667, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky4.translateY", value=0, time=0)
    cmds.setKeyframe("Character1_LeftHandPinky4.translateZ", value=0, time=0)
    #cmds.setKeyframe("Character1_LeftHandPinky4.rotate", 0, 0, 0.001)

    '''
    cmds.setKeyframe("Character1_RightArm.translate", -10.707, 0, -0)
    cmds.setKeyframe("Character1_RightArm.rotate", -10, 6, 75)
    cmds.setKeyframe("Character1_RightForeArm.translate", -27.305, -0.001, -0)
    cmds.setKeyframe("Character1_RightHand.translate", -26.697, 0, -0)
    cmds.setKeyframe("Character1_RightHandThumb1.translate", -4.349, 0.799, -4.282)
    cmds.setKeyframe("Character1_RightHandThumb2.translate", -2.513, 0.536, -0.707)
    cmds.setKeyframe("Character1_RightHandThumb3.translate", -2.543, -0, -0)
    cmds.setKeyframe("Character1_RightHandThumb4.translate", -2.677, 0, 0)
    cmds.setKeyframe("Character1_RightHandIndex1.translate", -8.822, -0.2, -3.472)
    cmds.setKeyframe("Character1_RightHandIndex1.rotate", -0, 2, 0)
    cmds.setKeyframe("Character1_RightHandIndex2.translate", -4.225, 0, 0)
    cmds.setKeyframe("Character1_RightHandIndex2.rotate", -0, 2, 0)
    cmds.setKeyframe("Character1_RightHandIndex3.translate", -2.647, 0, -0.185)
    cmds.setKeyframe("Character1_RightHandIndex3.rotate", -0, 2, 0)
    cmds.setKeyframe("Character1_RightHandIndex4.translate", -1.957, 0, -0.068)
    cmds.setKeyframe("Character1_RightHandIndex4.rotate", -0, 2, 0)
    cmds.setKeyframe("Character1_RightHandMiddle1.translate", -8.81, -0.501, -1.305)
    cmds.setKeyframe("Character1_RightHandMiddle1.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandMiddle2.translate", -4.863, -0, -0)
    cmds.setKeyframe("Character1_RightHandMiddle2.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandMiddle3.translate", -2.765, -0, -0)
    cmds.setKeyframe("Character1_RightHandMiddle3.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandMiddle4.translate", -2.006, -0, -0)
    cmds.setKeyframe("Character1_RightHandMiddle4.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandRing1.translate", -8.894, -0.38, 0.793)
    cmds.setKeyframe("Character1_RightHandRing1.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandRing2.translate", -4.538, -0, 0)
    cmds.setKeyframe("Character1_RightHandRing2.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandRing3.translate", -2.305, -0, -0)
    cmds.setKeyframe("Character1_RightHandRing3.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandRing4.translate", -1.923, -0, 0)
    cmds.setKeyframe("Character1_RightHandRing4.rotate", -0, 0.004, 0)
    cmds.setKeyframe("Character1_RightHandPinky1.translate", -8.882, 0.313, 2.49)
    cmds.setKeyframe("Character1_RightHandPinky1.rotate", -0, -0, -0.001)
    cmds.setKeyframe("Character1_RightHandPinky2.translate", -3.044, -0, -0)
    cmds.setKeyframe("Character1_RightHandPinky2.rotate", -0, -0, -0.001)
    cmds.setKeyframe("Character1_RightHandPinky3.translate", -1.975, -0, 0)
    cmds.setKeyframe("Character1_RightHandPinky3.rotate", -0, -0, -0.001)
    cmds.setKeyframe("Character1_RightHandPinky4.translate", -1.667, -0, -0)
    cmds.setKeyframe("Character1_RightHandPinky4.rotate", -0, -0, -0.001)
    '''

def readJson(json_name):
    json_path = 'D:/Workspace/GitHub/capstone-2021-2021-30/capston_db/motion_data_file/' + json_name
    #json_path = '../motion_data_file/' + json_name
    
    with open(json_path, 'r') as f:
        json_data = json.load(f)
       
    return json_data
   
#initPosition()
setKeyframes()