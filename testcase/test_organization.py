# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class AccountManager(mytest.MyAccountManager):
    """账号管理接口"""

    def test_get_organization_type(self):
        """获取机构类型列表"""
        printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'TUQIANG'
        logger.info('调用getOrganizationType类接口，发送参数platform_code:{}'.format(platform_code))
        try:
            r = printer.getOrganizationType(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_add_account(self):
        """添加账号"""
        printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        account_info = self.header.AddAccountInput(oid=0, userName='谷志军', password='q5310543', nickName='guzhijun',
                                                   phone='13028812388', email='281878321@qq.com')
        logger.info('调用addAccount类接口，发送参数account_info:{}'.format(account_info))
        try:
            r = printer.addAccount(self.account, account_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_disabled_account(self):
        """启用/禁用账号"""
        printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = 68308409778178  # 平台账号id
        operating = False  # 启用/禁用
        logger.info('调用disabledAccount类接口，发送参数:id:{},operating:{}'.format(id, operating))
        try:
            r = printer.disabledAccount(self.account, id, operating)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_account(self):
        """删除账号"""
        printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = 68308409778179  # 平台账号id
        logger.info('调用deleteAccount类接口，发送参数:id:{}'.format(id))
        try:
            r = printer.deleteAccount(self.account, id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_password(self):
        """重置密码"""
        printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = 68308409778180  # 平台账号id
        logger.info('调用resetPassword接口，发送参数:id:{}'.format(id))
        try:
            r = printer.resetPassword(self.account, id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_by_oid(self):
        """查询账号信息"""
        printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 0  # 机构oid
        logger.info('调用findByOid接口，发送参数:oid:{}'.format(oid))
        try:
            r = printer.findByOid(self.account, oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


class OrganizationManager(mytest.MyOrganizationManager):
    """机构管理接口"""

    def test_add_organization(self):
        """添加机构"""
        printer = self.organizationmanager.OrganizationManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        account_info = self.header.AddOrganizationInput(parent=68308409778176, code='Organization', name='谷志军下第san个部门',
                                                        email='1281878321@qq.com',
                                                        contact='研发部', phone='13028812387', province='广东省', city='深圳市',
                                                        region='宝安区',
                                                        details='高新奇综合楼四楼BC区')
        logger.info('调用addOrganization类接口，发送参数account_info:{}'.format(account_info))
        try:
            r = printer.addOrganization(self.account, account_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_disabled_organization(self):
        """禁用/启用机构"""
        printer = self.organizationmanager.OrganizationManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 68308409778176  # 机构id
        operating = False  # 启用/禁用
        logger.info('调用disabledOrganization接口，发送参数:id:{},operating:{}'.format(oid, operating))
        try:
            r = printer.disabledOrganization(self.account, oid, operating)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_findall_child_byOid(self):
        """查询下级机构基本信息"""
        printer = self.organizationmanager.OrganizationManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 68308409778176  # 机构id
        logger.info('调用findAllChildByOid接口，发送参数:id:{}'.format(oid))
        try:
            r = printer.findAllChildByOid(self.account, oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_byoid(self):
        """查询机构基本信息"""
        printer = self.organizationmanager.OrganizationManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 68308409778182  # 机构id
        logger.info('调用findByOid接口，发送参数:id:{}'.format(oid))
        try:
            r = printer.findByOid(self.account, oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_organization(self):
        """删除机构"""
        printer = self.organizationmanager.OrganizationManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 68308409778183  # 机构id
        logger.info('调用deleteOrganization接口，发送参数:oid:{}'.format(oid))
        try:
            r = printer.deleteOrganization(self.account, oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


class RoleManager(mytest.MyRoleManager):
    """角色管理接口"""
    def test_find_byoid(self):
        """查询机构角色基本信息"""
        printer = self.organizationmanager.RoleManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 68308409778176  # 机构id
        logger.info('调用findByOid接口，发送参数:oid:{}'.format(oid))
        try:
            r = printer.findByOid(self.account, oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_add_role(self):
        """添加角色"""
        printer = self.organizationmanager.RoleManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        role_info = self.header.AddRoleInput(oid=68308409778176, name='普通客服', memo='普通客服员工')
        logger.info('调用addRole接口，发送参数:role_info:{}'.format(role_info))
        try:
            r = printer.addRole(self.account, role_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_role(self):
        """删除角色"""
        printer = self.organizationmanager.RoleManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        role_id = '5d64d9a0f0313058672757a7'  # 角色id
        logger.info('调用deleteRole接口，发送参数:role_id:{}'.format(role_id))
        try:
            r = printer.deleteRole(self.account, role_id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_authorize(self):
        """授权"""
        printer = self.organizationmanager.RoleManagerPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        uid = 68308409778180
        role_id = ['5d64d8a8f0313058672757a5']
        logger.info('调用authorize接口，发送参数:uid:{},role_id:{}'.format(uid, role_id))
        try:
            r = printer.authorize(self.account, uid, role_id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


