#include "./organization_role_dto.ice"
module com { module jimi { module api { module user {
module organization {

    /**
     * 自定义参数Args3
     **/
    sequence<dto::RoleOutput> RoleList;
    /**
     * 自定义参数Args4
     **/
    sequence<string> RoleIdList;
    /**
     * 角色管理接口
     *
     * @date 2019年8月21日 下午2:13:12
     * @author yaojianping
     * @version 1.0
     **/
    interface OrganizationRoleApi {
        /**
         * 查询机构的角色基本信息
         *
         * @param oid 机构id
         * @return 角色列表
         * @author yaojianping
         * @date 2019年8月21日 下午2:34:07
         **/
        RoleList findByOid(long oid) throws com::jimi::api::ApiException;

        /**
         * 添加角色
         *
         * @param account 当前会话操作人
         * @param input 角色参数
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月21日 下午2:13:57
         **/
        bool addRole(com::jimi::api::CurrentAccount account, dto::AddRoleInput input) throws com::jimi::api::ApiException;

        /**
         * 删除角色
         *
         * @param account 当前会话操作人
         * @param roleId 角色id
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月21日 下午2:25:53
         **/
        bool deleteRole(com::jimi::api::CurrentAccount account, string roleId) throws com::jimi::api::ApiException;

        /**
         * 授权
         *
         * @param account 当前会话操作人
         * @param uid 用户id
         * @param roleId 角色id
         * @author yaojianping
         * @date 2019年8月21日 下午2:26:23
         **/
        void authorize(com::jimi::api::CurrentAccount account, long uid, RoleIdList roleId) throws com::jimi::api::ApiException;
    }
}
}}}}