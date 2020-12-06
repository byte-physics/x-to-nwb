"""
Simple conversion tests for the stored files
"""

import os
import pathlib

from x_to_nwb.conversion_utils import createCycleID
from x_to_nwb.conversion import convert
from x_to_nwb.ABF2Converter import ABF2Converter

top_level = pathlib.Path(__file__).parent.absolute()
data_folder = os.path.join(top_level, "data")


def test_conversion_abfv2():

    ABF2Converter.protocolStorageDir = os.path.join(data_folder, "protocols")
    convert(
        os.path.join(data_folder, "2018_03_21_0029.abfv2"), compression=False, overwrite=True, searchSettingsFile=False
    )


def test_conversion_abfv1():

    convert(
        os.path.join(data_folder, "19122043.abfv1"),
        compression=False,
        overwrite=True,
        acquisitionChannelName="IN 1",
        stimulusChannelName="OUT 0",
    )


def test_conversion_dat():

    convert(os.path.join(data_folder, "H18.28.015.11.14.dat"), compression=False, overwrite=True)


def test_createCycleID():

    assert createCycleID([1, 2, 3, 4], total=2) == 1234
    assert createCycleID([1, 2, 3, 4], total=20) == 1020304
    assert createCycleID([10, 2, 3, 4], total=20) == 10020304
    assert createCycleID([10, 2, 3, 40], total=20) == 10020340
    assert createCycleID([10, 20, 30, 4], total=20) == 10203004
    assert createCycleID([10, 20, 30, 40], total=20) == 10203040
