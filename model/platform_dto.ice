#include "./common.ice"
module com { module jimi { module api { module user { module system {
module dto {
    /**
     * 平台和应用 Key 和 Secret
     *
     * @date 2019年8月23日 上午10:05:28
     * @author lcy
     * @version 1.0
     **/
    ["java:getset"]
    class ClientDTO {
        /** Client ID **/
        string clientId;

        /** Client Secret **/
        string clientSecret;
    }

    /**
     * 创建平台APP输入参数
     *
     * @date 2019年8月23日 上午10:05:28
     * @author lcy
     * @version 1.0
     **/
    ["java:getset"]
    class PlatformAppInputDTO extends com::jimi::api::BaseInputDTO {
        /** 应用ID **/
        string appId;

        /** 图标 **/
        string icon;

        /** 应用名称 **/
        string name;

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
        ClientDTO push;
    }

    /**
     * 创建平台输入数据
     *
     * @date 2019年8月23日 上午10:05:28
     * @author lcy
     * @version 1.0
     **/
    ["java:getset"]
    class PlatformInputDTO extends com::jimi::api::BaseInputDTO {

        /** 平台编号 **/
        string code;

        /** 平台名称 **/
        string name;

        /** 平台地址 **/
        string address;

        /** 平台描述 **/
        string desc;
    }

    /**
     * 平台APP创建输出数据
     *
     * @date 2019年8月23日 上午10:05:28
     * @author lcy
     * @version 1.0
     **/
    ["java:getset"]
    class PlatformAppOutputDTO {
        /** 应用ID **/
        string appId;

        /** 图标 **/
        string icon;

        /** 应用名称 **/
        string name;

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
        ClientDTO push;

        /** 平台Client信息 **/
        ClientDTO client;
    }

    /**
     * 平台创建输出数据
     *
     * @date 2019年8月23日 上午10:05:28
     * @author lcy
     * @version 1.0
     **/
    ["java:getset"]
    class PlatformOutputDTO {

        /** 平台编号 **/
        string code;

        /** 平台名称 **/
        string name;

        /** 平台地址 **/
        string address;

        /** 平台描述 **/
        string desc;

        /** 平台登录接口权限校验 **/
        ClientDTO client;
    }

}
}}}}}