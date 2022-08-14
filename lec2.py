from manim import *


class Vid2Intro(Scene):
    def construct(self):
        trig = Text("Trigonometry").scale(2.5)
        subtitle = VGroup(Text("Unit 2", color=GRAY).scale(
            0.6),  Text("Trigonometric Functions", color=GRAY).scale(
            0.8)).arrange(DOWN).next_to(trig, DOWN).shift(DOWN * 0.25)
        self.play(Write(trig))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(trig), FadeOut(subtitle))
        self.wait(2)
        video_box = Rectangle(height=4.5, width=8,
                              color=BLUE)
        last_video = Text("Last Video").scale(0.8).next_to(video_box, UP)
        self.play(Write(last_video), Create(video_box))
        self.wait(2)

        self.play(FadeOut(last_video), FadeOut(video_box))


class Vid2Functions(Scene):
    def construct(self):
        functions = Text("Functions").scale(2.5)
        self.play(Write(functions))
        self.wait(2)
        self.play(functions.animate.to_edge(UP).scale(0.4))
        self.wait(2)

        function_box = Rectangle(height=2.5, width=4, color=BLUE).round_corners(
            0.5).shift(DOWN).set_fill(color=DARK_BLUE, opacity=0.25).set_stroke(BLUE, 3)

        self.play(Create(function_box))

        inner_text = Text("function").move_to(
            function_box.get_center()).scale(0.8)

        self.play(Write(inner_text))

        input_a = MathTex("x").next_to(
            function_box, LEFT).shift(LEFT*4).scale(2)
        input_arrow = Arrow(input_a.get_right() + RIGHT*0.2,
                            function_box.get_left() + LEFT*0.2, buff=0.1, color=GREEN)
        input_label = Text("Input").scale(0.75).next_to(input_arrow, DOWN)

        self.wait(1)
        self.play(Create(input_arrow), Write(input_label))
        self.wait(1)
        self.play(Write(input_a))

        output_a = MathTex("y").next_to(
            function_box, RIGHT).shift(RIGHT*4).scale(2)
        output_arrow = Arrow(function_box.get_right() + RIGHT*0.2,
                             output_a.get_left() + LEFT*0.2, buff=0.1, color=RED)
        output_label = Text("Output").scale(0.75).next_to(output_arrow, DOWN)

        self.play(Create(output_arrow), Write(output_label))
        self.wait(1)
        self.play(Write(output_a))
        self.wait(1)

        def f(x): return x + 5

        func_inner = MathTex(
            "x + 5").move_to(function_box.get_center()).scale(1.2)
        self.play(ReplacementTransform(inner_text, func_inner))

        input_b = MathTex("5").move_to(input_a.get_center()).scale(2)
        self.play(ReplacementTransform(input_a, input_b))

        output_b = MathTex("10").move_to(output_a.get_center()).scale(2)
        self.play(ReplacementTransform(output_a, output_b))

        func_diagram = VGroup(input_b, input_arrow, input_label,
                              output_b, output_arrow, output_label, func_inner, function_box)

        self.play(FadeOut(functions), func_diagram.animate.to_edge(UP))

        to_isolate = ["f", "(", ")", "=", "x", "+", "5"]

        tex_color_map = {
            "f": BLUE,
            "(": TEAL,
            ")": TEAL,
            "x": GREEN_A,
        }

        function_notation = MathTex(
            "f", "(", "x", ")", "=", "x", "+", "5").next_to(function_box, DOWN).set_color_by_tex_to_color_map(tex_color_map)

        self.play(Write(function_notation))

        input_value = ValueTracker(0)

        example_a = MathTex(f"f(x) = x + 5", substrings_to_isolate=to_isolate).next_to(
            function_notation, DOWN).shift(DOWN).set_color_by_tex_to_color_map(tex_color_map)
        example_a1 = MathTex(f"f({int(input_value.get_value())}) = {int(input_value.get_value())} + 5", substrings_to_isolate=to_isolate).next_to(
            function_notation, DOWN).shift(DOWN).set_color_by_tex_to_color_map(tex_color_map)
        example_a2 = MathTex(f"f({int(input_value.get_value())}) = {f(int(input_value.get_value()))}", substrings_to_isolate=to_isolate).next_to(
            function_notation, DOWN).shift(DOWN).set_color_by_tex_to_color_map(tex_color_map)

        examples = VGroup(example_a, example_a1, example_a2)
        for ex in examples:
            ex.scale(1.2)

        self.wait(1)
        self.play(TransformMatchingTex(function_notation.copy(), example_a))
        self.wait(1)
        self.play(TransformMatchingTex(example_a, example_a1))
        self.wait(1)
        self.play(TransformMatchingTex(example_a1, example_a2))

        self.play(FadeOut(func_diagram), FadeOut(function_notation))
        self.play(example_a2.animate.move_to(ORIGIN).scale(1.25))

        self.wait(2)


