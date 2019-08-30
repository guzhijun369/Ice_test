# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class Organization(mytest.MyOrganization):
    """机构管理接口"""

    def test_add_organization(self):
        """添加/修改机构"""
        printer = self.organization.OrganizationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        account_info = self.organization_dto.OrganizationInputDTO(operator='', platform='TUQIANG', oid='', parent='69426279874561',
                                                                  code='Department', name='这是低级机构1', email='28181121@qq.com',
                                                                  contact='古城1', phone='13028812388',
                                                                  province='广东省', city='深圳市', region='宝安区', detail='高新奇',
                                                                  appId='1sdfd1111', appSecret='sadasd', domain='gucheng.com',
                                                                  logo='http://jsdjkhdjka.com')
        logger.info('调用save接口，发送参数account_info:{}'.format(account_info))
        try:
            r = printer.save(account_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_disabled_organization(self):
        """禁用/启用机构"""
        printer = self.organization.OrganizationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = '69358797717505'  # 机构id
        operating = False  # 启用/禁用
        logger.info('调用disable接口，发送参数:id:{},operating:{}'.format(oid, operating))
        try:
            r = printer.disable(self.account, oid, operating)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_child_byOid(self):
        """查询下级机构基本信息"""
        printer = self.organization.OrganizationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = '69358797717505'  # 机构id
        logger.info('调用findChildrenByOid接口，发送参数:id:{}'.format(oid))
        try:
            r = printer.findChildrenByOid(oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_byoid(self):
        """查询机构基本信息"""
        printer = self.organization.OrganizationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = '69358797717505'  # 机构id
        logger.info('调用findByOid接口，发送参数:id:{}'.format(oid))
        try:
            r = printer.findByOid(oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_organization(self):
        """删除机构"""
        printer = self.organization.OrganizationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        oid = '69426279874560'  # 机构id
        logger.info('调用delete接口，发送参数:oid:{}'.format(oid))
        try:
            r = printer.delete(self.account, oid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


