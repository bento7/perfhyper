from manim import *
import random as rd
import numpy as np

class BraceAnnotation(Scene):

    config.frame_size=(1920,1080)

    def construct(self):
        target = ImageMobject("manim/bonhomme-blanc_trans")
        target.scale(0.3)
        target.to_edge(RIGHT, buff=1)
        target.to_edge(DOWN, buff=1)

        antenna = ImageMobject("manim/antenne")
        antenna.scale(0.5)
        antenna.to_edge(LEFT, buff=1)
        antenna.to_edge(DOWN, buff=1)
        self.add(target, antenna)
        self.add(Arrow(start=np.array([-3.5, -2, 0]), end=np.array([3 , -2, 0]), color=BLUE, stroke_width=2))
        self.add(Arrow(start=np.array([3 , -2, 0]), end=np.array([-3.5, -2, 0]), color=BLUE, stroke_width=2))

        text = MathTex("PERFHYPER",color=RED).scale(1.1).to_edge(UP).to_edge(RIGHT)
        framebox1 = SurroundingRectangle(text, buff=.1, color=RED)
        self.add(text,framebox1)



