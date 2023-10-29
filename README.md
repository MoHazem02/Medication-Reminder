# Medication Reminder

Medication Reminder is a prototype project that utilizes an ultrasonic sensor and an Arduino Uno to monitor the status of a medication box. The project aims to assist patients in keeping track of their medication schedule and receive reminders if they miss a dose. The software component of the project is a desktop application developed with PyQt5, and it communicates with the Arduino board via the FirmataExpress sketch. The project utilizes the pymata4, csv, and pyqt5 libraries.

## Features

- Monitoring the medication box using an ultrasonic sensor connected to an Arduino Uno.
- Recording medication usage data in a CSV file for future analysis and tracking.
- Scheduling medication dosages based on a prescription provided by the patient's doctor.
- Sending reminders to the patient if they miss a scheduled medication dose.
- User-friendly desktop application interface built with PyQt5.

## Hardware Requirements

- Arduino Uno board
- Ultrasonic sensor
- Medication box with suitable compartments

## Software Requirements

- Python 3.6 or above
- Arduino IDE
- PyQt5 library
- pymata4 library
- csv library

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/MoHazem02/Medication-Reminder.git
   
Install the required Python libraries:

```shell
pip install pyqt5 pymata4 csv
```

- Open the FirmataExpress sketch in the Arduino IDE and upload it to the Arduino Uno board.

- Connect the ultrasonic sensor to the Arduino Uno according to the wiring instructions provided in the project documentation.

- Launch the Medication Reminder application:

```shell
python main.py
```
## Usage
Load the prescription information provided by the doctor into the application.

Arrange the medications in the medication box according to the prescribed schedule.

Start the application, and it will begin monitoring the medication box using the ultrasonic sensor.

The application will provide reminders if a medication dose is missed.

The medication usage data will be recorded in a CSV file for future reference.

## Contributing
Contributions to the Medication Reminder project are welcome! If you find any bugs, have suggestions for improvements, or would like to add new features, please feel free to submit a pull request.


## Acknowledgments
PyQt5
pymata4
FirmataExpress
