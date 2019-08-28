#include "./organiz_common.ice"
module com {
module jimi {
module platform {
module user {
module generated {
/**
 * 自定义参数Args0
 **/
sequence<OrganizationTypeOutput> Args0;
/**
 * 自定义参数Args1
 **/
sequence<AccountOutput> Args1;
/**
 * 账号管理接口
 * 
 * @date 2019年8月21日 下午2:08:21
 * @author yaojianping
 * @version 1.0
 **/
interface AccountManager {
    /**
     * 获取机构类型列表(该接口用于添加机构客户界面)
     * 
     * @param accout 当前会话操作人
     * @param platform 平台标识
     * @return 返回对应平台机构类型列表
     * @author yaojianping
     * @date 2019年8月21日 下午2:03:24
     **/
    Args0 getOrganizationType(CurrentAccount accout, string platform);

    /**
     * 删除账号
     * 
     * @param accout 当前会话操作人
     * @param uid 账号id
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:56:03
     **/
    bool deleteAccount(CurrentAccount accout, long uid);

    /**
     * 添加账号
     * 
     * @param accout 当前会话操作人
     * @param input 账号参数输入
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:55:02
     **/
    bool addAccount(CurrentAccount accout, AddAccountInput input);

    /**
     * 禁用/启用账号
     * 
     * @param accout 当前会话操作人
     * @param uid 账号id
     * @param isDisabled true-禁用，false-启用
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:56:09
     **/
    bool disabledAccount(CurrentAccount accout, long uid, bool isDisabled);

    /**
     * 重置密码
     * 
     * @param accout 当前会话操作人
     * @param uid 账号id
     * @return 返回随机新密码
     * @author yaojianping
     * @date 2019年8月21日 下午2:57:02
     **/
    string resetPassword(CurrentAccount accout, long uid);

    /**
     * 查询账号信息
     * 
     * @param accout 当前会话操作人
     * @param oid 机构id
     * @return 账号列表
     * @author yaojianping
     * @date 2019年8月21日 下午2:57:33
     **/
    Args1 findByOid(CurrentAccount accout, long oid);

};
/**
 * 自定义参数Args2
 **/
sequence<OrganizationOutput> Args2;
/**
 * 机构管理接口
 * 
 * @date 2019年8月21日 上午11:46:17
 * @author yaojianping
 * @version 1.0
 **/
interface OrganizationManager {
    /**
     * 删除机构
     * 
     * @param accout 当前会话操作人
     * @param oid 机构id
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:06:26
     **/
    bool deleteOrganization(CurrentAccount accout, long oid);

    /**
     * 禁用/启用机构
     * 
     * @param accout 当前会话操作人
     * @param oid 机构id
     * @param isDisabled true-禁用，false-启用
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:02:33
     **/
    bool disabledOrganization(CurrentAccount accout, long oid, bool isDisabled);

    /**
     * 查询下级机构基本信息(该方法用于树形加载时)
     * 
     * @param accout 当前会话操作人
     * @param oid 机构id
     * @return 下级机构基本信息
     * @author yaojianping
     * @date 2019年8月21日 下午2:01:28
     **/
    Args2 findAllChildByOid(CurrentAccount accout, long oid);

    /**
     * 查询机构基本信息(该方法用于树形加载时)
     * 
     * @param accout 当前会话操作人
     * @param oid 机构id
     * @return 机构基本信息
     * @author yaojianping
     * @date 2019年8月21日 下午1:59:48
     **/
    OrganizationOutput findByOid(CurrentAccount accout, long oid);

    /**
     * 添加机构
     * 
     * @param accout 当前会话操作人
     * @param input 机构参数输入
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月22日 下午2:10:30
     **/
    bool addOrganization(CurrentAccount accout, AddOrganizationInput input);

};
/**
 * 自定义参数Args3
 **/
sequence<RoleOutput> Args3;
/**
 * 自定义参数Args4
 **/
sequence<string> Args4;
/**
 * 角色管理接口
 * 
 * @date 2019年8月21日 下午2:13:12
 * @author yaojianping
 * @version 1.0
 **/
interface RoleManager {
    /**
     * 查询机构的角色基本信息
     * 
     * @param accout 当前会话操作人
     * @param oid 机构id
     * @return 角色列表
     * @author yaojianping
     * @date 2019年8月21日 下午2:34:07
     **/
    Args3 findByOid(CurrentAccount accout, long oid);

    /**
     * 添加角色
     * 
     * @param accout 当前会话操作人
     * @param input 角色参数
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:13:57
     **/
    bool addRole(CurrentAccount accout, AddRoleInput input);

    /**
     * 删除角色
     * 
     * @param accout 当前会话操作人
     * @param roleId 角色id
     * @return true-成功，false-失败
     * @author yaojianping
     * @date 2019年8月21日 下午2:25:53
     **/
    bool deleteRole(CurrentAccount accout, string roleId);

    /**
     * 授权
     * 
     * @param accout 当前会话操作人
     * @param uid 用户id
     * @param roleId 角色id
     * @author yaojianping
     * @date 2019年8月21日 下午2:26:23
     **/
    void authorize(CurrentAccount accout, long uid, Args4 roleId);

};
};};};};};