#include "./common.ice"
module com { module jimi { module api { module user { module system {
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

module dto {

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
        constant::PermissionType type;

        /** 系统权限链接 **/
        string url;

        /** 系统权限所属平台 **/
        string platform;
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
        constant::PermissionType type;

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
        constant::PermissionType type;

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
    }
}
}}}}}