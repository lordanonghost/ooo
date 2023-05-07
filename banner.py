import requests
import re
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Cloudflare Checker')
parser.add_argument('-u', '--url', type=str, required=True, help='The URL of the website to check')
args = parser.parse_args()

# Send a request to the website with a known Cloudflare cookie
cf_cookie = {'__cfduid': 'd864bc3e05215ccfd62d50cfec46f82b91618135528'}
response = requests.get(args.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, cookies=cf_cookie)

# Check if the response contains the Cloudflare IUAM page
if re.search(r'cf-([0-9]{1,3}-){3}[0-9]{1,3}\.cloudflare.com', response.text):
    print('This website is protected by Cloudflare.')
else:
    print('This website is not protected by Cloudflare.')