from tkinter import Tk, Canvas, PhotoImage,NW,mainloop

def mandel_pixel(c):
  maxIt = 200
  z =  c
  for i in range(maxIt):
      a = z * z
      z=a + c
      if a.real  > 1000.:
         return i
  return 200

def mandelbrot(xa,xb,ya,yb,x,y):
    clr=[ ' #%02x%02x%02x' % (int(255*((i/255)**.25)),0,0) for i in range(200)]
    clr.append('black')
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
    return" ".join((("{"+" ".join(clr[mandel_pixel(complex(i,j))] for i in xm))+"}" for j in ym))

x=700
y=700

xa = -2.0; xb = 0.5
ya = -1.25; yb = 1.25


window = Tk()
canvas = Canvas(window, width = x, height = y, bg = "black");canvas.pack()
img = PhotoImage(width = x, height = y)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

img.put(mandelbrot(xa,xb,ya,yb,x,y))

mainloop()

#clr=[ ' #%02x%02x%02x' % (int(255*((i/255)**.25)),0,0) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.4)),67,0) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.4)),67,123) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.4)),167,123) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.4)),100,100) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.4)),34,200) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.4)),0,123) for i in range(200)]
#clr=[ ' #%02x%02x%02x' % (int(260*((i/255)**.1)),245,255) for i in range(200)]