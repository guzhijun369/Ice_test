# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class AppUser(mytest.MyAppUser):
    """App用户接口"""

    def test_add_appuser(self):
        """添加APP用户信息"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        app_info = self.appuser_dto.AddAppUserInputDTO(operator='0', platform='TUQIANG', phone='130288123881', nickName='谷志军1', password='q5310543')
        logger.info('调用addAppUser接口，发送参数app_info:{}'.format(app_info))
        try:
            r = printer.addAppUser(app_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_appuser(self):
        """更新APP用户信息"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        app_info = self.appuser_dto.UpdateAppUserInputDTO(operator='', platform='', id='5d68ed1336e28a6015f5cd6d', nickName='111')
        logger.info('调用updateAppUser接口，发送参数app_info:{}'.format(app_info))
        try:
            r = printer.updateAppUser(app_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_get_user_list(self):
        """获取用户列表(搜索)"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        dto = self.appuser_dto.FindListInputDTO(operator='', platform='', id='5d68e9db36e28a6015f5cd6c', phone='13028812388')
        pagenum = 0
        pagesize = 10
        logger.info('调用findPage接口，发送参数dto:{},pagenum:{}，pagesize:{}'.format(dto, pagenum, pagesize))
        try:
            r = printer.findPage(dto, pagenum, pagesize)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_login_auth(self):
        """登录认证"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        phone = '130288123881'
        password = 'q5310543'
        logger.info('调用loginAuth接口，发送参数phone:{},password:{}'.format(phone, password))
        try:
            r = printer.loginAuth(phone, password)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_get_userinfo(self):
        """获取用户信息"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        logger.info('调用findById接口，发送参数id:{}'.format(id))
        try:
            r = printer.findById(id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_pw(self):
        """修改密码"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        password = ''
        logger.info('调用updatePassword接口，发送参数id:{},password'.format(id, password))
        try:
            r = printer.updatePassword(id, password)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_pw(self):
        """重置密码"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        logger.info('调用resetPassword接口，发送参数id:{}'.format(id))
        try:
            r = printer.resetPassword(id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_enableappuser(self):
        """启用账号"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        logger.info('调用enableAppUser接口，发送参数id:{}'.format(id))
        try:
            r = printer.enableAppUser(id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_disableappuser(self):
        """禁用账号"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        logger.info('调用disableAppUser接口，发送参数id:{}'.format(id))
        try:
            r = printer.disableAppUser(id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_bind_org(self):
        """绑定用户到组织"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''  # 用户id
        orgId = ''  # 组织id
        logger.info('调用bindOrg接口，发送参数id:{}，orgId:{}'.format(id, orgId))
        try:
            r = printer.bindOrg(id, orgId)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_unbind_org(self):
        """解绑组织用户"""
        printer = self.appuser.AppUserApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''  # 用户id
        orgId = ''  # 组织id
        logger.info('调用unbindOrg接口，发送参数id:{}，orgId:{}'.format(id, orgId))
        try:
            r = printer.unbindOrg(id, orgId)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))