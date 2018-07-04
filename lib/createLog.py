# coding=utf-8
import logging
from conf import dataConfig


def create_log(logfile=dataConfig.fail_log):
    # 第一步，创建一个logger
    logger = logging.getLogger()

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logfile, mode='a+')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter(
            "%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    pass
