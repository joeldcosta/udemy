import requests
#ID = 100001

for ID in range(100000,200000):     
     try:
          url = 'https://www.udemy.com/api-2.0/discovery-units/?context=clp-free&from=0&page_size=6&item_count=18&course_id='+str(ID)+'&source_page=course_landing_page&locale=en_US&currency=inr&navigation_locale=en_US&skip_price=true'
          re = requests.get(url)
          json = re.json()

          u = json['units'][0]['source_objects'][0]['url']
          source = 'https://www.udemy.com'+u
          title = json['units'][0]['source_objects'][0]['title']
          

          price = 'https://www.udemy.com/api-2.0/pricing/?course_ids='+str(ID)+'&fields[pricing_result]=price,discount_price,list_price,price_detail,price_serve_tracking_id'
          p_re = requests.get(price)
          json_price = p_re.json()

          rate = json_price['courses'][str(ID)]['price']['price_string']
          print()
          print("ID no. "+str(ID))
          print(source)
          print(title)
          print(rate)
          if 'ython' in title:
               if 'Free' in rate:
                    with open('udemy.txt','a+') as udy:
                         udy.writelines("ID no. "+str(ID)+'\n'+
                                        source+'\n'+
                                        title+'\n'+
                                        rate+'\n')
     except:
          pass


