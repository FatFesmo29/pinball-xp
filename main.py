#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Точка входа в игру Pinball XP
"""

import pygame
from game import Game  # ← теперь импорт через пакет game

def main():
    pygame.init()
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"[Ошибка] {e}", file=sys.stderr)
        raise
    finally:
        pygame.quit()

if __name__ == "__main__":
    import sys
    main()