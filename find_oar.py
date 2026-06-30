import re
with open("rover-circuit.kicad_pcb", "r") as f:
    content = f.read()

pads = re.findall(r'\(pad.*?\n\s*\)', content, re.DOTALL)
for pad in pads:
    if "thru_hole" not in pad and "np_thru_hole" not in pad: continue
    size_m = re.search(r'\(size\s+([0-9.]+)\s+([0-9.]+)\)', pad)
    drill_m = re.search(r'\(drill\s+(?:oval\s+)?([0-9.]+)(?:\s+([0-9.]+))?\)', pad)
    if size_m and drill_m:
        sx, sy = float(size_m.group(1)), float(size_m.group(2))
        dx = float(drill_m.group(1))
        dy = float(drill_m.group(2)) if drill_m.group(2) else dx
        
        oar_x = (sx - dx)/2
        oar_y = (sy - dy)/2
        oar = min(oar_x, oar_y)
        print(f"Pad OAR {oar:.4f}")

