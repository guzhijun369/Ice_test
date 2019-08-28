# coding=utf-8
from loguru import logger
from public import mytest
# from ddt import ddt, data, unpack
import Ice


class MemberManager(mytest.MyMemberManager):
    """成员管理接口"""

    def test_add_member(self):
        """添加成员"""
        printer = self.systemmember.MemberManagerServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        member_info = self.header.AddMemberInputDTO(name='谷志军', email='281878321@qq.com', describe='这是一个测试账号', password='q5310543', operator=0)
        logger.info('调用addMember类接口，发送参数member_info:{}'.format(member_info))
        try:
            r = printer.addMember(member_info)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))