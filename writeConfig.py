import codecs
import configparser
import os


# os.chdir("D:\\Python_config")


def write_user_token(name, value):
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, "config.ini")

    cf = configparser.ConfigParser()

    # modify cf, be sure to read!
    cf.read(configPath)
    cf.set("HEADERS", name, value)

    # write to file
    with open(configPath, "w+") as f:
        cf.write(f)


def read_user_token(name):
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, "config.ini")

    cf = configparser.ConfigParser()

    # modify cf, be sure to read!
    cf.read(configPath)
    return cf.get("HEADERS", name)
# 导入codecs库，目的在于快速转化为UTF-8字符编码中的BOM
# import codecs
# import configparser
# import os
#
# proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir, "config.ini")
#
#
# class WriteConfig:
#     def __init__(self):
#         fd = open(configPath)
#         data = fd.read()
#
#         #  remove BOM
#         if data[:3] == codecs.BOM_UTF8:
#             data = data[3:]
#             file = codecs.open(configPath, "w")
#             file.write(data)
#             file.close()
#         fd.close()
#
#         self.cf = configparser.ConfigParser()
#         self.cf.read(configPath)
#
#     def set_headers(self, name, value):
#         self.cf.set(self,"HEADERS", name, value)
#
#         # write to file
#         with open(configPath, "w+") as f:
#             self.cf.write(f)
