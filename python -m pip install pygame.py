
import pygame
import random
import math
import sys

pygame.init()

# CONFIGURACION
ANCHO, ALTO = 1000, 650
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("NEON APOCALYPSE")
reloj = pygame.time.Clock()

NEGRO = (5, 7, 20)
CYAN = (0, 240, 255)
ROSA = (255, 35, 150)
MORADO = (150, 60, 255)
BLANCO = (255, 255, 255)
AMARILLO = (255, 220, 50)
ROJO = (255, 50, 65)
VERDE = (50, 255, 130)

fuente = pygame.font.SysFont("consolas", 22, bold=True)
titulo = pygame.font.SysFont("consolas", 48, bold=True)
pequena = pygame.font.SysFont("consolas", 16)

# ESTRELLAS
estrellas = [
    [random.randrange(ANCHO), random.randrange(ALTO),
     random.choice([1, 2, 3])]
    for _ in range(110)
]


def texto(mensaje, x, y, color=BLANCO, font=fuente, centro=False):
    imagen = font.render(mensaje, True, color)
    rect = imagen.get_rect()
    if centro:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    pantalla.blit(imagen, rect)


def distancia(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def particulas(lista, x, y, color, cantidad=15):
    for _ in range(cantidad):
        angulo = random.random() * math.tau
        velocidad = random.uniform(60, 260)
        lista.append([
            x, y,
            math.cos(angulo) * velocidad,
            math.sin(angulo) * velocidad,
            random.uniform(0.2, 0.7),
            color
        ])


def nuevo_juego():
    return {
        "x": ANCHO / 2,
        "y": ALTO / 2,
        "vida": 100,
        "energia": 100,
        "puntos": 0,
        "monedas": 0,
        "oleada": 1,
        "bajas": 0,
        "enemigos": [],
        "balas": [],
        "balas_enemigas": [],
        "particulas": [],
        "tiempo": 0,
        "aparicion": 0,
        "disparo": 0,
        "invulnerable": 0,
        "estado": "menu",
        "jefe_creado": False,
        "jefe_derrotado": False,
        "mensaje": 0,
    }


juego = nuevo_juego()


def crear_enemigo(jefe=False):
    lado = random.randrange(4)

    if lado == 0:
        x, y = random.randrange(ANCHO), -30
    elif lado == 1:
        x, y = ANCHO + 30, random.randrange(ALTO)
    elif lado == 2:
        x, y = random.randrange(ANCHO), ALTO + 30
    else:
        x, y = -30, random.randrange(ALTO)

    nivel = juego["oleada"]

    if jefe:
        radio = 38
        vida = 35 + nivel * 5
        velocidad = 65
        color = MORADO
    else:
        radio = random.randint(12, 18)
        vida = 1 + nivel // 4
        velocidad = random.randint(75, 110) + nivel * 3
        color = random.choice([ROSA, ROJO, MORADO])

    juego["enemigos"].append({
        "x": float(x),
        "y": float(y),
        "vida": vida,
        "vida_max": vida,
        "radio": radio,
        "velocidad": velocidad,
        "color": color,
        "jefe": jefe,
        "disparo": 1.5
    })


def eliminar_enemigo(enemigo):
    if enemigo not in juego["enemigos"]:
        return

    juego["enemigos"].remove(enemigo)
    juego["puntos"] += 1000 if enemigo["jefe"] else 100
    juego["monedas"] += 10 if enemigo["jefe"] else 2
    juego["bajas"] += 1

    particulas(
        juego["particulas"],
        enemigo["x"], enemigo["y"],
        enemigo["color"], 35 if enemigo["jefe"] else 14
    )

    if enemigo["jefe"]:
        juego["jefe_derrotado"] = True
        juego["vida"] = min(100, juego["vida"] + 30)
        juego["energia"] = 100
        juego["mensaje"] = 3


def pulso():
    if juego["energia"] < 35:
        return

    juego["energia"] -= 35
    x, y = juego["x"], juego["y"]

    particulas(juego["particulas"], x, y, CYAN, 55)

    for enemigo in juego["enemigos"][:]:
        d = distancia(x, y, enemigo["x"], enemigo["y"])

        if d < 200:
            enemigo["vida"] -= 5 if enemigo["jefe"] else 3
            particulas(
                juego["particulas"],
                enemigo["x"], enemigo["y"], CYAN, 8
            )

            if enemigo["vida"] <= 0:
                eliminar_enemigo(enemigo)


def disparar():
    mx, my = pygame.mouse.get_pos()
    dx = mx - juego["x"]
    dy = my - juego["y"]
    d = max(1, math.hypot(dx, dy))

    juego["balas"].append({
        "x": juego["x"],
        "y": juego["y"],
        "vx": dx / d * 620,
        "vy": dy / d * 620,
        "vida": 1.5
    })


def reiniciar():
    global juego
    juego = nuevo_juego()
    juego["estado"] = "jugando"


ejecutando = True

while ejecutando:
    dt = min(reloj.tick(60) / 1000, 0.035)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

            if evento.key == pygame.K_RETURN:
                if juego["estado"] in ("menu", "derrota", "victoria"):
                    reiniciar()

            if evento.key == pygame.K_p:
                if juego["estado"] == "jugando":
                    juego["estado"] = "pausa"
                elif juego["estado"] == "pausa":
                    juego["estado"] = "jugando"

            if evento.key == pygame.K_SPACE:
                if juego["estado"] == "jugando":
                    pulso()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and juego["estado"] == "jugando":
                if juego["disparo"] <= 0:
                    disparar()
                    juego["disparo"] = 0.14

    teclas = pygame.key.get_pressed()

    # ACTUALIZAR JUEGO
    if juego["estado"] == "jugando":
        j = juego

        dx = (
            int(teclas[pygame.K_d] or teclas[pygame.K_RIGHT])
            - int(teclas[pygame.K_a] or teclas[pygame.K_LEFT])
        )
        dy = (
            int(teclas[pygame.K_s] or teclas[pygame.K_DOWN])
            - int(teclas[pygame.K_w] or teclas[pygame.K_UP])
        )

        longitud = math.hypot(dx, dy)
        if longitud:
            dx /= longitud
            dy /= longitud

        j["x"] = max(15, min(ANCHO - 15, j["x"] + dx * 285 * dt))
        j["y"] = max(15, min(ALTO - 15, j["y"] + dy * 285 * dt))

        j["tiempo"] += dt
        j["aparicion"] -= dt
        j["disparo"] -= dt
        j["energia"] = min(100, j["energia"] + 7 * dt)
        j["invulnerable"] = max(0, j["invulnerable"] - dt)
        j["mensaje"] = max(0, j["mensaje"] - dt)

        nueva_oleada = 1 + int(j["tiempo"] // 15)

        if nueva_oleada > j["oleada"]:
            j["oleada"] = nueva_oleada
            j["mensaje"] = 2

        # JEFE CADA CINCO OLEADAS
        hay_jefe = any(e["jefe"] for e in j["enemigos"])

        if j["oleada"] % 5 == 0 and j["oleada"] >= 5:
            if not hay_jefe and not j["jefe_creado"]:
                crear_enemigo(True)
                j["jefe_creado"] = True
                j["mensaje"] = 3

        if j["oleada"] % 5 != 0:
            j["jefe_creado"] = False

        if j["aparicion"] <= 0:
            j["aparicion"] = max(0.25, 0.9 - j["oleada"] * 0.04)

            if len(j["enemigos"]) < 8 + j["oleada"]:
                crear_enemigo()

        # ENEMIGOS
        for e in j["enemigos"][:]:
            dx = j["x"] - e["x"]
            dy = j["y"] - e["y"]
            d = max(1, math.hypot(dx, dy))

            e["x"] += dx / d * e["velocidad"] * dt
            e["y"] += dy / d * e["velocidad"] * dt

            if distancia(j["x"], j["y"], e["x"], e["y"]) < e["radio"] + 14:
                if j["invulnerable"] <= 0:
                    j["vida"] -= 12 if e["jefe"] else 18
                    j["invulnerable"] = 0.55
                    particulas(j["particulas"], j["x"], j["y"], ROJO, 12)

                if not e["jefe"]:
                    eliminar_enemigo(e)

        # BALAS DEL JUGADOR
        for b in j["balas"][:]:
            b["x"] += b["vx"] * dt
            b["y"] += b["vy"] * dt
            b["vida"] -= dt

            if (
                b["vida"] <= 0
                or b["x"] < -20 or b["x"] > ANCHO + 20
                or b["y"] < -20 or b["y"] > ALTO + 20
            ):
                j["balas"].remove(b)
                continue

            for e in j["enemigos"][:]:
                if distancia(b["x"], b["y"], e["x"], e["y"]) < e["radio"] + 5:
                    e["vida"] -= 1

                    if b in j["balas"]:
                        j["balas"].remove(b)

                    particulas(j["particulas"], b["x"], b["y"], CYAN, 4)

                    if e["vida"] <= 0:
                        eliminar_enemigo(e)
                    break

        # DISPAROS DEL JEFE
        for e in j["enemigos"]:
            if e["jefe"]:
                e["disparo"] -= dt

                if e["disparo"] <= 0:
                    e["disparo"] = 1.15

                    for i in range(12):
                        angulo = math.tau * i / 12
                        j["balas_enemigas"].append({
                            "x": e["x"],
                            "y": e["y"],
                            "vx": math.cos(angulo) * 190,
                            "vy": math.sin(angulo) * 190,
                            "vida": 4
                        })

        # BALAS ENEMIGAS
        for b in j["balas_enemigas"][:]:
            b["x"] += b["vx"] * dt
            b["y"] += b["vy"] * dt
            b["vida"] -= dt

            if b["vida"] <= 0:
                j["balas_enemigas"].remove(b)
                continue

            if distancia(b["x"], b["y"], j["x"], j["y"]) < 19:
                if j["invulnerable"] <= 0:
                    j["vida"] -= 10
                    j["invulnerable"] = 0.5

                j["balas_enemigas"].remove(b)

        if j["vida"] <= 0:
            j["vida"] = 0
            j["estado"] = "derrota"

        if j["oleada"] >= 10 and j["jefe_derrotado"]:
            j["estado"] = "victoria"

    # PARTICULAS
    for p in juego["particulas"][:]:
        p[0] += p[2] * dt
        p[1] += p[3] * dt
        p[4] -= dt

        if p[4] <= 0:
            juego["particulas"].remove(p)

    # FONDO NEON
    pantalla.fill(NEGRO)

    for x in range(0, ANCHO, 40):
        pygame.draw.line(pantalla, (15, 25, 48), (x, 0), (x, ALTO))

    for y in range(0, ALTO, 40):
        pygame.draw.line(pantalla, (15, 25, 48), (0, y), (ANCHO, y))

    for estrella in estrellas:
        pygame.draw.circle(
            pantalla, (45, 75, 110),
            (estrella[0], estrella[1]), estrella[2]
        )

    # DIBUJAR PARTICULAS
    for p in juego["particulas"]:
        pygame.draw.circle(
            pantalla, p[5],
            (int(p[0]), int(p[1])),
            max(1, int(p[4] * 5))
        )

    # DIBUJAR BALAS
    for b in juego["balas"]:
        pygame.draw.circle(pantalla, CYAN, (int(b["x"]), int(b["y"])), 5)
        pygame.draw.circle(pantalla, BLANCO, (int(b["x"]), int(b["y"])), 2)

    for b in juego["balas_enemigas"]:
        pygame.draw.circle(pantalla, ROSA, (int(b["x"]), int(b["y"])), 7)
        pygame.draw.circle(pantalla, BLANCO, (int(b["x"]), int(b["y"])), 3)

    # DIBUJAR ENEMIGOS
    for e in juego["enemigos"]:
        x, y = int(e["x"]), int(e["y"])
        r = e["radio"]

        pygame.draw.circle(pantalla, e["color"], (x, y), r, 3)
        pygame.draw.circle(pantalla, e["color"], (x, y), max(3, r // 4))

        if e["jefe"]:
            pygame.draw.circle(pantalla, ROSA, (x, y), r + 7, 2)
            pygame.draw.rect(pantalla, ROJO, (x - 45, y - r - 14, 90, 7))
            ancho_vida = max(0, 90 * e["vida"] / e["vida_max"])
            pygame.draw.rect(
                pantalla, VERDE,
                (x - 45, y - r - 14, ancho_vida, 7)
            )

    # DIBUJAR JUGADOR
    if juego["estado"] != "menu":
        x, y = int(juego["x"]), int(juego["y"])
        mx, my = pygame.mouse.get_pos()
        angulo = math.atan2(my - y, mx - x)

        punta = (x + math.cos(angulo) * 25, y + math.sin(angulo) * 25)
        izquierda = (
            x + math.cos(angulo + 2.5) * 17,
            y + math.sin(angulo + 2.5) * 17
        )
        derecha = (
            x + math.cos(angulo - 2.5) * 17,
            y + math.sin(angulo - 2.5) * 17
        )

        if juego["invulnerable"] > 0:
            pygame.draw.circle(pantalla, BLANCO, (x, y), 25, 2)

        pygame.draw.polygon(pantalla, CYAN, [punta, izquierda, derecha])
        pygame.draw.polygon(pantalla, BLANCO, [punta, izquierda, derecha], 2)
        pygame.draw.circle(pantalla, BLANCO, (x, y), 4)

    # INTERFAZ
    if juego["estado"] != "menu":
        pygame.draw.rect(pantalla, (20, 25, 45), (20, 20, 260, 18))
        pygame.draw.rect(
            pantalla, VERDE if juego["vida"] > 30 else ROJO,
            (20, 20, 260 * juego["vida"] / 100, 18)
        )
        texto(f"VIDA: {int(juego['vida'])}", 22, 43, BLANCO, pequena)

        pygame.draw.rect(pantalla, (20, 25, 45), (20, 70, 260, 12))
        pygame.draw.rect(
            pantalla, MORADO,
            (20, 70, 260 * juego["energia"] / 100, 12)
        )
        texto("ENERGIA", 20, 88, CYAN, pequena)

        texto(f"OLEADA: {juego['oleada']}", ANCHO - 220, 20, CYAN)
        texto(f"PUNTOS: {juego['puntos']}", ANCHO - 220, 50, AMARILLO)
        texto(f"MONEDAS: {juego['monedas']}", ANCHO - 220, 80, ROSA)

        texto(
            "WASD MOVER | CLICK DISPARAR | ESPACIO PODER | P PAUSA",
            ANCHO // 2, ALTO - 20, BLANCO, pequena, True
        )

    # MENUS
    if juego["estado"] == "menu":
        texto("NEON APOCALYPSE", ANCHO // 2, 190, CYAN, titulo, True)
        texto("ULTIMO SOBREVIVIENTE", ANCHO // 2, 250, ROSA, fuente, True)
        texto("Sobrevive a las oleadas. Derrota al jefe.", ANCHO // 2, 315, BLANCO, fuente, True)
        texto("WASD = MOVER   |   MOUSE = DISPARAR", ANCHO // 2, 375, CYAN, pequena, True)
        texto("ESPACIO = PULSO DE ENERGIA", ANCHO // 2, 405, MORADO, pequena, True)
        texto("PRESIONA ENTER PARA COMENZAR", ANCHO // 2, 475, AMARILLO, fuente, True)

    elif juego["estado"] == "pausa":
        texto("PAUSA", ANCHO // 2, ALTO // 2, CYAN, titulo, True)
        texto("Presiona P para continuar", ANCHO // 2, ALTO // 2 + 60, BLANCO, fuente, True)

    elif juego["estado"] == "derrota":
        texto("GAME OVER", ANCHO // 2, 230, ROJO, titulo, True)
        texto(f"PUNTUACION FINAL: {juego['puntos']}", ANCHO // 2, 310, BLANCO, fuente, True)
        texto(f"OLEADA: {juego['oleada']} | BAJAS: {juego['bajas']}", ANCHO // 2, 355, ROSA, fuente, True)
        texto("ENTER = VOLVER A JUGAR", ANCHO // 2, 430, AMARILLO, fuente, True)

    elif juego["estado"] == "victoria":
        texto("¡ERES UNA LEYENDA!", ANCHO // 2, 230, CYAN, titulo, True)
        texto(f"PUNTUACION: {juego['puntos']}", ANCHO // 2, 310, AMARILLO, fuente, True)
        texto("¡SALVASTE LA CIUDAD!", ANCHO // 2, 370, BLANCO, fuente, True)
        texto("ENTER = JUGAR OTRA VEZ", ANCHO // 2, 440, ROSA, fuente, True)

    if juego["mensaje"] > 0 and juego["estado"] == "jugando":
        texto(
            "¡JEFE ELIMINADO!" if juego["jefe_derrotado"] else f"¡OLEADA {juego['oleada']}!",
            ANCHO // 2, ALTO // 2 - 100, AMARILLO, titulo, True
        )

    pygame.display.flip()

pygame.quit()
sys.exit()