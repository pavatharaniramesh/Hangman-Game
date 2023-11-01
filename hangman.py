import pygame
import random

pygame.init()

window_width = 1000
window_height = 500
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hangman Game")

word_list = ["PYTHON", "HELLO", "CODING", "GAMING", "GUESS","DEVELOP","BESANT","LAPTOP","STUDENT","GUIDE","PEOPLE"]
word = random.choice(word_list)
guessed_letters = set()

hangman_images = [pygame.image.load("img0.png"), pygame.image.load("img1.png"),
                  pygame.image.load("img2.png"), pygame.image.load("img3.png"),
                  pygame.image.load("img4.png"), pygame.image.load("img5.png"),
                  pygame.image.load("img6.png"), pygame.image.load("img7.png"),
                  pygame.image.load("img8.png"), pygame.image.load("img9.png"),
                  pygame.image.load("img10.png")]

hangman_x = 0  
hangman_y = 0
hangman_index = 0

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)  # Smaller font for guessed letters

def is_word_guessed():
    return all(letter in guessed_letters for letter in word)

game_over = False

def quit_game():
    pygame.quit()
    exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key in range(97, 123): 
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter not in word:
                            hangman_index += 1

            if hangman_index < len(hangman_images):
                win.blit(hangman_images[hangman_index], (hangman_x, hangman_y))

            display_word = ""
            for letter in word:
                if letter in guessed_letters:
                    display_word += letter
                else:
                    display_word += " _ "
            word_text = font.render(display_word, True, (0, 255, 0))
            win.blit(word_text, (hangman_x + 500, 150))  

            if is_word_guessed():
                win_text = font.render("You win! The word was: " + word, True, (255, 0, 0))
                win.blit(win_text, (hangman_x + 500, 350))  
                game_over = True  

            if hangman_index == len(hangman_images):
                lose_text = font.render("Game Over! The word was: " + word, True, (255, 0, 0))
                win.blit(lose_text, (hangman_x + 500, 350)) 
                game_over = True  

            guessed_x = hangman_x + 500
            guessed_y = 250 
            for letter in guessed_letters:
                letter_text = small_font.render(letter, True, (0, 0, 255))
                win.blit(letter_text, (guessed_x, guessed_y))
                guessed_x += letter_text.get_width() + 10 

        pygame.display.update()

    if game_over:
        restart_text = font.render("Press R to Restart (or) Q to Quit", True, (0, 0, 255))
        win.blit(restart_text, (hangman_x + 500, 450)) 
        pygame.display.update()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            word = random.choice(word_list)  
            guessed_letters = set()
            hangman_index = 0
            game_over = False

        if keys[pygame.K_q]:
            quit_game()

pygame.quit()
