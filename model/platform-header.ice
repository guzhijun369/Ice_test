module com {
module jimi {
module user {
module api {
module system {
module dto {
["java:getset"]
struct PushClient {
    /** Client ID **/
    string clientId;

    /** Client Secret **/
    string clientSecret;
};

["java:getset"]
struct Client {
    /** Client ID **/
    string clientId;

    /** Client Secret **/
    string clientSecret;
};

["java:getset"]
struct Member {
    /** 用户ID **/
    string userId;

    /** 用户名称 **/
    string name;
};

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
    string createMemberId;

    /** 平台更新用户ID **/
    string updateMemberId;
};

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
    Member create;

    /** 平台更新用户 **/
    Member update;

    /** 平台登录接口权限校验 **/
    Client client;

    /** 平台创建时间 **/
    long gmtCreate;

    /** 平台更新时间 **/
    long gmtModified;
};

};};};};};};