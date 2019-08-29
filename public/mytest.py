import unittest
from loguru import logger
from config import basic_config
from model import platform_ice, platform_dto_ice, common_ice
from model import organization_type_ice, organization_type_dto_ice
import Ice
import sys


# logger.info('log初始化')

# class MyTicket(unittest.TestCase):
#     def setUp(self):
#         self.ticket = demo_ice._M_ticket
#         self.url = basic_config.ConfigInit.ticket_url
#         self.communicator = Ice.initialize(sys.argv)
#         self.base = self.communicator.stringToProxy(self.url)
#         logger.info('********MyTicket类用例开始***********')
#
#
#     def tearDown(self):
#         self.communicator.destroy()
#         logger.info('********MyTicket类用例结束***********')
#
#
# class MySms(unittest.TestCase):
#     def setUp(self):
#         self.sms = demo_ice._M_sms
#         self.url = basic_config.ConfigInit.sms_url
#         self.communicator = Ice.initialize(sys.argv)
#         self.base = self.communicator.stringToProxy(self.url)
#         logger.info('********MySms类用例开始***********')
#
#
#     def tearDown(self):
#         self.communicator.destroy()
#         logger.info('********MySms类用例结束***********')


class MyPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = platform_ice._M_com.jimi.api.user.system  # platform 文件实例
        self.platform_dto = platform_dto_ice._M_com.jimi.api.user.system.dto  # platform_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.platformapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyPlatform类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyPlatform类用例结束***********')


class MyApplication(unittest.TestCase):
    def setUp(self):
        self.platform = platform_ice._M_com.jimi.api.user.system  # platform 文件实例
        self.platform_dto = platform_dto_ice._M_com.jimi.api.user.system.dto  # platform_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.applicationapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyApplication类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyApplication类用例结束***********')


class MyOrganizationType(unittest.TestCase):
    def setUp(self):
        self.organizationtype = organization_type_ice._M_com.jimi.api.user.organization  # organization_type 文件实例
        self.organizationtype_dto = organization_type_dto_ice._M_com.jimi.api.user.organization.dto  # organization_type_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.organizationtypeapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyOrganizationType类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyOrganizationType类用例结束***********')


class MyAccountManager(unittest.TestCase):
    def setUp(self):
        self.accountmanager = organiz_ice._M_com.jimi.platform.user.generated
        self.header = organiz_common_ice._M_com.jimi.platform.user.generated
        self.account = self.header.CurrentAccount()
        self.url = basic_config.ConfigInit.accountmanager_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyAccountManager类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyAccountManager类用例结束***********')


class MyOrganizationManager(unittest.TestCase):
    def setUp(self):
        self.organizationmanager = organiz_ice._M_com.jimi.platform.user.generated
        self.header = organiz_common_ice._M_com.jimi.platform.user.generated
        self.account = self.header.CurrentAccount()
        self.url = basic_config.ConfigInit.organizationmanager_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyOrganizationManager类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyOrganizationManager类用例结束***********')


class MyRoleManager(unittest.TestCase):
    def setUp(self):
        self.organizationmanager = organiz_ice._M_com.jimi.platform.user.generated
        self.header = organiz_common_ice._M_com.jimi.platform.user.generated
        self.account = self.header.CurrentAccount()
        self.url = basic_config.ConfigInit.rolemanager_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyRoleManager类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyRoleManager类用例结束***********')


class MyMemberManager(unittest.TestCase):
    def setUp(self):
        self.systemmember = systemmember_ice._M_com.jimi.user.api.system
        self.header = systemmember_ice._M_com.jimi.user.api.system.dto
        # self.account = self.header.CurrentAccount()
        self.url = basic_config.ConfigInit.membermanager_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyMemberManager类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyMemberManager类用例结束***********')