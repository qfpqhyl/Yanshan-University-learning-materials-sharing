% 目标函数参考的最优值：38.8503    
narvs = 2; % 变量个数
x_lb = [-3 4.1]; % x的下界
x_ub = [12.1 5.8]; % x的上界

%% 直接使用particleswarm函数
[x,fval] = particleswarm(@Obj_fun_1,narvs,x_lb,x_ub)
fval = -fval

%% 将粒子群算法得到的解作为初始值，继续调用fmincon函数求解
options = optimoptions('particleswarm','HybridFcn',@fmincon);
[x,fval] = particleswarm(@Obj_fun_1,narvs,x_lb,x_ub,options)
fval = -fval

%% 修改参数：这里要增加粒子个数，因为函数局部最小值太多了
options = optimoptions('particleswarm','FunctionTolerance',1e-12,'MaxStallIterations',100,'MaxIterations',20000,'SwarmSize',1000);
[x,fval] = particleswarm(@Obj_fun_1,narvs,x_lb,x_ub,options)
fval = -fval