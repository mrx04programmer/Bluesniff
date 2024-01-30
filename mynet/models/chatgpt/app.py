## Colors
# Author: Mrx04programmer
# Github : https://github.com/mrx04programmer
import requests, json
W = '\033[37m' # Default
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan

url = "https://chatgpt-open-ai-nlp.p.rapidapi.com/"
apikey = ""


def  main():
        payload = {
            "messages": [{
            "role": "system",
			"content": ""}],
            "temperature": "0.7"
            }
        headers = {
			"content-type": "application/json",
			"Type": "chatgpt4-chat",
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "chatgpt-open-ai-nlp.p.rapidapi.com"
			}
        
        while True:
            prompt = input(f"{P}chatgpt >> {W}")
            prompted = {
				"role": "system",
				"content": prompt
			}
            payload['messages'].append(prompted)
            resp = requests.post(url, json=payload, headers=headers)
            dataJson = resp.json()
            resp = requests.post(url, json=payload, headers=headers)
            #print(dataJson)
            dataGPT = dataJson['content']
            print(f"{G}[CHATGPT] {W}{dataGPT}\n")
   



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{R}[CHATGPT] {W}Error causado por : {ee}")