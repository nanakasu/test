from tools.api import request_tool





def test_post_addOrder(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '新增订单'  # allure报告中二级分类
    title = "新增订单全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token":"$token"}
    json_path = [{"productCode":"$.data[0].productCode"}]
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "ordeerPrice": 1888,
  "orderLineList": [
    {
      "qty": 0,
      "skuCode": "${skuCode}"
    }
  ],
  "receiver": "nanakasu11",
  "receiverPhone": "18817668777",
  "receivingAddress": "上海市",
  "sign": "${sign}",
  "userName": "nanakasu11"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,headers = headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]
    pub_data["prodCode"]=r.json()["data"][0]["productCode"]



def test_post_order_addOrderSignBody(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = 'Sign'  # allure报告中二级分类
    title = "加密全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None

    headers={"token":"$token"}
    s = "receiver=nanakasu11&ordeerPrice=1888&receiverPhone=18817668777&key=guoya"
    sign = md5_passwd(s,"")
    pub_data["sign"] = sign
    json_data = '''
    {
  "pwd": "xuepl123",
  "userName": "xuepl123"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
