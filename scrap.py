from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()
try:
	main_list = []
	main_list2 = []
	p_list = []
	m_list = []
	driver.get("https://www.investing.com/currencies/eur-usd-technical")
	time_list = driver.find_elements_by_xpath(".//ul[@id='timePeriodsWidget']/li")
	time_list[1].click()
	time.sleep(3)
	try:
		driver.find_elements_by_xpath(".//*[@id='timePeriodsWidget']/div[@class='right']/i[@class='popupCloseIcon']").click()
	except Exception as e:
		pass
	item = driver.find_element_by_xpath(".//*[@id='last_last']").text
	item2 = driver.find_element_by_xpath(".//*[@class='arial_20   pid-1-pc redFont']").text
	mabuy = driver.find_element_by_xpath(".//*[@id='maBuy']").text
	mabuy = mabuy[1:-1]
	tibuy = driver.find_element_by_xpath(".//*[@id='tiBuy']").text
	tibuy = tibuy[1:-1]
	datetimev = driver.find_element_by_xpath(".//*[@class='float_lang_base_2 arial_11 bold lighterGrayFont h3TitleDate']").text
	titable = driver.find_elements_by_xpath(".//*[@class='genTbl closedTbl technicalIndicatorsTbl smallTbl float_lang_base_1']/tbody/tr")
	for tr in titable:
		td_data_list = []
		tds = tr.find_elements_by_xpath(".//td")
		if len(tds) > 1:
			for td in tds:
				td_data_list.append(str(td.text))
		else:
			paragraphs = tds[0].find_elements_by_xpath(".//p")
			for p in paragraphs:
				p_list.append(str(p.text))
		if td_data_list:
			main_list.append(td_data_list)
	titable = driver.find_elements_by_xpath(".//*[@class='genTbl closedTbl movingAvgsTbl float_lang_base_2']/tbody/tr")
	for tr in titable:
		ma_data_list = []
		tds = tr.find_elements_by_xpath(".//td")
		if len(tds) > 1:
			for td in tds:
				ma_data_list.append(str(td.text))
		else:
			paragraphs = tds[0].find_elements_by_xpath(".//p")
			for p in paragraphs:
				m_list.append(str(p.text))
		if ma_data_list:
			main_list2.append(ma_data_list)

	driver.close()
	with open('output.csv', 'w+') as file:
		file.write(item+"#"+item2)
		file.write("\n")
		file.write("\n")
		file.write("Moving Averages#"+mabuy)
		file.write("\n")
		file.write("\n")
		file.write("Technical Indicators#"+tibuy)
		file.write("\n")
		file.write("\n")
		file.write("Technical Indicators#"+datetimev)
		file.write("\n")
		file.write("Name#Value#Action")
		file.write("\n")
		for i in main_list:
			data = "#".join(i)
			file.write(data)
			file.write("\n")
		file.write("#".join(p_list))
		file.write("\n")
		file.write("\n")
		file.write("Moving Averages#"+datetimev)
		file.write("\n")
		file.write("Name#Value#Action")
		file.write("\n")
		for i in main_list2:
			data = "#".join(i)
			file.write(data)
			file.write("\n")
		file.write("#".join(m_list))
except Exception as e:
	raise e