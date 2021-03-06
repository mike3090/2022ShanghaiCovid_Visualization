# README
Hi, User!  
欢迎使用本可视化系统。该系统使用起来有点麻烦，请阅读后使用。  
在最后会大致介绍文件结构。

## User's Guide
众所周知的，为了安全考虑，各浏览器禁止html访问本地文件。为了解决这一点，如下是一个解决方法。参照如下文章的“方法一”写成。  
https://blog.csdn.net/s1441101265/article/details/121220720  

请在VSCode安装 `Live Server` 扩展。安装后，请用VSCode **（不要直接双击打开html！）** 打开html文件，并右键，选择 `Open with live server` 即可。

为保证搜索功能可以正常使用，请在打开界面前，运行文件夹里的 `clawer.bat` 和 `local_server.bat` . 二者运行顺序没有要求。

可能会需要安装一些python库，如 `flask` , `numpy` 等以保证预测模块可以使用。  

完成以上三个步骤，您就可以使用本系统了！  

该系统依赖于 `test_original.html` , `test_original_second_part.html`, `test_original_prediction.html` 三个网页写成，分别对应地图模块、舆情模块、预测模块。点击哪一个都可以进入系统。  

`test_heatmap.html` 是对热力图的实现，这里面仅仅是一个热力图， **无法进入系统。** 就别点他了。

## Some Problems
1. 地图模块，代表每个病例所在位置的紫色小圆 `js/dot.png` 在初始时难以加载出来。不知道为什么。  
   这个很好解决：切换到单日界面，随便选一个日期，这个时候就能加载了。再回到总览界面，就没问题了。  
2. 地图模块，未能实现切换至热力图后，再回到散点图（病例分布信息）。这受到了 `d3.csv()` 内部作用域的限制，外部无法对其操作，暂时没有找到解决方案。所以如果需要切换回散点图，请刷新。
3. 舆情模块。初始一片空白，这是正常的，因为默认不显示任何日期的信息。  
   请拖动时间轴，选择一天的日期，就可以正常展现当日信息了。  
   搜索功能较慢，请等待。不要重复点击搜索按钮，否则报 `failed` .  
   如果搜索的东西过于小众，数据库里没有，也报 `failed` .


## File Structure

`event` 文件夹是舆情数据处理模块。  
`image` 文件夹存储了生成的词云图。这样就不用在每次运行时再生成了，减少了卡顿。  
`js` 文件夹存储了一些 `.js`文件，如 `heatmap.js` ，供未来调用。  
`opinion_data` 文件夹是对舆情数据的整理与总结。   
`positive_location_data` 文件夹是对病例所在地信息的处理模块。  
`prediction&estimation_data` 文件夹是疫情预测模块。  
`run` 文件夹为空。  
`上海各区final.csv` 应该没用。

## Acknowledegment
感谢王华秋、叶柯成、张仕震三人的卓越贡献！我做的工作和他们相比简直微不足道。  

分工：（拼音序）  
李盛忻：UI设计、卫健委数据处理、地图模块开发；  
叶柯成：UI实现；  
王华秋：疫情预测；  
张仕震：舆情数据处理、舆情模块开发。  

缺了你们哪一个人的工作，这个系统都难以开发成现在的样子。你们的工作量十分惊人。非常感谢！


---
李盛忻 2022.6.12 天津