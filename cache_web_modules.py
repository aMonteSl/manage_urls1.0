#!/usr/bin/python3

from robot import Robot
from cache import Cache

if __name__ == "__main__":
    # Try of class Robot
    # robot1
    robot_1 = Robot("https://www.urjc.es/")
    robot_1.retrieve()
    robot_1.show()
    robot_1.content()

    # robot2
    robot_2 = Robot("https://bobbyhadz.com/blog/python-count-in-for-loop")
    robot_2.retrieve()
    robot_2.show()
    robot_2.content()

    # Try of class Cache
    # cache1
    cache_1 = Cache()
    cache_1.retrieve("https://www.urjc.es/")
    cache_1.show("https://www.urjc.es/")
    cache_1.show_all()
    cache_1.content("https://bobbyhadz.com/blog/python-count-in-for-loop")
    cache_1.show_all()

    # cache2
    cache_2 = Cache()
    cache_2.show(
        "https://docs.python.org/3/library/urllib.request.html#examples")
    cache_2.retrieve(
        "https://docs.python.org/3/library/urllib.request.html#examples")
    cache_2.show_all()
    cache_2.content(
        "https://docs.python.org/3/library/urllib.request.html#httpredirecthandler-objects")
    cache_2.show_all()
