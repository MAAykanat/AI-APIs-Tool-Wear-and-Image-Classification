from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


class RequestCNCMachine(SQLModel):

    X1_ACTUALPOSITION:             float
    X1_ACTUALVELOCITY:             float
    X1_ACTUALACCELERATION:         float
    X1_COMMANDPOSITION:            float
    X1_COMMANDVELOCITY:            float
    X1_COMMANDACCELERATION:        float
    X1_CURRENTFEEDBACK:            float
    X1_DCBUSVOLTAGE:               float
    X1_OUTPUTCURRENT:              float
    X1_OUTPUTVOLTAGE:              float
    X1_OUTPUTPOWER:                float
    Y1_ACTUALPOSITION:             float
    Y1_ACTUALVELOCITY:             float
    Y1_ACTUALACCELERATION:         float
    Y1_COMMANDPOSITION:            float
    Y1_COMMANDVELOCITY:            float
    Y1_COMMANDACCELERATION:        float
    Y1_CURRENTFEEDBACK:            float
    Y1_DCBUSVOLTAGE:               float
    Y1_OUTPUTCURRENT:              float
    Y1_OUTPUTVOLTAGE:              float
    Y1_OUTPUTPOWER:                float
    Z1_ACTUALPOSITION:             float
    Z1_ACTUALVELOCITY:             float
    Z1_ACTUALACCELERATION:         float
    Z1_COMMANDPOSITION:            float
    Z1_COMMANDVELOCITY:            float
    Z1_COMMANDACCELERATION:        float
    Z1_CURRENTFEEDBACK:            float
    Z1_DCBUSVOLTAGE:               float
    Z1_OUTPUTCURRENT:              float
    Z1_OUTPUTVOLTAGE:              float
    S1_ACTUALPOSITION:             float
    S1_ACTUALVELOCITY:             float
    S1_ACTUALACCELERATION:         float
    S1_COMMANDPOSITION:            float
    S1_COMMANDVELOCITY:            float
    S1_COMMANDACCELERATION:        float
    S1_CURRENTFEEDBACK:            float
    S1_DCBUSVOLTAGE:               float
    S1_OUTPUTCURRENT:              float
    S1_OUTPUTVOLTAGE:              float
    S1_OUTPUTPOWER:                float
    S1_SYSTEMINERTIA:              float
    M1_CURRENT_PROGRAM_NUMBER:     float
    M1_SEQUENCE_NUMBER:            float
    M1_CURRENT_FEEDRATE:           float


    class Config:
        json_schema_extra = {
          
            "example": {
                "X1_ACTUALPOSITION":             162.000000,
                "X1_ACTUALVELOCITY":             -0.050000,
                "X1_ACTUALACCELERATION":         -18.800000,
                "X1_COMMANDPOSITION":            162.000000,
                "X1_COMMANDVELOCITY":              0.000000,
                "X1_COMMANDACCELERATION":          0.000000,
                "X1_CURRENTFEEDBACK":              2.210000,
                "X1_DCBUSVOLTAGE":                 0.053100,
                "X1_OUTPUTCURRENT":              327.000000,
                "X1_OUTPUTVOLTAGE":                7.060000,
                "X1_OUTPUTPOWER":                 -0.000016,
                "Y1_ACTUALPOSITION":              79.100000,
                "Y1_ACTUALVELOCITY":              -2.950000,
                "Y1_ACTUALACCELERATION":          18.800000,
                "Y1_COMMANDPOSITION":             79.100000,
                "Y1_COMMANDVELOCITY":             -3.000000,
                "Y1_COMMANDACCELERATION":          0.000000,
                "Y1_CURRENTFEEDBACK":             -6.730000,
                "Y1_DCBUSVOLTAGE":                 0.108000,
                "Y1_OUTPUTCURRENT":              325.000000,
                "Y1_OUTPUTVOLTAGE":               10.400000,
                "Y1_OUTPUTPOWER":                  0.000684,
                "Z1_ACTUALPOSITION":              28.500000,
                "Z1_ACTUALVELOCITY":              -0.025000,
                "Z1_ACTUALACCELERATION":         -12.500000,
                "Z1_COMMANDPOSITION":             28.500000,
                "Z1_COMMANDVELOCITY":              0.000000,
                "Z1_COMMANDACCELERATION":          0.000000,
                "Z1_CURRENTFEEDBACK":              0.000000,
                "Z1_DCBUSVOLTAGE":                 0.000000,
                "Z1_OUTPUTCURRENT":                0.000000,
                "Z1_OUTPUTVOLTAGE":                0.000000,
                "S1_ACTUALPOSITION":           -2010.000000,
                "S1_ACTUALVELOCITY":              53.200000,
                "S1_ACTUALACCELERATION":         -30.900000,
                "S1_COMMANDPOSITION":          -2010.000000,
                "S1_COMMANDVELOCITY":             53.300000,
                "S1_COMMANDACCELERATION":          0.000000,
                "S1_CURRENTFEEDBACK":             22.100000,
                "S1_DCBUSVOLTAGE":                 1.150000,
                "S1_OUTPUTCURRENT":              322.000000,
                "S1_OUTPUTVOLTAGE":              116.000000,
                "S1_OUTPUTPOWER":                  0.220000,
                "S1_SYSTEMINERTIA":               12.000000,
                "M1_CURRENT_PROGRAM_NUMBER":       1.000000,
                "M1_SEQUENCE_NUMBER":             84.000000,
                "M1_CURRENT_FEEDRATE":             3.000000,
            }
        }

