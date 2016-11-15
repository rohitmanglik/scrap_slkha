'''

from bs4 import BeautifulSoup
from urllib import urlopen
import requests
import csv



csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

with open('/home/aakash/data/sulekha_scrap_data2.csv','w') as mycsv:
	c = csv.writer(mycsv, dialect='mydialect')
	c.writerow(['Name','Phone','Address','City','Pincode','Country','Mail','Website','Person to Contact','Working Hours', 'Services Offered', 'About', 'Images URL'])

	
	x1 = 1
	while x1 != 0:
		url = 'http://yellowpages.sulekha.com/coaching-tuitions_delhi' + '_' + str(x1)
		headers = {'User-agent': 'Mozilla/5.0'}
		webpage = requests.get( url, headers=headers )
		soup = BeautifulSoup(webpage.content, "html.parser")

		if soup.find('li', class_ = 'next') is not None:
		
			stores_url = soup.find_all('a', class_='YPTRACK GAQ_C_BUSL')

			for store_url in stores_url :
				url = 'http://yellowpages.sulekha.com'+store_url['href']
		
				headers = {'User-agent': 'Mozilla/5.0'}
				webpage = requests.get( url, headers=headers )

				soup = BeautifulSoup(webpage.content, "html.parser")
	
				store_det = {}

				store_det['name']='N/A'
				store_det['phone']='N/A'
				store_det['addr']='N/A'
				store_det['mail']='N/A'
				store_det['website']='N/A'
				store_det['contact_person']='N/A'
				store_det['working_hours']='N/A'
				store_det['services_offered']=''
				store_det['about'] = 'N/A'
				store_det['images'] = ''

				temp = soup.find_all('div', class_='profile-child')

				#print(temp[4])
				#print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
				store_det['name'] = soup.find('span', itemprop='name').get_text()
				print(store_det['name'])

				store_det['phone'] = temp[0].find('em',itemprop='telephone').get_text()
				print(store_det['phone'])	
	
				if temp[1].find('span',itemprop='streetAddress') is not None and temp[1].find('span',itemprop='addressRegion') is not None and temp[1].find('span',itemprop='postalCode') is not None:
					store_det['addr'] = temp[1].find('span',itemprop='streetAddress').get_text() +', '+ temp[1].find('a').get_text() +', '+ temp[1].find('span',itemprop='addressRegion').get_text() +'-'+ temp[1].find('span',itemprop='postalCode').get_text()
				print(store_det['addr'])

				if temp[2].find('a') is not None:
					store_det['mail'] = temp[2].find('a')['href'].replace('mailto:','')
				print(store_det['mail'])
	
				if temp[3].find('a') is not None:
					store_det['website'] = temp[3].find('a')['weburl']
				print(store_det['website'])

				if temp[4] is not None:
					store_det['contact_person'] = temp[4].get_text()
				print(store_det['contact_person'] )

				if len(temp) >= 6 and temp[5].find('em') is not None:
					store_det['working_hours'] = temp[5].find('em').get_text()
				print(store_det['working_hours'])

				if len(temp) >= 7:
					temp2 = temp[6].find_all('a')
					for x in range(len(temp2)-1):
						if 'Show more' in temp2[x].get_text() : continue
						store_det['services_offered'] += temp2[x].get_text()+', '
				print(store_det['services_offered'])
	
				#print(soup.find('div', id='showlessabtbuslist'))
				#print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
				if soup.find('div', id='showlessabtbuslist') is not None and soup.find('div', id='showlessabtbuslist').find('p') is not None:
					store_det['about'] = soup.find('div', id='showlessabtbuslist').find('p').get_text()
				print(store_det['about'])
			
				#print(soup.find_all('img', class_='lazy-gallery'))
	
				if soup.find_all('img', class_='lazy-gallery') is not None:
					temp = soup.find_all('img', class_='lazy-gallery')
					for y in temp:
						store_det['images'] += y['data-original'] + ', '
				print(store_det['images'])

				pin = store_det['addr'][store_det['addr'].find('i-'):].replace('i-','')

				c.writerow([
				store_det['name'].encode('utf8'),
				store_det['phone'].encode('utf8'),
				store_det['addr'][:store_det['addr'].find(', Delhi')].encode('utf8'),
				"Delhi".encode('utf8'),
				pin.encode('utf8'),
				'India'.encode('utf8'),
				store_det['mail'].encode('utf8'),
				store_det['website'].encode('utf8'),
				store_det['contact_person'].encode('utf8'),
				store_det['working_hours'].encode('utf8'),
				store_det['services_offered'].encode('utf8'),
				store_det['about'].encode('utf8'),
				store_det['images'].encode('utf8') ])
		x1+=1
	
		print('\n--------------------------------------------\n')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print(x1)
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

'''

##########################################################################

from bs4 import BeautifulSoup
from urllib import urlopen
import requests
import csv

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)


