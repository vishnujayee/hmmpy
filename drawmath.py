import numpy as np
from PIL import Image
import math

width, height = 2000, 1200
img = np.zeros((height, width, 3), dtype=np.uint8)

for n in range(height):
    for m in range(width):
        x = (m - width/2) / 400
        y = (n - height/2) / 400
        
        r_val = 0
        g_val = 0
        b_val = 0
        
        for s in range(1, 20):
            mj = pow(1.5,s)*pow(1.5,s-1) +0.1118 
            freq = s * 0.9
            r_val += math.sin(freq * x + 5 * math.cos(freq * math.sin(y*x) * mj)) / s
            g_val += math.cos(freq * y + 1.5 * math.sin(freq * x) ) / s
            b_val += math.sin(freq * (x + y) + 1.2 * math.cos(freq * (x - y)* mj)) / s
        
        r = 0.5 + 0.2 * math.sin(r_val * 3)*mj
        g = 0.5 + 0.2 * math.cos(g_val * 3 + 1)*mj
        b = 0.5 + 0.3 * math.sin(b_val * 3 + 2)*mj
        

        img[n, m] = [int(r * 255), int(g * 246*mj*s), int(b * 255)]

Image.fromarray(img).save("yeganeh_style_copy_try.png")
print("Done! Check yeganeh_style.png")