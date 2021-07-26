#importo las librerias que voy a utilizar
import sys;
import pygame
import random
import imagenes
# defino el ancho y largo de la ventan en pixeles
size = (640, 480);
#defino colores 
blanco=(255,255,255)
verde=(0,255,0) 
negro=(0,0,0)
# inicio pygame
pygame.init()
pygame.mixer.init()
#defino la ventana con el icono y el nombre
icono = pygame.image.load('FROGRUN.png')
ventana = pygame.display.set_mode(size)
pygame.display.set_caption('Froggy')
pygame.display.set_icon(icono)
# defino el reloj del juego
reloj = pygame.time.Clock();
# defino los buqles a utilizar
arranque= True
submenu1= True
submenu2= True
jugando= True
jugando2= True
jugando3= True
jugando4= True
jugando5= True
finjuego= True
# creo botones 
empezar = pygame.Rect(210,120,200,50)  
controles = pygame.Rect(210,220,200,50)  
opciones = pygame.Rect(210,320,200,50)  
salir = pygame.Rect(250,420,120,50)  
volver = pygame.Rect(68,407,90,40)  
si = pygame.Rect(90,220,50,50)  
no = pygame.Rect(480,220,50,50)
#sonidos
ranasalta= pygame.mixer.Sound('Sonidos/Efectos/RANSALTA.WAV')
ranachoca= pygame.mixer.Sound('Sonidos/Efectos/RANAUTO.WAV')
ranagua= pygame.mixer.Sound('Sonidos/Efectos/RANAGUA.WAV')
fin= pygame.mixer.Sound('Sonidos/Efectos/RANFIN.WAV')
ranasalta.set_volume(0.6)
ranachoca.set_volume(0.6)
ranagua.set_volume(0.6)
fin.set_volume(0.6)
#creo la clase jugador que hereda de sprite
class Jugador(pygame.sprite.Sprite):
# Sprite del jugador
    def __init__(self):
# Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.transform.rotate(imagenes.rana[0], 0)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = ( 640//2,418)
        self.contador = 0

    def update(self,arriba,abajo,izquierda,derecha,rotacion):
 # compruebo la direccion del personaje
        if arriba:           
            while self.contador <5:
                if self.rect.top <0:
                     self.rect.top= 0
                reloj.tick(30);
                self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion)
                sprites.draw(ventana)
                pygame.display.flip()
                self.contador+=1
                self.rect.y -= 10
            self.contador= 0
            self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion)
        if abajo:           
            while self.contador <5:
                if self.rect.bottom >440:
                    self.rect.bottom= 440
                reloj.tick(30);
                self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion) 
                sprites.draw(ventana)
                pygame.display.flip()
                self.contador+=1
                self.rect.y += 10
            self.contador= 0
            self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion)
        if izquierda:           
            while self.contador <5:
                if self.rect.left <0:
                    self.rect.left= 0
                reloj.tick(30);
                self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion)
                sprites.draw(ventana)
                pygame.display.flip()
                self.contador+=1
                self.rect.x -= 10
            self.contador= 0
            self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion)
        if derecha:           
            while self.contador <5: 
                if self.rect.right >640:
                    self.rect.right= 640
                reloj.tick(30);
                self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion) 
                sprites.draw(ventana)
                pygame.display.flip()
                self.contador+=1
                self.rect.x += 10
            self.contador= 0
            self.image = pygame.transform.rotate(imagenes.rana[self.contador], rotacion)
        
        
    def mueve(self,numr):       
        self.rect.x +=numr
        sprites.draw(ventana)
        if self.rect.right >640:
            self.rect.right= 640
        if self.rect.left <0:
            self.rect.left= 0
            
#creo la clase auto
class Auto(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self,angulo,x,y,dire,vela):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.transform.rotate(imagenes.autos[random.randrange(15)], angulo)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = ( x, y)
        self.velocidada = vela
        self.direccion= dire
    def update(self):
        # compruebo la direccion del personaje
        if self.direccion:
            self.rect.x -= self.velocidada
            if self.rect.left <-300:
                
                self.rect.left= 940
        else:
            self.rect.x += self.velocidada
            if self.rect.right >940:
                
                self.rect.right= -100
            
#creo la calase agua
class Agua(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self,surfy,surfx,centy,centx):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.Surface((surfy, surfx))
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (centy,centx )
#creo la clase check

