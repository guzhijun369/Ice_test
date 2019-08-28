module com {
module jimi {
module user {
module api {
module system {
module dto {

/**
 * 当前会话账号信息
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct CurrentAccount {
    /**
     * 账号id
     **/
    long uid;
    /**
     * 机构id
     **/
    long oid;
    /**
     * 平台code
     **/
    long code;
};

/**
 * 应用极光推送 Key 和 Secret
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct PushClient {
    /** Client ID **/
    string clientId;

    /** Client Secret **/
    string clientSecret;
};

/**
 * 平台和应用 Key 和 Secret
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct Client {
    /** Client ID **/
    string clientId;

    /** Client Secret **/
    string clientSecret;
};

/**
 * 创建平台APP输入参数
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct PlatformAppInputDTO {
    /** 应用ID **/
    string appId;

    /** 图标 **/
    string icon;

    /** 平台类型 **/
    int type;

    /** 平台code **/
    string code;

    /** 域名 **/
    string domain;

    /** 联系人 **/
    string contact;

    /** 是否是生产环境 **/
    bool production;

    /** 短信ID **/
    string smsId;

    /** 平台APP配置推送信息 **/
    PushClient push;
}

/**
 * 创建平台输入数据
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct PlatformInputDTO {

    /** 平台编号 **/
    string code;

    /** 平台名称 **/
    string name;

    /** 平台地址 **/
    string address;

    /** 平台描述 **/
    string desc;

    /** 平台创建用户ID **/
    string createUserId;

    /** 平台更新用户ID **/
    string updateUserId;
};

/**
 * 平台APP创建输出数据
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct PlatformAppOutputDTO {
    /** 应用ID **/
    string appId;

    /** 图标 **/
    string icon;

    /** 平台类型 **/
    int type;

    /** 平台code **/
    string code;

    /** 域名 **/
    string domain;

    /** 联系人 **/
    string contact;

    /** 是否是生产环境 **/
    bool production;

    /** 短信ID **/
    string smsId;

    /** 平台APP配置推送信息 **/
    PushClient push;

    /** 平台Client信息 **/
    Client client;
}

/**
 * 平台创建输出数据
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
["java:getset"]
struct PlatformOutputDTO {

    /** 平台编号 **/
    string code;

    /** 平台名称 **/
    string name;

    /** 平台地址 **/
    string address;

    /** 平台描述 **/
    string desc;

    /** 平台创建用户 **/
    string createUserId;

    /** 平台更新用户 **/
    string updateUserId;

    /** 平台登录接口权限校验 **/
    Client client;

    /** 平台创建时间 **/
    long gmtCreate;

    /** 平台更新时间 **/
    long gmtModified;
};

};};};};};};