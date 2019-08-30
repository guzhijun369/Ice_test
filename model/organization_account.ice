#include "./organization_account_dto.ice"
module com { module jimi { module api { module user {
module organization {
    /**
     * 账号管理接口
     *
     * @date 2019年8月21日 下午2:08:21
     * @author yaojianping
     * @version 1.0
     **/
    interface OrganizationAccountApi {

        /**
         * 添加修改账号信息
         *
         * @param account 当前会话操作人
         * @param input 账号参数输入
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月21日 下午2:55:02
         **/
        void save(com::jimi::api::CurrentAccount account, dto::AccountInputDTO dto) throws
        com::jimi::api::ApiException;

        /**
         * 禁用/启用账号
         *
         * @param account 当前会话操作人
         * @param uid 账号id
         * @param isDisabled true-禁用，false-启用
         * @return true-成功，false-失败
         * @author yaojianping
         * @date 2019年8月21日 下午2:56:09
         **/
        void disable(com::jimi::api::CurrentAccount account, string uid, bool disabled) throws
        com::jimi::api::ApiException;

        /**
         * 重置密码
         *
         * @param account 当前会话操作人
         * @param uid 账号id
         * @return 返回随机新密码
         * @author yaojianping
         * @date 2019年8月21日 下午2:57:02
         **/
        string resetPassword(com::jimi::api::CurrentAccount account, string uid) throws com::jimi::api::ApiException;

        /**
         * 查询账号信息
         *
         * @param oid 机构id
         * @return 账号列表
         * @author yaojianping
         * @date 2019年8月21日 下午2:57:33
         **/
        dto::AccountPageOutputDTO page(dto::AccountPageInputDTO dto) throws com::jimi::api::ApiException;
    }
}
}}}}