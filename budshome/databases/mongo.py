#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from motor.motor_asyncio import AsyncIOMotorClient
from budshome.settings import MONGODB

class MotorObj:
    '''
    use motor to connect mongodb as client
    '''
    
    __instance = None
    
    def __new__(cls, *args, **kwd):
        if MotorObj.__instance is None:
            MotorObj.__instance = object.__new__(cls, *args, **kwd)
            print('\nCreate MotorObj instance ' + str(id(MotorObj.__instance)) + '\n')
        else:
            print('\nMotorObj instance is exists ' + str(id(MotorObj.__instance)) + '\n')
            
        return MotorObj.__instance
    
    host = MONGODB['HOST'] if MONGODB['HOST'] else 'localhost'
    port = MONGODB['PORT'] if MONGODB['PORT'] else 27017
    username = MONGODB['USERNAME'] if MONGODB['USERNAME'] else ''
    password = MONGODB['PASSWORD']  if MONGODB['PASSWORD'] else ''
    
    __client = None
    
    def client(self):
        self.mongo_uri = 'mongodb://{account}{host}:{port}'.format(
                                    account = '{username}:{password}@'.format(
                                        username = self.username, 
                                        password = self.password) if MONGODB['USERNAME'] else '', 
                                    host = self.host, 
                                    port = self.port)
        
        motor_client = AsyncIOMotorClient(self.mongo_uri)
        print('\nCreate AsyncIOMotorClient for ' + self.mongo_uri + ' ' + str(id(motor_client)))
        
        self.__client = motor_client
        
        return motor_client
    
    __db = None
    database = MONGODB['DATABASE'] if MONGODB['DATABASE'] else ''

    @property
    def db(self):
        if self.__db is None:
            self.__db = self.client()[self.database]
            print('Connected to database: ' + self.database + ', create motor_client ' + str(id(self.__db)) + '\n')
        else:
            print('Already connected to database: ' + self.database + ', use existing motor_client ' + str(id(self.__db)) + '\n')
            
        return self.__db

    @property
    def close(self):
        self.__client.close()
        print('close motor client : ' + str(id(self.__client)) + '\n')


    
motor_obj = MotorObj()
# mongo_obj = motor_obj.db


