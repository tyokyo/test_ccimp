__author__ = "zhangbo"


from ccimp_systemSettings_app.models.WebConfigModels import WebConfig

import json



#一对一约课记录查询数量
appointConfig = "AppointConfig"

# 调取默认配置表(configKey=AppointConfig)
webConfigs = WebConfig.objects.all()

for w1 in webConfigs:

    if (w1.keyConfig == appointConfig):

        dict_data = w1.valueConfig

        # src转dict
        w1 = json.loads(dict_data)

        limit_appoint_sum = int(w1["sum"])

        break

    else:

        limit_appoint_sum = 5

