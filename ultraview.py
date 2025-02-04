import psutil
import time
import ctypes
import os

class NetworkMonitor:
    def __init__(self, threshold=1000000000):  # 1 GB default threshold
        self.threshold = threshold
        self.previous_data = self.get_network_data()
    
    def get_network_data(self):
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent + net_io.bytes_recv

    def check_usage(self):
        current_data = self.get_network_data()
        usage = current_data - self.previous_data
        self.previous_data = current_data
        return usage

    def alert(self, message):
        ctypes.windll.user32.MessageBoxW(0, message, "UltraView Alert", 1)

    def control_usage(self):
        while True:
            usage = self.check_usage()
            print(f"Current usage: {usage / (1024**2):.2f} MB")
            if usage > self.threshold:
                self.alert("High network usage detected!")
                os.system("ipconfig /release")  # Release the IP address to cut off internet
                time.sleep(60)  # Wait a minute before re-enabling
                os.system("ipconfig /renew")  # Renew the IP address to restore internet
            time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor.control_usage()