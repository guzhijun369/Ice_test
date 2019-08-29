#include "./common.ice"
module com { module jimi { module api { module user { module organization {
module dto{
    /**
     * 机构类型服务入参
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
    ["java:getset"]
    class OrganizationTypeInputDTO extends com::jimi::api::BaseInputDTO {

        /**
         * 机构类型code
         */
        string code;

        /**
         * 机构类名称
         */
        string name;
    }

    /**
     * 机构类型服务入参
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
    ["java:getset"]
    class OrganizationTypeOutputDTO {

        /**
         * 机构类型code
         */
        string code;

        /**
         * 机构类名称
         */
        string name;
    }
}
}}}}}