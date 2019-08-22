from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class Generated(mytest.MyPlatform):
    def test_add_platform(self):
        printer = self.generated.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_info = self.header.PlatformInputDTO(code='111', name='途强在线', address='www.baidu', desc='这是一个测试平台',
                                                     createMemberId='1', updateMemberId='1')
        logger.info('调用addPlatform类接口，发送参数：{}'.format(platform_info))
        try:
            r = printer.addPlatform(platform_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_platform(self):
        printer = self.generated.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_info = self.header.PlatformInputDTO(code='179825190822110171', name='途强在线11', address='www.baidu11',
                                                     desc='这是一个测试平台11',
                                                     createMemberId='1', updateMemberId='1')
        logger.info('调用updatePlatform类接口，发送参数：{}'.format(platform_info))
        try:
            r = printer.updatePlatform(platform_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_platform(self):
        printer = self.generated.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = '174679190822104018'
        logger.info('调用deletePlatformBy类接口，发送参数：{}'.format(platform_code))
        try:
            r = printer.deletePlatformBy(platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_getall_platform(self):
        printer = self.generated.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        logger.info('调用deletePlatformBy类接口，发送参数：{}')
        try:
            r = printer.getAllPlatform()
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_platform_client_secret(self):
        printer = self.generated.PlatformServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        platform_code = '174679190822104018'
        logger.info('调用deletePlatformBy类接口，发送参数：{}')
        try:
            r = printer.updatePlatformClientSecret(platform_code)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))