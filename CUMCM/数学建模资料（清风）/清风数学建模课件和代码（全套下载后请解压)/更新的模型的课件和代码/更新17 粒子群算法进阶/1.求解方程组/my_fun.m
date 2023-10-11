function F = my_fun(x)
    F(1) =  abs(x(1)+x(2))-abs(x(3));
    F(2) =  x(1) * x(2) * x(3) + 18;
    F(3) = x(1)^2*x(2)+3*x(3);
end