import unittest
from loguru import logger
from config import basic_config
from model import platform_ice, platform_dto_ice, common_ice
from model import organization_type_ice, organization_type_dto_ice
from model import organization_account_ice, organization_account_dto_ice
from model import organization_info_ice, organization_info_dto_ice
from model import system_member_ice, system_member_dto_ice
from model import organization_role_ice, organization_role_dto_ice
from model import appuser_ice,appuser_dto_ice
import Ice
import sys


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


class MyOrganizationAccount(unittest.TestCase):
    def setUp(self):
        self.organizationaccount = organization_account_ice._M_com.jimi.api.user.organization  # organization_account 文件实例
        self.organizationaccount_dto = organization_account_dto_ice._M_com.jimi.api.user.organization.dto  # organization_account_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.organizationaccountapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyOrganizationAccount类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyOrganizationAccount类用例结束***********')


class MyOrganization(unittest.TestCase):
    def setUp(self):
        self.organization = organization_info_ice._M_com.jimi.api.user.organization  # organization_info 文件实例
        self.organization_dto = organization_info_dto_ice._M_com.jimi.api.user.organization.dto  # organization_info_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.organizationapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyOrganization类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyOrganization类用例结束***********')


class MyOrganizationRole(unittest.TestCase):
    def setUp(self):
        self.organizationrole = organization_role_ice._M_com.jimi.api.user.organization  # organization_role 文件实例
        self.organizationrole_dto = organization_role_dto_ice._M_com.jimi.api.user.organization.dto  # organization_role_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.organizationeoleapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyRoleManager类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyRoleManager类用例结束***********')


class MySystemMember(unittest.TestCase):
    def setUp(self):
        self.systemmember = system_member_ice._M_com.jimi.api.user.system  # system_member 文件实例
        self.systemmember_dto = system_member_dto_ice._M_com.jimi.api.user.system.dto# system_member_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.systemmemberapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyMemberManager类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyMemberManager类用例结束***********')


class MySystemGroup(unittest.TestCase):
    pass


class MySystemRole(unittest.TestCase):
    pass


class MySystemPermission(unittest.TestCase):
    pass


class MyAppUser(unittest.TestCase):
    def setUp(self):
        self.appuser = appuser_ice._M_com.jimi.api.user.app  # appuser 文件实例
        self.appuser_dto = appuser_dto_ice._M_com.jimi.api.user.app.dto  # appuser_dto 文件实例
        self.common = common_ice._M_com.jimi.api  # common 文件实例
        self.account = self.common.CurrentAccount()
        self.url = basic_config.ConfigInit.appuserapi_url
        self.communicator = Ice.initialize(sys.argv)
        self.base = self.communicator.stringToProxy(self.url)
        logger.info('********MyAppUser类用例开始***********')

    def tearDown(self):
        self.communicator.destroy()
        logger.info('********MyAppUser类用例结束***********')