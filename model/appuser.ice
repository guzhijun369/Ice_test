#include "./appuser_dto.ice"
module com { module jimi { module api { module user {
module app {

    /**
     * App用户接口
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
	interface AppUserApi {

        /**
         * 添加APP用户信息
         *
         * @param dto 用户数据输入参数
         * @return 添加用户状态
         */
        bool addAppUser(dto::AddAppUserInputDTO dto) throws com::jimi::api::ApiException;

        /**
         * 登录认证
         *
         * @param phone 用户手机号
         * @param password 用户密码
         * @return 用户信息
         */
        idempotent dto::AppUserOutputDTO loginAuth(string phone, string password) throws com::jimi::api::ApiException;

        /**
         * 通过用户ID查找用户信息
         *
         * @param id 用户ID
         * @return 用户信息
         */
        idempotent dto::AppUserOutputDTO findById(string id) throws com::jimi::api::ApiException;

        /**
         * 更新用户密码
         *
         * @param id 用户ID
         * @param password 用户更新密码
         * @return 是否更新成功
         */
        bool updatePassword(string id, string password) throws com::jimi::api::ApiException;

        /**
         * 重置用户密码
         *
         * @param id 用户ID
         * @return 是否更新成功
         */
        bool resetPassword(string id) throws com::jimi::api::ApiException;

        /**
         * 启用用户
         *
         * @param id 用户ID
         * @return 是否启用成功
         */
        bool enableAppUser(string id) throws com::jimi::api::ApiException;

        /**
         * 关闭启用用户
         *
         * @param id 用户ID
         * @return 是否关闭启用成功
         */
        bool disableAppUser(string id) throws com::jimi::api::ApiException;

        /**
         * 绑定用户到组织
         *
         * @param id 用户ID
         * @param orgId 组织ID
         * @return 是否绑定成功
         */
        bool bindOrg(string id, string orgId) throws com::jimi::api::ApiException;

        /**
         * 解绑组织用户
         *
         * @param id 用户ID
         * @param orgId 组织ID
         * @return 是否解绑成功
         */
        bool unbindOrg(string id, string orgId) throws com::jimi::api::ApiException;

        /**
         * 更新用户信息
         *
         * @param dto 更新的用户数据
         * @return 是否更新成功
         */
        bool updateAppUser(dto::UpdateAppUserInputDTO dto) throws com::jimi::api::ApiException;

        /**
         * 获取用户列表
         *
         * @param dto 查询用户数据
         * @return 用户数据列表
         */
        idempotent dto::AppUserListOutputDTO findList(dto::FindListInputDTO dto) throws com::jimi::api::ApiException;

        /**
         * 分页获取用户列表
         *
         * @param dto 查询用户数据
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 用户数据列表
         */
        idempotent dto::AppUserListOutputDTO findPage(dto::FindListInputDTO dto, int pageNum, int pageSize) throws com::jimi::api::ApiException;
	}
}
}}}}
