# Simple Reflex Agent for Air Quality Index (AQI)

## Project Overview

This project implements a **Simple Reflex Agent** in Python that determines the **Air Quality Index (AQI)** of a region using environmental sensor data.

The agent reads environmental parameters from sensors (provided as a data file) and immediately reacts using predefined rules to determine the AQI category.

The system simulates how environmental monitoring systems classify pollution levels in real time.

---

## Concept Used

### Simple Reflex Agent

A Simple Reflex Agent works based on the rule:

```
Condition → Action
```

It does not store past states and makes decisions based only on the current percept.

Example:

```
IF PM2.5 <= 50 → AQI = Good
IF PM2.5 <= 100 → AQI = Moderate
IF PM2.5 <= 150 → AQI = Unhealthy for Sensitive Groups
IF PM2.5 <= 200 → AQI = Unhealthy
ELSE → Very Unhealthy
```

---

## Environmental Parameters Used

The sensors provide the following pollutant values:

* PM2.5
* PM10
* CO
* NO2
* SO2

These values are used to estimate the overall AQI.

---

## Project Architecture

```
Sensors (Data File)
        ↓
Perception Module
        ↓
Simple Reflex Agent
        ↓
AQI Calculation Rules
        ↓
Output AQI Category
```

---

## Files Description

| File               | Purpose                 |
| ------------------ | ----------------------- |
| agent.py           | Main reflex agent logic |
| aqi_calculator.py  | AQI rule calculations   |
| sensors_data.txt   | Input sensor data       |
| output_example.txt | Example program output  |
| requirements.txt   | Python dependencies     |
| README.md          | Project documentation   |

---

## How the Agent Works

1. The agent reads sensor values from a file.
2. The AQI calculator processes pollutant values.
3. The reflex agent applies rule-based decisions.
4. The AQI category is printed.

---

## Example Sensor Data

```
PM2.5=85
PM10=120
CO=1.2
NO2=40
SO2=15
```

---

## Example Output

```
Air Quality Index Category: Moderate
Pollution Level: Medium
Health Advice: Sensitive individuals should reduce outdoor exertion.
```

---

## Running the Project

### Step 1

Install Python 3.

### Step 2

Clone the repository

```
git clone https://github.com/yourusername/AQI-Reflex-Agent.git
```

### Step 3

Navigate into the project

```
cd AQI-Reflex-Agent
```

### Step 4

Run the program

```
python agent.py
```

---

## Applications

* Smart city pollution monitoring
* Environmental research
* Public health monitoring systems
* IoT-based environmental sensors

---

## Author

Student AI Assignment Project
