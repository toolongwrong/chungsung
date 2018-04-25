
clc;

x = -pi: pi/100 :pi;

y1 = sin(x);

y2 = sin(2*x);

y3 = sin(3*x);

plot(x, y1, '--r');

hold on;

plot(x, y2,'--b');

hold on;

plot(x,y3,':g');

hold off;

title('homework2-1');

xlabel('x dot');
ylabel('y dot');
axis( [-6 6 -1.5 +1.5] );