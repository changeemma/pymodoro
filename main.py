import click
from pomodoro_session import PomodoroSession


@click.command()
@click.argument("pomodoro", type=click.INT, default=25)
@click.argument("short_break", type=click.INT, default=5)
@click.argument("long_break", type=click.INT, default=10)
@click.argument("set_length", type=click.INT, default=4)
def main(pomodoro, short_break, long_break, set_length):
    """Starts pomodoro session.

    \b
    POMODORO is the pomodoro interval in minutes. Defaults to 25.
    SHORT_BREAK is the break interval in minutes between pomodoro's. Defaults to 5.
    LONG_BREAK is the break interval in minutes between sets. Defaults to 10.
    SET_LENGTH is the count of pomodoro sessions in one set. Defaults to 4.
    """
    print(f"Pomodoro interval:     {pomodoro:2} minutes.")
    print(f"Break between pomodoro:{short_break:2} minutes.")
    print(f"Set length:            {set_length:2} pomodoro.")
    print(f"Break between sets:    {long_break:2} minutes.")
    print()
    session = PomodoroSession(pomodoro=pomodoro, short_break=short_break, long_break=long_break, set_length=set_length)
    session.start()


if __name__ == "__main__":
    main()
