from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class Platform(mytest.MyPlatform):
    """平台管理接口"""
    def test_add_platform(self):
        """添加平台信息"""
        printer = self.platform.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_info = self.header.PlatformInputDTO(code='111', name='途强风控', address='www.baidu.com', desc='这是测试的第一个数据',
                                                     createUserId='1', updateUserId='1')
        logger.info('调用addPlatform类接口，发送参数platform_info:{}'.format(platform_info))
        try:
            r = printer.addPlatform(self.account, platform_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_platform(self):
        """更新平台信息"""
        printer = self.platform.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_info = self.header.PlatformInputDTO(code='a11ebe0734cb47f5', name='途强风控1', address='www.baidu.com1',
                                                     desc='这是测试更新的第一个数据', createUserId='11', updateUserId='11')
        logger.info('调用addPlatform类接口，发送参数platform_info:{}'.format(platform_info))
        try:
            r = printer.updatePlatform(self.account, platform_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_platform(self):
        """删除平台信息"""
        printer = self.platform.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'a11ebe0734cb47f5'
        logger.info('调用deletePlatformBy类接口，发送参数：{}'.format(platform_code))
        try:
            r = printer.deletePlatformBy(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_getall_platform(self):
        """获取所有平台信息"""
        printer = self.platform.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        logger.info('调用deletePlatformBy类接口，发送参数：{}')
        try:
            r = printer.getAllPlatform(self.account)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_platform_client_secret(self):
        """重置平台Client相关内容"""
        printer = self.platform.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'c822d8bdd6214980'
        logger.info('调用resetPlatformClientSecret类接口，发送参数platform_code：{}'.format(platform_code))
        try:
            r = printer.resetPlatformClientSecret(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_lookup_platform_client_secret(self):
        """查看平台 Client Secret"""
        printer = self.platform.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'c822d8bdd6214980'
        logger.info('调用lookupPlatformClientSecret类接口，发送参数platform_code：{}'.format(platform_code))
        try:
            r = printer.lookupPlatformClientSecret(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


class PlatformApp(mytest.MyPlatformApp):
    """平台APP管理接口"""
    def test_add_application(self):
        """添加平台app信息"""
        printer = self.platform.ApplicationServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_app_info = self.header.PlatformAppInputDTO(appId='1112', icon='https://img.dsjakh111', type=1, code='111222',
                                                            domain='tuqiangapp.com', contact='13028812389', production=True,
                                                            smsId='9528', push=Ice._struct_marker)
        logger.info('调用addApplication类接口，发送参数:platform_app_info:{}'.format(platform_app_info))
        try:
            r = printer.addApplication(self.account, platform_app_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_application(self):
        """更新平台App信息"""
        printer = self.platform.ApplicationServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_app_info = self.header.PlatformAppInputDTO(appId='92f8430aedb44f64', icon='http:img/icon12', type=2,
                                                            code='465376190823170339',
                                                            domain='tuqiang.com', contact='1302881238812', production=True,
                                                            smsId='32112', push=Ice._struct_marker)
        logger.info('调用updateApplication类接口，发送参数:platform_app_info:{}'.format(platform_app_info))
        try:
            r = printer.updateApplication(self.account, platform_app_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_application(self):
        """删除平台APP信息"""
        printer = self.platform.ApplicationServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_appid = '92f8430aedb44f64'
        logger.info('调用deleteApplicationBy类接口，发送参数:platform_appid:{}'.format(platform_appid))
        try:
            r = printer.deleteApplicationBy(self.account, platform_appid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_getall_applications(self):
        """获取所有平台App信息"""
        printer = self.platform.ApplicationServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        logger.info('调用getAllApplications类接口，发送参数：{}')
        try:
            r = printer.getAllApplications(self.account)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_application_client_secret(self):
        """重置平台APP Client相关内容"""
        printer = self.platform.ApplicationServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = '14bc9aa199c44f35'
        logger.info('调用resetApplicationClientSecret类接口，发送参数platform_code：{}'.format(platform_code))
        try:
            r = printer.resetApplicationClientSecret(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_lookup_application_client_secret(self):
        """查看平台APP Client Secret"""
        printer = self.platform.ApplicationServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = '14bc9aa199c44f35'
        logger.info('调用lookupApplicationClientSecret类接口，发送参数platform_code：{}'.format(platform_code))
        try:
            r = printer.lookupApplicationClientSecret(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


