# #!/usr/bin/python
#
# # This Python script has been generated by the SKYDEL GNSS simulator
import time
import skydelsdx
from skydelsdx.commands import New
from skydelsdx.commands import GetSimulationElapsedTime
from skydelsdx.commands import SetModulationTarget
from skydelsdx.commands import ChangeModulationTargetSignals
import math
import datetime
import random
from skydelsdx import *
from skydelsdx.commands import *

sim = RemoteSimulator(True)

sim.connect()

sim.call(New(True))
sim.call(SetModulationTarget("DTA-2115B", "", "", True, "{2fcda393-2daa-49c5-bc02-455acd5e610e}"))
sim.call(ChangeModulationTargetSignals(0, 25000000, 85000000, "UpperL", "L1CA", 50, True,
                                       "{2fcda393-2daa-49c5-bc02-455acd5e610e}", None))
sim.call(SetVehicleTrajectory("Route"))
sim.call(Open("test_multipath.sdx", True))

sim.start()

elapsedTime = sim.call(GetSimulationElapsedTime())
time_seconds = elapsedTime.milliseconds() // 1000
formattedTime = datetime.timedelta(seconds=elapsedTime.milliseconds() // 1000)
# print("Simulation Elapsed Time: " + str(formattedTime))
# print(time_seconds)

elevation_mask_0 = 0  # (20 * math.pi) / 180
elevation_mask_1 = 25  # (40 * math.pi) / 180
elevation_mask_2 = 45  # (40 * math.pi) / 180

# print(elevation_mask_1, elevation_mask_2, elevation_mask_3)

result1 = sim.call(GetElevationAzimuthForSV("GPS", 1))
result2 = sim.call(GetElevationAzimuthForEachSV("GPS"))
# result3 = sim.call(GetElevationAzimuthForEachSVResult("GPS"))
# print(result1.getRelatedCommand().toString() + ": " + result1.getMessage())
# print(result2.getRelatedCommand().toString() + ": " + result2.getMessage())

time_0 = 0
time_1 = 180000  # (3 minutes)
time_2 = 240000  # ( 2 minutes)
time_3 = 300000  # ( 2 minutes)
time_4 = 360000  # (2 minutes)
time_5 = 480000  # (2 minutes)
list_id = []
while True:

    """if sim.call(GetSimulationElapsedTime()).milliseconds() >= time_0:  # 2 minutes OPEN SKY
    #
    #     # Get the list of all visible satellite
    #     visibles = sim.call(GetVisibleSV("GPS"))
    """

    if sim.call(GetSimulationElapsedTime()).milliseconds() >= time_1:  # 3 minutes

        # Get the list of all visible satellite

        """  Desable LOS of satellites below 25 evelation"""

        visibles = sim.call(GetVisibleSV("GPS"))

        for svId in visibles.svId():  # Echo and LOS

            # Get the power of that satellite
            el_az = sim.call(GetElevationAzimuthForSV("GPS", svId))
            el_az_func = el_az.elevationAzimuth()
            el = el_az_func['Elevation']
            az = el_az_func['Azimuth']
            el_eg = (el * 180) / math.pi

            if el_eg <= elevation_mask_1:

                pseu_1 = random.randint(1, 50)
                pseu_2 = random.randint(25, 75)
                pseu_3 = random.randint(50, 100)
                pseu_4 = random.randint(75, 150)

                sim.call(EnableLosForSV("GPS", svId, False))

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))

            else:

                pseu_1 = random.randint(1, 50)
                pseu_2 = random.randint(25, 75)

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))



    if sim.call(GetSimulationElapsedTime()).milliseconds() >= time_2:

        # Get the list of all visible satellite

        """  Desable LOS of satellites below 25 evelation"""

        visibles = sim.call(GetVisibleSV("GPS"))

        for svId in visibles.svId():  # Echo and LOS

            # Get the power of that satellite
            el_az = sim.call(GetElevationAzimuthForSV("GPS", svId))
            el_az_func = el_az.elevationAzimuth()
            el = el_az_func['Elevation']
            az = el_az_func['Azimuth']
            el_eg = (el * 180) / math.pi

            if el_eg <= elevation_mask_1:

                pseu_1 = random.randint(50, 200)
                pseu_2 = random.randint(75, 225)
                pseu_3 = random.randint(100, 250)
                pseu_4 = random.randint(125, 250)

                sim.call(EnableLosForSV("GPS", svId, False))

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))

            elif el_eg >= elevation_mask_1 and el_eg <= elevation_mask_2:
                pseu_1 = random.randint(50, 150)
                pseu_2 = random.randint(75, 175)
                pseu_3 = random.randint(100, 200)
                pseu_4 = random.randint(125, 200)

                sim.call(EnableLosForSV("GPS", svId, False))

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))

            else:

                pseu_1 = random.randint(50, 150)
                pseu_2 = random.randint(75, 175)
                pseu_3 = random.randint(100, 200)
                pseu_4 = random.randint(125, 200)

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))


    if sim.call(GetSimulationElapsedTime()).milliseconds() >= time_3:  # 3 minutes


        # Get the list of all visible satellite

        """  Desable LOS of satellites below 25 evelation"""

        visibles = sim.call(GetVisibleSV("GPS"))

        for svId in visibles.svId():  # Echo and LOS

            # Get the power of that satellite
            el_az = sim.call(GetElevationAzimuthForSV("GPS", svId))
            el_az_func = el_az.elevationAzimuth()
            el = el_az_func['Elevation']
            az = el_az_func['Azimuth']
            el_eg = (el * 180) / math.pi

            if el_eg <= elevation_mask_1:

                pseu_1 = random.randint(1, 20)
                pseu_2 = random.randint(1, 20)
                pseu_3 = random.randint(1, 20)
                pseu_4 = random.randint(1, 20)

                sim.call(EnableLosForSV("GPS", svId, False))

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))

            elif el_eg >= elevation_mask_1 and el_eg <= elevation_mask_2:
                pseu_1 = random.randint(1, 20)
                pseu_2 = random.randint(1, 20)
                pseu_3 = random.randint(1, 20)
                pseu_4 = random.randint(1, 20)

                sim.call(EnableLosForSV("GPS", svId, False))

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))

            else:

                pseu_1 = random.randint(1, 20)
                pseu_2 = random.randint(1, 20)
                pseu_3 = random.randint(1, 20)
                pseu_4 = random.randint(1, 20)

                id = "GPS-echo1-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_1, 0, 0, 1, id))

                id = "GPS-echo2-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_2, 0, 0, 2, id))

                id = "GPS-echo3-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_3, 0, 0, 3, id))

                id = "GPS-echo4-" + str(svId)
                if id not in list_id:
                    list_id.append(id)
                sim.call(SetMultipathForSV("L1CA", svId, 0, pseu_4, 0, 0, 4, id))


    time.sleep(0.001)


    if sim.call(GetSimulationElapsedTime()).milliseconds() >= time_4:
        break

