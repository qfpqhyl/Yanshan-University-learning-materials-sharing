function y = Obj_fun1(x)
    y = 11*sin(x) + 7*cos(5*x);
    %    y = -(11*sin(x) + 7*cos(5*x));  % 如果调用fmincon函数，则需要添加负号改为求最小值
end