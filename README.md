# RockitSoft


RockitSoft is a data plotting tool written in Python to support the Rockit Flight Computer made by @DanInvents.

WHAT IS THE ROCKIT FLIGHT COMPUTER?

Rockit is a Raspberry Pi RP2040 based flight computer designed for model rocketry. For more information please visit https://github.com/DanInvents/Rockit. 

DEPENDANCIES

Python must be installed along with plotly, dash and pandas.

To install plotly, dash and pandas enter the following at the command prompt.

pip install plotly

pip install dash

pip install pandas

USAGE
1. Copy the csv file from the SD card to the folder that contains RockitSoft.py
2. In terminal, navigate to the folder that contains both the RockitSoft program and data file.
3. Enter the following at the prompt: python RockitSoft.py
4. At the prompt, enter the name of the datafile with extension. (ex. 00.CSV)
5. Enter (CONTROL + C) to end.

The program will then launch your web browser and display graphs for the data collected.


TO DO:
1. Add a flight summery page that includes:
    a. Total flight time
    b. Highest altitude reached and at what time.
    c. Highest acceleration reached and at what time.
    d. Highest speed reached and at what time.

2. Have the software trim down the data to only include the actual flight.
3. Add the ability to load another data file without ending the program.



EXAMPLE SCREENS

ALTITUDE
<img width="1224" alt="Screen Shot 2022-03-13 at 4 03 13 PM" src="https://user-images.githubusercontent.com/66921702/158083132-c441553d-c93b-4bf0-b607-216d9b6faefa.png">

FILTERED ALTITUDE
<img width="1298" alt="Screen Shot 2022-03-13 at 3 56 27 PM" src="https://user-images.githubusercontent.com/66921702/158082883-2a166cb4-eee4-4663-b818-46de4949104d.png">

ACCELERATION
<img width="1296" alt="Screen Shot 2022-03-13 at 3 56 40 PM" src="https://user-images.githubusercontent.com/66921702/158082906-a47bd85a-64e8-45f0-b226-cf328bc85131.png">

PERPENDICULAR ACCELERATION
<img width="1298" alt="Screen Shot 2022-03-13 at 3 56 52 PM" src="https://user-images.githubusercontent.com/66921702/158082928-b433d9e9-29db-4905-898d-13e372473cbf.png">

TEMPERATURE
<img width="1297" alt="Screen Shot 2022-03-13 at 3 57 04 PM" src="https://user-images.githubusercontent.com/66921702/158082944-67ccc80f-ce37-4bdd-8177-2debdae5aa28.png">


