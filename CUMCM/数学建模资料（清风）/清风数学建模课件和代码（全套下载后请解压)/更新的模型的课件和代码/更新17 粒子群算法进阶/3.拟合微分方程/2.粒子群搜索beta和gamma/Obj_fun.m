function f = Obj_fun(h)  
    % 注意，h就是我们要估计的目标函数里面的参数
    % h的长度就是我们待估参数的个数
    global true_s  true_i  true_r n   % 在子函数中使用全局变量前也需要声明下
    beta = h(1);  % 易感染者与已感染者接触且被传染的强度
    gamma = h(2);  % 康复率
    [t,p]=ode45(@(t,x) SIR_fun(t,x,beta,gamma), [1:n],[true_s(1) true_i(1) true_r(1)]);   
    p = round(p);  % 对p进行四舍五入(人数为整数)
    % p的第一列是易感染者S的数量，p的第二列是患者I的数量，p的第三列是康复者R的数量
    f = sum((true_s - p(:,1)).^2  + (true_i -  p(:,2)).^2  + (true_r - p(:,3)).^2);
end