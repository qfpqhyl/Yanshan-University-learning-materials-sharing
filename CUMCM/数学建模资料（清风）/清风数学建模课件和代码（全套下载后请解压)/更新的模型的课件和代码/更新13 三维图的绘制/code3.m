%% contour函数: 绘制等高线图

[x,y] = meshgrid(-3:0.1:3);  
% 一个语句太长时，可以加上三个点然后在下一行继续写
z =  3*(1-x).^2.*exp(-(x.^2) - (y+1).^2)...  
    -10* (x/5 - x.^3 - y.^5).*exp(-x.^2-y.^2) ...
    - 1/3*exp(-(x+1).^2 - y.^2);  % matlab中内置的peaks函数，常常作为演示使用
% edit peaks

%% contour(x,y,z) 在x-y平面绘制等高线图，Matlab会自动选择等高线的层级
contour(x,y,z)
xlabel('x轴');  ylabel('y轴');  % 加上坐标轴的标签

%% contour(x,y,z,n) 在x-y平面绘制等高线图，n是一个标量，那么Matlab会将等高线的层数设置为n，且会自动选择层所在的高度。
contour(x,y,z,5)
contour(x,y,z,5,'LineWidth',2)  % 设置线的宽度为2
contour(x,y,z,5,'--')  % 设置等高线为虚线
contour(x,y,z,5,'ShowText','on')  % 显示每一层的高度
contour(x,y,z,5,'--','ShowText','on','LineWidth',2)  % 可以组合起来使用
colorbar % 显示颜色栏，也可以手动插入
xlabel('x轴');  ylabel('y轴');  % 加上坐标轴的标签

%% contour(x,y,z,levels) 若想得到固定的n个高度的等高线，将levels可以设置为n元行向量，其中向量中的值为高度值。
maxz = max(max(z))
minz = min(min(z))
levels = linspace(minz,maxz,10)  % 从最小值到最大值，等分成10个点
contour(x,y,z,levels,'ShowText','on','LineWidth',1)  % 最小值或者最大值可能显示不出来，因为Matlab会帮我们自动调整
xlabel('x轴');  ylabel('y轴');  % 加上坐标轴的标签

% 思考如果只想画出高度为3的单等高线怎么办?
contour(x,y,z,[3 3],'ShowText','on') 
xlabel('x轴');  ylabel('y轴');  % 加上坐标轴的标签

%% contourf函数：和contour函数类似，只不过画出来的等高线图有颜色填充
contourf(x,y,z,levels,'ShowText','on') 
xlabel('x轴');  ylabel('y轴');  % 加上坐标轴的标签

%% contour3函数：3维等高线图，等高线不再投影到x-y平面
contour3(x,y,z,levels,'ShowText','on') 
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签


% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）
