#ecoding=utf-8
# author:herui
# time:2019

import sys
import logging
import os
import pytest

sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

from initialization.sysconfig import sys_config

logger = logging.getLogger("auto.log")
logger.setLevel(10)

log_file = r'D:\study\pythonScript\weixin\log\auto.log'
output_file = logging.FileHandler(filename=log_file, mode='a', encoding="utf-8")


output_screen = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)')
output_file.setFormatter(formatter)
output_screen.setFormatter(formatter)

logger.addHandler(output_screen)
logger.addHandler(output_file)
logging.info("error")

if __name__ == '__main__':
    logging.info("start to excute automation cases")
    pytest.main(['-sq','testcase/contact/department/test_update_dep.py'])
