#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################
#  MONGO DB CONNECTION
##############################################
from pymongo import MongoClient
from comm_config import ENV_PROFILE
from utils import encrpyUtil

# 判断是否为生产环境
if ENV_PROFILE == "production":
    client = MongoClient("mongodb://localhost:27017")
    db = client['metacat']
    password = encrpyUtil.decrypt(15, 'CGKGLHOGMGOGLH')
    db.authenticate('metacat', password)
# 默认是否为开发环境
else:
    client = MongoClient("mongodb://mongoadmin:secret@metacat-db:27017/pmd?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
    db = client['metacat']
    # db.authenticate('metacat', 'metacat')
    # db.authenticate('mongoadmin', 'secret')

    # client = MongoClient("mongodb://localhost:27017")
    # db = client['metacat_dev']
    # password = encrpyUtil.decrypt(15, 'CGKGLHOGMGOGLHAFLGKGJH')
    # db.authenticate('metacat_dev', password)
