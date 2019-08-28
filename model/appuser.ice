module com {
module jimi {
module user {
module api {
module app {
    module dto{
        /**
         * 用户数据输出参数
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class AppUserOutputDTO {
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
        class AddAppUserInputDTO {
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
        class UpdateAppUserInputDTO {
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
        class FindListInputDTO {
            /** 用户ID **/
            string id;

            /** 用户手机号 **/
            string phone;
        };
    };

    /**
     * App用户接口
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
	interface AppUserService {

        /**
         * 添加APP用户信息
         *
         * @param addAppUserInputDTO 用户数据输入参数
         * @return 添加用户状态
         */
        bool addAppUser(dto::AddAppUserInputDTO addAppUserInputDTO);

        /**
         * 登录认证
         *
         * @param phone 用户手机号
         * @param password 用户密码
         * @return 用户信息
         */
        idempotent dto::AppUserOutputDTO loginAuth(string phone, string password);

        /**
         * 通过用户ID查找用户信息
         *
         * @param id 用户ID
         * @return 用户信息
         */
        idempotent dto::AppUserOutputDTO findById(string id);

        /**
         * 更新用户密码
         *
         * @param id 用户ID
         * @param password 用户更新密码
         * @return 是否更新成功
         */
        bool updatePassword(string id, string password);

        /**
         * 重置用户密码
         *
         * @param id 用户ID
         * @return 是否更新成功
         */
        bool resetPassword(string id);

        /**
         * 启用用户
         *
         * @param id 用户ID
         * @return 是否启用成功
         */
        bool enableAppUser(string id);

        /**
         * 关闭启用用户
         *
         * @param id 用户ID
         * @return 是否关闭启用成功
         */
        bool disableAppUesr(string id);

        /**
         * 绑定用户到组织
         *
         * @param id 用户ID
         * @param orgId 组织ID
         * @return 是否绑定成功
         */
        bool bindOrg(string id, string orgId);

        /**
         * 解绑组织用户
         *
         * @param id 用户ID
         * @param orgId 组织ID
         * @return 是否解绑成功
         */
        bool unbindOrg(string id, string orgId);

        /**
         * 更新用户信息
         *
         * @param updateAppUserInputDTO 更新的用户数据
         * @return 是否更新成功
         */
        bool updateAppUser(dto::UpdateAppUserInputDTO updateAppUserInputDTO);

        /**
         * 获取用户列表
         *
         * @param findListInputDTO 查询用户数据
         * @return 用户数据列表
         */
        idempotent dto::AppUserListOutputDTO findList(dto::FindListInputDTO findListInputDTO);

        /**
         * 分页获取用户列表
         *
         * @param findListInputDTO 查询用户数据
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 用户数据列表
         */
        idempotent dto::AppUserListOutputDTO findPage(dto::FindListInputDTO findListInputDTO, int pageNum, int pageSize);

	};
};
};
};
};
};
