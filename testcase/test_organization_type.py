# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class OrganizationType(mytest.MyOrganizationType):
    """机构类型服务接口"""
    def test_existsbycode(self):
        """检查机构类型code是否存在"""
        printer = self.organizationtype.OrganizationTypeApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        code = 'Department'
        logger.info('调用existsByCode接口，发送参数code:{}'.format(code))
        try:
            r = printer.existsByCode(code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_add_organizationtype(self):
        """添加机构类型"""
        printer = self.organizationtype.OrganizationTypeApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        organizationtype_info = self.organizationtype_dto.OrganizationTypeInputDTO(operator='0', platform='TUQIANG', code='group', name='小组')
        logger.info('调用addOrganizationType接口，发送参数organizationtype_info:{}'.format(organizationtype_info))
        try:
            r = printer.addOrganizationType(organizationtype_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_organizationtype(self):
        """更新机构类型"""
        printer = self.organizationtype.OrganizationTypeApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        organizationtype_info = self.organizationtype_dto.OrganizationTypeInputDTO(operator='0', platform='CESHI', code='Agent', name='代理商12')
        logger.info('调用updateOrganizationType接口，发送参数organizationtype_info:{}'.format(organizationtype_info))
        try:
            r = printer.updateOrganizationType(organizationtype_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_get_organizationtype(self):
        """根据平台获取机构类型列表"""
        printer = self.organizationtype.OrganizationTypeApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform = 'CESHI'
        pagesize =10
        pagenum = 0
        logger.info('调用findOrganizationTypeByPlatform接口，发送参数：platform:{},pagenum:{},pagesize{}'.format(platform, pagenum, pagesize))
        try:
            r = printer.findOrganizationTypeByPlatform(platform, pagenum, pagesize)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_organizationtype_info(self):
        """根据code获取机构类型信息"""
        printer = self.organizationtype.OrganizationTypeApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        organizationtype_code = 'Agent1'
        logger.info('调用findOrganizationTypeByCode接口，发送参数：organizationtype_code:{}'.format(organizationtype_code))
        try:
            r = printer.findOrganizationTypeByCode(organizationtype_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_organizationtype(self):
        """删除机构类型"""
        printer = self.organizationtype.OrganizationTypeApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        code = 'Agent'
        logger.info('调用deleteOrganizationTypeBy接口，发送参数：code:{}'.format(code))
        try:
            r = printer.deleteOrganizationTypeBy(self.account, code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))