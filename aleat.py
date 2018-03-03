import socket
import random
import webapp


class randurl(webapp.webApp):
        
	def process(self, parsedRequest):
		num = str(random.randrange(0, 1000000000000000000000))
		return ("200 OK", '<html><body><p>Hola.<a href = "http://localhost:1234/' + num  + '"' + '>Dame otra</a></p></body></html>')
        
if __name__ == "__main__":
	testWebApp = randurl("localhost", 1234)



