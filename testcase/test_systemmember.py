# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class SystemMember(mytest.MySystemMember):
    """成员管理接口"""

    def test_add_member(self):
        """添加成员"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        member_info = self.systemmember_dto.AddMemberInputDTO(name='谷志军', email='281878321@qq.com', describe='这是一个测试账号', password='q5310543', operator=0)
        logger.info('调用addMember接口，发送参数member_info:{}'.format(member_info))
        try:
            r = printer.addMember(member_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_member(self):
        """更新成员信息"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        member_info = self.systemmember_dto.UpdateMemberInputDTO(id='5d68c31736e28a25fd1a0756', name='古城', email='3221@qq.com', describe='这是更新数据', operator=0)
        logger.info('调用updateMember接口，发送参数member_info:{}'.format(member_info))
        try:
            r = printer.updateMember(member_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_delete_member(self):
        """删除成员"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        uid = '69426279874563'
        logger.info('调用deleteMember接口，发送参数uid:{}'.format(uid))
        try:
            r = printer.deleteMember(uid, 0)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_login_auth(self):
        """成员登录"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        email = '69426279874563'
        password = ''
        logger.info('调用loginAuth接口，发送参数email:{},password:{}'.format(email, password))
        try:
            r = printer.loginAuth(email, password)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_get_info(self):
        """获取成员信息"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        logger.info('调用findById接口，发送参数id:{}'.format(id))
        try:
            r = printer.findById(id)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_update_password(self):
        """更新成员密码"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        password = ''
        operator = 0
        logger.info('调用updatePassword接口，发送参数id:{},password:{}'.format(id, password))
        try:
            r = printer.updatePassword(id, password, operator)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_reset_password(self):
        """重置成员密码"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        operator = 0
        logger.info('调用resetPassword接口，发送参数id:{}'.format(id))
        try:
            r = printer.resetPassword(id, operator)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_enable_member(self):
        """启用成员"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        operator = 0
        logger.info('调用enableMember接口，发送参数id:{}'.format(id))
        try:
            r = printer.enableMember(id, operator)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_disable_member(self):
        """禁用成员"""
        printer = self.systemmember.SystemMemberApiPrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        id = ''
        operator = 0
        logger.info('调用disableMember接口，发送参数id:{}'.format(id))
        try:
            r = printer.disableMember(id, operator)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))