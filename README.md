# **原神自动强化圣遗物脚本**

在某一天的下午强化升级烦了，一拍脑袋写出来的粪作。

**2023.02.25**：本人现在处于考研备考时期，所以可能会暂时停止更新，有问题可以提issue，有时间我会尽量解决的。

***
## **功能介绍**

将原神的页面调整到强化界面，**管理员运行**GUI.py然后点击左侧的四个按钮进行操作，四个坐标都记录后便可以进行强化，两种强化模式都注册了快捷键，~~按下对应的快捷键即可进行强化~~ 在游戏里无法使用快捷键，只能通过切回桌面进行强化。

目前仅有两种强化模式

- 从当前等级强化到下一个关键等级（4,8,12,16,20）
- 从当前等级直接强化到满级

![强化界面](https://hiroshi-typota.oss-cn-chengdu.aliyuncs.com/img/%E5%BC%BA%E5%8C%96%E7%95%8C%E9%9D%A2.png)

## **使用说明**

目前仅支持全屏使用，并且作者只测试过国服,异形屏可能会因为*compare_level.py*中的图片处理写死而无法使用。

## **更新记录**

**2023.02.25**：新增了GUI界面。

## **Todo**

~~在做了~~

- [x] 图形化界面
- [ ] 自动拾取



## **其他**

所有操作，都是模拟鼠标点击，通过图像识别实现功能，不涉及任何内存读写或网络封包修改