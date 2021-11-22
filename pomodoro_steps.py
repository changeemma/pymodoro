from enum import Enum

from utils import Timer, send_notification


class PomodoroStepEnum(Enum):
    IDLE_STEP = 0
    POMODORO_STEP = 1
    SHORT_BREAK_STEP = 2
    LONG_BREAK_STEP = 3


class IdleStep:
    def __init__(self, session):
        self.session = session

    def start(self):
        pass

    def notify(self):
        pass

    def next_step(self):
        self.session.set_pomodoro()


class BaseStep:
    TIMER_NAME = "Base step"
    NOTIFICATION_MESSAGE = "Base step notification message"

    def __init__(self, duration_in_minutes, session):
        self.timer = Timer(self.TIMER_NAME, duration_in_minutes)
        self.session = session

    def start(self):
        self.timer.start()

    def notify(self):
        send_notification(self.NOTIFICATION_MESSAGE)


class PomodoroStep(BaseStep):
    TIMER_NAME = "Pomodoro"
    NOTIFICATION_MESSAGE = "Starting Pomodoro"

    def next_step(self):
        if self.session.is_set_done() is True:
            self.session.set_long_break()
        else:
            self.session.set_short_break()


class ShortBreakStep(BaseStep):
    TIMER_NAME = "Short break"
    NOTIFICATION_MESSAGE = "Let's take a break!"

    def next_step(self):
        self.session.set_pomodoro()


class LongBreakStep(BaseStep):
    TIMER_NAME = "Long break"
    NOTIFICATION_MESSAGE = "Nicely done! Have a break."

    def next_step(self):
        self.session.reset()