class UpdateCNCMachine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    X1_ACTUALPOSITION:             float
    X1_ACTUALVELOCITY:             float
    X1_ACTUALACCELERATION:         float
    X1_COMMANDPOSITION:            float
    X1_COMMANDVELOCITY:            float
    X1_COMMANDACCELERATION:        float
    X1_CURRENTFEEDBACK:            float
    X1_DCBUSVOLTAGE:               float
    X1_OUTPUTCURRENT:              float
    X1_OUTPUTVOLTAGE:              float
    X1_OUTPUTPOWER:                float
    Y1_ACTUALPOSITION:             float
    Y1_ACTUALVELOCITY:             float
    Y1_ACTUALACCELERATION:         float
    Y1_COMMANDPOSITION:            float
    Y1_COMMANDVELOCITY:            float
    Y1_COMMANDACCELERATION:        float
    Y1_CURRENTFEEDBACK:            float
    Y1_DCBUSVOLTAGE:               float
    Y1_OUTPUTCURRENT:              float
    Y1_OUTPUTVOLTAGE:              float
    Y1_OUTPUTPOWER:                float
    Z1_ACTUALPOSITION:             float
    Z1_ACTUALVELOCITY:             float
    Z1_ACTUALACCELERATION:         float
    Z1_COMMANDPOSITION:            float
    Z1_COMMANDVELOCITY:            float
    Z1_COMMANDACCELERATION:        float
    Z1_CURRENTFEEDBACK:            float
    Z1_DCBUSVOLTAGE:               float
    Z1_OUTPUTCURRENT:              float
    Z1_OUTPUTVOLTAGE:              float
    S1_ACTUALPOSITION:             float
    S1_ACTUALVELOCITY:             float
    S1_ACTUALACCELERATION:         float
    S1_COMMANDPOSITION:            float
    S1_COMMANDVELOCITY:            float
    S1_COMMANDACCELERATION:        float
    S1_CURRENTFEEDBACK:            float
    S1_DCBUSVOLTAGE:               float
    S1_OUTPUTCURRENT:              float
    S1_OUTPUTVOLTAGE:              float
    S1_OUTPUTPOWER:                float
    S1_SYSTEMINERTIA:              float
    M1_CURRENT_PROGRAM_NUMBER:     float
    M1_SEQUENCE_NUMBER:            float
    M1_CURRENT_FEEDRATE:           float
    prediction:                    float
    client_ip:                     str

class CNCMachineTrain(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    X1_ACTUALPOSITION:             float
    X1_ACTUALVELOCITY:             float
    X1_ACTUALACCELERATION:         float
    X1_COMMANDPOSITION:            float
    X1_COMMANDVELOCITY:            float
    X1_COMMANDACCELERATION:        float
    X1_CURRENTFEEDBACK:            float
    X1_DCBUSVOLTAGE:               float
    X1_OUTPUTCURRENT:              float
    X1_OUTPUTVOLTAGE:              float
    X1_OUTPUTPOWER:                float
    Y1_ACTUALPOSITION:             float
    Y1_ACTUALVELOCITY:             float
    Y1_ACTUALACCELERATION:         float
    Y1_COMMANDPOSITION:            float
    Y1_COMMANDVELOCITY:            float
    Y1_COMMANDACCELERATION:        float
    Y1_CURRENTFEEDBACK:            float
    Y1_DCBUSVOLTAGE:               float
    Y1_OUTPUTCURRENT:              float
    Y1_OUTPUTVOLTAGE:              float
    Y1_OUTPUTPOWER:                float
    Z1_ACTUALPOSITION:             float
    Z1_ACTUALVELOCITY:             float
    Z1_ACTUALACCELERATION:         float
    Z1_COMMANDPOSITION:            float
    Z1_COMMANDVELOCITY:            float
    Z1_COMMANDACCELERATION:        float
    Z1_CURRENTFEEDBACK:            float
    Z1_DCBUSVOLTAGE:               float
    Z1_OUTPUTCURRENT:              float
    Z1_OUTPUTVOLTAGE:              float
    S1_ACTUALPOSITION:             float
    S1_ACTUALVELOCITY:             float
    S1_ACTUALACCELERATION:         float
    S1_COMMANDPOSITION:            float
    S1_COMMANDVELOCITY:            float
    S1_COMMANDACCELERATION:        float
    S1_CURRENTFEEDBACK:            float
    S1_DCBUSVOLTAGE:               float
    S1_OUTPUTCURRENT:              float
    S1_OUTPUTVOLTAGE:              float
    S1_OUTPUTPOWER:                float
    S1_SYSTEMINERTIA:              float
    M1_CURRENT_PROGRAM_NUMBER:     float
    M1_SEQUENCE_NUMBER:            float
    M1_CURRENT_FEEDRATE:           float
    TARGET:                        float

class CNCMachineDriftInput(SQLModel):
    n_days_before: int

    class Config:
        json_schema_extra = {
            "example": {
                "n_days_before": 5,
            }
        }