#SingleInstance force
F2::
loop
{
ImageSearch,vx,vy, 0,0, 653, 653, *20 ti.JPG
IF ErrorLevel = 0
{
mouseclick,left,%vx%+100, %vy%+100
mouseclick, left, 907, 700
Send, {ESC}
break
}
}
return
