import unittest
from loguru import logger
from config import basic_config
from model import platform_ice, platform_header_ice
from model import demo_ice
import Ice
import sys


# logger.info('log初始化')

class MyTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = demo_ice._M_ticket
        self.url = basic_config.ConfigInit.ticket_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyTicket类用例开始***********')


    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyTicket类用例结束***********')


class MySms(unittest.TestCase):
    def setUp(self):
        self.sms = demo_ice._M_sms
        self.url = basic_config.ConfigInit.sms_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MySms类用例开始***********')


    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MySms类用例结束***********')


class MyPlatform(unittest.TestCase):
    def setUp(self):
        self.generated = platform_ice._M_com.jimi.user.api.system
        self.header = platform_header_ice._M_com.jimi.user.api.system.dto
        self.url = basic_config.ConfigInit.platform_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyPlatform类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyPlatform类用例结束***********')
