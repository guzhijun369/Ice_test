# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.2
#
# <auto-generated>
#
# Generated from file `platform.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
from model import platform_header_ice

# Included module com
_M_com = Ice.openModule('com')

# Included module com.jimi
_M_com.jimi = Ice.openModule('com.jimi')

# Included module com.jimi.user
_M_com.jimi.user = Ice.openModule('com.jimi.user')

# Included module com.jimi.user.api
_M_com.jimi.user.api = Ice.openModule('com.jimi.user.api')

# Included module com.jimi.user.api.system
_M_com.jimi.user.api.system = Ice.openModule('com.jimi.user.api.system')

# Included module com.jimi.user.api.system.dto
_M_com.jimi.user.api.system.dto = Ice.openModule('com.jimi.user.api.system.dto')

# Start of module com
__name__ = 'com'

# Start of module com.jimi
__name__ = 'com.jimi'

# Start of module com.jimi.user
__name__ = 'com.jimi.user'

# Start of module com.jimi.user.api
__name__ = 'com.jimi.user.api'

# Start of module com.jimi.user.api.system
__name__ = 'com.jimi.user.api.system'

if '_t_PlatformList' not in _M_com.jimi.user.api.system.__dict__:
    _M_com.jimi.user.api.system._t_PlatformList = IcePy.defineSequence('::com::jimi::user::api::system::PlatformList', (), _M_com.jimi.user.api.system.dto._t_PlatformOutputDTO)

if '_t_PlatformAppList' not in _M_com.jimi.user.api.system.__dict__:
    _M_com.jimi.user.api.system._t_PlatformAppList = IcePy.defineSequence('::com::jimi::user::api::system::PlatformAppList', (), _M_com.jimi.user.api.system.dto._t_PlatformAppOutputDTO)

_M_com.jimi.user.api.system._t_PlatformService = IcePy.defineValue('::com::jimi::user::api::system::PlatformService', Ice.Value, -1, (), False, True, None, ())

