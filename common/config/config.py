import configparser
import os


class Config:
    # def __init__(self):
    #     """
    #     初始化
    #     """
    #     self.config = configparser.ConfigParser()
    #     self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    #     if not os.path.exists(self.conf_path):
    #         raise FileNotFoundError("请确保配置文件存在！")

    config = configparser.ConfigParser()
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    if not os.path.exists(conf_path):
        raise FileNotFoundError("请确保配置文件存在！")

    @classmethod
    def get_value(cls, section, key):
        """
        获取某个节点的值
        :param section: 分组  ['directory', 'environment']
        :param key:  节点键  ['data_dir', 'page_dir', 'cookie_dir', 'report_xml_dir', 'report_html_dir', 'case_dir']
        :return:
        """
        cls.config.read(cls.conf_path, encoding='utf-8')
        value = cls.config.get(section, key)
        return value

    # def get_value(self,section, key):
    #     """
    #     获取某个节点的值
    #     :param section: 分组  ['directory', 'environment']
    #     :param key:  节点键  ['data_dir', 'page_dir', 'cookie_dir', 'report_xml_dir', 'report_html_dir', 'case_dir']
    #     :return:
    #     """
    #     self.config.read(self.conf_path, encoding='utf-8')
    #     value = self.config.get(section, key)
    #     return value
        # print(self.config.sections())
        # print(self.config.options(key))
        # print()

    @classmethod
    def set_option(cls,section, key, set_value):
        """
        修改节点的值，如果不存在该节点 则会创建
        :param section: 分组  ['directory', 'environment']
        :param key:  节点键  ['data_dir', 'page_dir', 'cookie_dir', 'report_xml_dir', 'report_html_dir', 'case_dir']
        :param set_value:
        :return:
        """
        cls.config.read(cls.conf_path, encoding='utf-8')
        cls.config.set(section, key, set_value)
        cls.config.write(open(cls.conf_path, 'w'))


if __name__ == "__main__":
    #c = Config()
    print(Config.get_value("directory", 'cookie_dir'))
    # c.set_option("environment","environment","b")

