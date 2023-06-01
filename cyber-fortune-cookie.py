import pygame, os

# read the fortunes and create a set
with open("assets/fortunes.txt", "r") as input:
	data = input.read()
	fortunes = data.replace('\n', '').split(";")
	for i in fortunes:
		if len(i) == 0:
			fortunes.remove(i)
	fortunes = set(fortunes)

# define button
"""
define button method from:
https://pythonprogramming.altervista.org/buttons-in-pygame/?doing_wp_cron=1685564739.9689290523529052734375
"""
buttons = []
class Button:
	def __init__(self,text,width,height,pos,elevation,onclickFunction=None):
		#Core attributes 
		self.pressed = False
		self.onclickFunction = onclickFunction
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
 
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = button_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
 
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					# print('click')
					self.onclickFunction()
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'

# define onclick functions
def eat():
	global full
	full = False
	global fortune
	f = fortunes.pop()
	fortunes.add(f)
	fortune = fortune_font.render(f, True, 'black')
	
def buy():
	global full
	full = True
	global current_frame
	current_frame = 0
	
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
icon = pygame.image.load(os.path.join('assets', 'icon.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption('Cyber fortune cookie')
clock = pygame.time.Clock()
button_font = pygame.font.Font(None,28)
fortune_font = pygame.font.Font(None,50)

# create the buttons
eat_button = Button('Show your fortune',200,40,(540,550),5,eat)
buy_button = Button('Open another one',200,40,(540,600),5,buy)

# load the images
cookie = pygame.image.load(os.path.join('assets', 'complete-cookie.png'))
cookies = []
for i in range(4):
	cookies.append(pygame.image.load(os.path.join('assets', 'cookie'+str(i+1)+'.png')))

full = True
current_frame = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			# sys.exit()

	if full:
		screen.fill('white')
		screen.blit(cookie, (340, 50))
		eat_button.draw()
		pygame.display.flip()
	else:
		match current_frame:
			case 0:
				screen.fill('white')
				screen.blit(cookie, (340, 50))
				pygame.display.flip()
				pygame.time.delay(150)
				current_frame += 1
			case 1:
				screen.fill('white')
				screen.blit(cookies[0], (340, 50))
				pygame.display.flip()
				pygame.time.delay(300)
				current_frame += 1
			case 2:
				screen.fill('white')
				screen.blit(cookies[1], (340, 50))
				screen.blit(fortune, fortune.get_rect(center = (640, 500)))
				pygame.display.flip()
				pygame.time.delay(800)
				current_frame += 1
			case 3:
				screen.fill('white')
				screen.blit(cookies[2], (340, 50))
				screen.blit(fortune, fortune.get_rect(center = (640, 500)))
				pygame.display.flip()
				pygame.time.delay(300)
				current_frame += 1
			case 4:
				screen.fill('white')
				screen.blit(cookies[3], (340, 50))
				screen.blit(fortune, fortune.get_rect(center = (640, 500)))
				buy_button.draw()
				pygame.display.flip()
	clock.tick(60)

pygame.quit()