function f = Obj_fun(x)
    f1= abs(x(1)+x(2))-abs(x(3)) ;
    f2 = x(1) * x(2) * x(3) + 18;
    f3= x(1)^2 * x(2) + 3*x(3);
    f = abs(f1) + abs(f2) + abs(f3);
end