if 'PlatformServicePrx' not in _M_com.jimi.user.api.system.__dict__:
    _M_com.jimi.user.api.system.PlatformServicePrx = Ice.createTempClass()
    class PlatformServicePrx(Ice.ObjectPrx):

        """
        添加平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        context -- The request context for the invocation.
        Returns: 平新增加平台信息
        """
        def addPlatform(self, accout, platformInputDTO, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_addPlatform.invoke(self, ((accout, platformInputDTO), context))

        """
        添加平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def addPlatformAsync(self, accout, platformInputDTO, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_addPlatform.invokeAsync(self, ((accout, platformInputDTO), context))

        """
        添加平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_addPlatform(self, accout, platformInputDTO, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_addPlatform.begin(self, ((accout, platformInputDTO), _response, _ex, _sent, context))

        """
        添加平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        Returns: 平新增加平台信息
        """
        def end_addPlatform(self, _r):
            return _M_com.jimi.user.api.system.PlatformService._op_addPlatform.end(self, _r)

        """
        更新平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        context -- The request context for the invocation.
        """
        def updatePlatform(self, accout, platformInputDTO, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_updatePlatform.invoke(self, ((accout, platformInputDTO), context))

        """
        更新平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def updatePlatformAsync(self, accout, platformInputDTO, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_updatePlatform.invokeAsync(self, ((accout, platformInputDTO), context))

        """
        更新平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_updatePlatform(self, accout, platformInputDTO, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_updatePlatform.begin(self, ((accout, platformInputDTO), _response, _ex, _sent, context))

        """
        更新平台信息
        Arguments:
        accout -- 当前会话操作人
        platformInputDTO -- 平台相关信息
        """
        def end_updatePlatform(self, _r):
            return _M_com.jimi.user.api.system.PlatformService._op_updatePlatform.end(self, _r)

        """
        删除平台信息
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        context -- The request context for the invocation.
        """
        def deletePlatformBy(self, accout, platformCode, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_deletePlatformBy.invoke(self, ((accout, platformCode), context))

        """
        删除平台信息
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def deletePlatformByAsync(self, accout, platformCode, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_deletePlatformBy.invokeAsync(self, ((accout, platformCode), context))

        """
        删除平台信息
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_deletePlatformBy(self, accout, platformCode, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_deletePlatformBy.begin(self, ((accout, platformCode), _response, _ex, _sent, context))

        """
        删除平台信息
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        """
        def end_deletePlatformBy(self, _r):
            return _M_com.jimi.user.api.system.PlatformService._op_deletePlatformBy.end(self, _r)

        """
        获取所有平台信息
        Arguments:
        accout -- 当前会话操作人
        context -- The request context for the invocation.
        Returns: 平台信息列表
        """
        def getAllPlatform(self, accout, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_getAllPlatform.invoke(self, ((accout, ), context))

        """
        获取所有平台信息
        Arguments:
        accout -- 当前会话操作人
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def getAllPlatformAsync(self, accout, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_getAllPlatform.invokeAsync(self, ((accout, ), context))

        """
        获取所有平台信息
        Arguments:
        accout -- 当前会话操作人
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getAllPlatform(self, accout, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_getAllPlatform.begin(self, ((accout, ), _response, _ex, _sent, context))

        """
        获取所有平台信息
        Arguments:
        accout -- 当前会话操作人
        Returns: 平台信息列表
        """
        def end_getAllPlatform(self, _r):
            return _M_com.jimi.user.api.system.PlatformService._op_getAllPlatform.end(self, _r)

        """
        重置平台Client相关内容
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        context -- The request context for the invocation.
        Returns: 重置后的平台 Client Secret
        """
        def resetPlatformClientSecret(self, accout, platformCode, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_resetPlatformClientSecret.invoke(self, ((accout, platformCode), context))

        """
        重置平台Client相关内容
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def resetPlatformClientSecretAsync(self, accout, platformCode, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_resetPlatformClientSecret.invokeAsync(self, ((accout, platformCode), context))

        """
        重置平台Client相关内容
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_resetPlatformClientSecret(self, accout, platformCode, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_resetPlatformClientSecret.begin(self, ((accout, platformCode), _response, _ex, _sent, context))

        """
        重置平台Client相关内容
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        Returns: 重置后的平台 Client Secret
        """
        def end_resetPlatformClientSecret(self, _r):
            return _M_com.jimi.user.api.system.PlatformService._op_resetPlatformClientSecret.end(self, _r)

        """
        查看平台 Client Secret
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        context -- The request context for the invocation.
        Returns: 平台 Client Secret
        """
        def lookupPlatformClientSecret(self, accout, platformCode, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_lookupPlatformClientSecret.invoke(self, ((accout, platformCode), context))

        """
        查看平台 Client Secret
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def lookupPlatformClientSecretAsync(self, accout, platformCode, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_lookupPlatformClientSecret.invokeAsync(self, ((accout, platformCode), context))

        """
        查看平台 Client Secret
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_lookupPlatformClientSecret(self, accout, platformCode, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.PlatformService._op_lookupPlatformClientSecret.begin(self, ((accout, platformCode), _response, _ex, _sent, context))

        """
        查看平台 Client Secret
        Arguments:
        accout -- 当前会话操作人
        platformCode -- 平台编码
        Returns: 平台 Client Secret
        """
        def end_lookupPlatformClientSecret(self, _r):
            return _M_com.jimi.user.api.system.PlatformService._op_lookupPlatformClientSecret.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_com.jimi.user.api.system.PlatformServicePrx.ice_checkedCast(proxy, '::com::jimi::user::api::system::PlatformService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_com.jimi.user.api.system.PlatformServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::com::jimi::user::api::system::PlatformService'
    _M_com.jimi.user.api.system._t_PlatformServicePrx = IcePy.defineProxy('::com::jimi::user::api::system::PlatformService', PlatformServicePrx)

    _M_com.jimi.user.api.system.PlatformServicePrx = PlatformServicePrx
    del PlatformServicePrx

    _M_com.jimi.user.api.system.PlatformService = Ice.createTempClass()
    class PlatformService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::com::jimi::user::api::system::PlatformService')

        def ice_id(self, current=None):
            return '::com::jimi::user::api::system::PlatformService'

        @staticmethod
        def ice_staticId():
            return '::com::jimi::user::api::system::PlatformService'

        def addPlatform(self, accout, platformInputDTO, current=None):
            """
            添加平台信息
            Arguments:
            accout -- 当前会话操作人
            platformInputDTO -- 平台相关信息
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'addPlatform' not implemented")

        def updatePlatform(self, accout, platformInputDTO, current=None):
            """
            更新平台信息
            Arguments:
            accout -- 当前会话操作人
            platformInputDTO -- 平台相关信息
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'updatePlatform' not implemented")

        def deletePlatformBy(self, accout, platformCode, current=None):
            """
            删除平台信息
            Arguments:
            accout -- 当前会话操作人
            platformCode -- 平台编码
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'deletePlatformBy' not implemented")

        def getAllPlatform(self, accout, current=None):
            """
            获取所有平台信息
            Arguments:
            accout -- 当前会话操作人
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'getAllPlatform' not implemented")

        def resetPlatformClientSecret(self, accout, platformCode, current=None):
            """
            重置平台Client相关内容
            Arguments:
            accout -- 当前会话操作人
            platformCode -- 平台编码
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'resetPlatformClientSecret' not implemented")

        def lookupPlatformClientSecret(self, accout, platformCode, current=None):
            """
            查看平台 Client Secret
            Arguments:
            accout -- 当前会话操作人
            platformCode -- 平台编码
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'lookupPlatformClientSecret' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_com.jimi.user.api.system._t_PlatformServiceDisp)

        __repr__ = __str__

    _M_com.jimi.user.api.system._t_PlatformServiceDisp = IcePy.defineClass('::com::jimi::user::api::system::PlatformService', PlatformService, (), None, ())
    PlatformService._ice_type = _M_com.jimi.user.api.system._t_PlatformServiceDisp

    PlatformService._op_addPlatform = IcePy.Operation('addPlatform', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), _M_com.jimi.user.api.system.dto._t_PlatformInputDTO, False, 0)), (), ((), _M_com.jimi.user.api.system.dto._t_PlatformOutputDTO, False, 0), ())
    PlatformService._op_updatePlatform = IcePy.Operation('updatePlatform', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), _M_com.jimi.user.api.system.dto._t_PlatformInputDTO, False, 0)), (), None, ())
    PlatformService._op_deletePlatformBy = IcePy.Operation('deletePlatformBy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())
    PlatformService._op_getAllPlatform = IcePy.Operation('getAllPlatform', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0),), (), ((), _M_com.jimi.user.api.system._t_PlatformList, False, 0), ())
    PlatformService._op_resetPlatformClientSecret = IcePy.Operation('resetPlatformClientSecret', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_string, False, 0), ())
    PlatformService._op_lookupPlatformClientSecret = IcePy.Operation('lookupPlatformClientSecret', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_string, False, 0), ())

    _M_com.jimi.user.api.system.PlatformService = PlatformService
    del PlatformService

_M_com.jimi.user.api.system._t_ApplicationService = IcePy.defineValue('::com::jimi::user::api::system::ApplicationService', Ice.Value, -1, (), False, True, None, ())

if 'ApplicationServicePrx' not in _M_com.jimi.user.api.system.__dict__:
    _M_com.jimi.user.api.system.ApplicationServicePrx = Ice.createTempClass()
    class ApplicationServicePrx(Ice.ObjectPrx):

        """
        添加平台APP信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        context -- The request context for the invocation.
        Returns: 平新增加平台App信息
        """
        def addApplication(self, accout, platformAppInputDTO, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_addApplication.invoke(self, ((accout, platformAppInputDTO), context))

        """
        添加平台APP信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def addApplicationAsync(self, accout, platformAppInputDTO, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_addApplication.invokeAsync(self, ((accout, platformAppInputDTO), context))

        """
        添加平台APP信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_addApplication(self, accout, platformAppInputDTO, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_addApplication.begin(self, ((accout, platformAppInputDTO), _response, _ex, _sent, context))

        """
        添加平台APP信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        Returns: 平新增加平台App信息
        """
        def end_addApplication(self, _r):
            return _M_com.jimi.user.api.system.ApplicationService._op_addApplication.end(self, _r)

        """
        删除平台APP信息
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP相关信息
        context -- The request context for the invocation.
        """
        def deleteApplicationBy(self, accout, appId, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_deleteApplicationBy.invoke(self, ((accout, appId), context))

        """
        删除平台APP信息
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP相关信息
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def deleteApplicationByAsync(self, accout, appId, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_deleteApplicationBy.invokeAsync(self, ((accout, appId), context))

        """
        删除平台APP信息
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP相关信息
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_deleteApplicationBy(self, accout, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_deleteApplicationBy.begin(self, ((accout, appId), _response, _ex, _sent, context))

        """
        删除平台APP信息
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP相关信息
        """
        def end_deleteApplicationBy(self, _r):
            return _M_com.jimi.user.api.system.ApplicationService._op_deleteApplicationBy.end(self, _r)

        """
        更新平台App信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        context -- The request context for the invocation.
        """
        def updateApplication(self, accout, platformAppInputDTO, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_updateApplication.invoke(self, ((accout, platformAppInputDTO), context))

        """
        更新平台App信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def updateApplicationAsync(self, accout, platformAppInputDTO, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_updateApplication.invokeAsync(self, ((accout, platformAppInputDTO), context))

        """
        更新平台App信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_updateApplication(self, accout, platformAppInputDTO, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_updateApplication.begin(self, ((accout, platformAppInputDTO), _response, _ex, _sent, context))

        """
        更新平台App信息
        Arguments:
        accout -- 当前会话操作人
        platformAppInputDTO -- 平台APP相关信息
        """
        def end_updateApplication(self, _r):
            return _M_com.jimi.user.api.system.ApplicationService._op_updateApplication.end(self, _r)

        """
        获取所有平台App信息
        Arguments:
        accout -- 当前会话操作人
        context -- The request context for the invocation.
        Returns: 平台APP信息列表
        """
        def getAllApplications(self, accout, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_getAllApplications.invoke(self, ((accout, ), context))

        """
        获取所有平台App信息
        Arguments:
        accout -- 当前会话操作人
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def getAllApplicationsAsync(self, accout, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_getAllApplications.invokeAsync(self, ((accout, ), context))

        """
        获取所有平台App信息
        Arguments:
        accout -- 当前会话操作人
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getAllApplications(self, accout, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_getAllApplications.begin(self, ((accout, ), _response, _ex, _sent, context))

        """
        获取所有平台App信息
        Arguments:
        accout -- 当前会话操作人
        Returns: 平台APP信息列表
        """
        def end_getAllApplications(self, _r):
            return _M_com.jimi.user.api.system.ApplicationService._op_getAllApplications.end(self, _r)

        """
        重置平台APP Client相关内容
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        context -- The request context for the invocation.
        Returns: 重置后平台APP Client Secret
        """
        def resetApplicationClientSecret(self, accout, appId, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_resetApplicationClientSecret.invoke(self, ((accout, appId), context))

        """
        重置平台APP Client相关内容
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def resetApplicationClientSecretAsync(self, accout, appId, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_resetApplicationClientSecret.invokeAsync(self, ((accout, appId), context))

        """
        重置平台APP Client相关内容
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_resetApplicationClientSecret(self, accout, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_resetApplicationClientSecret.begin(self, ((accout, appId), _response, _ex, _sent, context))

        """
        重置平台APP Client相关内容
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        Returns: 重置后平台APP Client Secret
        """
        def end_resetApplicationClientSecret(self, _r):
            return _M_com.jimi.user.api.system.ApplicationService._op_resetApplicationClientSecret.end(self, _r)

        """
        查看平台APP Client Secret
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        context -- The request context for the invocation.
        Returns: 平台APP Client Secret
        """
        def lookupApplicationClientSecret(self, accout, appId, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_lookupApplicationClientSecret.invoke(self, ((accout, appId), context))

        """
        查看平台APP Client Secret
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        context -- The request context for the invocation.
        Returns: A future object for the invocation.
        """
        def lookupApplicationClientSecretAsync(self, accout, appId, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_lookupApplicationClientSecret.invokeAsync(self, ((accout, appId), context))

        """
        查看平台APP Client Secret
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        context -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_lookupApplicationClientSecret(self, accout, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationService._op_lookupApplicationClientSecret.begin(self, ((accout, appId), _response, _ex, _sent, context))

        """
        查看平台APP Client Secret
        Arguments:
        accout -- 当前会话操作人
        appId -- 平台APP标识
        Returns: 平台APP Client Secret
        """
        def end_lookupApplicationClientSecret(self, _r):
            return _M_com.jimi.user.api.system.ApplicationService._op_lookupApplicationClientSecret.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_com.jimi.user.api.system.ApplicationServicePrx.ice_checkedCast(proxy, '::com::jimi::user::api::system::ApplicationService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_com.jimi.user.api.system.ApplicationServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::com::jimi::user::api::system::ApplicationService'
    _M_com.jimi.user.api.system._t_ApplicationServicePrx = IcePy.defineProxy('::com::jimi::user::api::system::ApplicationService', ApplicationServicePrx)

    _M_com.jimi.user.api.system.ApplicationServicePrx = ApplicationServicePrx
    del ApplicationServicePrx

    _M_com.jimi.user.api.system.ApplicationService = Ice.createTempClass()
    class ApplicationService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::com::jimi::user::api::system::ApplicationService')

        def ice_id(self, current=None):
            return '::com::jimi::user::api::system::ApplicationService'

        @staticmethod
        def ice_staticId():
            return '::com::jimi::user::api::system::ApplicationService'

        def addApplication(self, accout, platformAppInputDTO, current=None):
            """
            添加平台APP信息
            Arguments:
            accout -- 当前会话操作人
            platformAppInputDTO -- 平台APP相关信息
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'addApplication' not implemented")

        def deleteApplicationBy(self, accout, appId, current=None):
            """
            删除平台APP信息
            Arguments:
            accout -- 当前会话操作人
            appId -- 平台APP相关信息
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'deleteApplicationBy' not implemented")

        def updateApplication(self, accout, platformAppInputDTO, current=None):
            """
            更新平台App信息
            Arguments:
            accout -- 当前会话操作人
            platformAppInputDTO -- 平台APP相关信息
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'updateApplication' not implemented")

        def getAllApplications(self, accout, current=None):
            """
            获取所有平台App信息
            Arguments:
            accout -- 当前会话操作人
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'getAllApplications' not implemented")

        def resetApplicationClientSecret(self, accout, appId, current=None):
            """
            重置平台APP Client相关内容
            Arguments:
            accout -- 当前会话操作人
            appId -- 平台APP标识
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'resetApplicationClientSecret' not implemented")

        def lookupApplicationClientSecret(self, accout, appId, current=None):
            """
            查看平台APP Client Secret
            Arguments:
            accout -- 当前会话操作人
            appId -- 平台APP标识
            current -- The Current object for the invocation.
            Returns: A future object for the invocation.
            """
            raise NotImplementedError("servant method 'lookupApplicationClientSecret' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_com.jimi.user.api.system._t_ApplicationServiceDisp)

        __repr__ = __str__

    _M_com.jimi.user.api.system._t_ApplicationServiceDisp = IcePy.defineClass('::com::jimi::user::api::system::ApplicationService', ApplicationService, (), None, ())
    ApplicationService._ice_type = _M_com.jimi.user.api.system._t_ApplicationServiceDisp

    ApplicationService._op_addApplication = IcePy.Operation('addApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), _M_com.jimi.user.api.system.dto._t_PlatformAppInputDTO, False, 0)), (), ((), _M_com.jimi.user.api.system.dto._t_PlatformAppOutputDTO, False, 0), ())
    ApplicationService._op_deleteApplicationBy = IcePy.Operation('deleteApplicationBy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())
    ApplicationService._op_updateApplication = IcePy.Operation('updateApplication', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), _M_com.jimi.user.api.system.dto._t_PlatformAppInputDTO, False, 0)), (), None, ())
    ApplicationService._op_getAllApplications = IcePy.Operation('getAllApplications', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0),), (), ((), _M_com.jimi.user.api.system._t_PlatformAppList, False, 0), ())
    ApplicationService._op_resetApplicationClientSecret = IcePy.Operation('resetApplicationClientSecret', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_string, False, 0), ())
    ApplicationService._op_lookupApplicationClientSecret = IcePy.Operation('lookupApplicationClientSecret', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_com.jimi.user.api.system.dto._t_CurrentAccount, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_string, False, 0), ())

    _M_com.jimi.user.api.system.ApplicationService = ApplicationService
    del ApplicationService

# End of module com.jimi.user.api.system

__name__ = 'com.jimi.user.api'

# End of module com.jimi.user.api

__name__ = 'com.jimi.user'

# End of module com.jimi.user

__name__ = 'com.jimi'

# End of module com.jimi

__name__ = 'com'

# End of module com
