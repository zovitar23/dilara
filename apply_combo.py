import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- CSS FOR TWIN STARS AND TREE ---
css_updates = """
    /* Twin Stars */
    .twin-star {
      position: fixed;
      top: 0; left: 0;
      width: 14px; height: 14px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 10000;
      mix-blend-mode: screen;
      filter: blur(2px);
      transition: opacity 0.3s;
    }
    .star-1 {
      background: #72e4e7;
      box-shadow: 0 0 16px #72e4e7, 0 0 30px #72e4e7;
    }
    .star-2 {
      background: #9d81c4;
      box-shadow: 0 0 16px #9d81c4, 0 0 30px #9d81c4;
    }

    /* Timeline Tree additions */
    .love-counter {
      display: flex;
      align-items: center;
      gap: 16px;
      padding-right: 24px;
    }
    .timeline-tree {
      width: 48px;
      height: 70px;
      overflow: visible;
    }
    .tree-stem {
      stroke-dasharray: 200;
      stroke-dashoffset: 200;
      animation: growStem 3s ease-in forwards;
    }
    .tree-leaf {
      transform-origin: center;
      transform: scale(0);
      animation: popLeaf 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }
    .tree-leaf:nth-child(2) { animation-delay: 1.5s; }
    .tree-leaf:nth-child(3) { animation-delay: 1.8s; }
    .tree-leaf:nth-child(4) { animation-delay: 2.1s; }
    .top-leaf { animation-delay: 2.6s; }

    @keyframes growStem { to { stroke-dashoffset: 0; } }
    @keyframes popLeaf { to { transform: scale(1); } }
"""
content = content.replace('</style>', f'{css_updates}\n</style>')


# --- HTML FOR TIMELINE TREE ---
html_target = """  <div class="love-counter" id="loveCounter" aria-label="İlişki gün sayacı">
    <p class="love-counter-label">Biz</p>
    <p class="love-counter-value" id="loveCounterValue">2 gündür sevgiliyiz</p>
    <p class="love-counter-note" id="loveCounterNote">03.04.2026'dan beri</p>
  </div>"""

html_replacement = """  <div class="love-counter" id="loveCounter" aria-label="İlişki gün sayacı">
    <svg class="timeline-tree" viewBox="0 0 100 250">
      <path class="tree-stem" d="M50 250 Q60 200 40 150 T50 50" fill="none" stroke="#72e4e7" stroke-width="4" stroke-linecap="round"/>
      <path class="tree-leaf" d="M50 200 Q70 190 70 170 Q50 180 50 200" fill="#9d81c4" opacity="0.9"/>
      <path class="tree-leaf" d="M40 150 Q20 140 20 120 Q40 130 40 150" fill="#72e4e7" opacity="0.9"/>
      <path class="tree-leaf" d="M47 100 Q65 90 65 70 Q47 80 47 100" fill="#9d81c4" opacity="0.9"/>
      <path class="tree-leaf top-leaf" d="M50 50 Q40 20 50 0 Q60 20 50 50" fill="#72e4e7" opacity="0.9"/>
    </svg>
    <div class="counter-texts">
      <p class="love-counter-label">Aşk Ağacımız</p>
      <p class="love-counter-value" id="loveCounterValue">2 gündür sevgiliyiz</p>
      <p class="love-counter-note" id="loveCounterNote">03.04.2026'dan beri büyüyoruz</p>
    </div>
  </div>"""

content = content.replace(html_target, html_replacement)


# --- JS FOR TWIN STARS ---
js_updates = """
    // Twin Stars Logic
    const tStar1 = document.createElement("div");
    const tStar2 = document.createElement("div");
    tStar1.className = "twin-star star-1";
    tStar2.className = "twin-star star-2";
    document.body.appendChild(tStar1);
    document.body.appendChild(tStar2);

    let tAngle = 0;
    // We already have mouseX and mouseY from previous features, but let's re-declare them as global overrides safely 
    // Wait, earlier cursorGlow uses mouseX. We will just use window.globalMouseX
    window.globalMouseX = window.innerWidth / 2;
    window.globalMouseY = window.innerHeight / 2;
    
    window.addEventListener("mousemove", (e) => {
      window.globalMouseX = e.clientX;
      window.globalMouseY = e.clientY;
    });

    function animateTwinStars() {
      tAngle += 0.04;
      const radius = 35; // orbit distance
      const s1X = window.globalMouseX + Math.cos(tAngle) * radius - 7; // -7 for center of 14px 
      const s1Y = window.globalMouseY + Math.sin(tAngle) * radius - 7;
      const s2X = window.globalMouseX + Math.cos(tAngle + Math.PI) * radius - 7;
      const s2Y = window.globalMouseY + Math.sin(tAngle + Math.PI) * radius - 7;
      
      tStar1.style.transform = `translate(${s1X}px, ${s1Y}px)`;
      tStar2.style.transform = `translate(${s2X}px, ${s2Y}px)`;
      
      requestAnimationFrame(animateTwinStars);
    }
    animateTwinStars();
"""
content = content.replace('</script>', f'{js_updates}\n</script>')


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Combo features 1 and 6 applied successfully")
