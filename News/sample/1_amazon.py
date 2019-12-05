import requests

# 被禁止直接访问
# r = requests.get('https://www.amazon.cn/dp/B07FKJ8589?ref_=Oct_DotdV2_PC_5_GS_DOTD_4509c959&pf_rd_r=9TSSNP8MQVBNCATSEHAX&pf_rd_p=8c48638a-3752-448a-8685-5a17153fb132&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2')
#
# print(r.status_code)
#
# print(r.encoding)
#
# r.encoding = r.apparent_encoding
#
# print(r.request.headers)

# 修改user-agent
agent = {'user-agent':
         'Mozilla/5.0'}
url = 'https://www.amazon.cn/dp/B07FKJ8589?ref_=Oct_DotdV2_PC_5_GS_DOTD_4509c959&pf_rd_r=9TSSNP8MQVBNCATSEHAX&pf_rd_p=8c48638a-3752-448a-8685-5a17153fb132&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2'
response = requests.get(url, headers=agent)
print(response.status_code)
print(response.request.headers)  # 查看请求的头部
response.encoding = response.apparent_encoding
print(response.text)

