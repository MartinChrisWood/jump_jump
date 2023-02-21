import sys
import time as tic
import winsound


def boolify_str(x):
    """ Helper, create boolean from string """
    if x.lower().strip() == "false":
        return False
    elif x.lower().strip() == "true":
        return True
    else:
        raise ValueError(f"Can't read as boolean: {x}")


def main(wait, loop_on=True):
    """ Handles wait loop, only interruptible with Ctrl+C """
    print(f"Waiting for {int(wait / 60)} minutes, carry on = {loop_on}")
    looping = True
    while looping:
        tic.sleep(wait)
        print(f"Get up!")
        winsound.Beep(440, 500)
        looping = loop_on
    return None


if __name__ == "__main__":
    # Set some defaults
    wait = 60*10
    loop_on = True

    # Load wait time with input validation
    if len(sys.argv) > 1:
        try:
            wait = int(float(sys.argv[1]) * 60)
            if wait <= 0:
                raise ValueError(f"Cannot set wait for {wait}")
        except Exception as e:
            raise e
    
    # Load loop instruction with input validation
    if len(sys.argv) > 2:
        print(sys.argv)
        try:
            loop_on = boolify_str(sys.argv[2])
        except Exception as e:
            raise e
    
    main(wait, loop_on)
