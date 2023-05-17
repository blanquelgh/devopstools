import requests,json,flask,urllib,re,time,sys,socket,yaml

from urllib.request import Request,urlopen
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pprint import pprint
from flask import Flask,jsonify
from flask import current_app
from bottle import (  
    run, post, response, request as bottle_request
)

DOCUMENT = open('../python-bot/confbotservpy.yml', 'r')
PARSED = yaml.load(DOCUMENT)
GECKODRIVER_PATH=PARSED["geckrodiver"]["path"]
TELEGRAM_TOKEN=PARSED["telegram"]["token"]
SELENIUM_PATH=PARSED["selenium"]["path"]
IMAGES_PATH=PARSED["images"]["tempdir"]
API_URL=PARSED["apirest"]["url"]

BOT_URL = "https://api.telegram.org/bot"+TELEGRAM_TOKEN+"/"



def get_chat_id(data):  
    chat_id = data['message']['chat']['id']
    return chat_id
    
def get_message(data):  
    message_text = data['message']['text']
    return message_text
        
def send_selenium_image(chatid,url_test,urlname, sleep):

    try:
        #exec_path = '/usr/bin/firefox'
        #bin_path = '/opt/geckodriver-0.23.0'
        
        binary = FirefoxBinary(SELENIUM_PATH)
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(firefox_options=options, executable_path=GECKODRIVER_PATH)
        driver.set_window_size(1024, 768) # set the window size that you need 
        driver.set_page_load_timeout(60)
        driver.get(url_test)
        time.sleep(sleep)
        driver.save_screenshot('/tmp/'+urlname+'.png')
        driver.quit()
        message_url = BOT_URL + "sendPhoto?chat_id={}&text={}".format(chatid,url_test)
        headers = {'Content-type':'application/json','Accept':'test/plain'}
        data = {'chat_id': chatid}
        files = {'photo': open(IMAGES_PATH + urlname + '.png','rb')}
        requests.post(BOT_URL+"sendPhoto", files=files, data=data)
    except KeyError as kye:
        print( "yeilo_bot with KeyError - reason: " + kye.message)
        
    except AttributeError as ate:
        print( "yeilo_bot with general exception - reason: " + ate.message)
        
    except ConnectionError as cne:
        print("yeilo_bot with socket exception - reason:" + cne.message)
    
    except SocketError as ske:
        print("yeilo_bot with socket exception - reason:" + ske.message)
        
    except Exception as gne:
        print( "yeilo_bot with general exception - reason: " + gne.message)
        
    

def send_message(prepared_data,chatid):  
    try: 
        message_url = BOT_URL + "sendMessage?text={}&chat_id={}".format(prepared_data,chatid)
        headers = {'Content-type':'application/json','Accept':'test/plain'}
        requests.post(message_url, json=prepared_data,headers=headers,verify=False)  
    except KeyError as kye:
        print( "yeilo_bot with KeyError - reason: " + kye.message)
        
    except AttributeError as ate:
        print( "yeilo_bot with general exception - reason: " + ate.message)

    except ConnectionError as cne:
        print("yeilo_bot with socket exception - reason:" + cne.message)
        
    except Exception as gne:
        print( "yeilo_bot with general exception - reason: " + gne.message)
        
    
def agave_health_test_url(url):  
    """
    To enable turning our message inside out
    """
    url_code=urllib.request.urlopen(url).getcode()
    return url_code

def get_obpyme_url():
    url=PARSED["obpyme"]["urlfront"]
    return url
  
def get_cdpyme_url():
    url=PARSED["cdpyme"]["urlfront"]
    return url
 
def get_gopay_url():
    url=PARSED["gopay"]["urlfront"]
    return url

def get_sd500_url():
    url=PARSED["sd500"]["urlfront"]
    return url

def get_sd500_pyme_url():
    url=PARSED["sd500_pyme"]["urlfront"]
    return url

def get_sd500_beneficios_url():
    url=PARSED["sd500_beneficios"]["urlfront"]
    return url

def get_sd500_colectivos_url():
    url=PARSED["sd500_colectivos"]["urlfront"]
    return url
 
def get_wallet_tokenman_url():
    url=PARSED["wallet_tokenman"]["urlfront"]
    return url
 
def get_wallet_pagos_url():
    url=PARSED["wallet_pagos"]["urlfront"]
    return url

def get_autocompara_url():
    url=PARSED["autocompara"]["urlfront"]
    return url

def get_idlc_url():
    url=PARSED["idlc"]["urlfront"]
    return url 

def get_c2s_frontbt_url():
    url=PARSED["frontbt"]["urlfront"]
    return url 

def get_loyaltyhub_url():
    url=PARSED["loyaltyhub"]["urlfront"]
    return url

def get_customer_smsw_url():
    url=PARSED["customer"]["urlfront"]
    return url 

def get_customer_sn_url():
    url=PARSED["customer_sn"]["urlfront"]
    return url 

def get_ocrneoris_url():
    url=PARSED["ocrneoris"]["urlfront"]
    return url 

