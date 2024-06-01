# import urllib.request as urllib2
# import http.cookiejar as cookielib

# def TryToLoginFB(username,password):
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
#     url1 = "https://login.facebook.com"
#     url2 = "https://login.facebook.com/login.php?login_attempt=1"
#     data = "&email="+username+"&pass="+password
#     socket = opener.open(url1)
#     socket = opener.open(url2,data)
#     return socket

# socket = TryToLoginFB("elprofessor201211@hotmail.com","A7med.M201400")

# if "logout" in socket.read():
#     print ("OK")
# else:
#     print ("Error")