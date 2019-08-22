[["java:package:com.jimi.test"]]
module ticket {

	exception TestException
	{
    string code;
    string msg;
    };
	
	/**
	 * ������Ϣ
	 */
	struct Order {
		/**
		 * ������
		 */
		long orderId;
		// �ֻ���
		string phone;
		string orderNum;
		long orderDate;
		int ticketType;
		double amount;
		int orderStatus;
	};

	sequence<Order> orderSeq;
	
	/**����ҵ����*/
	interface OrderService {
		/**��������
		@param  myOrder ������Ϣ
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