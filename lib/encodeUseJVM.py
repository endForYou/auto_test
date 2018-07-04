# coding=utf8
import requests
import os.path
import os
import re
import sys
reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')


def encodeUseJVM(string, method="url"):
    if method == "url":
        try:
            url = "http://192.168.1.109:8080/rsa/result?p=" + string
            response = requests.get(url)
            text = response.text
            text = text.encode("utf8")
            matchPattern = re.search(
                "\"data\": \"(?P<encodeString>\w+)\"", text)
            encodeString = matchPattern.group("encodeString")
        except BaseException:
            encodeString = ""
        return encodeString

    if method == "jpype":
        print "通过调用jar进行加密..."
        try:
            import jpype
            if not jpype.isJVMStarted():
                jvmPath = jpype.getDefaultJVMPath()
                jarPath = os.path.join(os.path.abspath(os.path.pardir), "")
                jarPath1 = os.listdir(jarPath)
                allJarPath = ""
                for i in jarPath1:
                    try:
                        if i[-3:] == "jar":
                            allJarPath = allJarPath + \
                                os.path.join(jarPath, i) + ";"
                    except BaseException:
                        pass
                jpype.startJVM(
                    jvmPath,
                    "-ea",
                    "-Djava.class.path=%s" %
                    allJarPath)
            JDClass = jpype.JClass("WebEncrypt")
            jd = JDClass()
            encodeString = jd.encode(string)
        except BaseException:
            encodeString = ""
        return encodeString


def encodeImageAndNotice():
    # 获取图形验证码和手机验证码所需参数的加密函数
    # coding=utf8
    import base64
    string = "IaLql1WTB20jIBr4ytclRK329Pk5PU88bhVQE+T4wN0qDjdV2e79IRJ54nLR9Ga2YvlU6ZPzasakNc8aO0VQZycGciDdm/TzCxZzhsE5ZPl0RebNwMSqGPuQCi8AUh/GNgmcluqbRvsrKvWSnR30n2zBd1FL43RL2tE/BuikHg="
    string = "BUD5e5GLRJ3XdxIkDnjZnlwujT6vTbdfHI9+Jor+IJs+mNAaywathRgJRE/o000qib2vU5UOE6PBlbmXS8odGZ+i+FvddlMSLn6H9TrcD03V/xFDETdZCuu9EY5gfP4fQFH5TcPyzuqqlehnJoNzXnPOwhg8htyNm/cq4dq9SAc="
    # coding=utf8
    from Crypto import Random
    from Crypto.Hash import SHA
    from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
    from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
    from Crypto.PublicKey import RSA
    import base64

    with open('aaa.pem') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(string))
    print text


if __name__ == "__main__":
    # print encodeUseJVM("19720161129",method="url")
    string = "123"
    encodeImageAndNotice()
