#include "./system_member_dto.ice"
module com { module jimi { module api { module user {
module system {
    /**
     * 成员管理接口
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
	interface SystemMemberApi {
        /**
         * 添加成员
         *
         * @param AddMemberInputDTO 成员数据
         * @return 添加成员状态
         */
	    bool addMember(dto::AddMemberInputDTO AddMemberInputDTO) throws com::jimi::api::ApiException;

        /**
         * 更新成员信息
         *
         * @param updateMemberInputDTO 更新成员数据
         * @return  更新成员状态
         */
        bool updateMember(dto::UpdateMemberInputDTO updateMemberInputDTO) throws com::jimi::api::ApiException;

        /**
         * 删除成员
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 删除成员状态
         */
        bool deleteMember(string id, long operator) throws com::jimi::api::ApiException;

        /**
         * 认证成员
         *
         * @param email 成员邮箱
         * @param password 成员密码
         * @return 成员数据
         */
        idempotent dto::MemberOutputDTO loginAuth(string email, string password) throws com::jimi::api::ApiException;

        /**
         * 查询成员
         *
         * @param id 成员ID
         * @return 成员数据
         */
        idempotent dto::MemberOutputDTO findById(string id) throws com::jimi::api::ApiException;

        /**
         * 更新成员密码
         *
         * @param id 成员ID
         * @param password 成员密码
         * @param operator 操作者ID
         * @return 更新成员密码状态
         */
        bool updatePassword(string id, string password, long operator) throws com::jimi::api::ApiException;

        /**
         * 重置成员密码
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 重置成员密码状态
         */
        bool resetPassword(string id, long operator) throws com::jimi::api::ApiException;

        /**
         * 启用成员
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 启用成员状态
         */
        bool enableMember(string id, long operator) throws com::jimi::api::ApiException;

        /**
         * 关闭启动成员
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 关闭启动成员状态
         */
        bool disableMember(string id, long operator) throws com::jimi::api::ApiException;

        /**
         * 绑定成员到群组
         *
         * @param uid 成员ID
         * @param groupIdArr 群组ID集合
         * @param operator 操作者ID
         * @return 绑定成员到群组状态
         */
        bool bindGroup(long uid, dto::GroupIdArr groupIdArr, long operator) throws com::jimi::api::ApiException;

        /**
         * 解绑成员
         *
         * @param uid 成员ID
         * @param groupIdArr 群组ID集合
         * @param operator 操作者ID
         * @return 解绑成员状态
         */
        bool unbindGroup(long uid, dto::GroupIdArr groupIdArr, long operator) throws com::jimi::api::ApiException;

        /**
         * 查找群组成员
         *
         * @param groupId 群组ID
         * @return 群组成员列表
         */
        idempotent dto::MemberListOutputDTO findByGroupId(string groupId) throws com::jimi::api::ApiException;

        /**
         * 通过关键字查询成员信息
         *
         * @param keyword 关键字
         * @return 成员信息列表
         */
        idempotent dto::MemberListOutputDTO findList(string keyword) throws com::jimi::api::ApiException;

        /**
         * 通过关键字分页查询成员信息
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 成员信息列表
         */
        idempotent dto::MemberListOutputDTO findPage(string keyword, int pageNum, int pageSize) throws com::jimi::api::ApiException;

	};

	interface SystemGroupApi {

	    /**
         * 添加群组
         *
         * @param addSystemGroupInputDTO 群组输入参数
         * @return 添加群组状态
         */
	    bool addSystemGroup(dto::AddSystemGroupInputDTO addSystemGroupInputDTO) throws com::jimi::api::ApiException;

	    /**
         * 更新系统群组信息
         *
         * @param updateSystemGroupInputDTO 群组输入参数
         * @return 更新系统群组信息状态
         */
	    bool updateSystemGroup(dto::UpdateSystemGroupInputDTO updateSystemGroupInputDTO) throws com::jimi::api::ApiException;

	    /**
         * 删除群组
         *
         * @param id 群组ID
         * @param operator 操作者
         * @return 删除群组状态
         */
	    bool deleteSystemGroup(string id, long operator) throws com::jimi::api::ApiException;

	    /**
         * 关联群组角色
         *
         * @param groupId 群组ID
         * @param operator 操作者
         * @param roleIds 角色ID集合
         * @return 关联群组角色状态
         */
	    bool bindRole(string groupId, dto::RoleIdArr roleIds, long operator) throws com::jimi::api::ApiException;