class Vid2Main(Scene):
    def construct(self):

        tex_color_map = {
            "\\theta": GREEN_A,
            "opp": BLUE,
            "hyp": RED,
            "adj": GREEN,
            "f": BLUE,
            "(": TEAL,
            ")": TEAL,
            "sin": TEAL
        }

        to_isolate = ["f", "(", ")", "=", "x", "+", "5"]
        example_a2 = MathTex(f"f({0}) = {5}",
                             substrings_to_isolate=to_isolate).set_color_by_tex_to_color_map(tex_color_map).scale(1.5)

        self.add(example_a2)
        self.wait(4)

        sin_tex = MathTex("sin", "(", "0", ")", "=", "0").scale(
            1.5).set_color_by_tex_to_color_map(tex_color_map)

        self.play(TransformMatchingTex(
            example_a2, sin_tex), run_time=2.5)

        self.wait(2)

        sin_tex_1 = MathTex("sin", "(", "\\theta", ")", "=",
                            "{opp", "\\over", "hyp}").scale(1.5)
        sin_tex_1.set_color_by_tex_to_color_map(tex_color_map)

        self.play(TransformMatchingTex(sin_tex, sin_tex_1), run_time=2)

        self.wait(2)

        function_box = Rectangle(height=2, width=3, color=BLUE).round_corners(
            0.5).set_fill(color=DARK_BLUE, opacity=0.25).set_stroke(BLUE, 3)

        func_inner = MathTex("sin").move_to(
            function_box.get_center()).scale(1.2)

        input_a = MathTex("\\theta").move_to(
            function_box.get_left() + LEFT*4.5).scale(2)
        input_arrow = Arrow(input_a.get_right() + RIGHT*0.2,
                            function_box.get_left() + LEFT*0.2, buff=0.1, color=GREEN)
        input_label = Text("Input").scale(0.75).next_to(input_arrow, DOWN)

        output_a = MathTex("opp", "\\over", "hyp").move_to(
            function_box.get_right() + RIGHT*4.5).set_color_by_tex_to_color_map(tex_color_map)
        output_arrow = Arrow(function_box.get_right() + RIGHT*0.2,
                             output_a.get_left() + LEFT*0.2, buff=0.1, color=RED)
        output_label = Text("Output").scale(0.75).next_to(output_arrow, DOWN)

        func_diagram = VGroup(func_inner, function_box, input_a, VGroup(input_arrow, input_label),
                              VGroup(output_arrow, output_label, output_a)).to_edge(UP)

        for i in func_diagram:
            if "manim.mobject.text" in str(type(i)):
                self.play(Write(i), run_time=0.5)
            else:
                self.play(Create(i), run_time=0.5)
            self.wait(0.5)

        self.play(FadeOut(sin_tex_1))
        self.play(func_diagram.animate.move_to(ORIGIN))

        self.play(FadeOut(input_a, input_arrow, input_label),
                  FadeOut(output_a, output_arrow, output_label))

        self.play(function_box.animate.scale(10), run_time=2)
        self.wait(1)
        sin_example = MathTex("sin", "(", "40", ")").scale(
            1.2).set_color_by_tex_to_color_map(tex_color_map)
        self.play(TransformMatchingTex(func_inner, sin_example))
        self.wait(2)
        self.play(sin_example.animate.to_edge(UP))

        theta_value = ValueTracker(-40)

        base_ref = Line([3, -2, 0], [-3, -2, 0])
        hyp = base_ref.copy().set_color(RED)
        hyp.save_state()
        hyp.rotate(
            theta_value.get_value() * DEGREES, about_point=hyp.get_start())
        hyp_label = always_redraw(lambda: MathTex(
            "hyp").move_to(hyp.get_center() + RIGHT * 0.5).set_color(RED).scale(0.75))
        adj = always_redraw(lambda: Line(
            hyp.get_start(), [hyp.get_end()[0], hyp.get_start()[1], 0], color=GREEN))
        opp = always_redraw(lambda: Line(
            adj.get_end(), hyp.get_end(), color=BLUE))
        opp_label = always_redraw(lambda: MathTex(
            "opp").move_to(opp.get_center() + LEFT * 0.5).set_color(BLUE).scale(0.75))
        theta = always_redraw(lambda: Angle(
            hyp, base_ref, color=GREEN_A, radius=0.5))
        theta_label = Integer(-1 * theta_value.get_value()).scale(
            0.75).move_to(theta.get_center() + UL * 0.2)

        theta_label.add_updater(lambda m: m.move_to(
            Angle(
                hyp, base_ref, radius=0.5 + 3 * SMALL_BUFF
            ).point_from_proportion(0.5)
        ))

        theta_label.add_updater(
            lambda m: m.set_value(-1 * theta_value.get_value()))

        def rotater(m):
            m.restore()
            m.rotate(theta_value.get_value() * DEGREES,
                     about_point=m.get_start())

        hyp.add_updater(rotater)

        triangle = VGroup(adj, opp, hyp)

        self.play(Create(triangle))
        self.wait(1)
        self.play(Create(theta), Write(theta_label))

        opp_arrow = Arrow(theta.get_center() + UL * 0.25,
                          opp.get_center())

        self.play(Create(opp_arrow))
        self.wait(0.5)
        self.play(Write(opp_label))
        self.wait(1)
        self.play(FadeOut(opp_arrow))
        self.wait(0.5)
        self.play(Write(hyp_label))

        self.wait(2)

        sin_example_2 = MathTex("sin", "(", "40", ")", "=").scale(
            1.2).set_color_by_tex_to_color_map(tex_color_map).to_edge(UP)
        self.play(TransformMatchingTex(sin_example, sin_example_2))

        sin_value = ValueTracker(
            np.sin(-1 * theta_value.get_value() * DEGREES))

        sin_val_tex = MathTex("opp", "\\over", "hyp").next_to(
            sin_example_2, RIGHT).set_color_by_tex_to_color_map(tex_color_map)

        self.play(TransformMatchingTex(opp_label.copy(), sin_val_tex))
        self.wait(1)

        sin_val_num = always_redraw(lambda: DecimalNumber(
            sin_value.get_value(), include_sign=False).next_to(sin_example_2, RIGHT))

        self.play(Transform(sin_val_tex, sin_val_num))
        self.wait(2)
        self.play(FadeOut(sin_example_2), FadeOut(sin_val_tex))
        self.wait(2)


