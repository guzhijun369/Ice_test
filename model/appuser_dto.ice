#include "./common.ice"
module com { module jimi { module api { module user { module app {
module dto{
    /**
     * 用户数据输出参数
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
    ["java:getset"]
    class AppUserOutputDTO extends com::jimi::api::BaseOutputDTO {
        /** 用户ID **/
        string id;

        /** 用户手机号 **/
        string phone;

        /** 用户昵称 **/
        string nickName;

        /** 用户账号是否启用 **/
        bool enableFlag;

        /** 创建日期 **/
        long gmtCreate;

        /** 更新日期 **/
        long gmtModified;
    };

    sequence<AppUserOutputDTO> AppUserListOutputDTO;

    /**
     * 用户输入数据参数
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
    ["java:getset"]
    class AddAppUserInputDTO extends com::jimi::api::BaseInputDTO {
        /** 用户手机号 **/
        string phone;

        /** 用户昵称 **/
        string nickName;

        /** 用户密码 **/
        string password;
    };

    /**
     * 更新用户数据输入参数
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
    ["java:getset"]
    class UpdateAppUserInputDTO extends com::jimi::api::BaseInputDTO {
        /** 用户ID **/
        string id;

        /** 用户昵称 **/
        string nickName;
    };

    /**
     * 查询用户数据输入参数
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
    ["java:getset"]
    class FindListInputDTO extends com::jimi::api::BaseInputDTO {
        /** 用户ID **/
        string id;

        /** 用户手机号 **/
        string phone;
    }
}
}}}}}