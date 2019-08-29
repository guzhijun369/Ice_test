#include "./organization_type_dto.ice"
module com { module jimi { module api { module user {
module organization{

    sequence<dto::OrganizationTypeOutputDTO> OrganizationTypeList;
    /**
     * 机构类型服务接口
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
    interface OrganizationTypeApi {
        /**
         * 检查机构类型code是否存在
         *
         * @return long
         * @date 2019-08-22 15:56
         * @author zhangduanfeng
         * @since 1.0.0
         */
        bool existsByCode(string code) throws com::jimi::api::ApiException;

        /**
         * 添加机构类型
         *
         * @param organizationTypeInputDTO 机构类型输入参数
         * @return organizationTypeInputDTO 机构类型信息
         * @date 2019-08-22 15:56
         * @author zhangduanfeng
         * @since 1.0.0
         */
        dto::OrganizationTypeOutputDTO addOrganizationType(dto::OrganizationTypeInputDTO organizationTypeInputDTO) throws com::jimi::api::ApiException;

        /**
         * 更新机构类型
         *
         * @param organizationTypeInputDTO
         * @return 更新后机构类型信息
         */
        bool updatePlatform(dto::OrganizationTypeInputDTO organizationTypeInputDTO) throws com::jimi::api::ApiException;

        /**
         * 获取所有机构类型列表
         *
         * @param platform 平台  传null 获取所有列表
         * @param pageNum 页码
         * @param pageSize 页数
         * @return 机构类型列表
         */
        OrganizationTypeList findOrganizationTypeByPlatform(string platform, int pageNum, int pageSize);

        /**
         * 根据机构类型编码机构类型
         *
         * @param organizationTypeCode 机构类型编码
         * @return 机构类型信息
         */
        dto::OrganizationTypeOutputDTO findOrganizationTypeByCode(string organizationTypeCode);

        /**
         * 删除机构类型
         *
         * @param account 操作人
         * @param organizationTypeCode 机构类型编码
         * @return void
         */
        void deletePlatformBy(com::jimi::api::CurrentAccount account, string organizationTypeCode) throws com::jimi::api::ApiException;
    }
}
}}}}