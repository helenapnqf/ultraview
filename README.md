# UltraView

UltraView is a Python program designed to monitor and control network usage on Windows systems. It helps prevent excessive bandwidth consumption by alerting users and temporarily disabling the network connection if usage exceeds a specified threshold.

## Features

- Monitors network data consumption in real-time.
- Alerts users when network usage exceeds a predefined threshold.
- Temporarily disables network connection to prevent excessive usage, and restores it after a cooldown period.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Ensure you have Python 3 installed on your Windows machine.
2. Install the `psutil` library using pip:
   ```
   pip install psutil
   ```

## Usage

1. Download or clone the `ultraview.py` script to your local machine.
2. Open a command prompt and navigate to the directory containing `ultraview.py`.
3. Run the script:
   ```
   python ultraview.py
   ```

## Configuration

- The default network usage threshold is set to 1 GB. You can modify this by changing the `threshold` value in the `NetworkMonitor` class initializer.
- The script checks network usage every 5 seconds. You can adjust this interval by changing the `time.sleep(5)` value in the `control_usage` method.

## Disclaimer

- This program temporarily disables the network connection by releasing the IP address. Ensure this behavior is acceptable for your environment before running the script.
- The program is developed for educational purposes and should be used responsibly.

## License

This project is licensed under the MIT License.