count = 0
with open('/home/4r0r4/Desktop/data/sulekha/scrap'+str(count)+'-'+str(count+1000)+'.csv', 'w') as mycsv:
	c = csv.writer(mycsv, dialect='mydialect')	
	c.writerow(['Name','Phone1','Phone2','Phone3','Phone4','Phone5','Street Address','Locality','Pincode','City','Country',
		'Mail','Website','Person to Contact','Working Hours', 'Services Offered', 'Details', 'Images URL','Keywords'])
					

	url = 'http://yellowpages.sulekha.com/administration-training-centres_all-cities#listing'

	headers = {'User-agent': 'Mozilla/5.0'}
	webpage = requests.get( url, headers=headers )
	soup = BeautifulSoup(webpage.content, "html.parser")

	cities_li = []
	cities_temp = soup.find_all('ul', class_='unstyled')
	for x in cities_temp :
		for y in x.find_all('a'):
			t = y['href']
			cities_li.append(t[t.find('_')+1:])
	print(cities_li)

	temp_count = 1
	for city in cities_li:

		print('!!!!!!!!!!CITY!!!!!!!!!!')
		print(city)
		
		try : 
			url1 = 'http://yellowpages.sulekha.com/coaching-tuitions_'+ city + '_'+ str(temp_count)
			temp_count += 1
			####################NEXT PAGE
			

			while(True):

				headers = {'User-agent': 'Mozilla/5.0'}
				webpage = requests.get( url1, headers=headers )
				soup = BeautifulSoup(webpage.content, "html.parser")


				stores_url = soup.find_all('a', class_='YPTRACK GAQ_C_BUSL')

				for store_url in stores_url :

					url_t = 'http://yellowpages.sulekha.com'+store_url['href']
					print(url_t)

					headers = {'User-agent': 'Mozilla/5.0'}
					webpage = requests.get( url_t, headers=headers )
					soup = BeautifulSoup(webpage.content, "html.parser")

					keywords = ''
					image_urls = ''
					details = ''
					services_offered = ''
					working_hours = ''
					contact_person = ''
					website = ''
					mail = ''
					postal_code = ''
					locality_address = ''
					street_address = ''
					phones = ''
					name = ''
					country = 'India'
					phone = ['', '', '', '', '']

					name = soup.find('span', itemprop='name').get_text()
					print(name)

					temp_det = soup.find('div', class_='profile-list')

					if temp_det.find('em', itemprop='telephone') is not None:
						phones = temp_det.find('em', itemprop='telephone').get_text()
					print(phones)
					temp_phones = phones.split(',')
					for p in range(len(temp_phones)):
						if p < 5:
							phone[p] = temp_phones[p]
					
					if temp_det.find('span', itemprop='streetAddress') is not None:
						street_address = temp_det.find('span', itemprop='streetAddress').get_text()
					print(street_address)
					if temp_det.find('span', itemprop='addressLocality') is not None and temp_det.find('span', itemprop='addressLocality').find('a') is not None:
						locality_address = temp_det.find('span', itemprop='addressLocality').get_text()
					print(locality_address)
					if temp_det.find('span', itemprop='postalCode') is not None:
						postal_code = temp_det.find('span', itemprop='postalCode').get_text()
					print(postal_code)
					print(city)
					print('*************')

					if temp_det.find('span', itemprop='email') is not None and  temp_det.find('span', itemprop='email').find('a') is not None:
						mail = temp_det.find('span', itemprop='email').find('a').get_text()
					print(mail)
					
					if temp_det.find('a', id='websitelink') is not None:
						website = temp_det.find('a', id='websitelink')['weburl']
					print(website)

					for x in temp_det.find_all('div', class_='profile-details'):
						if x.find('strong') is not None and 'Contact Person' in x.find('strong').get_text() and x.find('div', class_='profile-child') is not None :
							contact_person = x.find('div', class_='profile-child').get_text()
					print(contact_person)

					if temp_det.find('time', itemprop='openingHours') is not None and temp_det.find('time', itemprop='openingHours').find('em') is not None:
						working_hours = temp_det.find('time', itemprop='openingHours').find('em').get_text()
					print(working_hours)

					services_offered = ''
					if temp_det.find('span', id='showlesscatlist') is not None:
						for x in temp_det.find('span', id='showlesscatlist').find_all('a', itemprop='name'):
							services_offered += x.get_text() + ' # '
					print(services_offered)

					if soup.find('div', id='showlessabtbuslist') is not None and soup.find('div', id='showlessabtbuslist').find('p') is not None:
						details = soup.find('div', id='showlessabtbuslist').get_text()
						details = details.encode('ascii',errors='ignore').replace('Show less','')
					print(details)

					image_urls = ''
					if soup.find_all('img', class_='lazy-gallery') is not None:
						temp_images = soup.find_all('img', class_='lazy-gallery')
						for y in temp_images:
							if 'gif' not in str(y['data-original']):
								image_urls += y['data-original'] + ' # '
					print(image_urls)

					keywords = ''
					if soup.find('ul', id='alldivtype') is not None:
						for x in soup.find('ul', id='alldivtype').find_all('a'):
							keywords += x.get_text() + ' # '
					print(keywords)

					print('\n----------------------------------------------------\n')

					c.writerow([
						name.encode('utf8'),
						phone[0].encode('utf8'),
						phone[1].encode('utf8'),
						phone[2].encode('utf8'),
						phone[3].encode('utf8'),
						phone[4].encode('utf8'),
						street_address.encode('utf8'),
						locality_address.encode('utf8'),
						postal_code.encode('utf8'),
						city.encode('utf8'),
						'India'.encode('utf8'),
						mail.encode('utf8'),
						website.encode('utf8'),
						contact_person.encode('utf8'),
						working_hours.encode('utf8'),
						services_offered.encode('utf8'),
						details.encode('utf8'),
						image_urls.encode('utf8'),
						keywords.encode('utf8')
						])

					count += 1
					print 'count : ', count

				print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
				
		except:
			continue




		'''
		url = 'http://yellowpages.sulekha.com/computer-training-centres_'+city+'_clistings'
		
		headers = {'User-agent': 'Mozilla/5.0'}
		webpage = requests.get( url, headers=headers )
		soup = BeautifulSoup(webpage.content, "html.parser")

		'''