class Vid2Graphing(Scene):
    def construct(self):

        color_map = {
            "g": GREEN,
            "(": GREEN,
            ")": GREEN,
            "x": BLUE,
            "sin": TEAL,
            "cos": RED,
        }

        to_isolate = list(color_map.keys())

        title = Text("Graphing Functions").scale(1.2).to_edge(UP)
        self.play(Write(title))

        self.wait(1)

        func_g = MathTex("g", "(", "x", ")", "=", "x^2", substrings_to_isolate=to_isolate).scale(
            1.5).set_color_by_tex_to_color_map(color_map)
        self.play(Write(func_g))

        self.wait(1)
        self.play(func_g.animate.shift(UP))

        examples = VGroup(
            MathTex("g", "(", "1", ")", "=", "1"),
            MathTex("g", "(", "2", ")", "=", "4"),
            MathTex("g", "(", "3", ")", "=", "9"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF).next_to(func_g, DOWN)

        for i in examples:
            i.set_color_by_tex_to_color_map(color_map)
            self.play(TransformMatchingTex(func_g.copy(), i))
            self.wait(1)

        self.wait(2)

        self.play(FadeOut(title), FadeOut(examples))

        self.play(func_g.animate.to_edge(UP))

        self.wait(1)

        # graph g(x) with axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 40, 4],
            y_axis_config={
                "numbers_to_include": np.arange(0, 40, 4)
            }
        ).next_to(func_g, DOWN)

        labels = VGroup(axes.get_x_axis_label("input"),
                        axes.get_y_axis_label("output"))

        graph = axes.plot(lambda x: x**2, color=GREEN)

        graph_label = axes.get_graph_label(graph, label="g(x)")

        def g(x): return x**2

        points = Group()
        for i in range(1, 7):
            dot = Dot(axes.coords_to_point(i, g(i))).scale(0.8)
            points.add(
                VGroup(
                    dot,
                    MathTex("(", str(i), ",", str(g(i)), ")").next_to(
                        dot, UP).set_color_by_tex_to_color_map(color_map)
                )
            )

        self.play(Create(axes))
        self.play(Write(labels))
        self.wait(1)
        for i in points:
            self.play(Create(i[0]), Write(i[1]))
            self.wait(1)

        self.wait(2)

        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        self.play(FadeOut(points, graph, graph_label, labels,))

        axes1 = Axes(
            x_range=[0, 24, 1],
            y_range=[-2, 2, 1],
            y_axis_config={
                "numbers_to_include": np.arange(-2, 2, 1),
                "unit_size": 3,
            }
        ).next_to(func_g, DOWN)

        func_sin = MathTex("sin", "(", "x", ")", substrings_to_isolate=to_isolate).scale(
            1.5).set_color_by_tex_to_color_map(color_map).to_edge(UP)

        self.play(TransformMatchingTex(func_g, func_sin))
        self.wait(1)
        self.play(Transform(axes, axes1))
        self.wait(2)

        func_cos = MathTex("cos", "(", "x", ")", substrings_to_isolate=to_isolate).scale(
            1.5).set_color_by_tex_to_color_map(color_map).next_to(func_sin, RIGHT)

        graph_sin = axes1.plot(lambda x: np.sin(x), color=TEAL)
        graph_sin_label = axes1.get_graph_label(graph_sin, label="sin(x)")

        graph_cos = axes1.plot(lambda x: np.cos(x), color=RED)
        graph_cos_label = axes1.get_graph_label(graph_cos, label="cos(x)")

        self.play(Create(graph_sin), Write(graph_sin_label), run_time=2.5)
        self.wait(2)
        self.play(Write(func_cos))
        self.play(Create(graph_cos), Write(graph_cos_label), run_time=2.5)
        self.wait(2)
        self.play(FadeOut(graph_sin, graph_sin_label, graph_cos,
                  graph_cos_label, axes, labels, func_sin, func_cos))
        self.wait(2)


