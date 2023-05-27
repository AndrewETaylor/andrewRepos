
import os

# Download file only if file doesnot exits already.
def  downloadPriceTxt():
	if not os.path.isfile('prices.txt'):
		import urllib.request
		PRICES_URL ='https://gist.githubusercontent.com/anibali/85f5c4e8eb9881f64650822aa03aa55b/raw/49adefb8a7ffa92da35e4f637cbebdd8ef53352f/prices.txt'
		with open('prices.txt', 'w') as f:
			f.write(urllib.request.urlopen(PRICES_URL).read().decode())
		del f

def main():
	prices_file = open('prices.txt', 'r')

	price_data = prices_file.read().splitlines()

	prices_file.close()

	base_average_calculation_value = 100	# base value =>  will calculate value below this value
	cheapest_value = int(price_data[0])		# Consider Intial first value as cheapest value
	total_base_average_value = []			# Store the value below base value in list

	for each_price_value in price_data:
		each_price_value = int(each_price_value)
		if  each_price_value< cheapest_value:
			cheapest_value = each_price_value

		if each_price_value < base_average_calculation_value:
			total_base_average_value.append(each_price_value)


	print (f"Cheapest item: ${cheapest_value :.2f}")
	print (f"Average price of items under ${base_average_calculation_value}: ${sum(total_base_average_value)/len(total_base_average_value):.2f}")


if __name__ =="__main__":
	downloadPriceTxt()		# Download the price txt file
	main()					# Calculate the average and cheapest value