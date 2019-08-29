import os
import time

class ConfigInit():
    ticket_url = 'ticketOrderIce:default -h 172.16.0.8 -p 11000'
    sms_url = 'smsIce123:default -h 172.16.0.8 -p 11000'
    platformapi_url = 'PlatformApi:default -h 172.16.0.57 -p 11000'
    applicationapi_url = 'ApplicationApi:default -h 172.16.0.57 -p 11000'
    accountmanager_url = 'accountApi:default -h 172.16.0.57 -p 11000'
    organizationtypeapi_url = 'OrganizationTypeApi:default -h 172.16.0.57 -p 11000'
    rolemanager_url = 'organizationRoleApi:default -h 172.16.0.57 -p 11000'
    membermanager_url = 'systemMemberApi:default -h 172.16.0.57 -p 11000'




    data_file_name = 'data.xlsx'

# class QueryData():
