# AI 机器人课程作业合集
 
姓名：白夏
课程：AI Robotics  
内容：第 2 周到第 13 周课程实验整理  

---

## 简介

这是我的 AI 机器人课程学习仓库，记录了从基础环境配置到机器人仿真、计算机视觉、Docker 容器、网页部署和期末项目的完整学习过程。仓库按照周次整理，每个文件夹对应一次课程主题，包含实验说明、运行截图、代码文件和阶段性总结。

课程前半部分主要围绕 Linux、WSL、ROS2 和 Python 编程展开：先完成开发环境配置，再通过 turtlesim 学习 ROS2 节点、话题、速度控制和位姿观察。中间部分进一步学习机器人运动学、传感器数据、Docker 桌面容器和 OpenCV 图像处理。后半部分把网络通信、手机摄像头、四足机器人仿真和网页控制结合起来，逐步过渡到完整的机器人系统项目。

---

## 目录

| 周次 | 内容 | 链接 |
| --- | --- | --- |
| Week 2 | WSL、Ubuntu 与 ROS2 环境配置 | [Week2](week2/) |
| Week 3 | GitHub SSH、VS Code 与 ROS2 命令行交互 | [Week3](week3/) |
| Week 4 | 命令行、机器人基础概念与 Python 仿真 | [Week4](week4/) |
| Week 5 | Linux 目录操作与机器人运动学 | [Week5](week5/) |
| Week 6 | 传感器介绍与 ROS2 KITTI 实验 | [Week6](week6/) |
| Week 7 | Markdown 与 GitHub 作业整理 | [Week7](week7/) |
| Week 8 | Docker 安装与 ROS2 桌面容器 | [Week8](week8/) |
| Week 9 | 机器人与机器视觉数学基础 | [Week9](week9/) |
| Week 10 | Docker 概念与 OpenCV 实验 | [Week10](week10/) |
| Week 11 | Docker 进阶与 GitHub Pages 网页部署 | [Week11](week11/) |
| Week 12 | 手机摄像头、ArUco 识别与距离测量 | [Week12](week12/) |
| Week 13 | 四足机器人入门与强化学习实验 | [Week13](week13/) |
| Week 14 | 手机遥控与 turtlesim 自动迷宫探索 | [Week14](week14/) |

---

## 期末项目简介

期末项目选择 Week 14 方向 B：使用手机网页控制 ROS2 turtlesim 乌龟，在二维迷宫中完成手动遥控和自动探索。项目包含 WebSocket 网页遥控器、ROS2 桥接程序、迷宫碰撞检测、A* 自动路径规划和轨迹展示界面。

主要代码位于 `week14/turtlesim_remote/`：

- `turtlesim_web_bridge.py`：负责 ROS2 通信、WebSocket 服务、碰撞检测和自动模式调度。
- `maze.py`：生成 6x6 迷宫并提供边界、障碍物、起点和终点信息。
- `explorer.py`：使用 A* 算法规划通往终点的路径。
- `index.html`：手机遥控网页，支持手动/自动模式切换和实时轨迹绘制。

---

## 学习收获

通过这些周次的实验，我逐步理解了机器人系统不是单独的算法或单独的网页，而是由环境、通信、控制、传感器、仿真和展示共同组成的工程链路。前面的 ROS2、Docker、OpenCV 和 GitHub Pages 练习，为最后的手机遥控迷宫探索项目提供了基础。整个仓库也是我从命令行操作到完整项目组织的一次持续练习。

---

### 在线页面：

[https://nanami-mio.github.io/AI-Robot-baixia/](https://nanami-mio.github.io/AI-Robot-baixia/)


