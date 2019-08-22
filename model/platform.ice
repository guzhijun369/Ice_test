#include "./platform-header.ice"
module com {
module jimi {
module user {
module api {
module system {
sequence<dto::PlatformOutputDTO> PlatformList;
sequence<dto::PlatformAppOutputDTO> PlatformAppList;
interface PlatformService {

    /**
     * 添加平台信息
     *
     * @param platformInputDTO 平台相关信息
     * @return 平台信息
     */
    dto::PlatformOutputDTO addPlatform(dto::PlatformInputDTO platformInputDTO);

    /**
     * 更新平台信息
     *
     * @param platformInputDTO 平台相关信息
     */
    void updatePlatform(dto::PlatformInputDTO platformInputDTO);

    /**
     * 删除平台信息
     *
     * @param platformCode 平台编码
     */
    void deletePlatformBy(string platformCode);

    /**
     * 获取平台信息
     *
     * @return 所有平台信息集合
     */
    PlatformList getAllPlatform();

    /**
     * 更新平台Client相关内容
     *
     * @param platformCode 平台编码
     * @return 平台信息
     */
    dto::PlatformOutputDTO updatePlatformClientSecret(string platformCode);

    /**
     * 添加平台APP信息
     *
     * @param platformAppInputDTO 平台APP相关信息
     * @return 平台App信息
     */
    dto::PlatformAppOutputDTO addPlatformApp(dto::PlatformAppInputDTO platformAppInputDTO);

    /**
     * 删除平台APP信息
     *
     * @param appId 平台APP相关信息
     */
    void deletePlatformAppBy(string appId);

    /**
     * 更新平台App信息
     *
     * @param platformAppInputDTO 平台APP相关信息
     * @return 平台APP信息
     */
    void updatePlatformApp(dto::PlatformAppInputDTO platformAppInputDTO);

    /**
     * 获取平台APP信息
     *
     * @return 所有平台APP集合
     */
    PlatformAppList getAllPlatformApp();

    /**
     * 更新平台APP Client相关内容
     *
     * @param platformCode 平台编码
     * @return 平台信息
     */
    dto::PlatformAppOutputDTO updatePlatformAppClientSecret(string appId);
};
};};};};};