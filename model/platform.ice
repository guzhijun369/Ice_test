#include "./platform_dto.ice"
module com { module jimi { module api { module user {
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
    interface PlatformApi {

        /**
         * 添加平台信息
         *
         * @param platformInputDTO 平台相关信息
         * @return 平新增加平台信息
         */
        dto::PlatformOutputDTO addPlatform(dto::PlatformInputDTO platformInputDTO) throws com::jimi::api::ApiException;

        /**
         * 更新平台信息
         *
         * @param platformInputDTO 平台相关信息
         * @return 更新后平台的相关信息
         */
        bool updatePlatform(dto::PlatformInputDTO platformInputDTO) throws com::jimi::api::ApiException;

        /**
         * 删除平台信息
         *
         * @param platformCode 平台编码
         * @return void
         */
        void deletePlatformBy(com::jimi::api::CurrentAccount account, string platformCode) throws com::jimi::api::ApiException;

        /**
         * 获取所有平台信息
         *
         * @param pageNum 页码
         * @param pageSize 页数
         * @return 平台信息列表
         */
        PlatformList getAllPlatform(int pageNum, int pageSize);

        /**
         * 通过平台code获取平台信息
         *
         * @return 平台信息列表
         */
        dto::PlatformOutputDTO findPlatformByCode(string platformCode);

        /**
         * 重置平台Client相关内容
         *
         * @param platformCode 平台编码
         * @return 重置后的平台 Client Secret
         */
        string resetPlatformClientSecret(com::jimi::api::CurrentAccount account, string platformCode) throws com::jimi::api::ApiException;

        /**
         * 查看平台 Client Secret
         *
         * @param platformCode 平台编码
         * @return 平台 Client Secret
         */
         string lookupPlatformClientSecret(com::jimi::api::CurrentAccount account, string platformCode) throws com::jimi::api::ApiException;
    };

    /**
     * 平台APP管理接口
     *
     * @date 2019年8月23日 上午10:05:28
     * @author lcy
     * @version 1.0
     **/
    interface ApplicationApi {

        /**
         * 添加平台APP信息
         *
         * @param platformAppInputDTO 平台APP相关信息
         * @return 平新增加平台App信息
         */
        dto::PlatformAppOutputDTO addApplication(dto::PlatformAppInputDTO platformAppInputDTO) throws com::jimi::api::ApiException;

        /**
         * 删除平台APP信息
         *
         * @param appId 平台APP相关信息
         * @return void
         */
        void deleteApplicationBy(com::jimi::api::CurrentAccount account, string appId) throws com::jimi::api::ApiException;

        /**
         * 更新平台App信息
         *
         * @param platformAppInputDTO 平台APP相关信息
         * @return 更新后平台APP相关信息
         */
        bool updateApplication(com::jimi::api::CurrentAccount account, dto::PlatformAppInputDTO platformAppInputDTO);

        /**
         * 获取所有平台App信息
         *
         * @param pageNum 页码
         * @param pageSize 页数

         * @return 平台APP信息
         */
        PlatformAppList getAllApplications(int pageNum, int pageSize);

        /**
         * 获取指定的APP信息
         *
         * @param appId AppId
         * @return 平台APP信息列表
         */
        dto::PlatformAppOutputDTO getApplicationByAppId(string appId);

        /**
         * 重置平台APP Client相关内容
         *
         * @param account 当前会话操作人
         * @param appId 平台APP标识
         * @return 重置后平台APP Client Secret
         */
        string resetApplicationClientSecret(com::jimi::api::CurrentAccount account, string appId) throws com::jimi::api::ApiException;

        /**
         * 查看平台APP Client Secret
         *
         * @param account 当前会话操作人
         * @param appId 平台APP标识
         * @return 平台APP Client Secret
         */
         string lookupApplicationClientSecret(string appId) throws com::jimi::api::ApiException;
    };

}
}}}}