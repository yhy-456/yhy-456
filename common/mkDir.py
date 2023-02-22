import os
import sys
sys.path.append(os.path.dirname(sys.path[0]))

from common.Log import MyLog


def mk_dir(path):
    # 去除首位空格
    path = path.strip()
    path = path.rstrip("\\")
    path = path.rstrip("/")

    # 判断路径是否存在
    is_exists = os.path.exists(path)

    if not is_exists:
        try:
            os.makedirs(path)
        except Exception as e:
            MyLog.error("logs目录创建失败：{}".format(e))

    else:
        # 如果目录存在则不创建，并提示目录已存在
        MyLog.error("logs目录已存在：{}".format(path))
        pass
