from loguru import logger
from public import mytest
from ddt import ddt, data, unpack


class Send(mytest.MySms):
    def test_send_sms(self):
        printer = self.sms.SMSServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        send_msg = '你好'
        logger.info('调用sendSmsMsg类接口，发送参数：{}'.format(send_msg))
        try:
            r = printer.sendSmsMsg('send_msg')
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


