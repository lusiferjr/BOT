from time import time
from math import *
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

def drawgraph(eq, prec=10, fpath=''):
    if '=' in eq:
            l=eq.split('=')
            eq = l[0] + '-(' + l[1] + ')'
    elif 'y' not in eq:
        if 'x' not in eq:
            return 'Error: x not found'
        eq = eq + '- y'
    try:
        eq = compile(eq,'string','eval')
    except Exception as e:
        return 'Error: Wrong Equation - '+ str(e)
    
    def plot(x,y,w=0):
        x=prec*x+wh
        y=-prec*y+hh
        if w:
            fig.ellipse((x-w,y-w,x+w,y+w),0)
        else:
            x=int(x)
            y=int(y)
            img.putpixel((x,y),0)
    def plot2(x,y,w=0):
        if w:
            fig.ellipse((x-w,y-w,x+w,y+w),0)
        else:
            img.putpixel((x,y),0)

    w,h=600,400

    wh,hh=w//2,h//2
    img=Image.new('1',(w,h),1)
    fig=ImageDraw.Draw(img)
    font=ImageFont.truetype(fpath+"arial.ttf", h//25)

    

    fig.line((0,hh,w,hh),0,1)
    y=hh
    for x in range(0,wh+1,h//10):
        plot2(wh-x,y,h//200)
        plot2(wh+x,y,h//200)
        fig.text((wh+x,y),str(x//prec),0,align='center',font=font)
        fig.text((wh-x,y),str(-x//prec),0,align='center',font=font)

    fig.line((wh,0,wh,h),0,1)
    x=wh
    for y in range(h//10,hh+1,h//10):
        plot2(x,hh-y,h//200)
        plot2(x,hh+y,h//200)
        fig.text((x,hh+y),'  '+str(-y//prec),0,align='center',font=font)
        fig.text((x,hh-y),'  '+str(y//prec),0,align='center',font=font)

    t=time()
    inc=1/(prec*2)
    maxx=wh/prec+1
    maxy=hh/prec+1

    x=-maxx
    oldz=0
    flag=True
    while x<=maxx:
        x+=inc
        y=-maxy
        while y<=maxy:
            y+=inc
            try:
                z=eval(eq)
                if flag and (z==0 or (z<0)^(oldz<0)):
                    plot(x,y,1)
                oldz=z
                flag=True
            except (SyntaxError,TypeError,NameError):
                return 'Error: Enter correct syntax'
            except:
                flag=False
        flag=False

    y= -maxy
    oldz=0
    flag=True
    while y<=maxy:
        y+=inc
        x=-maxx
        while x<=maxx:
            x+=inc
            try:
                z=eval(eq)
                if flag and (z==0 or (z<0)^(oldz<0)):
                    plot(x,y,1)
                oldz=z
                flag=True
            except (SyntaxError,TypeError,NameError):
                return 'Error: Enter correct syntax'
            except:
                flag=False
        flag=False

    #img.save('fig.png')
    imdata = BytesIO()
    img.save(imdata,format='png')
    return imdata.getvalue()

if __name__=='__main__':
    obj = drawgraph('y-2*x')
    
#z= ((y-8)**2+2*((x-8)**2)-40)*((y-8)**2+2*((x+8)**2)-40)*(y*y+2*x*x-900)*((y+16)**4+.02*(x**4)-40)
