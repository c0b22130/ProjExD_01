import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    tori_img = pg.image.load("ex01-20230613/fig/3.png")
    tori_img = pg.transform.flip(tori_img,True,False)
    bg_img_t = pg.transform.flip(bg_img,True,False)
    rotate_img = pg.transform.rotozoom(tori_img,5,1.0)
    rotate_img2 = pg.transform.rotozoom(tori_img,10,1.0) 
    rotate_img3 = pg.transform.rotozoom(tori_img,15,1.0) 
    rotate_img4 = pg.transform.rotozoom(tori_img,20,1.0)
    rotate_img5 = pg.transform.rotozoom(tori_img,25,1.0)
    rotate_img6 = pg.transform.rotozoom(tori_img,30,1.0)
    rotate_img7 = pg.transform.rotozoom(tori_img,35,1.0)
    rotate_img8 = pg.transform.rotozoom(tori_img,40,1.0)
    rotate_img9 = pg.transform.rotozoom(tori_img,45,1.0)
    rotate_img10 = pg.transform.rotozoom(tori_img,50,1.0)
    img_lst = [tori_img,rotate_img,rotate_img2,rotate_img3,rotate_img4,rotate_img5,rotate_img6,rotate_img7,rotate_img8,rotate_img9,rotate_img10,rotate_img9,rotate_img8,rotate_img7,rotate_img6,rotate_img5,rotate_img4,rotate_img3,rotate_img2]
    tmr = 0
    x=0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_t,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(img_lst[tmr%len(img_lst)],[300,200])
        pg.display.update()
        tmr += 4
        x=tmr%3200       
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()