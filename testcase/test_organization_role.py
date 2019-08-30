# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class OrganizationRole(mytest.MyOrganizationRole):
    """角色管理接口"""

    def test_find_byoid(self):
        """查询机构角色基本信息"""
        printer = self.organizationrole.OrganizationRoleApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = 69358797717505  # 机构id
        logger.info('调用findByOid接口，发送参数:oid:{}'.format(oid))
        try:
            r = printer.findByOid(oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_add_role(self):
        """添加角色"""
        printer = self.organizationrole.OrganizationRoleApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        role_info = self.organizationrole_dto.AddRoleInput(operator='', platform='TUQIANG',oid='69358797717505', name='悲伤的', memo='拥有财务权限')
        logger.info('调用addRole接口，发送参数:role_info:{}'.format(role_info))
        try:
            r = printer.addRole(self.account, role_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_role(self):
        """删除角色"""
        printer = self.organizationrole.OrganizationRoleApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        role_id = '5d68caa736e28a31d9813dad'  # 角色id
        logger.info('调用deleteRole接口，发送参数:role_id:{}'.format(role_id))
        try:
            r = printer.deleteRole(self.account, role_id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_authorize(self):
        """授权"""
        printer = self.organizationrole.OrganizationRoleApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        uid = 69358797717504
        role_id = ['5d68ca1636e28a25fd1a078a']
        logger.info('调用authorize接口，发送参数:uid:{},role_id:{}'.format(uid, role_id))
        try:
            r = printer.authorize(self.account, uid, role_id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))
