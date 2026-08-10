# Development of Swarm Drone

A multi-drone coordination project focused on developing and testing **leader–follower swarm behavior** using autonomous flight control, MAVLink communication, and DroneKit.

The current implementation establishes a basic two-drone swarm architecture in which one drone acts as the **Leader** and another as the **Follower**. The follower monitors the leader's state and automatically performs corresponding actions such as arming and takeoff.

## 🚁 Project Overview

The goal of this project is to progressively develop a reliable framework for coordinating multiple UAVs and eventually extend it toward larger autonomous drone formations.

The current prototype focuses on:

* Connecting multiple drones through serial interfaces
* Establishing Leader–Follower communication
* Monitoring the Leader's armed state
* Automatically switching the Follower to `GUIDED` mode
* Arming the Follower through MAVLink
* Detecting the Leader's takeoff
* Automatically commanding the Follower to take off
* Matching the Leader's target altitude

The current implementation serves as the foundation for more advanced swarm behaviors such as position tracking, formation control, trajectory synchronization, and multi-drone coordination.

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │        LEADER        │
                 │                      │
                 │  Manual / Autonomous │
                 │       Flight         │
                 └──────────┬───────────┘
                            │
                            │ State Monitoring
                            │
                            ▼
                 ┌──────────────────────┐
                 │       FOLLOWER       │
                 │                      │
                 │  GUIDED Mode         │
                 │  Auto Arm            │
                 │  Auto Takeoff        │
                 │  Altitude Matching   │
                 └──────────────────────┘
```

### Current Control Flow

```text
Connect to Leader
        │
        ▼
Connect to Follower
        │
        ▼
Wait for Leader to ARM
        │
        ▼
Set Follower → GUIDED
        │
        ▼
ARM Follower using MAVLink
        │
        ▼
Wait for Leader Takeoff
        │
        ▼
Read Leader Altitude
        │
        ▼
Follower Takeoff
        │
        ▼
Reach Target Altitude
```

## 🛠️ Technology Stack

* **Python**
* **DroneKit-Python**
* **MAVLink**
* **ArduPilot**
* **GUIDED Flight Mode**
* **Serial / COM Port Communication**

## 📂 Project Structure

```text
development-of-swarm-drone/
│
├── takeoff_test.py
├── test_connection.py
│
├── autonomous_flight.mp4
├── swarm_drone.mp4
│
└── README.md
```

### Scripts

#### `test_connection.py`

Used to test communication with the Leader and Follower drones and verify the arming sequence.

The script connects to both drones at a configured baud rate, waits for the Leader to arm, switches the Follower to `GUIDED`, and sends a MAVLink arm command.

#### `takeoff_test.py`

Implements the initial Leader–Follower takeoff synchronization.

The Follower waits for the Leader to arm and take off, reads the Leader's relative altitude, and then performs its own takeoff to the detected target altitude.

## ⚙️ Configuration

The drone connections are configured using serial COM ports and a baud rate.

Example:

```python
LEADER_PORT = "COM15"
FOLLOWER_PORT = "COM10"
BAUD_RATE = 57600
```

These values depend on the connected flight controllers and should be changed according to the system configuration.

> **Important:** Do not assume the COM port numbers shown in the example will be the same on another computer.

## ▶️ Running the Project

### 1. Install Dependencies

```bash
pip install dronekit
```

Depending on the flight-controller setup, additional MAVLink/ArduPilot dependencies may be required.

### 2. Connect the Flight Controllers

Connect the Leader and Follower flight controllers to the computer through their respective serial interfaces.

### 3. Configure COM Ports

Update the port configuration inside the Python scripts:

```python
LEADER_PORT = "COM15"
FOLLOWER_PORT = "COM10"
```

### 4. Test the Connection

```bash
python test_connection.py
```

The script should establish connections to both drones and monitor the Leader's armed state.

### 5. Test Leader–Follower Takeoff

```bash
python takeoff_test.py
```

The expected sequence is:

```text
Leader ARM
     ↓
Follower → GUIDED
     ↓
Follower ARM
     ↓
Leader TAKEOFF
     ↓
Follower detects takeoff
     ↓
Follower TAKEOFF
     ↓
Follower reaches target altitude
```

## 🧪 Current Status

### Implemented

* [x] Multi-drone serial connection
* [x] Leader–Follower architecture
* [x] Leader arm detection
* [x] Follower GUIDED mode
* [x] Follower automatic arming
* [x] Leader takeoff detection
* [x] Leader altitude reading
* [x] Follower automatic takeoff
* [x] Basic two-drone coordination

### In Development

* [ ] Real-time position synchronization
* [ ] Leader position tracking
* [ ] Distance/offset-based following
* [ ] Formation control
* [ ] Multiple follower drones
* [ ] Collision avoidance
* [ ] Autonomous waypoint coordination
* [ ] Robust communication and fault handling
* [ ] Full swarm behavior

## 🔭 Future Scope

The current two-drone Leader–Follower system is intended to be extended into a scalable swarm architecture.

Future development will focus on:

### 1. Formation Control

Maintain predefined geometric formations such as:

```text
        Leader
          ▲
          │
     ┌────┴────┐
     │         │
 Follower 1  Follower 2
```

### 2. Position-Based Following

Instead of only synchronizing takeoff altitude, followers will maintain a defined spatial offset from the Leader.

### 3. Multi-Follower Swarm

Extend the system from:

```text
Leader → Follower
```

to:

```text
              ┌──→ Follower 1
              │
Leader ───────┼──→ Follower 2
              │
              └──→ Follower 3
```

### 4. Autonomous Mission Coordination

Enable multiple drones to coordinate waypoint execution and mission trajectories.

### 5. Safety and Fault Handling

Introduce mechanisms for:

* Communication loss
* GPS degradation
* Drone failure
* Emergency landing
* Collision prevention
* Leader failure and role reassignment

## ⚠️ Safety Notice

This project involves autonomous UAV control and should be tested carefully.

Initial testing should be performed in a **simulation environment or controlled test area** before attempting autonomous flight with physical drones.

Always verify:

* Flight controller configuration
* GPS availability
* Arming checks
* Failsafe configuration
* Flight mode
* Communication links
* Local UAV regulations

## 📌 Project Goal

The long-term objective is to develop a **scalable autonomous swarm-drone coordination system** capable of coordinating multiple UAVs with minimal human intervention.

The project is being developed incrementally, beginning with reliable two-drone Leader–Follower coordination and progressing toward autonomous formation flight and multi-UAV swarm intelligence.

---

**Status:** 🚧 Active Development
**Focus:** Autonomous Multi-Drone Coordination
**Architecture:** Leader–Follower
**Platform:** ArduPilot + DroneKit + MAVLink
