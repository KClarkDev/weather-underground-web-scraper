# Author: Katherine Clark
# Date: 12/28/2020
# This script is used to retrieve precipitation totals from WeatherUnderground through web scraping and append those
# values into a CSV file
print("Progress: 0%")

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import datetime
import time
import math
import os

start_time = time.time()
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday_formatted = yesterday.strftime('%Y-%m-%d')

# Create the CSV file to write the data to
# filename = 'rain_data_{}.csv'.format(yesterday_formatted)
filename = r'R:\Resgis\entgis\Resources\Scripts\Inspections_Rain_Data_Script\Script Output\rain_data_{}.csv'.format(yesterday_formatted)
f = open(filename, 'w')
first_line = "Rain Data for {}\n".format(yesterday_formatted)
headers = 'Station, Precipitation_Total\n'
f.write(first_line)
f.write(headers)
f.close()

clear = lambda: os.system('cls')

stations = [
	'KMDMOUNT186','KMDBRAND6', 'KMDBELAI145','KVACLIFT92', 'KVAAPPOM38',
	'KVAAPPOM44', 'KVAEMPOR2', 'KVAWARRE75', 'KVARUSTB22', 'KVANORFO42', 'KVAROCKV3', 'KVASURRY18',
	'KVAPALMY12', 'KVACHEST96','KVACHEST28' ,'KVAWESTP8','KVARUTHE25','KVAWOODB83', 'KVANEWKE12', 'KVASTAFF59',
	'KVAWOODF5', 'KVACHEST109', 'KVAHOPEW6','KVAFRANK27','KVAWILLI55', 'KVAMIDRI1','KVASMITH36','KVAMIDLO191', 'KVAWARRE59']

# stations_test = ['KWVCABIN2', 'KWVMAYSV9', 'KMDWOODS12', 'KMDPOOLE21', 'KMDUPPER33', 'KDCA']
num_stations = len(stations)
count = 0

for station in stations:
	clear()
	count += 1
	percent = round((count / num_stations) * 100)
        
	#url = r"https://www.wunderground.com/dashboard/pws/{}/graph/{}/{}/daily".format(station, yesterday_formatted, yesterday_formatted)

	##################################################################################################################################
	# Date format example: 2020-08-19
	# Example final URL format: https://www.wunderground.com/dashboard/pws/KMDUPPER33/graph/2020-08-19/2020-08-19/daily
        # This is a "quick and dirty" solution for being able to pull rain data from any date in the past, instead of the default which
        #   retrieves the previous days rain data. Note that the CSV output file name will not have the hard-coded date in it, it will
        #   still reflect yesterday's date. However, the data itself s from the hard-coded date specified in the URL.
	# Enter the date you want as a hard-coded value in the url below, then delete the hashtag at the beginning of the line
	#   and add a hashtag to the beginning of the previous url statement above.
	url = r"https://www.wunderground.com/dashboard/pws/{}/graph/2023-03-24/2023-03-24/daily".format(station)
        ##################################################################################################################################

	print(f'Progress: {percent}%')
	# opening up the connection to the page and retrieving the HTML into a variable
	try:
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page_html = urlopen(req).read()

		# making HTML 'human readable' with BeautifulSoup HTML parser
		page_soup = soup(page_html, "html.parser")  # <class 'bs4.BeautifulSoup'>

		# print(soup.prettify())

		tables = page_soup.findAll("table", attrs={"class": "summary-table"})  # <class 'bs4.element.ResultSet'>

		spans = tables[0].findAll("span", attrs={"class": "wu-value wu-value-to"})

		precip_val = spans[9].text
		# print(precip_val.text)

		# Open the CSV in 'append' mode
		f = open(filename, 'a')
		f.write(station + "," + precip_val + '\n')
		f.close()
	except:
		f = open(filename, 'a')
		f.write(station + "," + 'Error' + '\n')
		f.close()

end_time = time.time()
time_elapsed = end_time - start_time
seconds = round(time_elapsed % 60)
minutes = math.floor((time_elapsed)/60)

print(f'Time elapsed: {minutes} minutes, {seconds} seconds')
print("The script has run successfully. Check the Script Output folder for the CSV.")
