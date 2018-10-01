
import pygame


class Player:

    def __init__ (self,x,y):

        self.x = x
        self.y = y

 

class Our_player(Player):

    def __init__ (self):

        self.x = 50
        self.y = 100
        self.image = pygame.image.load('images/our_player.png').convert_alpha()

class Enemy_player(Player):

    def __init__ (self):

        self.x = 50
        self.y = 200
        self.image = pygame.image.load('images/enemy_player2.png').convert_alpha()


class Finish_line():
    def __init__(self):

        self.x = 900
        self.y = 75
        self.image = pygame.image.load('images/finish_line.png').convert_alpha() 

class Key_to_press:

    def __init__ (self):

        self.x = 500
        self.y = 10
        self.key = ['a','a','a','s','d','d','s','d','f','g','k','k','g','g','d','d','a','a','g','f','d','s','a',
        'a','a','a','s','d','d','s','d','f','g','k','k','g','g','d','d','a','a','g','f','d','s','a',
        'a','a','a','s','d','d','s','d','f','g','k','k','g','g','d','d','a','a','g','f','d','s','a']








def main():

    width = 1000
    height = 300
    color = (157,232,159)

    pygame.mixer.init()
    sound_a = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68437__pinkyfinger__piano-a.wav')
    sound_b = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68438__pinkyfinger__piano-b.wav')
    sound_bb = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68439__pinkyfinger__piano-bb.wav')
    sound_c = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68440__pinkyfinger__piano-c.wav')
    sound_csharp = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68441__pinkyfinger__piano-c.wav')
    sound_d = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68442__pinkyfinger__piano-d.wav')
    sound_e = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68443__pinkyfinger__piano-e.wav')
    sound_eb = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68444__pinkyfinger__piano-eb.wav')
    sound_f = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68445__pinkyfinger__piano-f.wav')
    sound_fsharp = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68446__pinkyfinger__piano-f.wav')
    sound_g = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68447__pinkyfinger__piano-g.wav')
    sound_gsharp = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/68448__pinkyfinger__piano-g.wav')
    error = pygame.mixer.Sound('4409__pinkyfinger__piano-notes-1-octave/error.wav')

    sounds = [sound_c,sound_c,sound_f,sound_f,sound_f,sound_f,sound_f,sound_e,sound_f,sound_g,
    sound_c,sound_c,sound_f,sound_f,sound_f,sound_f,sound_f,sound_e,sound_f,sound_g,sound_c,sound_c,sound_f,sound_f,sound_f,sound_f,sound_f,sound_e,sound_f,sound_g,
    sound_c,sound_c,sound_f,sound_f,sound_f,sound_f,sound_f,sound_e,sound_f,sound_g,sound_c,sound_c,sound_f,sound_f,sound_f,sound_f,sound_f,sound_e,sound_f,sound_g,
    sound_c,sound_c,sound_f,sound_f,sound_f,sound_f,sound_f,sound_e,sound_f,sound_g]

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Racing Game')
    clock = pygame.time.Clock()
    counter = 0
    us = Our_player()
    enemy = Enemy_player()
    finish = Finish_line()
    finish.image = pygame.transform.scale (finish.image, (200,50))
    finish.image = pygame.transform.rotate (finish.image, 90)
    
    font = pygame.font.SysFont('monospace',50)
    key = Key_to_press()

    game_over = "GAME OVER!"

    
    
    
    
    our_song = [pygame.K_a,pygame.K_a,pygame.K_a,pygame.K_s,pygame.K_d,
    pygame.K_d,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g,
    pygame.K_k,pygame.K_k,pygame.K_g,pygame.K_g,pygame.K_d,pygame.K_d,pygame.K_a,pygame.K_a,
    pygame.K_g,pygame.K_f,pygame.K_d,pygame.K_s,pygame.K_a,pygame.K_a,pygame.K_a,pygame.K_a,pygame.K_s,pygame.K_d,
    pygame.K_d,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g,
    pygame.K_k,pygame.K_k,pygame.K_g,pygame.K_g,pygame.K_d,pygame.K_d,pygame.K_a,pygame.K_a,
    pygame.K_g,pygame.K_f,pygame.K_d,pygame.K_s,pygame.K_a,pygame.K_a,pygame.K_a,pygame.K_a,pygame.K_s,pygame.K_d,
    pygame.K_d,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g,
    pygame.K_k,pygame.K_k,pygame.K_g,pygame.K_g,pygame.K_d,pygame.K_d,pygame.K_a,pygame.K_a,
    pygame.K_g,pygame.K_f,pygame.K_d,pygame.K_s,pygame.K_a]
    
    stop_game = False
    while not stop_game:
        enemy.x += 1
        for event in pygame.event.get():

        
            if event.type == pygame.KEYDOWN:
            
            
            
                    if event.key == our_song[counter]:
                        us.x += 30
                        sounds[counter].play()
                        print (event.key,our_song[counter])
                        
                        counter += 1

                        break
                    else:
                        us.x -= 10    
                        error.play()
                        print (event.key,our_song[counter])
                        break

         

            # Event handling



            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(color)

        # Game display
        screen.blit(finish.image,(finish.x,finish.y))

        us.image = pygame.transform.scale (us.image, (72,36))
        screen.blit(us.image,(us.x,us.y))
    
        enemy.image = pygame.transform.scale (enemy.image, (72,36))
        screen.blit(enemy.image,(enemy.x,enemy.y))


        key_display = font.render(key.key[counter],1,(0,0,0))
        screen.blit(key_display,(key.x,key.y))
        if us.x and enemy.x > 900:
            end_game = font.render(game_over,1,(0,0,0))
            screen.blit(end_game,(10,10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
