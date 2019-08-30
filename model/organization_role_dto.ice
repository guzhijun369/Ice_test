#include "./common.ice"
module com { module jimi { module api { module user { module organization {
module dto {
    /**
     * 添加角色输入
     *
     * @date 2019年8月21日 上午11:28:15
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class AddRoleInput extends com::jimi::api::BaseInputDTO {
        /**
         * 机构id
         **/
        string oid;
        /**
         * 角色名称
         **/
        string name;
        /**
         * 备注
         **/
        string memo;
    }

    /**
     * 角色基本信息
     *
     * @date 2019年8月21日 下午2:30:34
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class RoleOutput extends com::jimi::api::BaseOutputDTO {
        /**
         * 角色id
         **/
        string id;
        /**
         * 角色名称
         **/
        string name;
    }
}
}}}}}