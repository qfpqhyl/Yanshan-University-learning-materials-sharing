function y_hat = fit_fun(k,x)
    y_hat = exp(-k(1)*x(:,1)) .* sin(k(2)*x(:,2)) + x(:,3).^2;  % 返回的函数就是我们的拟合值
end