class Vid2ThetaRel(Scene):
    def construct(self):

        tex_color_map = {
            "\\theta": GREEN_A,
            "opp": BLUE,
            "hyp": RED,
            "adj": GREEN,
            "f": BLUE,
            "(": TEAL,
            ")": TEAL,
            "sin": TEAL
        }

        theta_value = ValueTracker(-40)

        base_ref = Line([3, -2, 0], [-3, -2, 0])
        hyp = base_ref.copy().set_color(RED)
        hyp.save_state()
        hyp.rotate(
            theta_value.get_value() * DEGREES, about_point=hyp.get_start())
        hyp_label = always_redraw(lambda: MathTex(
            "hyp").move_to(hyp.get_center() + RIGHT * 0.5).set_color(RED).scale(0.75))
        adj = always_redraw(lambda: Line(
            hyp.get_start(), [hyp.get_end()[0], hyp.get_start()[1], 0], color=GREEN))
        opp = always_redraw(lambda: Line(
            adj.get_end(), hyp.get_end(), color=BLUE))
        opp_label = always_redraw(lambda: MathTex(
            "opp").move_to(opp.get_center() + LEFT * 0.5).set_color(BLUE).scale(0.75))
        theta = always_redraw(lambda: Angle(
            hyp, base_ref, color=GREEN_A, radius=0.5))
        theta_label = Integer(-1 * theta_value.get_value()).scale(
            0.75).move_to(Angle(
                hyp, base_ref, radius=0.5 + 3 * SMALL_BUFF
            ).point_from_proportion(0.5))

        theta_label.add_updater(lambda m: m.move_to(
            Angle(
                hyp, base_ref, radius=0.5 + 3 * SMALL_BUFF
            ).point_from_proportion(0.5)
        ))

        theta_label.add_updater(
            lambda m: m.set_value(-1 * theta_value.get_value()))

        def rotater(m):
            m.restore()
            m.rotate(theta_value.get_value() * DEGREES,
                     about_point=m.get_start())

        hyp.add_updater(rotater)

        triangle = VGroup(adj, opp, hyp)
        sin_tex = MathTex("sin", "(", "40", ")", "=").scale(
            1.2).set_color_by_tex_to_color_map(tex_color_map).to_edge(UP)
        sin_num = DecimalNumber(np.sin(-1 * theta_value.get_value() * DEGREES),
                                include_sign=True).next_to(sin_tex, RIGHT)

        sin_tex_1 = MathTex("sin", "(", "\\theta", ")", "=").scale(
            1.2).set_color_by_tex_to_color_map(tex_color_map).to_edge(UP)
        triangle = VGroup(adj, opp, hyp)
        sin_tex = MathTex("sin", "(", "40", ")", "=").scale(
            1.2).set_color_by_tex_to_color_map(tex_color_map).to_edge(UP)

        sin_num.add_updater(lambda m: m.set_value(
            np.sin(-1 * theta_value.get_value() * DEGREES)))

        up_arrow = Arrow((sin_num.get_bottom() + 0.5 * DOWN) +
                         RIGHT, (sin_num.get_top() + 0.5 * UP) + RIGHT)
        up_arrow.set_color(GREEN)
        down_arrow = Arrow((sin_num.get_top() + 0.5 * UP) +
                           RIGHT, (sin_num.get_bottom() + 0.5 * DOWN) + RIGHT)
        down_arrow.set_color(RED)

        sin_prop = MathTex("sin", "(", "\\theta", ")",
                           "\\propto", "\\theta", " ?").set_color_by_tex_to_color_map(tex_color_map).to_edge(UP)
        sin_prop.next_to(sin_num, DR).shift(DR).shift(DOWN)

        self.add(triangle)
        self.add(theta)
        self.add(theta_label, opp_label, hyp_label)
        self.add(sin_tex, sin_num)
        self.wait(2)

        self.play(TransformMatchingTex(sin_tex, sin_tex_1))

        self.play(Create(up_arrow))
        self.play(theta_value.animate.set_value(-50))
        self.wait(2)
        self.play(ReplacementTransform(up_arrow, down_arrow))
        self.play(theta_value.animate.set_value(-30))
        self.wait(2)
        self.play(Write(sin_prop))
        self.wait(2)
        self.play(FadeOut(sin_prop))
        self.wait(1)
        self.play(FadeOut(theta), FadeOut(theta_label),
                  FadeOut(hyp_label), FadeOut(opp_label), FadeOut(triangle), FadeOut(sin_tex_1), FadeOut(sin_num), FadeOut(down_arrow))
        self.wait(2)
