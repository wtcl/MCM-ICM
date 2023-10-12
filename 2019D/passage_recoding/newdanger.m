clearall
clc

emerg=[580,550];
X=[X;emerg];
C=X;
n=size(C,1);
totaldens=0.4;
viewpoint=21;
C=[C,zeros(n,1)];
holdon
thread=0;
e=[0,0,0,0];
Rfield=21;
Nfield=zeros(n,1);
rho=zeros(3700,1);
Wemerg=zeros(3700,1);
Wexit=zeros(3700,1);
Neg=zeros(3700,1);
for i=1:n
for j=1:n
if i~=j
D(i,j)=sqrt((C(i,1)-C(j,1))^2+(C(i,2)-C(j,2))^2);
else
D(i,j)=0;
end
D(j,i)=D(i,j);
end
end
for i=1:n
for j=1:n
if D(i,j)>viewpoint||sqrt((C(i,1)−emerg(1,1))^2+(C(i,2)−emerg(1,2))^2)<=
read
D(i,j)=inf;
end
end
end
for i=1:3700
ifrand<=totaldens&&(sqrt((C(i,1)−emerg(1,1))^2+(C(i,2)−emerg(1,2))^2)>
read)
C(i,3)=1;
end
end

for i=1:3700
for j=max(1,i−64):min(i+64,3700)
if(sqrt((C(i,1)−C(j,1))^2+(C(i,2)−C(j,2))^2)<=21)&&(C(j,3)==1)
Nfield(i,1)=Nfield(i,1)+1;
end
end
end
for i=1:3700
start=i;
exit=X(3701:3704,:);
[mydistance1,mypath1]=Djsk(D,start,3701);
[mydistance2,mypath2]=Djsk(D,start,3702);
[mydistance3,mypath3]=Djsk(D,start,3703);
[mydistance4,mypath4]=Djsk(D,start,3704);
Pd=[mydistance1,mydistance2,mydistance3,mydistance4];
[value,index]=min(Pd);
Wexit(i,1)=value;
disemerg=sqrt((C(i,1)−emerg(1,1))^2+(C(i,2)−emerg(1,2))^2);
Wemerg(i,1)=1/disemerg;
end
for i=1:3700
rho(i,1)=Nfield(i,1)/(pi∗Rfield^2);
end
a=10^2;
b=10^4;
c=1;
for i=1:3700
Neg(i,1)=a∗rho(i,1)+b∗Wemerg(i,1)+c∗Wexit(i,1);
end
f1=1:600;
f2=1:1000;
[F1,F2]=meshgrid(f1,f2);
F3=zeros(600,1000);
F1=F1’;F2=F2’;
for i=1:600
for j=1:1000
for ii=1:3700
ifi==X(ii,1)&&j==X(ii,2)
F3(i,j)=Neg(ii,1);
end
end
end
end
mesh(F1,F2,F3);