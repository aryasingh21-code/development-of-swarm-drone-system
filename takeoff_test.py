from dronekit import connect, VehicleMode
import time

LEADER_PORT = "COM10"
FOLLOWER_PORT = "COM28"

print("Connecting to leader...")
leader = connect(LEADER_PORT, baud=57600, wait_ready=False)

print("Connecting to follower...")
follower = connect(FOLLOWER_PORT, baud=57600, wait_ready=False)

print("Both drones connected")

# WAIT FOR LEADER ARM
while not leader.armed:
    print("Waiting for leader to arm...")
    time.sleep(1)

print("Leader armed detected")

# SET FOLLOWER MODE
print("Setting follower to GUIDED")
follower.mode = VehicleMode("GUIDED")
time.sleep(2)

# FORCE ARM FOLLOWER
print("Force arming follower")

follower._master.mav.command_long_send(
    follower._master.target_system,
    follower._master.target_component,
    400,
    0,
    1,
    21196,
    0,0,0,0,0
)

time.sleep(3)

print("Follower armed:", follower.armed)

# WAIT FOR LEADER TAKEOFF
print("Waiting for leader to take off")

while leader.location.global_relative_frame.alt < 1:
    print("Leader altitude:", leader.location.global_relative_frame.alt)
    time.sleep(1)

print("Leader takeoff detected")

# FOLLOWER TAKEOFF
target_alt = leader.location.global_relative_frame.alt

print("Follower taking off to:", target_alt)

follower.simple_takeoff(target_alt)

while follower.location.global_relative_frame.alt < target_alt * 0.9:
    print("Follower altitude:", follower.location.global_relative_frame.alt)
    time.sleep(1)

print("Follower takeoff complete")