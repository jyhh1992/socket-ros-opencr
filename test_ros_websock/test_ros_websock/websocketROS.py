import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import asyncio
import websockets

# echo(들어온 데이터를 다시 보냄)서버 예제입니다.
class WebSockBridge(Node):

    def __init__(self):
        super().__init__('websock_bridge')
        self.publisher_ = self.create_publisher(String, 'websock_echo', 10)
        self.count = 0

        start_server = websockets.serve(self.accept, "localhost", 9998)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def accept(self, websocket, path):
      while True:
        data = await websocket.recv()
        print("receive : " + data)
        await websocket.send("echo : " + data)

        msg = String()
        msg.data = data
        self.publisher_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    websock_bridge = WebSockBridge()
    rclpy.spin(websock_bridge)

    websock_bridge.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()