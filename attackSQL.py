import requests

class attackSQL:


    listOfLengthResponse = []
    listOfPayloads = []

    def showEffect(self):
        listOfCounter = {}

        for res in self.listOfLengthResponse:
            if(listOfCounter.get(res) == None):
                listOfCounter[res] = 1
            else:
                listOfCounter[res] += 1

        print("Count [Length response] <-> {The number of repetitions}")
        for x in listOfCounter:
            print("[" + str(x) + "] <-> {" + str(listOfCounter[x]) + "}")

        print()
        print()
        print("Payloads for [repetitions < 10]:")
        for x in listOfCounter:
            if(listOfCounter[x] < 10):
                counter = 0
                for y in self.listOfLengthResponse:
                    if(x == y):
                        print("         " + self.listOfPayloads[counter])
                    counter += 1
        
    def addData(self, payload, response):
        self.listOfLengthResponse.append(str(len(str(response))))
        self.listOfPayloads.append(payload)

    def attack(self, url, payload, method="GET"):
        response = ''
        if(method == 'GET'):
            response = requests.get(url, data=payload)
        else:
            response = requests.post(url, data=payload)
        self.addData(payload, response)

    def attackHeaders(self, url, payload, method, headers):
        response = ''
        if(method == "GET"):
            response = requests.get(url, data=payload, headers=headers)
        else:
            response = requests.post(url, data=payload, headers=headers)
        self.addData(payload, response)

    def attackHeadersCookie(self, url, payload, method, headers, cookies):
        response = ''
        if(method == "GET"):
            response = requests.get(url, data=payload, headers=headers, cookies=cookies)
        else:
            response = requests.post(url, data=payload, headers=headers, cookies=cookies)
        self.addData(payload, response)

    def attackCookie(self, url, payload, method, cookies):
        response = ''
        if(method == "GET"):
            response = requests.get(url, data=payload, cookies=cookies)
        else:
            response = requests.post(url, data=payload, cookies=cookies)
        self.addData(payload, response)
