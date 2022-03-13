# RockitSoft


RockitSoft is a data plotting tool written in Python to support the Rockit Flight Computer made by @DanInvents.

WHAT IS ROCKIT?
Rockit is a RP2040 based flight computer designed for model rocketry. More information please visit https://github.com/DanInvents/Rockit. 

DEPENDANCIES
pip install plotly
pip install dash
pip install pandas

USAGE
1. Copy the csv file from the SD card to the folder that contains RockitSoft.py
2. In terminal, navigate to the folder that contains both the RockitSoft program and data file.
3. Enter the following at the prompt: python RockitSoft.py
4. At the prompt, enter the name of the datafile with extension. (ex. 00.CSV)

The program will then launch your web browser and display graphs for the data collected.


TO DO:
1. Add a flight summery page that includes:
    a. Total flight time
    b. Highest altitude reached and at what time.
    c. Highest acceleration reached and at what time.
    d. Highest speed reached and at what time.

2. Have the software trim down the data to only include the actual flight
