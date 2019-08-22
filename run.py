import unittest
import time
from loguru import logger
import os
from testcase import test_generated


path = os.path.join(os.path.abspath('.'), 'log\\','test_{}.log'.format(time.strftime('%Y-%m-%d')))
logger.add(path)  # 日志初始化


def run(method, test=None):
    # 执行全部测试用例
    if method == 'all':
        test_dir = './testcase'
        suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
        unittest.TextTestRunner(verbosity=2).run(suite)
    if method == 'one':
    # 执行单条
        suit = unittest.TestSuite()
        suit.addTest(test)  # 把这个类中需要执行的测试用例加进去，有多条再加即可
        runner = unittest.TextTestRunner()
        runner.run(suit)

if __name__ == '__main__':
    run('one',test_generated.Generated("test_update_platform_client_secret"))   # 指定执行哪一条，第二个参数为：用例文件名.类方法（用例名称）
    # run('all') # 执行全部