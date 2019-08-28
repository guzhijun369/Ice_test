#include "./platform_header.ice"
module com {
module jimi {
module user {
module api {
module system {
sequence<dto::PlatformOutputDTO> PlatformList;
sequence<dto::PlatformAppOutputDTO> PlatformAppList;
/**
 * 平台管理接口
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
interface PlatformService {

    /**
     * 添加平台信息
     *
     * @param accout 当前会话操作人
     * @param platformInputDTO 平台相关信息
     * @return 平新增加平台信息
     */
    dto::PlatformOutputDTO addPlatform(dto::CurrentAccount accout, dto::PlatformInputDTO platformInputDTO);

    /**
     * 更新平台信息
     *
     * @param accout 当前会话操作人
     * @param platformInputDTO 平台相关信息
     * @return 更新后平台的相关信息
     */
    void updatePlatform(dto::CurrentAccount accout, dto::PlatformInputDTO platformInputDTO);

    /**
     * 删除平台信息
     *
     * @param accout 当前会话操作人
     * @param platformCode 平台编码
     * @return void
     */
    void deletePlatformBy(dto::CurrentAccount accout, string platformCode);

    /**
     * 获取所有平台信息
     *
     * @param accout 当前会话操作人
     * @return 平台信息列表
     */
    PlatformList getAllPlatform(dto::CurrentAccount accout);

    /**
     * 重置平台Client相关内容
     *
     * @param accout 当前会话操作人
     * @param platformCode 平台编码
     * @return 重置后的平台 Client Secret
     */
    string resetPlatformClientSecret(dto::CurrentAccount accout, string platformCode);

    /**
     * 查看平台 Client Secret
     *
     * @param accout 当前会话操作人
     * @param platformCode 平台编码
     * @return 平台 Client Secret
     */
     string lookupPlatformClientSecret(dto::CurrentAccount accout, string platformCode);
};

/**
 * 平台APP管理接口
 *
 * @date 2019年8月23日 上午10:05:28
 * @author lcy
 * @version 1.0
 **/
interface ApplicationService {

    /**
     * 添加平台APP信息
     *
     * @param accout 当前会话操作人
     * @param platformAppInputDTO 平台APP相关信息
     * @return 平新增加平台App信息
     */
    dto::PlatformAppOutputDTO addApplication(dto::CurrentAccount accout, dto::PlatformAppInputDTO platformAppInputDTO);

    /**
     * 删除平台APP信息
     *
     * @param accout 当前会话操作人
     * @param appId 平台APP相关信息
     * @return void
     */
    void deleteApplicationBy(dto::CurrentAccount accout, string appId);

    /**
     * 更新平台App信息
     *
     * @param accout 当前会话操作人
     * @param platformAppInputDTO 平台APP相关信息
     * @return 更新后平台APP相关信息
     */
    void updateApplication(dto::CurrentAccount accout, dto::PlatformAppInputDTO platformAppInputDTO);

    /**
     * 获取所有平台App信息
     *
     * @param accout 当前会话操作人
     * @return 平台APP信息列表
     */
    PlatformAppList getAllApplications(dto::CurrentAccount accout);

    /**
     * 重置平台APP Client相关内容
     *
     * @param accout 当前会话操作人
     * @param appId 平台APP标识
     * @return 重置后平台APP Client Secret
     */
    string resetApplicationClientSecret(dto::CurrentAccount accout, string appId);

    /**
     * 查看平台APP Client Secret
     *
     * @param accout 当前会话操作人
     * @param appId 平台APP标识
     * @return 平台APP Client Secret
     */
     string lookupApplicationClientSecret(dto::CurrentAccount accout, string appId);
};

};};};};};