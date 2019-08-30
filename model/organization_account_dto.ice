#include "./common.ice"
module com { module jimi { module api { module user { module organization {
module dto {
    /**
     * 账号基本信息
     *
     * @date 2019年8月21日 上午11:27:37
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class AccountOutputDTO extends com::jimi::api::BaseOutputDTO {
        /** 账号id*/
        string uid;
        /** 用户名(可用于登录)*/
        string userName;
        /** 昵称*/
        string nickName;
        /** 手机号(可用于登录)*/
        string phone;
        /** 邮箱(可用于登录)*/
        string email;
    }
    /**
     * 添加账号输入
     *
     * @date 2019年8月21日 上午11:27:37
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class AccountInputDTO extends com::jimi::api::BaseInputDTO {
        /** 账号id*/
        string uid;
        /** 机构id*/
        string oid;
        /** 用户名(可用于登录)*/
        string userName;
        /** 密码*/
        string password;
        /** 昵称*/
        string nickName;
        /** 手机号(可用于登录)*/
        string phone;
        /** 邮箱(可用于登录)*/
        string email;
    }

    /**
     * 账号基本信息
     *
     * @date 2019年8月21日 上午11:27:37
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class AccountPageInputDTO extends com::jimi::api::BasePageInputDTO {
        /** 机构id*/
        string oid;
    }

    /**
     * 自定义参数AccountList
     **/
    ["java:type:java.util.ArrayList<AccountOutputDTO>"]
    sequence<AccountOutputDTO> AccountList;

    /**
     * 账号基本信息
     *
     * @date 2019年8月21日 上午11:27:37
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class AccountPageOutputDTO extends com::jimi::api::BasePageOutputDTO {
        /** 分页结果*/
        AccountList data;
    }
}
}}}}}