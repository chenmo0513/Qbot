#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import wx
import sys
import subprocess
import atexit

from gui.mainframe import MainFrame

if __name__ == "__main__":

    app = wx.App()
    frame = MainFrame(None, title="AI学习")
    frame.Show()

    # 启动外部脚本
    try:
        # 使用当前Python解释器路径执行脚本
        process = subprocess.Popen(
            [sys.executable, r"E:\workspace\Qbot\auto_monitor.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except Exception as e:
        wx.LogError(f"启动自动监控脚本失败: {str(e)}")
    else:
        # 注册退出处理函数，尝试终止子进程
        def cleanup_process():
            if process.poll() is None:  # 检查是否仍在运行
                process.terminate()     # 尝试终止
                try:
                    process.wait(timeout=5)  # 等待5秒
                except subprocess.TimeoutExpired:
                    process.kill()      # 强制终止
        atexit.register(cleanup_process)

    app.MainLoop()
