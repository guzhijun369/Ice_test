# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class OrganizationAccount(mytest.MyOrganizationAccount):
    """账号管理接口"""

    def test_get_organization_type(self):
        """获取机构类型列表"""
        printer = self.organizationaccount.OrganizationAccountApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'TUQIANG'
        logger.info('调用getOrganizationType类接口，发送参数platform_code:{}'.format(platform_code))
        try:
            r = printer.getOrganizationType(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_save_account(self):
        """添加/修改账号"""
        printer = self.organizationaccount.OrganizationAccountApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        account_info = self.organizationaccount_dto.AccountInputDTO(operator='0', platform='TUQIANG', uid='69358797717504', oid=' ',
                                                                    userName='guzhijun', password='q53105431', nickName='谷志军1',
                                                                    phone='130288123881', email='2818783211@qq.com')  # 修改时，username不可改
        logger.info('调用save接口，发送参数account_info:{}'.format(account_info))
        try:
            r = printer.save(self.account, account_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_disabled_account(self):
        """启用/禁用账号"""
        printer = self.organizationaccount.OrganizationAccountApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = '69358797717504'  # 平台账号id
        operating = False  # 启用/禁用
        logger.info('调用disable类接口，发送参数:id:{},operating:{}'.format(id, operating))
        try:
            r = printer.disable(self.account, id, operating)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    # def test_delete_account(self):
    #     """删除账号"""
    #     printer = self.accountmanager.AccountManagerPrx.checkedCast(self.base)
    #     if not printer:
    #         raise RuntimeError("Invalid proxy")
    #     id = 68308409778179  # 平台账号id
    #     logger.info('调用deleteAccount类接口，发送参数:id:{}'.format(id))
    #     try:
    #         r = printer.deleteAccount(self.account, id)
    #         logger.info('success，返回：{}'.format(r))
    #     except Exception as e:
    #         logger.error('fail，错误：{}'.format(e))

    def test_reset_password(self):
        """重置密码"""
        printer = self.organizationaccount.OrganizationAccountApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = '69358797717504'  # 平台账号id
        logger.info('调用resetPassword接口，发送参数:id:{}'.format(id))
        try:
            r = printer.resetPassword(self.account, id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_by_oid(self):
        """查询账号信息"""
        printer = self.organizationaccount.OrganizationAccountApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        data = self.organizationaccount_dto.AccountPageInputDTO(operator='', platform='', page=1, size=10, oid='0')
        logger.info('调用page接口，发送参数:data:{}'.format(data))
        try:
            r = printer.page(data)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

