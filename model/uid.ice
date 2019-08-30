#include "./common.ice"
module com { module jimi { module api {
module uid{
    /**
     * 全局ID服务
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
    interface IdApi {
        /**
         * 获取64位长整型的ID
         *
         * @return long
         * @date 2019-08-22 15:56
         * @author zhangduanfeng
         * @since 1.0.0
         */
        long getId() throws com::jimi::api::ApiException;
    }
}
}}}