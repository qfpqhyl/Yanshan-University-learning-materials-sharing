%% surf函数：绘制出在某一区间内完整的曲面图
% surf函数和mesh函数的的调用格式基本相同
% 两者的区别： mesh绘出彩色的线，surf绘出彩色的面

%% 例题1的对比
[x,y] = meshgrid(linspace(0,5,11));
% [x,y] = meshgrid([0:0.5:5]);  或者直接写成[x,y] = meshgrid(0:0.5:5);
z = x.^2 - y.^2;
subplot(1,2,1)  % subplot(m,n,index)
mesh(x,y,z)
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
title('mesh(x,y,z)')

subplot(1,2,2)
surf(x,y,z)  
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
% axis([0,5,0,5,-inf,+inf])  % 设置坐标轴刻度范围
title('surf(x,y,z)')

%% 例题2的对比
[x,y] = meshgrid(-5:0.5:5);  % 快速生成网格所需的数据
tem = sqrt(x.^2+y.^2)+1e-12;   
z = sin(tem)./tem;  % 如果不对tem处理，那么z的最中间的一个值 0/0 = NaN
subplot(1,2,1)
mesh(x,y,z)
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
title('mesh(x,y,z)')

subplot(1,2,2)
surf(x,y,z)  % (X(j), Y(i), Z(i,j))是线框网格线的交点
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
title('surf(x,y,z)')

%% surfc函数：除了surf函数图形外，还在xy平面上绘制曲面的等高线
surfc(x,y,z)
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示

%% surfl函数：加上了灯光效果,看起来自然点
surfl(x,y,z)
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示

%% 设置色彩模式
% shading 是用来处理色彩效果的，分以下三种：
% shading faceted是默认的模式 
% shading flat 在faceted的基础上去掉图上的网格线
% shading interp 在flat的基础上进行色彩的插值处理，使色彩平滑过渡
subplot(1,3,1)
surf(x,y,z)  % (X(j), Y(i), Z(i,j))是线框网格线的交点
shading faceted % 默认的色彩模式
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
title('shading faceted')

subplot(1,3,2)
surf(x,y,z)  % (X(j), Y(i), Z(i,j))是线框网格线的交点
shading flat % 看起来光滑一点
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
title('shading flat')

subplot(1,3,3)
surf(x,y,z)  % (X(j), Y(i), Z(i,j))是线框网格线的交点
shading interp % 看起来最光滑
xlabel('x轴');  ylabel('y轴');  zlabel('z轴');  % 加上坐标轴的标签
axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
title('shading interp')



% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）