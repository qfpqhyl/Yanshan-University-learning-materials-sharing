function dx=SIR_fun(t,x,beta1,beta2,a,b)  
    % beta1 : t<=15时，易感染者与已感染者接触且被传染的强度
    % beta2   : t>15时，易感染者与已感染者接触且被传染的强度
    % a  : 康复率gamma = a+bt
    % b  : 康复率gamma = a+bt
    if t <=15
        beta = beta1;
    else
        beta = beta2;
    end
    gamma = a + b * t;  
    dx = zeros(3,1);  % x(1)表示S  x(2)表示I  x(3)表示R
    C = x(1)+x(2);  % 传染病系统中的有效人群,也就是课件中的N' = S+I
    dx(1) = - beta*x(1)*x(2)/C;  
    dx(2) = beta*x(1)*x(2)/C - gamma*x(2);
    dx(3) = gamma*x(2); 
end
