function [fitresult, gof] = createFit(year, population)
%CREATEFIT(YEAR,POPULATION)
%  Create a fit.
%
%  Data for 'untitled fit 1' fit:
%      X Input : year
%      Y Output: population
%      Weights : year
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  另请参阅 FIT, CFIT, SFIT.

%  由 MATLAB 于 22-Aug-2023 16:13:24 自动生成


%% Fit: 'untitled fit 1'.
[xData, yData, weights] = prepareCurveData( year, population, year );

% Set up fittype and options.
ft = fittype( 'xm/(1+(xm/3.9-1)*exp(-r*(t-1790)))', 'independent', 't', 'dependent', 'y' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.StartPoint = [0.02 500];
opts.Weights = weights;

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

% Plot fit with data.
figure( 'Name', 'untitled fit 1' );
h = plot( fitresult, xData, yData );
legend( h, 'population vs. year with year', 'untitled fit 1', 'Location', 'NorthEast' );
% Label axes
xlabel year
ylabel population
grid on


