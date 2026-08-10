from dronekit import connect, VehicleMode
import time

# -----------------------------
# CONNECTION SETTINGS
# -----------------------------

LEADER_PORT = "COM15"
FOLLOWER_PORT = "COM10"
BAUD_RATE = 57600

# -----------------------------
# CONNECT TO DRONES
# -----------------------------

print("Connecting to Leader...")
leader = connect(LEADER_PORT, baud=BAUD_RATE, wait_ready=False)

print("Connecting to Follower...")
follower = connect(FOLLOWER_PORT, baud=BAUD_RATE, wait_ready=False)

print("Both drones connected")

# -----------------------------
# WAIT FOR LEADER ARM
# -----------------------------

while True:

    print("Leader armed:", leader.armed)

    if leader.armed:

        print("Leader detected ARMED")

        # set follower mode
        follower.mode = VehicleMode("GUIDED")
        time.sleep(2)

        print("Force arming follower...")

        # MAVLink FORCE ARM
        follower._master.mav.command_long_send(
            follower._master.target_system,
            follower._master.target_component,
            400,      # MAV_CMD_COMPONENT_ARM_DISARM
            0,
            1,        # 1 = ARM
            21196,    # FORCE ARM code
            0,0,0,0,0
        )

        time.sleep(3)

        print("Follower armed status:", follower.armed)

        break

    time.sleep(1)

print("Arm test completed")