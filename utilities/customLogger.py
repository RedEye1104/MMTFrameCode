import logging
class Log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%Y-%m-%d %H:%M", force=True,
                            handlers = [logging.FileHandler("test_log.log"),
                                        logging.StreamHandler()
                                        ]
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
