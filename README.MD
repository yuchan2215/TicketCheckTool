# このプログラムについて
APIを叩き、返答の`parkticketgroupname`と`saleStatus`を監視し、`saleStatus`が3以外になった場合にLineNotifyへ通知します。同じ状況が続いている場合には通知しません。
なお、このプログラムは自己責任にて利用してください。

# 本番動作確認環境
 - Python
   - 3.10.1  
 - (pip) requests
   - 2.26.0  
 - Windows 11
   - 21H2 22000.376
# テスト動作環境
 - Python 
   - 3.10.1  
 - (pip) requests
   - 2.26.0  
 - Node.js
   - 16.13.1  
 - NPM
   - 8.1.2  
 - (npm)json-server
   - 0.17.0  
 - Windows 11
   - 21H2 22000.376

# 本番実行方法
`py main.py APIのURL 検索したい日付(yyyyMMdd) bearerToken(LineNotify) 確認周期秒数`  
Example:
`py main.py https://resort.jp/ticket/ajax/searchTicket/ 20220215 TOKEN_HERE 120`

# テスト環境実行方法
json-server:
`json-server --watch .\json-server\test01.json -m .\json-server\middleware.js`  
watcher:`py main.py http://localhost:3000/api 20220215 HOGEHOGE 5`
