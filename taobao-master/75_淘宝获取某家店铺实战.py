import re
import requests
import json
import csv
import time

with open('taobao2.csv','w',encoding='ANSI',newline='') as filename: 
        csvwriter = csv.DictWriter(filename,fieldnames=['标题','价格','店铺','购买人数','地点','商品详情页','店铺链接','图片链接'])
        csvwriter.writeheader()
        for i in range(1,100):
                time.sleep(2)
                url = f'https://s.taobao.com/search?q=%E7%88%B1%E4%BE%9D%E6%9C%8D&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20221026&ie=utf8&bcoffset=2&ntoffset=2&p4ppushleft=2%2C48&s={i*44}'
                headers = {
                        'cookie': 'thw=cn; cna=SJBLGjLZ8A0CAXFaa2FGCY+B; tracknick=%5Cu6708%5Cu4EAE%5Cu6708%5Cu4EAEduang; miid=6691168651885012083; lgc=%5Cu6708%5Cu4EAE%5Cu6708%5Cu4EAEduang; t=e9469098d189b4ce89caa76500ece25e; enc=%2BMYZumBqrxN8tksebnCB0X12K3h2stwpzcmBvTLx1qtrJTX6IPi8oLVU2ypy5ZDph%2FDS8PRpWrf5KebjKgKNdw%3D%3D; mt=ci=27_1; _m_h5_tk=662113fc01a6706d46387f50092b4677_1666687433553; _m_h5_tk_enc=48356351c26577b03510dcc93906a4a3; _samesite_flag_=true; cookie2=1e7c2b464aac0d59ae98b2f46bb2f58b; _tb_token_=ee8b85530333e; unb=2356524382; cancelledSubSites=empty; cookie17=UUtO%2FnNrzSi82A%3D%3D; dnk=%5Cu6708%5Cu4EAE%5Cu6708%5Cu4EAEduang; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=g25; _nk_=%5Cu6708%5Cu4EAE%5Cu6708%5Cu4EAEduang; cookie1=VACOTbYetMGBJ40PDCJ4PF%2FoIQZAYlc1HdTnjTRx9Sk%3D; xlly_s=1; sgcookie=E100vX6QvI7e8hitR10TRR7ebDE8%2BoDVijS8FcwV%2F11CMgzDRHcUDpB%2BfMsw5PYrII8KH94dJ0zgdcNX7IMNvVrAapYVbi4F8ZCgQzb0Hytbb3Y%3D; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie14=UoeyCGHzjkDPnw%3D%3D&existShop=false&pas=0; uc3=id2=UUtO%2FnNrzSi82A%3D%3D&vt3=F8dCv4oe2OgHJJjdsyg%3D&lg2=UtASsssmOIJ0bQ%3D%3D&nk2=txRmxvwawPg5k0FEZg%3D%3D; csg=95cfb877; skt=768c30978e8806bd; existShop=MTY2Njc3NzUxMg%3D%3D; uc4=id4=0%40U2l0u27JK4MKxZ52fbRCpbiFlOzn&nk4=0%40tWdApSCho72ZUcJSDW0A2oXJ4IRu74Eo; alitrackid=www.tmall.com; lastalitrackid=www.tmall.com; JSESSIONID=1D59A9A2D762B081C51E09D371C431B2; l=eBInJlPPg81JpUcEBOfwourza77OSIRA_uPzaNbMiOCP96fp5BcRW6y_IqT9C3GVh6byR3JmWBbDBeYBqIv4n5U62j-la_kmn; isg=BGRk0Ytk2474rS3ycst3yP-8NWJW_Yhn5MqwC36F8C_yKQTzpg1Y95qL6YEx9sC_; tfstk=cbXNBAXeYRea6osYypvVUARlxl9OZKODav-vsrbT9wS44hOGiq3vxll6Y3nEoCf..',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': "Windows",
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'upgrade-insecure-requests': '1',
                        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
                        }
                response = requests.get(url=url,headers=headers)
                # print(response.text)
                html_data = re.findall('g_page_config = (.*);',response.text)[0]
                # print(html_data)
                json_data = json.loads(html_data)
                # print(json_data)
                data = json_data['mods']['itemlist']['data']['auctions']
                for index in data:
                        try:
                                dict = {
                                        '标题':index['raw_title'],
                                        '价格':index['view_price'],
                                        '店铺':index['nick'],
                                        '购买人数':index['view_sales'],
                                        '地点':index['item_loc'],
                                        '商品详情页':'https:'+index['detail_url'],
                                        '店铺链接':'https:'+index['shopLink'],
                                        '图片链接':'https:'+index['pic_url']
                                        }
                                csvwriter.writerow(dict)
                                print(dict)  
                        except Exception as e:
                                print(e)
                        

