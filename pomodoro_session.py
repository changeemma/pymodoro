from pomodoro_steps import PomodoroStepEnum
from pomodoro_steps import IdleStep, PomodoroStep, ShortBreakStep, LongBreakStep


class PomodoroSession:
    def __init__(
        self, pomodoro: int, short_break: int, long_break: int, set_length: int = 4
    ):
        self.set_length = set_length
        self.steps = {
            PomodoroStepEnum.IDLE_STEP: IdleStep(self),
            PomodoroStepEnum.POMODORO_STEP: PomodoroStep(pomodoro, self),
            PomodoroStepEnum.SHORT_BREAK_STEP: ShortBreakStep(short_break, self),
            PomodoroStepEnum.LONG_BREAK_STEP: LongBreakStep(long_break, self),
        }
        self.counter = 0
        self.state = self.steps[PomodoroStepEnum.IDLE_STEP]

    def start(self):
        try:
            while True:
                self.state.next_step()
                self.state.notify()
                self.state.start()
        except KeyboardInterrupt:
            print("\r")

    def is_set_done(self) -> bool:
        return self.counter >= self.set_length

    def reset(self):
        self.state = self.steps[PomodoroStepEnum.IDLE_STEP]
        self.counter = 0

    def set_pomodoro(self):
        self.state = self.steps[PomodoroStepEnum.POMODORO_STEP]
        self.counter += 1

    def set_short_break(self):
        self.state = self.steps[PomodoroStepEnum.SHORT_BREAK_STEP]

    def set_long_break(self):
        self.state = self.steps[PomodoroStepEnum.LONG_BREAK_STEP]
