from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
HALF_W, HALF_H = 25, 45  # 스프라이트 안의 소년 크기 절반 (경계 판정용)

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
SPEED = 5
IDLE_FRAME_SPEED = 0.6  # IDLE일 때는 프레임을 천천히 넘김 (RUN은 1)
face = 1  # 1: 오른쪽, -1: 왼쪽 (위/아래 이동 시에는 기존 방향 유지)

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir_x > 0:
        face = 1
    elif dir_x < 0:
        face = -1

    idle = dir_x == 0 and dir_y == 0
    if idle:
        action = 3 if face == 1 else 2  # IDLE
    else:
        action = 1 if face == 1 else 0  # RUN
    character.clip_draw(int(frame) * 100, action * 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + (IDLE_FRAME_SPEED if idle else 1)) % 8
    x = clamp(HALF_W, x + dir_x * SPEED, TUK_WIDTH - HALF_W)
    y = clamp(HALF_H, y + dir_y * SPEED, TUK_HEIGHT - HALF_H)
    delay(0.05)

close_canvas()
