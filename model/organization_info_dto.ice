#include "./common.ice"
module com { module jimi { module api { module user { module organization {
module dto {
    /**
     * 机构参数
     *
     * @date 2019年8月21日 上午11:27:16
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class OrganizationInputDTO extends com::jimi::api::BaseInputDTO {
        /** oid，如果是修改*/
        string oid;
        /**
         * 父机构oid
         **/
        string parent;
        /**
         * 机构类型code
         **/
        string code;
        /**
         * 机构/公司名称
         **/
        string name;
        /**
         * 邮箱
         **/
        string email;
        /**
         * 联系人
         **/
        string contact;
        /**
         * 手机号
         **/
        string phone;
        /**
         * 省
         **/
        string province;
        /**
         * 市
         **/
        string city;
        /**
         * 区
         **/
        string region;
        /**
         * 详细地址
         **/
        string detail;

        /** 机构秘钥*/
        string appId;

        /** 机构秘钥*/
        string appSecret;

        /** 域名*/
        string domain;

        /** logo*/
        string logo;
    };

    /**
     * 机构基本信息
     *
     * @date 2019年8月21日 上午11:27:16
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class OrganizationOutputDTO extends com::jimi::api::BaseOutputDTO {
        /**
         * 机构Id
         **/
        string oid;
        /**
         * 机构/公司名称
         **/
        string name;
        /**
         * 机构类型
         **/
        string type;
        /**
         * 父id
         **/
        string parent;
        /**
         * 是否有下级
         **/
        bool hasChild;
    };
}
}}}}}