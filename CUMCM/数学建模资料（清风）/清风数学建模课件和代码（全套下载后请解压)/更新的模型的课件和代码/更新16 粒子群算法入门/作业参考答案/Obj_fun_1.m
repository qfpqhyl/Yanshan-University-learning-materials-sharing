function y = Obj_fun_1(x)
     y =- (21.5 + x(1)*sin(4*pi*x(1)) + x(2)*sin(20*pi*x(2)));  % 如果调用fmincon函数或者particleswarm函数，则需要添加负号改为求最小值
end