
import msgpack

try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')

    # Now try to retrieve data in a blocking fashion (i.e. a service call):
    res,objs=sim.simxGetObjects(clientID,sim.sim_handle_all,sim.simx_opmode_blocking)
    if res==sim.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
    else:
        print ('Remote API function call returned with error code: ',res)

    time.sleep(2)

    sim.simxAddStatusbarMessage(clientID,'Hello CoppeliaSim!',sim.simx_opmode_oneshot)
    sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL2", sim.sim_scripttype_childscript, 'headToGoal', [1,2], [],
                               [], "msgpack.packb([])", sim.simx_opmode_blocking)

    res, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL2",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)
        # 这里是检测小车是否到达目标，如果到达，会返回1，没到就是0
    while retInts[0]==0:
        res, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL2",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)
    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    
    sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL", sim.sim_scripttype_childscript, 'headToGoal', [7], [],
                               [], "msgpack.packb([])", sim.simx_opmode_blocking)
    sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL1", sim.sim_scripttype_childscript, 'headToGoal', [5], [],
                               [], "msgpack.packb([])", sim.simx_opmode_blocking)
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_oneshot)
    res2, retInts2, retFloats2, retStrings2, retBuffer2 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL1",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_oneshot)                                                                                    
        # 这里是检测小车是否到达目标，如果到达，会返回1，没到就是0
    while retInts1[0]==0 or retInts2[0]==0:
        res1, retInts1, retFloats1, retStrings1, retBuffer1 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_oneshot)
        res2, retInts2, retFloats2, retStrings2, retBuffer2 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL1",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_oneshot)

    sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL", sim.sim_scripttype_childscript, 'headToGoal', [4], [],
                               [], "msgpack.packb([])", sim.simx_opmode_blocking)
    sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL1", sim.sim_scripttype_childscript, 'headToGoal', [6], [],
                               [], "msgpack.packb([])", sim.simx_opmode_blocking)
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)
    res2, retInts2, retFloats2, retStrings2, retBuffer2 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL1",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)                                                                                    
        # 这里是检测小车是否到达目标，如果到达，会返回1，没到就是0
    while retInts1[0]==0 or retInts2[0]==0 :
        res1, retInts1, retFloats1, retStrings1, retBuffer1 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)
        res2, retInts2, retFloats2, retStrings2, retBuffer2 = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL1",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)

    sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL2", sim.sim_scripttype_childscript, 'headToGoal', [3], [],
                               [], "msgpack.packb([])", sim.simx_opmode_blocking)

    res, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL2",
                                                                                    sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)
        # 这里是检测小车是否到达目标，如果到达，会返回1，没到就是0
    while retInts[0]==0:
        res, retInts, retFloats, retStrings, retBuffer = sim.simxCallScriptFunction(clientID, "Robotnik_Summit_XL2",
     
    ##                                                                               sim.sim_scripttype_childscript,
                                                                                    'HasArrived',
                                                                                    [], [], [], "msgpack.packb([])",
                                                                                    sim.simx_opmode_blocking)                                                                                                                                                                        
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
