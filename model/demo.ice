[["java:package:com.jimi.test"]]
module ticket {

	exception TestException
	{
    string code;
    string msg;
    };
	
	/**
	 * 订单信息
	 */
	struct Order {
		/**
		 * 订单号
		 */
		long orderId;
		// 手机号
		string phone;
		string orderNum;
		long orderDate;
		int ticketType;
		double amount;
		int orderStatus;
	};

	sequence<Order> orderSeq;
	
	/**订单业务类*/
	interface OrderService {
		/**创建订单
		@param  myOrder 订单信息
		@return */
		bool createOrder(Order myOrder) throws TestException;
		orderSeq queryByPhone(string phone);
		bool cannelOrder(long orderId) throws TestException;
	};
};

module sms {
	interface SMSService {
		void sendSmsMsg(string msg);
	};
};