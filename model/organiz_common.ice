module com {
module jimi {
module platform {
module user {
module generated {
/**
 * 账号基本信息
 * 
 * @date 2019年8月21日 上午11:27:37
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct AccountOutput {
    /**
     * 账号id
     **/
    long uid;
    /**
     * 用户名(可用于登录)
     **/
    string userName;
    /**
     * 昵称
     **/
    string nickName;
    /**
     * 手机号(可用于登录)
     **/
    string phone;
    /**
     * 邮箱(可用于登录)
     **/
    string email;
};
/**
 * 添加账号输入
 * 
 * @date 2019年8月21日 上午11:27:37
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct AddAccountInput {
    /**
     * 机构id
     **/
    long oid;
    /**
     * 用户名(可用于登录)
     **/
    string userName;
    /**
     * 密码
     **/
    string password;
    /**
     * 昵称
     **/
    string nickName;
    /**
     * 手机号(可用于登录)
     **/
    string phone;
    /**
     * 邮箱(可用于登录)
     **/
    string email;
};
/**
 * 添加机构输入
 * 
 * @date 2019年8月21日 上午11:27:16
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct AddOrganizationInput {
    /**
     * 父机构oid
     **/
    long parent;
    /**
     * 机构类型code
     **/
    string code;
    /**
     * 机构/公司名称
     **/
    string name;
    /**
     * 邮箱
     **/
    string email;
    /**
     * 联系人
     **/
    string contact;
    /**
     * 手机号
     **/
    string phone;
    /**
     * 省
     **/
    string province;
    /**
     * 市
     **/
    string city;
    /**
     * 区
     **/
    string region;
    /**
     * 详细地址
     **/
    string details;
};
/**
 * 添加角色输入
 * 
 * @date 2019年8月21日 上午11:28:15
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct AddRoleInput {
    /**
     * 机构id
     **/
    long oid;
    /**
     * 角色名称
     **/
    string name;
    /**
     * 备注
     **/
    string memo;
};
/**
 * 当前会话账号信息
 * 
 * @date 2019年8月22日 下午2:05:28
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct CurrentAccount {
    /**
     * 账号id
     **/
    long uid;
    /**
     * 机构id
     **/
    long oid;
    /**
     * 平台code
     **/
    long code;
};
/**
 * 机构基本信息
 * 
 * @date 2019年8月21日 上午11:27:16
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct OrganizationOutput {
    /**
     * 机构Id
     **/
    long oid;
    /**
     * 机构/公司名称
     **/
    string name;
    /**
     * 机构类型
     **/
    string type;
    /**
     * 父id
     **/
    long parent;
    /**
     * 是否有下级
     **/
    bool hasChild;
};
/**
 * 机构类型
 * 
 * @date 2019年8月21日 上午11:27:16
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct OrganizationTypeOutput {
    /**
     * 机构类型code
     **/
    string code;
    /**
     * 机构类名称
     **/
    string name;
};
/**
 * 角色基本信息
 * 
 * @date 2019年8月21日 下午2:30:34
 * @author yaojianping
 * @version 1.0
 **/
["java:getset"]
struct RoleOutput {
    /**
     * 角色id
     **/
    string id;
    /**
     * 角色名称
     **/
    string name;
};
};};};};};