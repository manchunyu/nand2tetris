lines = [
    "(ball.new)",
    "(ball.move$if_end1)",
    "(ball.move$if_end4)",
    "(ball.bounce$if_end0)",
    "(ball.bounce$if_end3)",
    "(ponggame.run$if_end1)",
    "(ponggame.run$while_exp2)",
    "(ponggame.moveball$if_end3)",
    "(ponggame.moveball$if_false1)",
    "(keyboard.readline$if_false0)",
    "(math.multiply$while_exp0)",
    "(math.divide$if_false1)",
    "(math.divide$while_exp1)",
    "(memory.dealloc$if_end0)",
    "(output.printchar$if_end1)",
    "(screen.drawline$if_end3)",
    "(screen.drawhorizontal$if_false0)",
    "(string.intvalue$while_exp0)",
    "(string.setint$if_end4)",
    "(sys.halt$while_exp0)",
    "(sys.wait)",
    "(sys.wait$while_exp0)",
]

for i, s in enumerate(lines):
   
    if s.startswith("("):
        lines.pop(i)

print(lines)
