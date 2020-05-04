import time

print("Starting the keep alive script... ")
print("Press (Ctrl + C) to exit!")


def print_after_duration(text, duration=1, end=''):
    time.sleep(duration)
    print(text, end=end, flush=True)


def keep_alive():
    while 1 == 1:
        print_after_duration("I ")
        print_after_duration("am ")
        print_after_duration("Alive!")
        print_after_duration("\b\b\b\b\b\b\b\b\b\b\b           ", end="\r")


keep_alive()
