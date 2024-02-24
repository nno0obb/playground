import os
from typing import *


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []

        for log in logs:
            identifier, contents = log.split()[0], log.split()[1:]

            if ''.join(contents).islower():
                letter_logs.append(log)
            elif ''.join(contents).isdigit():
                digit_logs.append(log)
            else:
                raise RuntimeError()

        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_logs + digit_logs


if __name__ == '__main__':
    os.system('python3 937_test.py')
