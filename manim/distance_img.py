from manim import *
import random as rd
import numpy as np


class BraceAnnotation(Scene):

    config.frame_size=(1350,730)
    def __init__(self,distance,deltaf):
        self.distance=distance
        self.deltaf=deltaf


    def construct(self):
        para = Text("Paramètres :",color=WHITE)
        para.to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.5).scale(0.8)

        fsamp = MathTex("f_{samp} = 15GHz",color=WHITE).to_edge(UP, buff=1.5).to_edge(LEFT, buff=1.5).scale(0.8)
        delta_f = MathTex("\Delta f_{chirp} = "+str(self.deltaf)+"MHz",color=WHITE).to_edge(UP, buff=2).to_edge(LEFT, buff=1.5).scale(0.8)
        distance = MathTex("d = "+str(self.distance)+"m",color=ORANGE).next_to(np.array([-1.5, -0.5, 0])).scale(2)
        self.add(fsamp,para,delta_f,distance)


        target = ImageMobject("../manim/bonhomme-blanc_trans")
        target.scale(0.3)
        target.to_edge(RIGHT, buff=0.5)
        target.to_edge(DOWN, buff=1)

        antenna = ImageMobject("../manim/antenne")
        antenna.scale(0.5)
        antenna.to_edge(LEFT, buff=0.5)
        antenna.to_edge(DOWN, buff=1)
        self.add(target, antenna)
        self.add(Arrow(start=np.array([-4, -2, 0]), end=np.array([3.5 , -2, 0]), color=BLUE, stroke_width=2))
        self.add(Arrow(start=np.array([3.5 , -2, 0]), end=np.array([-4, -2, 0]), color=BLUE, stroke_width=2))

        text = MathTex("PERFHYPER",color=RED).scale(1.2).to_edge(UP,buff=0.5).to_edge(RIGHT,buff=0.5)
        framebox1 = SurroundingRectangle(text, buff=.1, color=RED)
        self.add(text,framebox1)



