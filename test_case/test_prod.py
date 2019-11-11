from tools.api import request_tool
from tools.security.md5_tool import md5_passwd


def test_post_json_prod_1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '商品新增'  # allure报告中二级分类
    title = "商品新增正常流1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers ={"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "brand": "红牛牛",
  "colors": [
    "黑色","白色"
  ],
  "price": 1888,
  "productCode": "自动生成 字符串 5 数字字母",
  "productName": "V5",
  "sizes": [
    "翻盖"
  ],
  "type": "mobilPhone"
}
    '''
    status_code = 200  # 响应状态码
    json_path = [{"productCode":"$.data[0].productCode"}]
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]
    pub_data["prodCode"]=r.json()["data"][0]["productCode"]

def test_change_price(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "商品价格全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":pub_data["skuCode"],"price":3333}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


def test_post_changePriceByProdCode(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '商品模块'  # allure报告中二级分类
    title = "商品模块全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"prodCode":pub_data["prodCode"],"price":3333}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    json_path = [{"productCode":"$.data[0].productCode"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_product_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '商品模块'  # allure报告中二级分类
    title = "修改商品下架全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":"${prodCode}"}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # json_path = [{"productCode":"$.productCode"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


def test_post_product_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '锁定用户'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/user/lock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"userName":'xuepl122'}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


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
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_addOrder(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '新增订单'  # allure报告中二级分类
    title = "新增订单全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token":"$token"}
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
    request_tool.request(headers = headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)





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
