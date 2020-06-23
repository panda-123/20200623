#ecoding=utf-8
# author:herui
# time:2019

import configparser

def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file)
    return cfg

sys_config = read_config(r"E:\Hogwarts\python\weixin\cfg\auto.cfg")

if __name__=="__main__":
    cfg = read_config(r"E:\Hogwarts\python\weixin\cfg\auto.cfg")
    print(cfg.get('contact_para','create_dep_url'))