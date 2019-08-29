module com { module jimi { module api {
    /**
     * 错误信息枚举，标注错误信息。不包含消息体（message）
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
    enum ErrorCode {
        /** 未知错误*/
        Unknown,
        /** 不存在*/
        NotFound,
        /** 已存在*/
        Existed
    }
    /**
     * Api接口异常类
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
    exception ApiException {
        /** 错误码，枚举。也可以string*/
        ErrorCode errorCode;
    }
    /**
     * 参数输入DTO
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
     ["java:getset"]
    class BaseInputDTO {
        /** 操作人*/
        long operator;
        /** 平台code*/
        string platform;
    }
    /**
     * 分页查询DTO
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
     ["java:getset"]
    class BasePageInputDTO extends BaseInputDTO{
        /** 页面*/
        int page = 1;
        int size = 20;
    }
    /**
     * 参数输出DTO
     *
     * @author zhangduanfeng
     * @date 2019-08-26
     * @since 1.0.0
     */
     ["java:getset"]
    class BaseOutputDTO {}

    /**
     * 当前会话账号信息
     *
     * @date 2019年8月22日 下午2:05:28
     * @author yaojianping
     * @version 1.0
     **/
    ["java:getset"]
    class CurrentAccount {
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
        string platform;
    }
}}}
