# Autonomous Mobile Robot – Line Following & Pick-and-Place

Academic project developed as part of the Automation and Robotics program.
The goal was to design and implement control software for a mobile robot
capable of following a colored line and performing a pick-and-place task
in a physical environment.

## Project Overview

The robot autonomously navigates along a track marked with colored tape.
Depending on detected colors, it performs different actions such as:
- following the line,
- changing direction,
- picking up an object,
- transporting and placing the object at a designated location.

The project was implemented and tested on a real Lego Mindstorms platform.

## Hardware

- Lego Mindstorms EV3
- Two DC motors for differential drive
- One medium motor controlling the gripper
- Two color sensors (line detection)
- One touch sensor (start signal)
- Tracked chassis

## Software

- Python 3
- ev3dev2 library

## Control Architecture

The robot behavior is controlled using a Finite State Machine.
Each state corresponds to a specific phase of the task, including:
- initialization and start,
- black line following,
- color-based event detection,
- object pickup,
- object transport and release.

State transitions depend on:
- color sensor readings,
- elapsed time (timer),
- previously detected line position.

## Line Following Algorithm

The line-following algorithm uses two color sensors mounted at the front
of the robot. Based on their readings:
- the robot moves straight when both sensors detect the line,
- steering corrections are applied by differentiating motor speeds,
- when the line is lost, a recovery rotation sequence is executed.

The algorithm stores the last known line position
and limits oscillations using timers.

## Pick-and-Place Task

The pick-and-place task is implemented as a sequence of FSM states.
It includes:
- detection of a specific color indicating the pickup point or the drop-off point,
- gripper control and release using a medium motor,

Due to limited sensory input, selected actions rely on time-based control.

## Testing and Calibration

The robot was tested in a physical environment with different starting
positions and track configurations.
Motion parameters such as speed and rotation timing
were tuned empirically based on observed behavior.

Changes in track geometry often required re-tuning, highlighting the
sensitivity of the system to environmental conditions.

## Project Structure

- "line_following.py" – basic line-following algorithm
- "pick_place.py" – full FSM implementation with pick-and-place logic
- "images/" – photos of the robot platform during testing
- "project_description.pdf" - documentation in polish

## Author and Contribution

Team project (2 people).

My responsibility:
- implementation of control algorithms in Python,
- FSM design,
- motion tuning,
- testing and debugging in a real environment.

## Notes

This project focuses on practical engineering trade-offs encountered
in real robotic systems, such as sensor placement and parameter tuning.
