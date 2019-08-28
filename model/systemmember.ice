module com {
module jimi {
module user {
module api {
module system {
    module constant{
        /**
         * 权限类型
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        enum PermissionType{
            /** 菜单 **/
            MENU,

            /** 按钮 **/
            BUTTON
        };
    }

    module dto{

        dictionary<string, string> GroupMapOutputDTO;

        dictionary<string, string> RoleMapOutputDTO;

        dictionary<string, string> PermissionMapOutputDTO;

        /**
         * 成员输出数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class MemberOutputDTO {
            /** 成员ID **/
            string id;

            /** 成员邮箱 **/
            string email;

            /** 成员描述 **/
            string describe;

            /** 成员分组 **/
            GroupMapOutputDTO groups;

            /** 成员创建者 **/
            string creater;

            /** 成员创建时间 **/
            long gmtCreate;

            /** 成员更新者 **/
            string updater;

            /** 成员更新时间 **/
            long gmtModified;
        };

        /**
         * 系统群组输出数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class SystemGroupOutputDTO {
            /** 系统群组ID **/
            string id;

            /** 系统群组名称 **/
            string name;

            /** 系统群组描述 **/
            string describe;

            /** 系统群组角色列表 **/
            RoleMapOutputDTO roles;

            /** 系统群组创建者 **/
            string creater;

            /** 系统群组创建时间 **/
            long gmtCreate;

            /** 系统群组更新者 **/
            string updater;

            /** 系统群组更新时间 **/
            long gmtModified;
        };

        /**
         * 系统角色输出数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class SystemRoleOutputDTO {
            /** 系统角色ID **/
            string id;

            /** 系统角色名称 **/
            string name;

            /** 系统角色描述 **/
            string describe;

            /** 系统角色权限列表 **/
            PermissionMapOutputDTO permissions;

            /** 系统角色创建者 **/
            string creater;

            /** 系统角色创建时间 **/
            long gmtCreate;

            /** 系统角色更新者 **/
            string updater;

            /** 系统角色更新时间 **/
            long gmtModified;
        };

        /**
         * 系统权限输出数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class SystemPermissionOutputDTO {
            /** 系统权限ID **/
            string id;

            /** 系统权限名称 **/
            string name;

            /** 系统权限code **/
            string code;

            /** 系统权限类型 **/
            com::jimi::user::api::system::constant::PermissionType type;

            /** 系统权限链接 **/
            string url;

            /** 系统权限所属平台 **/
            string platform;

            /** 系统权限创建者 **/
            string creater;

            /** 系统权限创建时间 **/
            long gmtCreate;

            /** 系统权限更新者 **/
            string updater;

            /** 系统权限更新时间 **/
            long gmtModified;
        };

        sequence<MemberOutputDTO> MemberListOutputDTO;

        sequence<SystemGroupOutputDTO> GroupListOutputDTO;

        sequence<SystemRoleOutputDTO> SystemRoleListOutputDTO;

        sequence<SystemRoleOutputDTO> SystemPermissionListOutputDTO;


        sequence<string> GroupIdArr;
        sequence<string> RoleIdArr;
        sequence<string> PermissionIdArr;

        /**
         * 添加成员输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class AddMemberInputDTO {

            /** 成员名称 **/
            string name;

            /** 成员邮箱 **/
            string email;

            /** 成员描述 **/
            string describe;

            /** 成员密码 **/
            string password;

            /** 成员操作者 **/
            long operator;
        };

        /**
         * 更新成员输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class UpdateMemberInputDTO {
            /** 成员ID **/
            string id;

            /** 成员名称 **/
            string name;

            /** 成员邮箱 **/
            string email;

            /** 成员描述 **/
            string describe;

            /** 成员操作者 **/
            long operator;
        };

        /**
         * 添加系统群组输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class AddSystemGroupInputDTO {
            /** 系统群组名称 **/
            string name;

            /** 系统群组描述 **/
            string describe;

            /** 系统群组操作者 **/
            long operator;
        };

        /**
         * 更新系统群组输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class UpdateSystemGroupInputDTO {

            /** 系统群组ID **/
            string id;

            /** 系统群组名称 **/
            string name;

            /** 系统群组描述 **/
            string describe;

            /** 系统群组操作者 **/
            long operator;
        };

        /**
         * 添加系统角色输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class AddSystemRoleInputDTO {
            /** 系统角色名称 **/
            string name;

            /** 系统角色描述 **/
            string describe;

            /** 系统角色操作者 **/
            long operator;
        };

        /**
         * 更新系统角色输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class UpdateSystemRoleInputDTO {
            /** 系统角色ID **/
            string id;

            /** 系统角色名称 **/
            string name;

            /** 系统角色描述 **/
            string describe;

            /** 系统角色操作者 **/
            long operator;
        };

        /**
         * 添加系统权限输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class AddSystemPermissionInputDTO {
            /** 系统权限名称 **/
            string name;

            /** 系统权限类型 **/
            com::jimi::user::api::system::constant::PermissionType type;

            /** 系统权限链接 **/
            string url;

            /** 系统权限编码 **/
            string code;

            /** 系统权限所属平台 **/
            string platform;

            /** 系统权限描述 **/
            string describe;

            /** 系统权限操作者 **/
            long operator;
        };

        /**
         * 更新系统权限输入数据
         *
         * @date 2019年8月23日 上午10:05:28
         * @author wangke
         * @version 1.0
         **/
        ["java:getset"]
        class UpdateSystemPermissionInputDTO {
            /** 系统权限ID **/
            string id;

            /** 系统权限名称 **/
            string name;

            /** 系统权限类型 **/
            com::jimi::user::api::system::constant::PermissionType type;

            /** 系统权限链接 **/
            string url;

            /** 系统权限编码 **/
            string code;

            /** 系统权限所属平台 **/
            string platform;

            /** 系统权限描述 **/
            string describe;

            /** 系统权限操作者 **/
            long operator;
        };
    };

    /**
     * 成员管理接口
     *
     * @date 2019年8月23日 上午10:05:28
     * @author wangke
     * @version 1.0
     **/
	interface MemberManagerService {
        /**
         * 添加成员
         *
         * @param AddMemberInputDTO 成员数据
         * @return 添加成员状态
         */
	    bool addMember(com::jimi::user::api::system::dto::AddMemberInputDTO AddMemberInputDTO);

        /**
         * 更新成员信息
         *
         * @param updateMemberInputDTO 更新成员数据
         * @return  更新成员状态
         */
        bool updateMember(com::jimi::user::api::system::dto::UpdateMemberInputDTO updateMemberInputDTO);

        /**
         * 删除成员
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 删除成员状态
         */
        bool deleteMember(string id, long operator);

        /**
         * 认证成员
         *
         * @param email 成员邮箱
         * @param password 成员密码
         * @return 成员数据
         */
        idempotent com::jimi::user::api::system::dto::MemberOutputDTO loginAuth(string email, string password);

        /**
         * 查询成员
         *
         * @param id 成员ID
         * @return 成员数据
         */
        idempotent com::jimi::user::api::system::dto::MemberOutputDTO findById(string id);

        /**
         * 更新成员密码
         *
         * @param id 成员ID
         * @param password 成员密码
         * @param operator 操作者ID
         * @return 更新成员密码状态
         */
        bool updatePassword(string id, string password, long operator);

        /**
         * 重置成员密码
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 重置成员密码状态
         */
        bool resetPassword(string id, long operator);

        /**
         * 启用成员
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 启用成员状态
         */
        bool enableMember(string id, long operator);

        /**
         * 关闭启动成员
         *
         * @param id 成员ID
         * @param operator 操作者ID
         * @return 关闭启动成员状态
         */
        bool disableMember(string id, long operator);

        /**
         * 绑定成员到群组
         *
         * @param uid 成员ID
         * @param groupIdArr 群组ID集合
         * @param operator 操作者ID
         * @return 绑定成员到群组状态
         */
        bool bindGroup(long uid, com::jimi::user::api::system::dto::GroupIdArr groupIdArr, long operator);

        /**
         * 解绑成员
         *
         * @param uid 成员ID
         * @param groupIdArr 群组ID集合
         * @param operator 操作者ID
         * @return 解绑成员状态
         */
        bool unbindGroup(long uid, com::jimi::user::api::system::dto::GroupIdArr groupIdArr, long operator);

        /**
         * 查找群组成员
         *
         * @param groupId 群组ID
         * @return 群组成员列表
         */
        idempotent com::jimi::user::api::system::dto::MemberListOutputDTO findByGroupId(string groupId);

        /**
         * 通过关键字查询成员信息
         *
         * @param keyword 关键字
         * @return 成员信息列表
         */
        idempotent com::jimi::user::api::system::dto::MemberListOutputDTO findList(string keyword);

        /**
         * 通过关键字分页查询成员信息
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 成员信息列表
         */
        idempotent com::jimi::user::api::system::dto::MemberListOutputDTO findPage(string keyword, int pageNum, int pageSize);

	};

	interface GroupManagerService {

	    /**
         * 添加群组
         *
         * @param addSystemGroupInputDTO 群组输入参数
         * @return 添加群组状态
         */
	    bool addSystemGroup(com::jimi::user::api::system::dto::AddSystemGroupInputDTO addSystemGroupInputDTO);

	    /**
         * 更新系统群组信息
         *
         * @param updateSystemGroupInputDTO 群组输入参数
         * @return 更新系统群组信息状态
         */
	    bool updateSystemGroup(com::jimi::user::api::system::dto::UpdateSystemGroupInputDTO updateSystemGroupInputDTO);

	    /**
         * 删除群组
         *
         * @param id 群组ID
         * @param operator 操作者
         * @return 删除群组状态
         */
	    bool deleteSystemGroup(string id, long operator);

	    /**
         * 关联群组角色
         *
         * @param groupId 群组ID
         * @param operator 操作者
         * @param roleIds 角色ID集合
         * @return 关联群组角色状态
         */
	    bool bindRole(string groupId, com::jimi::user::api::system::dto::RoleIdArr roleIds, long operator);

	    /**
         * 解绑群组角色
         *
         * @param groupId 群组ID
         * @param operator 操作者
         * @param roleIds 角色ID集合
         * @return 添加用户状态
         */
	    bool unbinRole(string groupId, com::jimi::user::api::system::dto::RoleIdArr roleIds, long operator);

	    /**
         * 查找群组信息
         *
         * @param id 群组ID
         * @return 群组信息
         */
	    idempotent com::jimi::user::api::system::dto::SystemGroupOutputDTO findById(string id);
	
	    /**
         * 获取群组列表
         *
         * @param keyword 搜索关键字
         * @return 群组列表
         */
	    idempotent com::jimi::user::api::system::dto::GroupListOutputDTO findList(string keyword);
	
	    /**
         * 分页获取群组列表
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 成员信息列表
         */
	    idempotent com::jimi::user::api::system::dto::GroupListOutputDTO findPage(string keyword, int pageNum, int pageSize);

    };

    interface RoleManagerService {
		
	    /**
         * 添加角色
         *
         * @param addSystemRoleInputDTO 角色输入信息
         * @return 添加角色状态
         */
        bool addSystemRole(com::jimi::user::api::system::dto::AddSystemRoleInputDTO addSystemRoleInputDTO);
	
	    /**
         * 更新角色
         *
         * @param updateSystemRoleInputDTO 更新角色输入信息
         * @return 更新角色状态
         */
        bool updateSystemRole(com::jimi::user::api::system::dto::UpdateSystemRoleInputDTO updateSystemRoleInputDTO);
	
	    /**
         * 删除角色
         *
         * @param id 角色ID
         * @param operator 操作者
         * @return 删除角色状态
         */
        bool deleteSystemRole(string id, long operator);

	    /**
         * 获取角色信息
         *
         * @param id 角色ID
         * @return 角色信息
         */
        idempotent com::jimi::user::api::system::dto::SystemRoleOutputDTO findById(string id);
	
	    /**
         * 获取角色列表
         *
         * @param keyword 搜索关键字
         * @return 角色列表
         */
        idempotent com::jimi::user::api::system::dto::SystemRoleListOutputDTO findList(string keyword);

	    /**
         * 分页获取角色列表
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 角色列表
         */
        idempotent com::jimi::user::api::system::dto::SystemRoleListOutputDTO findPage(string keyword, int pageNum, int pageSize);

	    /**
         * 角色绑定权限
         *
         * @param roleId 角色ID
         * @param permissions 权限ID集合
         * @param operator 操作者
         * @return 角色绑定权限状态
         */
        bool bindPermission(string roleId, com::jimi::user::api::system::dto::PermissionIdArr permissions, long operator);

	    /**
         * 解绑角色权限
         *
         * @param roleId 角色ID
         * @param permissions 权限ID集合
         * @param operator 操作者
         * @return 角色绑定权限状态
         */
        bool unbindPermission(string roleId, com::jimi::user::api::system::dto::PermissionIdArr permissions, long operator);

    };

    interface PermissionManagerService {
	
	    /**
         * 添加系统权限
         *
         * @param addSystemPermissionInputDTO 权限数据输入参数
         * @return 添加系统权限状态
         */
        bool addSystemPermission(com::jimi::user::api::system::dto::AddSystemPermissionInputDTO addSystemPermissionInputDTO);
	
	    /**
         * 更新权限数据
         *
         * @param updateSystemPermissionInputDTO 权限数据输入参数
         * @return 更新权限数据状态
         */
        bool updateSystemPermission(com::jimi::user::api::system::dto::UpdateSystemPermissionInputDTO updateSystemPermissionInputDTO);

	    /**
         * 删除系统权限
         *
         * @param id 权限ID
         * @param operator 操作者
         * @return 删除系统权限状态
         */
        bool deleteSystemPermission(string id, long operator);

	    /**
         * 获取权限信息
         *
         * @param id 角色ID
         * @param operator 操作者
         * @return 权限信息数据
         */
        idempotent com::jimi::user::api::system::dto::SystemPermissionOutputDTO findById(string id);

	    /**
         * 获取权限列表
         *
         * @param keyword 搜索关键字
         * @return 权限列表
         */
        idempotent com::jimi::user::api::system::dto::SystemPermissionListOutputDTO findList(string keyword);
	
	    /**
         * 分页获取权限列表
         *
         * @param keyword 关键字
         * @param pageNum 页数
         * @param pageSize 每页数据大小
         * @return 权限列表
         */
        idempotent com::jimi::user::api::system::dto::SystemPermissionListOutputDTO findPage(string keyword, int pageNum, int pageSize);

    };

};
};
};
};
};