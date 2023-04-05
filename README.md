
Realtime Object Detector
========================

![Realtime Object Detector demo](./demo.gif)

**Realtime Object Detector** 是一个使用 Python 和 OpenCV 库实现的摄像头应用程序。该应用程序可以调用计算机的摄像头，实时显示摄像头的视频流，并检测视频流中的物体并在其周围描绘红色边框。该应用程序使用 Canny 算法进行边缘检测和形态学操作，可以在实时视频流中快速和准确地检测主要物体。

安装
--

1.  安装 Python 3.x 版本。
    
2.  克隆项目到本地：
    
    ```bash
    git clone https://github.com/DongJunze/Realtime-Object-Detector.git
    ```
    
3.  进入项目目录：
    
    ```bash
    cd Realtime-Object-Detector
    ```
    
4.  安装必要的 Python 库：
    
    ```
    pip install -r requirements.txt
    ```
    

使用
--

1.  运行程序：
    
    ```
    python app.py
    ```
    
2.  在程序窗口中，您将看到摄像头的实时视频流，并在视频流中检测到的物体周围描绘红色边框。
    
3.  要退出程序，请按 "q" 键。
    

示例
--

您可以通过运行以下命令来查看应用程序的演示：

```
python app.py
```

该命令将调用计算机的摄像头，实时显示摄像头的视频流，并检测视频流中的物体并在其周围描绘红色边框。

贡献
--

欢迎贡献代码和提出问题！
