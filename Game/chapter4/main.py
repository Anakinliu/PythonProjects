import pygame

pygame.init()  # 返回一个元组，成功，失败

surfaceObject = pygame.display.set_mode((800, 600))
# print(type(surfaceObject))  # pygame.Surface
print(pygame.display.update())

exitGame = False
while not exitGame:
    for event in pygame.event.get():
        # print(event)
        pass


# win = pygame.display.set_mode((800, 600))
#
# pygame.display.set_caption("Game 窗口")
#
# x, y, width, height, vel = 50, 50, 10, 10, 6
# run = True
# while run:
#     pygame.time.delay(50)
#     win.fill((0, 0, 0))  # 不断填充背景
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pass
#         pass
#     pygame.draw.rect(win, (0, 255, 0),
#                      (x, y, width, height))
#     pygame.display.update()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_a]:
#         x -= vel
#         pass
#     if keys[pygame.K_d]:
#         x += vel
#         pass
#     if keys[pygame.K_w]:
#         y -= vel
#         pass
#     if keys[pygame.K_s]:
#         y += vel
#         pass
#
#     pass
#
#
# pygame.quit()