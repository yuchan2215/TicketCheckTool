import requests,sys,json
arg0 = sys.argv[1]

print(arg0,"からデータを取得します")
requestData = {'useDays':1,"useDateFrom":20220206,'parkTicketSalesForm':1}
headerData = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
response = requests.post(arg0, params=requestData, headers=headerData)
print("データ取得完了")