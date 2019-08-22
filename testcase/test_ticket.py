import sys
import Ice
from public import mytest
from loguru import logger
import json
from ddt import ddt,data,unpack

class Login(mytest.MyTicket):

    def test_createorder(self):
        printer = self.ticket.OrderServicePrx.checkedCast(self.base)
        logger.info('连接 {} 服务'.format(self.url))
        if not printer:
            raise RuntimeError("Invalid proxy")
        order = self.ticket.Order(orderId=333, phone='13028812388', orderNum='0182', orderDate=20190819,
                                         ticketType=1, amount=3.8, orderStatus=1)

        order_dict = order.__dict__
        logger.info('调用createOrder类接口，发送参数：{}'.format(json.dumps(order_dict)))
        try:
            r = printer.createOrder(order)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))


    def test_cannelorder(self):
        printer = self.ticket.OrderServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        order_id = 123456
        logger.info('调用cannelOrder类接口，发送参数：{}'.format(order_id))
        try:
            r = printer.cannelOrder(order_id)
            logger.info('success，返回：{}'.format(json.dumps(r)))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))

    def test_queryphone(self):
        printer = self.ticket.OrderServicePrx.checkedCast(self.base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        phone = '13028812388'
        logger.info('调用queryByPhone类接口，发送参数：{}'.format(phone))
        try:
            r = printer.queryByPhone(phone)
            logger.info('success，返回：{}'.format(r))
        except Exception as e:
            logger.error('fail，错误：{}'.format(e))
