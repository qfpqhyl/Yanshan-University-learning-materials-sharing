%% 综合应用：粒子群算法PSO: 求解函数y = 21.5+x(1)*sin(4*pi*x(1))+x(2)*sin(20*pi*x(2))在x1属于[-3,12.1]，x2属于[4.1,5.8]内的最大值(动画演示）
clear; clc   % 目标函数参考的最优值：38.8503    

%% 绘制函数的图形
% x1 = -3:0.01:12.1;
% x2 = 4.1:0.01:5.8;
% [x1,x2] = meshgrid(x1,x2);
% y = 21.5 + x1.*sin(4*pi*x1) + x2.*sin(20*pi*x2);
% mesh(x1,x2,y)
% xlabel('x1');  ylabel('x2');  zlabel('y');  % 加上坐标轴的标签
% axis vis3d % 冻结屏幕高宽比，使得一个三维对象的旋转不会改变坐标轴的刻度显示
% hold on  % 不关闭图形，继续在上面画图

%% 粒子群算法中的预设参数（参数的设置不是固定的，可以适当修改）
n = 1000; % 粒子数量
narvs = 2; % 变量个数
c1 = 2.05;  % 每个粒子的个体学习因子，也称为个体加速常数
c2 = 2.05;  % 每个粒子的社会学习因子，也称为社会加速常数
C = c1+c2; 
fai = 2/abs((2-C-sqrt(C^2-4*C))); % 收缩因子
w_max = 0.9;  % 最大惯性权重，通常取0.9
w_min = 0.4; % 最小惯性权重，通常取0.4
K = 100;  % 迭代的次数
vmax = [1.51 0.17]; % 粒子的最大速度
x_lb = [-3 4.1]; % x的下界
x_ub = [12.1 5.8]; % x的上界

%% 初始化粒子的位置和速度
x = zeros(n,narvs);
for i = 1: narvs
    x(:,i) = x_lb(i) + (x_ub(i)-x_lb(i))*rand(n,1);    % 随机初始化粒子所在的位置在定义域内
end
v = -vmax + 2*vmax .* rand(n,narvs);  % 随机初始化粒子的速度（这里我们设置为[-vmax,vmax]）

%% 计算适应度
fit = zeros(n,1);  % 初始化这n个粒子的适应度全为0
for i = 1:n  % 循环整个粒子群，计算每一个粒子的适应度
    fit(i) = Obj_fun_2(x(i,:));   % 调用Obj_fun_2函数来计算适应度
end 
pbest = x;   % 初始化这n个粒子迄今为止找到的最佳位置（是一个n*narvs的向量）
ind = find(fit == max(fit), 1);  % 找到适应度最大的那个粒子的下标
gbest = x(ind,:);  % 定义所有粒子迄今为止找到的最佳位置（是一个1*narvs的向量）

%% 在图上标上这n个粒子的位置用于演示
% h = scatter3(x(:,1),x(:,2),fit,'*r');  % scatter3是绘制三维散点图的函数（这里返回h是为了得到图形的句柄，未来我们对其位置进行更新）

%% 迭代K次来更新速度与位置
fitnessbest = ones(K,1);  % 初始化每次迭代得到的最佳的适应度
for d = 1:K  % 开始迭代，一共迭代K次
    for i = 1:n   % 依次更新第i个粒子的速度与位置
        f_i = fit(i);  % 取出第i个粒子的适应度
        f_avg = sum(fit)/n;  % 计算此时适应度的平均值
        f_max = max(fit); % 计算此时适应度的最大值
        if f_i >= f_avg  
             if f_avg ~= f_max  % 如果分母为0，我们就干脆令w=w_min
                w = w_min + (w_max - w_min)*(f_max - f_i)/(f_max - f_avg);
            else
                w = w_min;
             end
        else
            w = w_max;
        end
        v(i,:) = fai * (w*v(i,:) + c1*rand(1)*(pbest(i,:) - x(i,:)) + c2*rand(1)*(gbest - x(i,:)));  % 更新第i个粒子的速度
        x(i,:) = x(i,:) + v(i,:); % 更新第i个粒子的位置
        % 如果粒子的位置超出了定义域，就对其进行调整
        for j = 1: narvs
            if x(i,j) < x_lb(j)
                x(i,j) = x_lb(j);
            elseif x(i,j) > x_ub(j)
                x(i,j) = x_ub(j);
            end
        end
        fit(i) = Obj_fun_2(x(i,:));  % 重新计算第i个粒子的适应度
        if fit(i) > Obj_fun_2(pbest(i,:))   % 如果第i个粒子的适应度大于这个粒子迄今为止找到的最佳位置对应的适应度
           pbest(i,:) = x(i,:);   % 那就更新第i个粒子迄今为止找到的最佳位置
        end
        if  fit(i) > Obj_fun_2(gbest)  % 如果第i个粒子的适应度大于所有的粒子迄今为止找到的最佳位置对应的适应度
            gbest = pbest(i,:);   % 那就更新所有粒子迄今为止找到的最佳位置
        end
    end
    fitnessbest(d) = Obj_fun_2(gbest);  % 更新第d次迭代得到的最佳的适应度
%     pause(0.1)  % 暂停0.1s
%     h.XData = x(:,1);  % 更新散点图句柄的x轴的数据（此时粒子的位置在图上发生了变化）
%     h.YData = x(:,2);   % 更新散点图句柄的y轴的数据（此时粒子的位置在图上发生了变化）
%     h.ZData = fit;  % 更新散点图句柄的z轴的数据（此时粒子的位置在图上发生了变化）
end

figure(2) 
plot(fitnessbest)  % 绘制出每次迭代最佳适应度的变化图
xlabel('迭代次数');
disp('最佳的位置是：'); disp(gbest)
disp('此时最优值是：'); disp(Obj_fun_2(gbest))