# base64转码，将转码后的文件存入icon.py中
import base64

open_icon = open("C://Users//live02//Desktop//草莓.ico", "rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = %s" % b64str
f = open("icon.py", "w+")
f.write(write_data)
f.close()


