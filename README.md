# Sesame
Stimulus Generator and Data Analysis for Sequence Learning and Memory Project

# TODO:
- expected data analysis methods and results.

# Project: Representation and Prediction of Sequence Information in Mice Primary Visual Cortex

## Background:
- Essential Function of Brain, particularly neocortex: Prediction
- There is a universal learning algorithm
- Sensory Information is a function of Time.
- How is sequence information represented in V1:
- Further: How is sequence information be encoded, represented, decoded, stored, retrieved in brain.

## Setups

### Design
#### Phase I -- Behavior Validation
- GO/NO-GO discrimination paradigm:
    - head-fixed water-restricted mice, watching screens with colors in a sequence.
    - after a specific sequence of color, mice could get water; otherwise, no water.
    - HIT, MISS, CORRECT REJECTION, FALSE ALARM
    - GO trial: ABB
    - NO-GO trial: AAB

#### Phase II -- Neurons Activities Validation
- Two-Photon Imaging in V1
    - Layer 1
    - Layer 2/3
    - Layer 4
    - Layer 5/6

#### Phase III -- Circuit Model Abstraction
- What information flowed in and out
- Possible micro-circuit model

#### Phase IV -- Model Validation
- Multichannel Clamping and Dying in V1

### Expectation

## Interpretation and Future

- How is sequence information be encoded, represented, decoded, stored, retrieved in brain.

## Data Structure

```sql
CREATE TABLE summary {
    SessionID TEXT,
    SessionType TEXT,
    SessionSerial INT,
    SessionDate INT,
    SessionTime REAL,
    Mouse TEXT,
    Setup TEXT,
    Result TEXT,
    HitRate REAL,
    FalseAlarmRate REAL
};
```
