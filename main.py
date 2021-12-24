import requests,sys,json,time
arg0 = sys.argv[1]
arg1 = sys.argv[2]
arg2 = sys.argv[3]
arg3 = sys.argv[4]
dic = {}

class alert():
    date = arg1
    token = arg2
    def alertRun(self,ticketType,status):
        #もしチケットが発売しているときの処理
        print('{}の販売状況が更新されたため通知します'.format(ticketType))
        message('{}の{}の販売状況が売り切れ以外に変更されました。\nステータスコード:{}'.format(self.date,ticketType,status))
def message(message):
    requestData = {'message':message}
    header = {'Authorization':'Bearer {}'.format(arg2)}
    requests.post('https://notify-api.line.me/api/notify',params=requestData,headers=header)

def run():
    print(arg0,"から",arg1,"のデータを取得します")
    requestData = {'useDays':1,"useDateFrom":arg1,'parkTicketSalesForm':1}
    headerData = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    response = requests.post(arg0, params=requestData, headers=headerData)
    print("データ取得完了",response.text[:30])

    jsonData = json.loads(response.text)
    for i in jsonData:
        ticketType = i['parkticketgroupname']
        status = int(i['saleStatus'])
        #もし辞書に入っていなければ追加する
        if ticketType not in dic:
            dic[ticketType] = -1

        #違うステータスなら
        if dic[ticketType] != status:
            #売り切れではないなら
            if status != 3:
                #通知する
                alert().alertRun(ticketType,status)
            dic[ticketType] = status
message("プログラムが起動しました")
while True:
    run()
    time.sleep(int(arg3))