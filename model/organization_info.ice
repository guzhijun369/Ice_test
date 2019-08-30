#include "./organization_info_dto.ice"
module com { module jimi { module api { module user {
module organization {

    /**
     * 自定义参数OrgList
     **/
    sequence<dto::OrganizationOutputDTO> OrgList;
    /**
     * 机构管理接口
     *
     * @date 2019年8月21日 上午11:46:17
     * @author yaojianping
     * @version 1.0
     **/
    interface OrganizationApi {
        /**
         * 删除机构
         *
         * @param account 当前会话操作人
         * @param oid 机构id
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月21日 下午2:06:26
         **/
        void delete(com::jimi::api::CurrentAccount account, string oid) throws com::jimi::api::ApiException;

        /**
         * 禁用/启用机构
         *
         * @param account 当前会话操作人
         * @param oid 机构id
         * @param isDisabled true-禁用，false-启用
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月21日 下午2:02:33
         **/
        void disable(com::jimi::api::CurrentAccount account, string oid, bool disabled) throws
        com::jimi::api::ApiException;

        /**
         * 查询下级机构基本信息(该方法用于树形加载时)
         *
         * @param account 当前会话操作人
         * @param oid 机构id
         * @return 下级机构基本信息
         * @author yaojianping
         * @date 2019年8月21日 下午2:01:28
         **/
        OrgList findChildrenByOid(string oid) throws com::jimi::api::ApiException;

        /**
         * 查询机构基本信息(该方法用于树形加载时)
         *
         * @param account 当前会话操作人
         * @param oid 机构id
         * @return 机构基本信息
         * @author yaojianping
         * @date 2019年8月21日 下午1:59:48
         **/
        dto::OrganizationOutputDTO findByOid(string oid) throws com::jimi::api::ApiException;

        /**
         * 添加或修改机构信息
         *
         * @param dto 机构参数输入
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月22日 下午2:10:30
         **/
        void save(dto::OrganizationInputDTO dto) throws com::jimi::api::ApiException;
    };
}
}}}}