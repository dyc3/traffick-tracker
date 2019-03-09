from bs4 import BeautifulSoup;
def parse_message(element):
    return(element.p.div.string,element.p.body.string)
    
def parse_messages_code(code):
    soup = BeautifulSoup(code,"html.parser");
    lst = []
    while soup.p != None:
        lst.append(parse_message(soup))
        code = code[code.find("</p>")+4:]
        soup = BeautifulSoup(code,"html.parser")
    return lst
#parse_messages_code("<html><head><title>Messages</title></head><body><p><div class = \"user\">blank-user-name</div><body>Hey broski what's up, anyways you free to do illegal stuff later? See you soon brotowski</body></p><p><div class = \"user\">blank-user-name-4</div><body>DUDE YOU WILL NOT BELIEVE WHAT MICHELLE DID</body><div class = \"ip\">123.123.123.222</div> </p><p><div classs = \"user\">blank-user-name-2</div><body>man i'm so tired, let's go clubbing</body><div class = \"ip\">096.211.111.090.</div></p><p><div class = \"user\">blank-user-name-1</div><body>who cares if she's from hoboken, it's a tuesday night! live a little</body><div classs = \"ip\">087.049.123.255</div></p><p><div classs = \"user\">blank-user-name</div><body>sup, whatcvhu doing tomorrow at 6:10am outside the grill, lmk asap</body></p><p><div classs = \"user\">blank-user-name-2</div><body>who said you could do that</body><div classs = \"ip\">222.009.111.222</div></p> <p><div classs = \"user\">blank-user-name-3</div><body>honestly the best star wars movie is episode 2 becausde hayden christensen</body><div classs = \"ip\">036.046.111.222</div></p><p><div classs = \"user\">blank-user-name-4</div><body>despacito, this is how we do it in puerto rico</body></p><p><div classs = \"user\">blank-user-name-3</div><body>wanna buy drugs</body></p><p><div classs = \"user\">blank-user-name</div><body>i'm so busy man</body><div classs = \"ip\">222.111.233.199</div></p></body></html>")
        
