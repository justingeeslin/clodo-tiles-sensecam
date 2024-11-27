# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Sensor Functions
def sensor_new_setting_detected():
    """
    filters:
      - name: Sensitivity
        modifiers:
          - name: Sensitivity
            options: [Low, Medium, High]
    """
    pass

# Actuator Functions
def actuator_take_photo():
    """
    filters:
      - name: Now
        modifiers:
          - name: Pace
            options: [Fast, Slow]
      - name: On an interval
        modifiers:
          - name: Every
            options: [1 second, 5 seconds]
    """
    pass

def actuator_stop_photo_capture():
    """
    """
    pass

def actuator_privacy_mode():
    """
     filters:
      - name: Activate
      - name: Deactivate
    """
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Ran')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