print(list_id)

for echo_id in list_id:  # Echo and LOS
    print(echo_id)
    sim.call(EnableMultipath(False, echo_id))

sim.call(ClearAllLOSForSystem("GPS"))

# visibles = sim.call(GetVisibleSV("GPS"))
    # gpsSvIdMax = 32
    #
    # for svId in visibles.svId():  # Echo and LOS
    #
    #     sim.call(EnableLosForSV("GPS", svId, False))
    #
    #     for svId in visibles.svId():  # Echo and LOS
    #
    #         # Get the power of that satellite
    #         el_az = sim.call(GetElevationAzimuthForSV("GPS", svId))
    #         el_az_func = el_az.elevationAzimuth()
    #         el = el_az_func['Elevation']
    #         az = el_az_func['Azimuth']
    #         el_eg = (el * 180) / math.pi
    #
    #         if el_eg <= elevation_mask_1:
    #
    #             pseu_1 = random.randint(1, 50)
    #             pseu_2 = random.randint(25, 75)
    #             pseu_3 = random.randint(50, 100)
    #             pseu_4 = random.randint(75, 150)
    #
    #             sim.call(EnableLosForSV("GPS", svId, False))
    #
    #             id = "GPS-echo1-" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo2-" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo3-" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo4-" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #
    #         else:
    #
    #             pseu_1 = random.randint(1, 50)
    #             pseu_2 = random.randint(25, 75)
    #
    #             id = "GPS-echo1-else-" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo2-else-" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #
    #         #
    #         # try:
    #         #
    #         #     id = "GPS-echo1-" + str(svId)
    #         #     sim.call(EnableMultipath(False, id))
    #         #     id = "GPS-echo2-" + str(svId)
    #         #     sim.call(EnableMultipath(False, id))
    #         #     id = "GPS-echo3-" + str(svId)
    #         #     sim.call(EnableMultipath(False, id))
    #         #     id = "GPS-echo4-" + str(svId)
    #         #     sim.call(EnableMultipath(False, id))
    #         #
    #         # except:
    #         #     pass
    #
    #         if el_eg <= elevation_mask_1:
    #
    #
    #             id = "GPS-echo1-1" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo2-1" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo3-1" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo4-1" + str(svtime2Id)
    #             sim.call(EnableMultipath(False, id))
    #
    #         elif el_eg >= elevation_mask_1 and el_eg <= elevation_mask_2:
    #
    #             id = "GPS-echo1-2" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo2-2" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo3-2" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo4-2" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #
    #         else:
    #
    #             id = "GPS-echo1-3" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo2-3" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo3-3" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #             id = "GPS-echo4-3" + str(svId)
    #             sim.call(EnableMultipath(False, id))
    #
    #             #### sim.post(EnableLosForSV("GPS", svId, False), 1000)

sim.stop(480)
sim.disconnect()
