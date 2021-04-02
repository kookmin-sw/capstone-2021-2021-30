import maya.cmds as cmds

def setKeyframes():
    objs = cmds.ls(selection=True)  # ['Character1_Reference'] 형식
    obj = objs[0]
    '''
    for obj in objs:
        print(obj)
    '''
    
    
    xVal = 0
    yVal = 0
    zVal = 0
    frame = 0
    maxVal = 0
    
    for i in range(0, 20):
        frame = i * 10
        xVal = i * 2
        if i % 2 == 1:
            yVal = 0
        else:
            yVal = maxVal
            maxVal *= 0.8
            
        cmds.setKeyframe(obj + '.translateX', value=xVal, time=frame)
        cmds.setKeyframe(obj + '.translateX', value=yVal, time=frame)
        cmds.setKeyframe(obj + '.translateX', value=zVal, time=frame)
        
setKeyframes()