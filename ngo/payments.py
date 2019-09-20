from  .models import donations
import requests


data = {
	'amount':'5000',
	'currency':'INR'
	'receipt':'Receipt #20'
	'payment_capture':'1'
}

response = requests.post('https://api.razorpay.com/v1/orders', data=data, auth=('rzp_test_WxBmujEooZGzKM', 'v5cFlhcgdvAzYrJ4O2ItYEpr'))