import httplib2
import json

HOST = "py_server:3000"

def getServerData(requestMessage : dict) -> str:

    print("getServerData({0})".format(requestMessage))
    connection = httplib2.HTTPConnectionWithTimeout(HOST)
    connection.request("GET", requestMessage)
    response = connection.getresponse()

    print("\tResponse status: ", response.status)
    data = response.read()
    print("\tResponse data  : ", data.decode("utf-8"))

    connection.close()


def postServerData(requestMessage : str) -> str:

    print("postServerData({0})".format(requestMessage))
    connection = httplib2.HTTPConnectionWithTimeout(HOST)
    #connection.putheader("Content-type", "text/json")
    #connection.endheaders()
    connection.request(
        "POST", 
        url = HOST, 
        body = json.dumps(requestMessage),
        headers= {"Content-type" : "text/json"})
    response = connection.getresponse()
    
    print("\tResponse status: ", response.status)
    data = response.read()
    print("\tResponse data  : ", data.decode("utf-8"))

    connection.close()

def main():
    getServerData("getMessage")
    getServerData("otherMessage")
    getServerData("xyz")
    
    postServerData({ "value" : 100, "name" : "cheese"})
    postServerData({ "value" : 110, "name" : "water"})
   


if __name__ == "__main__":
    main()