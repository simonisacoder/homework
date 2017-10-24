clear all;
close all;
clc;

N = 3;
NUMBER_OF_SAMPLES = 5;
FILTER_COEFFICIENTS = [0.1 -0.1 0.4 1.0 -0.7 0.2 -0.9 -0.4 -0.8];
x = [-9  4 -2  0 -3  0  8  3  6  0, ...
     -7 -9 -5  2  1  2  8 -4 -6 -4];
 
%example 6
y = filter(1, [1 -0.5], x(1:10))

%example 7
y = filter(1, [1 -FILTER_COEFFICIENTS(1:N-1)], x (1:NUMBER_OF_SAMPLES))
