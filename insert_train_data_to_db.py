import pandas as pd
from sqlalchemy.sql import text as sa_text
from database import engine
from models import CNCMachineTrain
from sqlmodel import Session

# read data
df = pd.read_csv("dataset/train.csv")
df.columns = df.columns.str.upper()
print(df.head())

df["TARGET"] = df["TARGET"].apply(lambda x: 1 if x == "worn" else 0) # Convert to binary
df.drop(["EXP_NO","MACHINING_PROCESS"], axis=1, inplace=True) # Drop the experiment number amd machining status column


# # Truncate table with sqlalchemy
# with Session(engine) as session:
#     session.execute(sa_text(''' TRUNCATE TABLE advertisingtrain  '''))
#     session.commit()

with Session(engine) as session:
        session.execute(sa_text('TRUNCATE TABLE cncmachinetrain'))
        session.commit()
        
        for index, row in df.iterrows():
            # Create an instance of CNCMachineTrain for each row
            cnc_machine_train = CNCMachineTrain(**row.to_dict())
            session.add(cnc_machine_train)

        # Commit the session to save the records
        session.commit()


"""
# Insert training data
records_to_insert = []

print(records_to_insert)
# print(records_to_insert)

for df_idx, line in df.iterrows():
    records_to_insert.append(
                    CNCMachineTrain(X1_ACTUALPOSITION = line[1],
                                    X1_ACTUALVELOCITY = line[2],
                                    X1_ACTUALACCELERATION = line[3],
                                    X1_COMMANDPOSITION = line[4],
                                    X1_COMMANDVELOCITY = line[5],
                                    X1_COMMANDACCELERATION = line[6],
                                    X1_CURRENTFEEDBACK = line[7],
                                    X1_DCBUSVOLTAGE = line[8],
                                    X1_OUTPUTCURRENT = line[9],
                                    X1_OUTPUTVOLTAGE = line[10],
                                    X1_OUTPUTPOWER = line[11],
                                    Y1_ACTUALPOSITION = line[12],
                                    Y1_ACTUALVELOCITY = line[13],
                                    Y1_ACTUALACCELERATION = line[14],
                                    Y1_COMMANDPOSITION = line[15],
                                    Y1_COMMANDVELOCITY = line[16],
                                    Y1_COMMANDACCELERATION = line[17],
                                    Y1_CURRENTFEEDBACK = line[18],
                                    Y1_DCBUSVOLTAGE = line[19],
                                    Y1_OUTPUTCURRENT = line[20],
                                    Y1_OUTPUTVOLTAGE = line[21],
                                    Y1_OUTPUTPOWER = line[22],
                                    Z1_ACTUALPOSITION = line[23],
                                    Z1_ACTUALVELOCITY = line[24],
                                    Z1_ACTUALACCELERATION = line[25],
                                    Z1_COMMANDPOSITION = line[26],
                                    Z1_COMMANDVELOCITY = line[27],
                                    Z1_COMMANDACCELERATION = line[28],
                                    Z1_CURRENTFEEDBACK = line[29],
                                    Z1_DCBUSVOLTAGE = line[30],
                                    Z1_OUTPUTCURRENT = line[31],
                                    Z1_OUTPUTVOLTAGE = line[32],
                                    S1_ACTUALPOSITION = line[33],
                                    S1_ACTUALVELOCITY = line[34],
                                    S1_ACTUALACCELERATION = line[35],
                                    S1_COMMANDPOSITION = line[36],
                                    S1_COMMANDVELOCITY = line[37],
                                    S1_COMMANDACCELERATION = line[38],
                                    S1_CURRENTFEEDBACK = line[39],
                                    S1_DCBUSVOLTAGE = line[40],
                                    S1_OUTPUTCURRENT = line[41],
                                    S1_OUTPUTVOLTAGE = line[42],
                                    S1_OUTPUTPOWER = line[43],
                                    S1_SYSTEMINERTIA = line[44],
                                    M1_CURRENT_PROGRAM_NUMBER = line[45],
                                    M1_SEQUENCE_NUMBER = line[46],
                                    M1_CURRENT_FEEDRATE = line[47],
                                    TARGET=line[48]
                    )
    )
    print(records_to_insert)
    print("Inserted record: ", df_idx+1)

session.bulk_save_objects(records_to_insert)
session.commit()
# Ends database insertion
"""