class Check(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self,x,y):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.Surface((20, 40))
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (x,y )
#creo la calse votes
class Votes(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self,x,y,invertido,vel):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.transform.rotate(imagenes.votes[random.randrange(5)],0)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = ( x, y)
        self.contador = 0
        self.direccioni = invertido
        self.velocidad= vel
        
    def update(self):
        if self.direccioni:
            self.rect.x -= self.velocidad
            if self.rect.right <-100:
                self.rect.right= 940
        else:
            self.rect.x += self.velocidad
            if self.rect.right >940:
                self.rect.right= -100  
            
#defino la funcion texto que me da la fuente, el mensaje, el tamanio, las posiciones y el color
def texto(surface, text, size, x, y,color):
    font = pygame.font.SysFont("comicsansms",size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop =(x, y)
    surface.blit(text_surface, text_rect)       
# menu principal
def menuP():
    ventana.blit(imagenes.fondos[0], [0, 0])
    texto(ventana,'Empezar', 50, 310, 100,blanco)
    texto(ventana,'Controles', 50, 310, 200,blanco)
    texto(ventana,'Opciones', 50, 310, 300,blanco)
    texto(ventana,'Salir', 50, 310, 400,blanco)   
    if empezar.collidepoint(pygame.mouse.get_pos()):
        texto(ventana,'Empezar', 50, 310, 100,verde)
        if pygame.mouse.get_pressed()[0]:    
            jugar()
    if controles.collidepoint(pygame.mouse.get_pos()):
        texto(ventana,'Controles', 50, 310, 200,verde)
        if pygame.mouse.get_pressed()[0]:
            menuA()
    if opciones.collidepoint(pygame.mouse.get_pos()):
        texto(ventana,'Opciones', 50, 310, 300,verde)
        if pygame.mouse.get_pressed()[0]:
            menuO()
    if salir.collidepoint(pygame.mouse.get_pos()):
        texto(ventana,'Salir', 50, 310, 400,verde)
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
# creo la funcion menua que va a iniciar otro bucle que muestre el menu de ayuda del juego
def menuA():
    while submenu1:   
        ventana.blit(imagenes.fondos[2], [0, 0])
        texto(ventana,'Volver', 30, 110, 400,blanco)
        if volver.collidepoint(pygame.mouse.get_pos()):
            texto(ventana,'Volver', 30, 110, 400,verde)
            if pygame.mouse.get_pressed()[0]:
                break
        pygame.display.flip()
        for event in pygame.event.get():
        # en caso de apretar en la cruz de la ventana esta se cierra y termian el proceso.
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
# creo la funcion menuo que va a iniciar otro bucle que muestre las opciones de sonido del juego
def menuO():
    while submenu2:
        ventana.blit(imagenes.fondos[1], [0, 0])
        texto(ventana,'Desea sonido', 50, 310, 100,blanco)
        texto(ventana,'Si', 50, 110, 200,blanco)
        texto(ventana,'No', 50, 510, 200,blanco)
        if si.collidepoint(pygame.mouse.get_pos()):
            texto(ventana,'Si', 50, 110, 200,verde)
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.load('Sonidos/Musica/COMP2U.OGG')
                pygame.mixer.music.play()
                break

        if no.collidepoint(pygame.mouse.get_pos()):
           texto(ventana,'No', 50, 510, 200,verde)
           if pygame.mouse.get_pressed()[0]:
               pygame.mixer.music.stop()
               break
        pygame.display.flip()
        for event in pygame.event.get():
        # en caso de apretar en la cruz de la ventana esta se cierra y termian el proceso.
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
def finJ():
    while finjuego:
        ventana.blit(imagenes.fondos[0], [0, 0])
        texto(ventana,'Fin del juego', 50, 310, 100,blanco)
        texto(ventana,'Desea volver a intentar?', 50, 310, 150,blanco)
        texto(ventana,'Si', 50, 110, 200,blanco)
        texto(ventana,'No', 50, 510, 200,blanco)
        if si.collidepoint(pygame.mouse.get_pos()):
            texto(ventana,'Si', 50, 110, 200,verde)
            if pygame.mouse.get_pressed()[0]:
                jugar()

        if no.collidepoint(pygame.mouse.get_pos()):
           texto(ventana,'No', 50, 510, 200,verde)
           if pygame.mouse.get_pressed()[0]:
              break
        pygame.display.flip()
        for event in pygame.event.get():
        # en caso de apretar en la cruz de la ventana esta se cierra y termian el proceso.
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()             
#instancio clases
#clase votes
#clase personaje
sprites = pygame.sprite.Group()
jugador = Jugador()
sprites.add(jugador)
#clase jugar Nivel 1
def jugar():
    pygame.mixer.music.load('Sonidos/Musica/CIRCLE.OGG')
    pygame.mixer.music.play()
    votesprite=pygame.sprite.Group()
    votespritei=pygame.sprite.Group()
    vote1 = Votes(-100, 60,False,1)
    vote2 = Votes(-500, 60,False,1)
    vote3 = Votes(-900, 60,False,1)
    votei1 = Votes(970, 120,True,2)
    votei2 = Votes(1200, 120,True,2)
    votei3 = Votes(1600, 120,True,2)
    vote4 = Votes(-100, 170,False,1)
    vote5 = Votes(-500, 170,False,1)
    vote6 = Votes(-900, 170,False,1)
    votesprite.add(vote1,vote2,vote3,vote4,vote5,vote6)
    votespritei.add(votei1,votei2,votei3)
    #Clase ceckpoint
    checkpoint=pygame.sprite.Group()
    check=Check(70,20)
    check1=Check(170,20)
    check2=Check(270,20)
    check3=Check(370,20)
    check4=Check(470,20)
    check5=Check(570,20)
    checkpoint.add(check)
    checkpoint.add(check1)
    checkpoint.add(check2)
    checkpoint.add(check3)
    checkpoint.add(check4)
    checkpoint.add(check5)
    #Clase agua
    spriteagua=pygame.sprite.Group()
    agua= Agua(640, 140,640//2,119)
    spriteagua.add(agua)
    #clase auto
    autosde = pygame.sprite.Group()
    autod1 = Auto(0, -10, 365,False,1)
    autod2 = Auto(0, -400, 365,False,1)
    autod3 = Auto(0, -700, 365,False,1)
    autod4 = Auto(0, -10, 265,False,2)
    autod5 = Auto(0, -400, 265,False,2)
    autod6 = Auto(0, -700, 265,False,2)
    autoi1 = Auto(180, 700, 315,True,4)
    autoi2 = Auto(180, 1000, 315,True,4)
    autoi3 = Auto(180, 1500, 315,True,4)
    autosde.add(autod1)
    autosde.add(autod2)
    autosde.add(autod3)
    autosde.add(autoi1)
    autosde.add(autoi2)
    autosde.add(autoi3)
    autosde.add(autod4)
    autosde.add(autod5)
    autosde.add(autod6)
    vida= 5
    rx=[-50,-50,-50,-50,-50,-50]
    ranallegar=0
    arriba = True
    abajo = False
    izquierda = False
    derecha = False
    rotacion = 0
    ranallego= pygame.transform.rotate(imagenes.rana[0], 180) 
    while jugando:
        reloj.tick(30);
        pygame.display.flip()
        checkpoint.draw(ventana)
        ventana.blit(imagenes.mapa1, [0, 0])
        ventana.blit(imagenes.barra, [0, 440])
        if vida>=1:
            ventana.blit(imagenes.ranabarra[0], [20, 445])
        elif vida<1:
            ventana.blit(imagenes.ranabarra[1], [20, 445])
            break
        if vida>=2:
            ventana.blit(imagenes.ranabarra[0], [60, 445])
        elif vida<2:
            ventana.blit(imagenes.ranabarra[1], [60, 445])
        if vida>=3:
            ventana.blit(imagenes.ranabarra[0], [100, 445])
        elif vida<3:
            ventana.blit(imagenes.ranabarra[1], [100, 445])
        if vida>=4:
            ventana.blit(imagenes.ranabarra[0], [140, 445])
        elif vida<4:
            ventana.blit(imagenes.ranabarra[1], [140, 445])
        if vida>=5:
            ventana.blit(imagenes.ranabarra[0], [180, 445])
        elif vida<5:
            ventana.blit(imagenes.ranabarra[1], [180, 445])
        sprites.draw(ventana)
        autosde.draw(ventana)
        autosde.update()
        votesprite.draw(ventana)
        votesprite.update()
        votespritei.draw(ventana)
        votespritei.update()
        #spriteagua.draw(ventana)
        colision = pygame.sprite.spritecollide(jugador, autosde, False)
        colision2= pygame.sprite.spritecollide(jugador, spriteagua, False)
        colision3= pygame.sprite.spritecollide(jugador, votesprite, False)
        colision4= pygame.sprite.spritecollide(jugador, votespritei, False)
        llego= pygame.sprite.spritecollide(jugador, checkpoint, True)
        if colision:
            ranachoca.play()
            vida-=1
            jugador.rect.center = ( 640//2,420)
        if colision2:
            if colision3:
                jugador.mueve(0.5)
            elif colision4:
                jugador.mueve(-1)
            else:
                ranagua.play()
                vida-=1
                
                jugador.rect.center = ( 640//2,420)
        
            #vida-=1
            #jugador.rect.center = ( 640//2,420)
        if llego:
            fin.play()
            rx[ranallegar]=jugador.rect.x  
            ranallegar+=1
            jugador.rect.center = ( 640//2,420)
            
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[0],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[1],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[2],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[3],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[4],2])
        if ranallegar==6:
            ventana.blit(ranallego, [rx[5],2])
            break
        if colision4:
            jugador.mueve(-1)
        if colision3:
            jugador.mueve(1)
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     sprites.update(arriba,abajo,izquierda,derecha,rotacion)
                     ranasalta.play()
                 if event.key == pygame.K_UP:
                     arriba = True
                     abajo = False
                     izquierda = False
                     derecha = False
                     rotacion =0
                 if event.key == pygame.K_DOWN:
                     arriba = False
                     abajo = True
                     izquierda = False
                     derecha = False
                     rotacion = 180
                 if event.key == pygame.K_LEFT:
                     arriba = False
                     abajo = False
                     izquierda = True
                     derecha = False
                     rotacion = 90
                 if event.key == pygame.K_RIGHT:
                     arriba = False
                     abajo = False
                     izquierda = False
                     derecha = True
                     rotacion = 270
    if ranallegar==6:
        jugar2()
    else:
        finJ() 
    pygame.mixer.music.stop()
# nivel 2
def jugar2():
    pygame.mixer.music.load('Sonidos/Musica/JUSTCANT.OGG')
    pygame.mixer.music.play()
    votespritei=pygame.sprite.Group()
    votesprite=pygame.sprite.Group()
    vote1 = Votes(-100, 60,False,2)
    vote2 = Votes(-500, 60,False,2)
    vote3 = Votes(-900, 60,False,2)
    vote4 = Votes(-100, 170,False,1)
    vote5 = Votes(-500, 170,False,1)
    vote6 = Votes(-900, 170,False,1)
    votesprite.add(vote4,vote5,vote6)
    votespritei.add(vote1,vote2,vote3)
    #Clase ceckpoint
    checkpoint=pygame.sprite.Group()
    check=Check(70,20)
    check1=Check(170,20)
    check2=Check(270,20)
    check3=Check(370,20)
    check4=Check(470,20)
    check5=Check(570,20)
    checkpoint.add(check)
    checkpoint.add(check1)
    checkpoint.add(check2)
    checkpoint.add(check3)
    checkpoint.add(check4)
    checkpoint.add(check5)
    #Clase agua
    spriteagua=pygame.sprite.Group()
    agua= Agua(640, 40,640//2,65)
    agua2= Agua(640, 40,640//2,165)
    spriteagua.add(agua,agua2)
    #clase auto
    autosde = pygame.sprite.Group()
    autod1 = Auto(0, -10, 365,False,1)
    autod2 = Auto(0, -400, 365,False,1)
    autod3 = Auto(0, -700, 365,False,1)
    autod4 = Auto(0, -10, 265,False,2)
    autod5 = Auto(0, -400, 265,False,2)
    autod6 = Auto(0, -700, 265,False,2)
    autoi1 = Auto(180, 700, 315,True,4)
    autoi2 = Auto(180, 1000, 315,True,4)
    autoi3 = Auto(180, 1500, 315,True,4)
    autoi4 = Auto(180, 700, 115,True,5)
    autoi5 = Auto(180, 1000, 115,True,5)
    autoi6 = Auto(180, 1500, 115,True,5)
    autoi7 = Auto(180, 700, 215,True,4)
    autoi8 = Auto(180, 1000, 215,True,4)
    autoi9 = Auto(180, 1500, 215,True,4)
    autoi10 = Auto(180, 700, 415,True,1)
    autoi11 = Auto(180, 1000, 415,True,1)
    autoi12 = Auto(180, 1500, 415,True,1)
    autosde.add(autod1,autod2,autod3,autoi1,autoi2,autoi3,autod4,autod5,autod6,autoi4,autoi5,autoi6,autoi7,autoi8,autoi9,
                autoi10,autoi11,autoi12)
    vida= 5
    rx=[-50,-50,-50,-50,-50,-50]
    ranallegar=0
    arriba = True
    abajo = False
    izquierda = False
    derecha = False
    rotacion = 0
    ranallego= pygame.transform.rotate(imagenes.rana[0], 180) 
    while jugando2:
        reloj.tick(30);
        pygame.display.flip()
        checkpoint.draw(ventana)
        ventana.blit(imagenes.mapa2, [0, 0])
        ventana.blit(imagenes.barra, [0, 440])
        if vida>=1:
            ventana.blit(imagenes.ranabarra[0], [20, 445])
        elif vida<1:
            ventana.blit(imagenes.ranabarra[1], [20, 445])
            break
        if vida>=2:
            ventana.blit(imagenes.ranabarra[0], [60, 445])
        elif vida<2:
            ventana.blit(imagenes.ranabarra[1], [60, 445])
        if vida>=3:
            ventana.blit(imagenes.ranabarra[0], [100, 445])
        elif vida<3:
            ventana.blit(imagenes.ranabarra[1], [100, 445])
        if vida>=4:
            ventana.blit(imagenes.ranabarra[0], [140, 445])
        elif vida<4:
            ventana.blit(imagenes.ranabarra[1], [140, 445])
        if vida>=5:
            ventana.blit(imagenes.ranabarra[0], [180, 445])
        elif vida<5:
            ventana.blit(imagenes.ranabarra[1], [180, 445])
        sprites.draw(ventana)
        autosde.draw(ventana)
        autosde.update()
        votesprite.draw(ventana)
        votesprite.update()
        votespritei.draw(ventana)
        votespritei.update()
        #spriteagua.draw(ventana)
        colision = pygame.sprite.spritecollide(jugador, autosde, False)
        colision2= pygame.sprite.spritecollide(jugador, spriteagua, False)
        colision3= pygame.sprite.spritecollide(jugador, votesprite, False)
        colision4= pygame.sprite.spritecollide(jugador, votespritei, False)
        llego= pygame.sprite.spritecollide(jugador, checkpoint, True)
        if colision:
            ranachoca.play()
            vida-=1
            jugador.rect.center = ( 640//2,420)
        if colision2:
            if colision3:
                jugador.mueve(0.5)
            elif colision4:
                jugador.mueve(2)
            else:
                ranagua.play()
                vida-=1
                jugador.rect.center = ( 640//2,420)
           
        if llego:
            fin.play()
            rx[ranallegar]=jugador.rect.x  
            ranallegar+=1
            jugador.rect.center = ( 640//2,420)
            
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[0],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[1],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[2],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[3],2])
        if ranallegar<=6:
            ventana.blit(ranallego, [rx[4],2])
        if ranallegar==6:
            ventana.blit(ranallego, [rx[5],2])
            break
        if colision3:
            jugador.mueve(1)
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     sprites.update(arriba,abajo,izquierda,derecha,rotacion)
                     ranasalta.play()
                 if event.key == pygame.K_UP:
                     arriba = True
                     abajo = False
                     izquierda = False
                     derecha = False
                     rotacion =0
                 if event.key == pygame.K_DOWN:
                     arriba = False
                     abajo = True
                     izquierda = False
                     derecha = False
                     rotacion = 180
                 if event.key == pygame.K_LEFT:
                     arriba = False
                     abajo = False
                     izquierda = True
                     derecha = False
                     rotacion = 90
                 if event.key == pygame.K_RIGHT:
                     arriba = False
                     abajo = False
                     izquierda = False
                     derecha = True
                     rotacion = 270
    print(ranallegar)
    pygame.mixer.music.stop()
    finJ()    
def bucleprincipal():
    pygame.mixer.music.load('Sonidos/Musica/COMP2U.OGG')
    pygame.mixer.music.play()
    while arranque:      
        menuP()
        #creo un for que escanea los eventos de la pantalla.
        pygame.display.flip()
        for event in pygame.event.get():
            # en caso de apretar en la cruz de la ventana esta se cierra y termian el proceso.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
bucleprincipal()