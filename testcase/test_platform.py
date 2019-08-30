from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class Platform(mytest.MyPlatform):
    """平台管理接口"""

    def test_add_platform(self):
        """添加平台信息"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_info = self.platform_dto.PlatformInputDTO(operator='0', platform='', code='SHANCHU', name='测试平台', address='www.baidu.com',
                                                  desc='这是一个测试平台')
        logger.info('调用addPlatform接口，发送参数platform_info:{}'.format(platform_info))
        try:
            r = printer.addPlatform(platform_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_platform(self):
        """更新平台信息"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        # 平台里code是唯一标识
        platform_info = self.platform_dto.PlatformInputDTO(operator='0', platform='', code='CESHI', name='测试平台', address='www.baidu.com',
                                                  desc='这是一个测试平台')
        logger.info('调用addPlatform接口，发送参数platform_info:{}'.format(platform_info))
        try:
            r = printer.updatePlatform(platform_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_platform(self):
        """删除平台信息"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'SHANCHU'
        logger.info('调用deletePlatformBy接口，发送参数：{}'.format(platform_code))
        try:
            r = printer.deletePlatformBy(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_getall_platform(self):
        """获取所有平台信息"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        pagenum = 0  # 页码
        pagesize = 10  # 每页数量
        logger.info('调用getAllPlatform接口，发送参数：pagenum:{},pagesize{}'.format(pagenum, pagesize))
        try:
            r = printer.getAllPlatform(pagenum, pagesize)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_find_platform(self):
        """通过code获取平台信息"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platformCode = 'CESHI'
        logger.info('调用findPlatformByCode接口，发送参数：platformCode:{}'.format(platformCode))
        try:
            r = printer.findPlatformByCode(platformCode)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_platform_client_secret(self):
        """重置平台Client相关内容"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'CESHI'
        logger.info('调用resetPlatformClientSecret类接口，发送参数platform_code：{}'.format(platform_code))
        try:
            r = printer.resetPlatformClientSecret(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_lookup_platform_client_secret(self):
        """查看平台 Client Secret"""
        printer = self.platform.PlatformApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = 'CESHI'
        logger.info('调用lookupPlatformClientSecret类接口，发送参数platform_code：{}'.format(platform_code))
        try:
            r = printer.lookupPlatformClientSecret(self.account, platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


class Application(mytest.MyApplication):
    """平台APP管理接口"""

    def test_add_application(self):
        """添加平台app信息"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        push = self.platform_dto.ClientDTO()
        application_info = self.platform_dto.PlatformAppInputDTO(operator='0', platform='CESHI', appId='2341', icon='https://tubiao.com', name='测试APP', type=1, code='CESHIAPP',
                                                        domain='ceshi.com', contact='谷志军22', production=False, smsId='086', push=push)
        logger.info('调用addApplication类接口，发送参数:platform_app_info:{}'.format(application_info))
        try:
            r = printer.addApplication(application_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_application(self):
        """更新平台App信息"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        # 平台里appID是唯一标识
        push = self.platform_dto.ClientDTO()
        application_info = self.platform_dto.PlatformAppInputDTO(operator='0', platform='CESHI', appId='ffebaf59032f49ac', icon='https://tubiao.com', name='测试APP', type=1, code='CESHIAPP',
                                                        domain='ceshi.com', contact='谷志军', production=False, smsId='0861', push=push)
        logger.info('调用updateApplication类接口，发送参数:platform_app_info:{}'.format(application_info))
        try:
            r = printer.updateApplication(self.account, application_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_application(self):
        """删除平台APP信息"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_appid = '4b5029508c56419c'  # appID
        logger.info('调用deleteApplicationBy类接口，发送参数:platform_appid:{}'.format(platform_appid))
        try:
            r = printer.deleteApplicationBy(self.account, platform_appid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_getall_applications(self):
        """获取所有平台App信息"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        pagenum = 0  # 页码
        pagesize = 10  # 每页数量
        logger.info('调用getAllApplications接口，发送参数：pagenum:{},pagesize{}'.format(pagenum, pagesize))
        try:
            r = printer.getAllApplications(pagenum, pagesize)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_get_application(self):
        """通过appID获取指定的APP信息"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_appid = 'ffebaf59032f49ac'
        logger.info('调用getApplicationByAppId接口，发送参数：platform_appid:{}'.format(platform_appid))
        try:
            r = printer.getApplicationByAppId(platform_appid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_application_client_secret(self):
        """重置平台APP Client相关内容"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_appid = 'ffebaf59032f49ac'
        logger.info('调用resetApplicationClientSecret类接口，发送参数platform_appid：{}'.format(platform_appid))
        try:
            r = printer.resetApplicationClientSecret(self.account, platform_appid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_lookup_application_client_secret(self):
        """查看平台APP Client Secret"""
        printer = self.platform.ApplicationApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_appid = 'ffebaf59032f49ac'
        logger.info('调用lookupApplicationClientSecret类接口，发送参数platform_appid：{}'.format(platform_appid))
        try:
            r = printer.lookupApplicationClientSecret(platform_appid)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))
