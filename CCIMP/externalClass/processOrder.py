# -*- coding: utf-8 -*-：


__author__ = 'zhangbo'
import time
import json


from externalClass.adminLogin import adminLogin

def processOrder(req,order_id_check_val):

    order_id_check_val_list = json.loads(order_id_check_val)

    order_id_check_val_length = len(order_id_check_val_list)

    for i in range(0,order_id_check_val_length):

        processUrl = 'http://crm.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id_check_val_list[i])

        responses_result = req.get(url=processUrl)

        time.sleep(1)

        if (i == order_id_check_val_length -1 ):

            return responses_result


if __name__ == '__main__':

    #调取后台登录接口
    admin_login = adminLogin()

    order_id = "1802055234"

    #调取后台处理订单接口
    processUrl = 'http://crm.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id)

    info = admin_login.get(url=processUrl)

    print(info.text,info.status_code)