	    /**
         * 解绑群组角色
         *
         * @param groupId 群组ID
         * @param operator 操作者
         * @param roleIds 角色ID集合
         * @return 添加用户状态
         */
	    bool unbinRole(string groupId, dto::RoleIdArr roleIds, long operator) throws com::jimi::api::ApiException;

	    /**
         * 查找群组信息
         *
         * @param id 群组ID
         * @return 群组信息
         */
	    idempotent dto::SystemGroupOutputDTO findById(string id) throws com::jimi::api::ApiException;
	
	    /**
         * 获取群组列表
         *
         * @param keyword 搜索关键字
         * @return 群组列表
         */
	    idempotent dto::GroupListOutputDTO findList(string keyword) throws com::jimi::api::ApiException;
	
	    /**
         * 分页获取群组列表
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 成员信息列表
         */
	    idempotent dto::GroupListOutputDTO findPage(string keyword, int pageNum, int pageSize) throws com::jimi::api::ApiException;

    };

    interface SystemRoleApi {
		
	    /**
         * 添加角色
         *
         * @param addSystemRoleInputDTO 角色输入信息
         * @return 添加角色状态
         */
        bool addSystemRole(dto::AddSystemRoleInputDTO addSystemRoleInputDTO) throws com::jimi::api::ApiException;
	
	    /**
         * 更新角色
         *
         * @param updateSystemRoleInputDTO 更新角色输入信息
         * @return 更新角色状态
         */
        bool updateSystemRole(dto::UpdateSystemRoleInputDTO updateSystemRoleInputDTO) throws com::jimi::api::ApiException;
	
	    /**
         * 删除角色
         *
         * @param id 角色ID
         * @param operator 操作者
         * @return 删除角色状态
         */
        bool deleteSystemRole(string id, long operator) throws com::jimi::api::ApiException;

	    /**
         * 获取角色信息
         *
         * @param id 角色ID
         * @return 角色信息
         */
        idempotent dto::SystemRoleOutputDTO findById(string id) throws com::jimi::api::ApiException;
	
	    /**
         * 获取角色列表
         *
         * @param keyword 搜索关键字
         * @return 角色列表
         */
        idempotent dto::SystemRoleListOutputDTO findList(string keyword) throws com::jimi::api::ApiException;

	    /**
         * 分页获取角色列表
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 角色列表
         */
        idempotent dto::SystemRoleListOutputDTO findPage(string keyword, int pageNum, int pageSize) throws com::jimi::api::ApiException;

	    /**
         * 角色绑定权限
         *
         * @param roleId 角色ID
         * @param permissions 权限ID集合
         * @param operator 操作者
         * @return 角色绑定权限状态
         */
        bool bindPermission(string roleId, dto::PermissionIdArr permissions, long operator) throws com::jimi::api::ApiException;

	    /**
         * 解绑角色权限
         *
         * @param roleId 角色ID
         * @param permissions 权限ID集合
         * @param operator 操作者
         * @return 角色绑定权限状态
         */
        bool unbindPermission(string roleId, dto::PermissionIdArr permissions, long operator) throws com::jimi::api::ApiException;

    };

    interface SystemPermissionApi {
	
	    /**
         * 添加系统权限
         *
         * @param addSystemPermissionInputDTO 权限数据输入参数
         * @return 添加系统权限状态
         */
        bool addSystemPermission(dto::AddSystemPermissionInputDTO addSystemPermissionInputDTO) throws com::jimi::api::ApiException;
	
	    /**
         * 更新权限数据
         *
         * @param updateSystemPermissionInputDTO 权限数据输入参数
         * @return 更新权限数据状态
         */
        bool updateSystemPermission(dto::UpdateSystemPermissionInputDTO updateSystemPermissionInputDTO) throws com::jimi::api::ApiException;

	    /**
         * 删除系统权限
         *
         * @param id 权限ID
         * @param operator 操作者
         * @return 删除系统权限状态
         */
        bool deleteSystemPermission(string id, long operator) throws com::jimi::api::ApiException;

	    /**
         * 获取权限信息
         *
         * @param id 角色ID
         * @param operator 操作者
         * @return 权限信息数据
         */
        idempotent dto::SystemPermissionOutputDTO findById(string id) throws com::jimi::api::ApiException;

	    /**
         * 获取权限列表
         *
         * @param keyword 搜索关键字
         * @return 权限列表
         */
        idempotent dto::SystemPermissionListOutputDTO findList(string keyword) throws com::jimi::api::ApiException;
	
	    /**
         * 分页获取权限列表
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 权限列表
         */
        idempotent dto::SystemPermissionListOutputDTO findPage(string keyword, int pageNum, int pageSize) throws com::jimi::api::ApiException;
    }

}
}}}}