def get_sherpa_front_url():
    url=PARSED["sherpa"]["urlfront"]
    return url  

def get_sherpa_vtoken_url():
    url=PARSED["sherpa_vtoken"]["urlfront"]
    return url  

def get_biockeck_url():
    url=PARSED["biockeck"]["urlfront"]
    return url

def get_c2sfrontprueba_url():
    url=PARSED["c2sfrontprueba"]["urlfront"]
    return url


def get_apitest():

    header = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'curl/7.47.1'}
    
    try:
        response = requests.post(API_URL,headers=header,verify=False)
        
        if response.status_code == 200:
            response.encoding = 'utf-8'
            print('Success with datas:' + response.text)
            
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' +  err)
    else:
        print('Success!' + response.text)
    
    return response
    
@post('/')
def main():
    app = Flask(__name__)
    with app.app_context():
       
        
        request_data = bottle_request.json
        print(request_data)
        chatid=get_chat_id(request_data)
        text=get_message(request_data)
        print(text)    
        sys.tracebacklimit=0
        
       
        if re.match("/checkup-obpyme", text):
            send_message("esperando screenshot de obpyme ...", chatid)
            url_test=get_obpyme_url()
            url_name='cuentadigitalpyme'
            send_selenium_image(chatid, url_test, url_name, 3)
            send_message("Screenshot resuelto de obpyme", chatid)
    
        elif re.match("/checkup-api", text):
            send_message("esperando respuesta de api test ...", chatid)
            api_test=get_apitest()
            
        elif re.match("/checkup-autocompara", text):
            send_message("esperando screenshot de autocompara ...", chatid)
            url_test=get_autocompara_url()
            url_name='autocomp'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto de autocompara", chatid)
            
        elif re.match("/checkup-click2sell", text):
            send_message("esperando screenshot de click2sell ...", chatid)
            url_test=get_c2sfrontprueba_url()
            url_name='c2cfront'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto click2sell", chatid)
    
        elif re.match("/checkup-biometricos", text):
            send_message("esperando screenshot de biometricos ...", chatid)
            url_test=get_biockeck_url()
            url_name='biochk'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto de biometricos", chatid)
    
    
        elif re.match("/checkup-gopay", text):
            send_message("esperando screenshot de gopay ...", chatid)
            url_test=get_gopay_url()
            url_name='gopay'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto de gopay", chatid)
    
    
        elif re.match("/checkup-sd500", text):
            send_message("esperando screenshot de sd500 ...", chatid)
            url_test=get_sd500_url()
            url_name='sd500'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshots resueltos de sd500", chatid)
    
        elif re.match("/checkup-cdpyme", text):
            send_message("esperando screenshot de cdpyme ...", chatid)
            url_test=get_cdpyme_url()
            url_name='creditodigitalpyme'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto de cdpyme", chatid)
    
        elif re.match("/checkup-wallet", text):
            send_message("esperando screenshots de wallet ...", chatid)
            url_test=get_wallet_pagos_url()
            url_name='walletpagos'
            send_selenium_image(chatid, url_test, url_name, 0.5)
    
            send_message("esperando screenshots de wallet ...", chatid)
    
            url_test=get_wallet_tokenman_url()
            url_name='wallettoken'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshots resueltos de wallet", chatid)
    
        elif re.match("/checkup-customer", text):
            send_message("esperando screenshot de customer ...", chatid)
            url_test=get_customer_smsw_url()
            url_name='smsw'
            send_selenium_image(chatid, url_test, url_name, 0.5)
    
            send_message("esperando screenshot de customer ...", chatid)
    
            url_test=get_customer_sn_url()
            url_name='sn'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshots resueltos de customer", chatid)
    
        elif re.match("/checkup-sherpa", text):
            send_message("esperando screenshot de sherpa ...", chatid)
            url_test=get_sherpa_front_url()
            url_name='sherpafront'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto de sherpa", chatid)
    
        elif re.match("/checkup-loyaltyhub", text):
            send_message("esperando screenshot de loyaltyhub ...", chatid)
            url_test=get_loyaltyhub_url()
            url_name='loyaltyfront'
            send_selenium_image(chatid, url_test, url_name, 0.5)
            send_message("Screenshot resuelto de loyaltyhub", chatid)

        elif re.match("/checkup-ocrims", text):
            send_message("esperando screenshot de OCR Neoris ...", chatid)
            url_test=get_ocrneoris_url()
            url_name='ocrimsfront'
            send_selenium_image(chatid, url_test, url_name, 3)
            send_message("Screenshot resuelto de OCR Neoris", chatid)
                
        else:    
            nok_response="!Error! "+ text +" no registrado como checkup. Intentalo de nuevo!"#agave_health_test_url()
            send_message(nok_response, chatid)  # status 200 OK by default
           

if __name__ == '__main__':  
    run(host='0.0.0.0', port=8080, debug=True)
    #serve(Flask(__name__),host='0.0.0.0', port=80, thread=50)
    #run(debug=True)
