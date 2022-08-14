from manim import *


class Intro1(Scene):
    def construct(self):
        trig = Text("Trigonometry").scale(2.5)
        trigonometry = Text("Trigonometry", t2c={
                            "Trigono": RED, "metry": BLUE}).shift(UP)

        self.play(Write(trig))
        self.play(trig.animate.shift(UP*0.25))

        subtitle = VGroup(Text("Unit 1", color=GRAY).scale(
            0.6),  Text("INTRODUCTION", color=GRAY).scale(
            0.8)).arrange(DOWN).next_to(trig, DOWN).shift(DOWN * 0.25)

        self.play(Write(subtitle))

        self.wait(2)

        self.play(FadeOut(subtitle))

        self.play(Transform(trig, trigonometry))
        self.remove(trig)
        self.play(trigonometry.animate.shift(UP))

        measure_arrow = Arrow(
            ORIGIN, 2 * DL, color=RED).next_to(trigonometry, DOWN)
        triangle_arrow = Arrow(
            ORIGIN, 2 * DR, color=BLUE).next_to(trigonometry, DOWN)

        to_measure = Text("To measure", color=BLUE).next_to(
            measure_arrow, DL)
        to_triangle = Text("Triangles", color=RED).next_to(
            triangle_arrow, DR)

        self.play(Create(measure_arrow), Write(to_measure))
        self.play(Create(triangle_arrow), Write(to_triangle))

        self.play(FadeOut(measure_arrow, to_measure,
                  triangle_arrow, to_triangle))
        self.wait(1)

        self.play(trigonometry.animate.shift(UP).set_color(WHITE))

        triangle1 = Group(
            Line(DR*2, UL*2, color=RED),
            Line(DL*2, DR*2, color=GREEN),
            Line(DL*2, UL*2, color=BLUE)
        )
        right_angle = RightAngle(
            triangle1[1], triangle1[2], 0.5, color=WHITE)
        right_label = Text("90°").next_to(
            right_angle, UR).scale(0.5).shift(DL*0.3)

        self.play(Create(triangle1[1]), Create(triangle1[2]))
        self.play(Create(triangle1[0]))

        self.play(Create(right_angle), Write(right_label))

        self.wait(2)

        hyp = Text("hyp", color=RED).move_to(RIGHT*0.8).scale(0.5)
        adj = Text("adj", color=GREEN).move_to(DOWN*2.25).scale(0.5)
        opp = Text("opp", color=BLUE).move_to(LEFT*2.4).scale(0.5)
        theta = Angle(triangle1[0], Line(DR*2, DL*2), color=WHITE, radius=0.5)
        theta_label = Text("θ").scale(0.5).next_to(
            theta, UL).shift(DOWN*0.45)

        for i in [hyp, adj, opp]:
            self.play(Write(i))
            self.wait(0.2)
        self.wait(1)
        self.play(Write(theta), Write(theta_label))

        triangle_group = Group(triangle1, right_angle,
                               right_label, theta, theta_label, hyp, adj, opp)
        self.play(triangle_group.animate.shift(LEFT*4))

        theta_value = Text("θ = 45°").next_to(triangle_group, DOWN)
        self.play(Write(theta_value))

        self.wait(1)

        sin_label = MathTex(r"{opp", r"\over", r"hyp}", r"=").next_to(
            trigonometry, DR).shift(DOWN*0.5)
        sin_label[0].set_color(BLUE)
        sin_label[2].set_color(RED)
        sin_ratio = DecimalNumber(
            0.70, num_decimal_places=2).next_to(sin_label, RIGHT)

        sin_opp = opp.copy()
        sin_hyp = hyp.copy()
        self.play(sin_opp.animate.move_to(
            sin_label.get_top() + LEFT * 0.25))
        self.play(sin_hyp.animate.next_to(sin_opp, DOWN))

        self.play(ReplacementTransform(Group(sin_opp, sin_hyp),
                  Group(sin_label, sin_ratio)))
        self.wait(2)

        theta_box = SurroundingRectangle(theta_value, color=YELLOW)
        self.play(Create(theta_box))

        self.wait(2)

        cos_label = MathTex(r"{adj", r"\over", r"hyp}", r"=").next_to(
            sin_label, DOWN).shift(DOWN*0.5)
        cos_label[0].set_color(GREEN)
        cos_label[2].set_color(RED)
        cos_ratio = DecimalNumber(
            0.52, num_decimal_places=2).next_to(cos_label, RIGHT)

        cos_adj = adj.copy()
        cos_hyp = hyp.copy()
        self.play(cos_adj.animate.move_to(
            cos_label.get_top() + LEFT * 0.25))
        self.play(cos_hyp.animate.next_to(cos_adj, DOWN))

        self.play(ReplacementTransform(Group(cos_adj, cos_hyp),
                  Group(cos_label, cos_ratio)))
        self.wait(1)

        tan_label = MathTex(r"{opp", r"\over", r"adj}", r"=").next_to(
            cos_label, DOWN).shift(DOWN*0.5)
        tan_label[0].set_color(BLUE)
        tan_label[2].set_color(GREEN)
        tan_ratio = DecimalNumber(
            1, num_decimal_places=2).next_to(tan_label, RIGHT)

        tan_opp = opp.copy()
        tan_adj = adj.copy()
        self.play(tan_opp.animate.move_to(
            tan_label.get_top() + LEFT * 0.25))
        self.play(tan_adj.animate.next_to(tan_opp, DOWN))

        self.play(ReplacementTransform(Group(tan_opp, tan_adj),
                                       Group(tan_label, tan_ratio)))
        self.wait(1)

        sin_name_label = MathTex(
            r"\sin(\theta)", r"=").next_to(sin_label, LEFT)
        cos_name_label = MathTex(
            r"\cos(\theta)", r"=").next_to(cos_label, LEFT)
        tan_name_label = MathTex(
            r"\tan(\theta)", r"=").next_to(tan_label, LEFT)
        for i in [sin_name_label, cos_name_label, tan_name_label]:
            self.play(Write(i))
            self.wait(0.2)

        for i in [sin_name_label[0], cos_name_label[0], tan_name_label[0]]:
            self.play(ScaleInPlace(i, 1.5))
            self.wait(0.1)
            self.play(ScaleInPlace(i, 1/1.5))
            self.wait(0.25)

        self.wait(2)
