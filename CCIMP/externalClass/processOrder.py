# -*- coding: utf-8 -*-：


__author__ = 'zhangbo'



from externalClass.adminLogin import adminLogin

def processOrder(req,order_id):

    processUrl = 'http://crm.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id)

    responses_result = req.get(url=processUrl)

    return responses_result


if __name__ == '__main__':

    #调取后台登录接口
    admin_login = adminLogin()

    order_id = "1802055234"

    #调取后台处理订单接口
    processUrl = 'http://crm.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id)

    info = admin_login.get(url=processUrl)

    print(info.text,info.status_code)
