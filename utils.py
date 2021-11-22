import pynotifier
import shutil
import sys
import time


def send_notification(message):
    pynotifier.Notification(
        title="Pymodoro",
        description=message,
        icon_path="/home/a445856/repositories/pymodoro/icon-32x32.png",  # On Windows .ico is required, on Linux - .png
        duration=3,  # Duration in seconds
        urgency="normal",
    ).send()


class Timer:
    def __init__(self, name, duration_in_minutes):
        self.name = name
        self.duration_in_minutes = duration_in_minutes

    def start(self):
        terminal_size = shutil.get_terminal_size()
        terminal_width = terminal_size.columns

        def write_line(line):
            sys.stdout.write(f"\r{' ' * terminal_width}")
            sys.stdout.flush()
            sys.stdout.write(f"\r{line}")

        for i in reversed(range(self.duration_in_minutes)):
            for j in reversed(range(3)):
                write_line(f"{self.name} - {i:02}:{j:02}")
                time.sleep(1)
        write_line(f"{self.name} - Done\n")
