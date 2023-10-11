function f = Obj_fun(k)
    global x y;  % 在子函数中使用全局变量前也需要声明下
    y_hat = exp(-k(1)*x(:,1)) .* sin(k(2)*x(:,2)) + x(:,3).^2;  % 拟合值
    f = sum((y - y_hat) .^ 2);
end