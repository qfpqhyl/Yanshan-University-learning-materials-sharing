clear;clc
load mydata.mat  % 导入数据（共三列，分别是S,I,R的数量）
global true_s true_i true_r  n  % 定义全局变量
n = size(mydata,1);  % 一共有多少行数据
true_s = mydata(:,1);
true_i = mydata(:,2);
true_r = mydata(:,3);
figure(1)
plot(1:n,true_i,'b-',1:n,true_r,'g-') % 单独画出I和R的数量
legend('I','R')

% 粒子群算法来求解
% beta1,beta2,a,b
% 给定参数的搜索范围（根据题目来给），后期可缩小范围
lb = [0 0 -1 -1]; 
ub = [1 1 1 1];  
% lb = [0 0 -0.2 -0.2]; 
% ub = [0.3 0.3 0.2 0.2];  
options = optimoptions('particleswarm','Display','iter','SwarmSize',200);
[h, fval] = particleswarm(@Obj_fun, 4, lb, ub, options)  % h就是要优化的参数，fval是目标函数值, 第二个输入参数4代表我们有4个变量需要搜索

beta1 = h(1);  % t<=15时，易感染者与已感染者接触且被传染的强度
beta2 = h(2);  % t>15时，易感染者与已感染者接触且被传染的强度
a = h(3); % 康复率gamma = a+bt
b = h(4);  % 康复率gamma = a+bt
[t,p]=ode45(@(t,x) SIR_fun(t,x,beta1,beta2,a,b), [1:n],[true_s(1) true_i(1) true_r(1)]);   
p = round(p);  % 对p进行四舍五入(人数为整数)

figure(3)  % 真实的人数和拟合的人数放到一起看看
plot(1:n,true_i,'b-',1:n,true_r,'g-') 
hold on
plot(1:n,p(:,2),'b--',1:n,p(:,3),'g--') 
legend('I','R','拟合的I','拟合的R')

% 预测未来的趋势
N = 27; % 计算N天
[t,p]=ode45(@(t,x) SIR_fun(t,x,beta1,beta2,a,b), [1:N],[true_s(1) true_i(1) true_r(1)]);   
p = round(p);  % 对p进行四舍五入(人数为整数)
figure(4)
plot(1:n,true_i,'b-',1:n,true_r,'g-') 
hold on
plot(1:N,p(:,2),'b--',1:N,p(:,3),'g--') 
legend('I','R','拟合的I','拟合的R')





% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）
