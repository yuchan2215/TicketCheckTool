import requests,sys,json
arg0 = sys.argv[1]
arg1 = sys.argv[2]

print(arg0,"から",arg1,"のデータを取得します")
requestData = {'useDays':1,"useDateFrom":arg1,'parkTicketSalesForm':1}
headerData = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
response = requests.post(arg0, params=requestData, headers=headerData)
print("データ取得完了")