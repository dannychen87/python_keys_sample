import os
import time

import pytest

date_ = time.strftime('%Y-%m-%d')
time_ = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

if __name__ == '__main__':
    pytest.main()
    # Copy environment file to temp folder for allure report
    os.system('copy environment.properties temp\\environment.properties')
    time.sleep(2)
    os.system(f'allure generate ./temp -o ./reports/{date_}/report_{time_} --clean')
