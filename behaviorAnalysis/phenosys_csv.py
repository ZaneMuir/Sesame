"""convert phenosys csv into pandas dataframe."""
import pandas as pd
import numpy as np


def convertExcelDateToTimestamp(excel_T):
    """Convert Excel datetime format into Unix timestamp."""
    return (excel_T - 25569)*86400 - 8*3600


def normalizeWindowsCSVFile(filename):
    """Trim the 0x00, 0xff, 0xfe, 0x1d out from the file."""
    with open(filename, "rb") as inputfile:
        data = inputfile.read()
    data = bytes(filter(lambda x: x not in [0x00, 0xff, 0xfe, 13], data))
    with open(filename, "wb") as outputfile:
        outputfile.write(data)


def get_lick_list(filename, start_time=0):
    """Get lick time numpy.array from phenosys csv."""
    normalizeWindowsCSVFile(filename)
    phenosys_datasheet = pd.read_csv(filename)

    lick_filter = phenosys_datasheet[phenosys_datasheet.SystemMsg == "lick"]
    lick_filter = lick_filter["DateTime"].values

    return np.array([i-start_time for i in list(map(
                                convertExcelDateToTimestamp,
                                lick_filter))])
