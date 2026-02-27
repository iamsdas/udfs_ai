@fused.udf
def udf(color: str = "#FF6B6B", thickness: int = 10, flip_x: bool = True, flip_y: bool = False):
    sx = -1 if flip_x else 1
    sy = -1 if flip_y else 1
    return f"""<html>
<body style="margin:0; background:transparent;">
<svg width="100%" height="100%" viewBox="0 0 340 340" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"
     style="transform: scale({sx},{sy});">
  <path d="M 30 30 Q 40 280 260 290" fill="none" stroke="{color}" stroke-width="{thickness}" stroke-linecap="round"/>
  <path d="M 230 270 L 265 295 L 240 310" fill="none" stroke="{color}" stroke-width="{thickness}" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
</body></html>"""
