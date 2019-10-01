import pickle
from datetime import datetime
from api.common.utils import load_pickle_from_s3
import logging


class PickleLoader:
    __instance = None
    __crystallball = None
    __logger = logging.getLogger('gunicorn.error')

    @staticmethod
    def getInstance():
        if PickleLoader.__instance == None:
            PickleLoader()
        return PickleLoader.__instance

    def __init__(self):
        if PickleLoader.__instance != None:
            raise Exception("Trying to create multiple instances, you nasty boy!")
        else:
            PickleLoader.__instance = self

    def refresh_pickle(self, pickle_path):
        start_time = datetime.now()
        formatted_start_time = start_time.strftime("%m/%d/%Y, %H:%M:%S")
        self.__logger.info('Start loading pickle from path= %s at time=%s', pickle_path, formatted_start_time)
        with open(pickle_path, 'rb') as fp:
            self.__crystallball = pickle.load(fp)
        end_time = datetime.now()
        formatted_end_time = end_time.strftime("%m/%d/%Y, %H:%M:%S")
        self.__logger.info('Finished loading pickle from path=%s at time=%s', pickle_path, formatted_end_time)
        self.__logger.info('Total Time taken to finish loading=%s seconds', end_time.__sub__(start_time))

    def refresh_pickle_from_s3_aws(self, path):
        start_time = datetime.now()
        formatted_start_time = start_time.strftime("%m/%d/%Y, %H:%M:%S")
        self.__logger.info('Start loading pickle at time=%s', formatted_start_time)
        self.__crystallball = load_pickle_from_s3(path)
        end_time = datetime.now()
        formatted_end_time = end_time.strftime("%m/%d/%Y, %H:%M:%S")
        self.__logger.info('Finished loading pickle at time=%s', formatted_end_time)
        self.__logger.info('Total Time taken to finish loading=%s seconds', end_time.__sub__(start_time))

    @property
    def crystallball(self):
        return self.__crystallball
