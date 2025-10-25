# 代码生成时间: 2025-10-25 14:34:53
import requests
from requests.exceptions import RequestException
import logging
import sys

# 设置日志记录
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class LiveStreamingPusher:
    def __init__(self, base_url, stream_url):
        """
        初始化直播推流系统。
        :param base_url: RTMP服务器的Base URL
        :param stream_url: RTMP服务器的推流地址
        """
        self.base_url = base_url
        self.stream_url = stream_url

    def push_stream(self, stream_key):
        """
        推送直播流到RTMP服务器。
        :param stream_key: 推流密钥
        """
        try:
            # 构造完整的RTMP推流地址
            full_stream_url = f"{self.stream_url}?{stream_key}"
            logging.info(f"开始推流到RTMP服务器：{full_stream_url}")

            # 发送推流请求
            response = requests.get(full_stream_url, stream=True)
            response.raise_for_status()  # 检查响应状态码是否为200

            logging.info(f"推流成功，服务器响应：{response.text}")
        except RequestException as e:
            logging.error(f"推流失败：{e}")
        except Exception as e:
            logging.error(f"发生未知错误：{e}")

    def stop_stream(self, stream_key):
        """
        停止推送直播流。
        :param stream_key: 推流密钥
        """
        try:
            # 构造停止推流的请求URL
            stop_url = f"{self.base_url}/stop?{stream_key}"
            logging.info(f"停止推流：{stop_url}")

            # 发送停止推流请求
            response = requests.post(stop_url)
            response.raise_for_status()  # 检查响应状态码是否为200

            logging.info(f"停止推流成功，服务器响应：{response.text}")
        except RequestException as e:
            logging.error(f"停止推流失败：{e}")
        except Exception as e:
            logging.error(f"发生未知错误：{e}")

# 示例用法
if __name__ == '__main__':
    base_url = "https://example.com/api"
    stream_url = "rtmp://example.com/live"
    stream_key = "my_stream_key"

    pusher = LiveStreamingPusher(base_url, stream_url)
    pusher.push_stream(stream_key)
    # 稍后可以调用 stop_stream 方法来停止推流
    # pusher.stop_stream(stream_key)