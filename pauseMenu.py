
import pygame, main
pygame.init()
def p():
    WIDTH=1280
    HEIGHT=720
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    bg = pygame.image.load('bg2.jpg')
    bg_scaled=pygame.transform.scale(bg,(1280,720))
    pygame.display.set_caption("Pause Menu")
    hImg = pygame.image.load(main.hero.imageSource)
    player_stats = {'lvl':main.hero.level,'hp': main.hero.hp, 'atk': main.hero.atk, 'def': main.hero.dfs, 'spd': main.hero.spd}
    move_stats_1= {'bp':main.hero.move1bp,'acc': main.hero.move1acc, 'pp': main.hero.move1pp, 'pri': main.hero.move1priority}
    move_stats_2= {'bp':main.hero.move2bp,'acc': main.hero.move2acc, 'pp': main.hero.move2pp, 'pri': main.hero.move2priority}
    move_stats_3= {'bp':main.hero.move3bp,'acc': main.hero.move3acc, 'pp': main.hero.move3pp, 'pri': main.hero.move3priority}
    move_stats_4= {'bp':main.hero.move4bp,'acc': main.hero.move4acc, 'pp': main.hero.move4pp, 'pri': main.hero.move4priority}

    heroImg = pygame.transform.scale(hImg,(320, 440))

    def pause():
        screen.blit(bg_scaled,(0,0))
        if move1==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_1, m_render_rect_1)
        
        if move2==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_2, m_render_rect_2)
        
        if move3==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_3, m_render_rect_3)
        
        if move4==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_4, m_render_rect_4)

        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',30)
        continue_t=f.render('Continue', True, (0,0,0))
        quit_t=f.render('Quit',True,(0,0,0))
        move_box=pygame.Rect(WIDTH/2+100, HEIGHT/2-230, 400, 340)
        pygame.draw.rect(screen, (255, 255, 255), move_box)
        pygame.draw.rect(screen, (0, 0, 0), move_box, 2)
        c_box=pygame.Rect(WIDTH/2-360, HEIGHT*8.5/10, 120, 70)
        pygame.draw.rect(screen, (255, 255, 255), c_box)
        pygame.draw.rect(screen, (0, 0, 0), c_box, 2)

        q_box=pygame.Rect(WIDTH/2+240, HEIGHT*8.5/10, 120, 70)
        pygame.draw.rect(screen, (255, 255, 255), q_box)
        pygame.draw.rect(screen, (0, 0, 0), q_box, 2)
        move_1=f.render(main.hero.move1name, True,(0,0,0))
        move_2=f.render(main.hero.move2name, True,(0,0,0))
        move_3=f.render(main.hero.move3name, True,(0,0,0))
        move_4=f.render(main.hero.move4name, True,(0,0,0))
        h_r=heroImg.get_rect(center=(WIDTH/2-300,HEIGHT/2-50))
        move_1_r=move_1.get_rect(center=(WIDTH/2+300,HEIGHT/2-150))
        move_2_r=move_2.get_rect(center=(WIDTH/2+300,HEIGHT/2-75))
        move_3_r=move_3.get_rect(center=(WIDTH/2+300,HEIGHT/2-0))
        move_4_r=move_4.get_rect(center=(WIDTH/2+300,HEIGHT/2+75))

        continue_r= continue_t.get_rect(center=(WIDTH/2-300,HEIGHT*9/10))
        quit_r= quit_t.get_rect(center=(WIDTH/2+300,HEIGHT*9/10))

        pygame.draw.rect(screen,(0,0,0), continue_r,2)

        pygame.draw.rect(screen,(0,0,0), (WIDTH,HEIGHT,150,150))
        dim=pygame.Surface(screen.get_size())
        dim.set_alpha(64)
        dim.fill((255,255,255))
        screen.blit(dim,(0,0))
        pygame.draw.rect(screen,(0,0,0), continue_r,2)
        pygame.draw.rect(screen,(0,0,0), quit_r,2)
        pygame.draw.rect(screen,(0,0,0), move_1_r,2)
        pygame.draw.rect(screen,(0,0,0), move_2_r,2)
        pygame.draw.rect(screen,(0,0,0), move_3_r,2)
        pygame.draw.rect(screen,(0,0,0), move_4_r,2)
        pygame.draw.rect(screen,(0,0,0), h_r)

        screen.blit(heroImg,h_r)
        screen.blit(continue_t,continue_r)
        screen.blit(quit_t,quit_r)
        screen.blit(move_1,move_1_r)
        screen.blit(move_2,move_2_r)
        screen.blit(move_3,move_3_r)
        screen.blit(move_4,move_4_r)
        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',20)
        lvl_box = pygame.Rect(WIDTH/2-460, HEIGHT/2-340, 320, 70)
        pygame.draw.rect(screen, (255, 255, 255), lvl_box)
        pygame.draw.rect(screen, (0, 0, 0), lvl_box, 2)
        name= f.render(main.hero.fighterName, True,(0,0,0))
        name_r=name.get_rect(center=(WIDTH/2-330,HEIGHT/2-325))
        stat_box = pygame.Rect(WIDTH/2-460, HEIGHT/2+160, 320, 50)
        pygame.draw.rect(screen, (255, 255, 255), stat_box)
        pygame.draw.rect(screen, (0, 0, 0), stat_box, 2)
        lvl_text = f"LVL: {player_stats['lvl']}"
        lvl_render = f.render(lvl_text, True, (0, 0, 0))


        lvl_render_rect = lvl_render.get_rect(center=(WIDTH/2-330,HEIGHT/2-285))
        screen.blit(lvl_render, lvl_render_rect)
        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',20)

        stat_text = f"HP: {player_stats['hp']}  ATK: {player_stats['atk']}"
        stat_text_2=f"DEF: {player_stats['def']}  SPD: {player_stats['spd']}"
        stat_render = f.render(stat_text, True, (0, 0, 0))
        stat_render_rect = stat_render.get_rect(center=(WIDTH/2-350,HEIGHT/2+174))
        screen.blit(stat_render, stat_render_rect)

        stat_render_2 = f.render(stat_text_2, True, (0, 0, 0))
        stat_render_rect_2 = stat_render_2.get_rect(center=(WIDTH/2-350,HEIGHT/2+194))
        screen.blit(stat_render_2, stat_render_rect_2)
        screen.blit(name, name_r)

        pygame.display.update()

    running = True
    paused = True
    move1=False
    move2=False
    move3=False
    move4=False
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if paused:
                        f=pygame.font.Font(None,50)
                        continue_t=f.render('Continue', True, (0,0,0),2)
                        quit_t=f.render('Quit',True,(0,0,0),2)
                        continue_r= continue_t.get_rect(center=(WIDTH/2-300,HEIGHT*9/10))
                        quit_r= quit_t.get_rect(center=(WIDTH/2+300,HEIGHT*9/10))
                        move_1=f.render(main.hero.move1name, True,(0,0,0),2)
                        move_2=f.render(main.hero.move2name, True,(0,0,0),2)
                        move_3=f.render(main.hero.move3name, True,(0,0,0),2)
                        move_4=f.render(main.hero.move4name, True,(0,0,0),2)
                        move_1_r=move_1.get_rect(center=(WIDTH/2+300,HEIGHT/2-150))
                        move_2_r=move_2.get_rect(center=(WIDTH/2+300,HEIGHT/2-75))
                        move_3_r=move_3.get_rect(center=(WIDTH/2+300,HEIGHT/2-0))
                        move_4_r=move_4.get_rect(center=(WIDTH/2+300,HEIGHT/2+75))
                        

                        m_stats_1 = f"Base Power: {move_stats_1['bp']}  Accuracy: {move_stats_1['acc']} Power Points: {move_stats_1['pp']} Priority: {move_stats_1['pri']}"
                        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',20)
                        m_render_1 = f.render(m_stats_1, True, (0, 0, 0))
                        m_render_rect_1 = m_render_1.get_rect(center=(WIDTH/2+300,HEIGHT/2+210))

                        m_stats_2 = f"Base Power: {move_stats_2['bp']}  Accuracy: {move_stats_2['acc']} Power Points: {move_stats_2['pp']} Priority: {move_stats_2['pri']}"
                        m_render_2 = f.render(m_stats_2, True, (0, 0, 0))
                        m_render_rect_2 = m_render_2.get_rect(center=(WIDTH/2+300,HEIGHT/2+210))

                        m_stats_3 = f"Base Power: {move_stats_3['bp']}  Accuracy: {move_stats_3['acc']} Power Points: {move_stats_3['pp']} Priority: {move_stats_3['pri']}"
                        m_render_3 = f.render(m_stats_3, True, (0, 0, 0))
                        m_render_rect_3 = m_render_3.get_rect(center=(WIDTH/2+300,HEIGHT/2+210))

                        m_stats_4 = f"Base Power: {move_stats_4['bp']}  Accuracy: {move_stats_4['acc']} Power Points: {move_stats_4['pp']} Priority: {move_stats_4['pri']}"
                        m_render_4 = f.render(m_stats_4, True, (0, 0, 0))
                        m_render_rect_4 = m_render_4.get_rect(center=(WIDTH/2+300,HEIGHT/2+210))


                        mouse_pos = pygame.mouse.get_pos()
                        if continue_r.collidepoint(mouse_pos):
                            paused = False
                            return False
                        elif quit_r.collidepoint(mouse_pos):
                            paused=False
                            return True
                        elif move_1_r.collidepoint(mouse_pos):
                            move1=True
                            move2=False
                            move3=False
                            move4=False
                        elif move_2_r.collidepoint(mouse_pos):
                            move1=False
                            move2=True
                            move3=False
                            move4=False
                        elif move_3_r.collidepoint(mouse_pos):
                            move1=False
                            move2=False
                            move3=True
                            move4=False
                        elif move_4_r.collidepoint(mouse_pos):
                            move1=False
                            move2=False
                            move3=False
                            move4=True            

        if move1==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_1, m_render_rect_1)
        
        if move2==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_2, m_render_rect_2)
        
        if move3==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_3, m_render_rect_3)
        
        if move4==True:
            descBox = pygame.Rect(WIDTH/2, HEIGHT/2+195, 600, 60)
            pygame.draw.rect(screen, (255, 255, 255), descBox)
            pygame.draw.rect(screen, (0, 0, 0), descBox, 2)
            screen.blit(m_render_4, m_render_rect_4)
        
        if paused==True:
            pause()

            
            
        pygame.display.flip()    
    pygame.quit()