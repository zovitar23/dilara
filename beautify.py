import os
import re

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Google Fonts
head_target = "<title>Sessiz Sayfalar</title>"
fonts_link = """<title>Sessiz Sayfalar</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">"""
content = content.replace(head_target, fonts_link)

# 2. Update Colors
root_target = """:root {
      --bg-1: #2c2138;
      --bg-2: #130f1f;
      --paper: #ebe4f1;
      --paper-edge: #cdbfdc;
      --ink: #1e1630;
      --muted: rgba(46, 31, 67, 0.6);
      --shadow: 0 30px 90px rgba(5, 3, 11, 0.58);
      --page-shadow: 0 18px 40px rgba(10, 8, 22, 0.26);
      --line: rgba(95, 78, 122, 0.2);
      --accent: #8d79a9;
      --cyan: #8ee8ea;
      --cyan-soft: rgba(142, 232, 234, 0.14);
      --glow-soft: rgba(173, 124, 228, 0.16);
    }"""
root_replacement = """:root {
      --bg-1: #1a0f26;
      --bg-2: #080512;
      --paper: #faf6fc;
      --paper-edge: #e6ddf1;
      --ink: #150b24;
      --muted: rgba(62, 45, 87, 0.65);
      --shadow: 0 45px 120px rgba(0, 0, 4, 0.85);
      --page-shadow: 0 25px 60px rgba(8, 6, 22, 0.4);
      --line: rgba(126, 98, 168, 0.25);
      --accent: #a389cc;
      --cyan: #6de2e6;
      --cyan-soft: rgba(109, 226, 230, 0.2);
      --glow-soft: rgba(200, 142, 255, 0.25);
    }"""
content = content.replace(root_target, root_replacement)

# 3. Update Fonts
content = content.replace('"Segoe UI", "Helvetica Neue", Arial, sans-serif', '"Outfit", "Segoe UI", sans-serif')
content = content.replace('"Georgia", "Times New Roman", serif', '"Playfair Display", "Georgia", serif')

# 4. Add Cursor Glow HTML
body_target = """<body>
  <div class="ambient-glow" aria-hidden="true"></div>"""
body_replacement = """<body>
  <div class="cursor-glow" id="cursorGlow" aria-hidden="true"></div>
  <div class="ambient-glow" aria-hidden="true"></div>"""
content = content.replace(body_target, body_replacement)

# 5. Add polaroid styles and cursor styles
custom_css = """
    .cursor-glow {
      position: fixed;
      top: -100px;
      left: -100px;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(142, 232, 234, 0.15) 0%, rgba(173, 124, 228, 0.08) 30%, transparent 60%);
      border-radius: 50%;
      pointer-events: none;
      z-index: 100;
      transform: translate(-50%, -50%);
      transition: width 0.3s, height 0.3s;
      mix-blend-mode: screen;
    }

    .polaroid {
      position: absolute;
      top: 15%;
      right: 8%;
      width: clamp(140px, 20vw, 220px);
      background: #fafafa;
      padding: 10px 10px 30px 10px;
      box-shadow: 0 10px 24px rgba(0,0,0,0.2), 0 2px 4px rgba(0,0,0,0.1);
      transform: rotate(4deg);
      z-index: 2;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: 2px;
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .polaroid:hover {
      transform: rotate(0deg) scale(1.05) translateY(-5px);
      box-shadow: 0 16px 32px rgba(0,0,0,0.25), 0 4px 8px rgba(0,0,0,0.15);
      z-index: 10;
    }
    .polaroid img {
      width: 100%;
      height: auto;
      display: block;
      filter: sepia(0.2) contrast(1.1) brightness(0.9);
      border-radius: 1px;
    }
    .polaroid::after {
      content: "";
      position: absolute;
      inset: 0;
      box-shadow: inset 0 0 40px rgba(0,0,0,0.1);
      pointer-events: none;
    }
    .polaroid-caption {
      position: absolute;
      bottom: 8px;
      left: 0;
      width: 100%;
      text-align: center;
      font-family: 'Brush Script MT', cursive;
      font-size: 1.1rem;
      color: #333;
      opacity: 0.8;
    }

    .polaroid-2 {
      top: auto;
      bottom: 12%;
      right: auto;
      left: 8%;
      transform: rotate(-5deg);
    }
    """
css_target = """    @keyframes pageDust {"""
content = content.replace(css_target, custom_css + "\n    @keyframes pageDust {")

# 6. Add images to RenderPages logic
render_target = """          <div class="page-content">
            <div class="page-meta">"""
render_replacement = """
          ${index === 0 ? `<div class="polaroid">
              <img src="romantic-couple.png" alt="Sen ve Ben">
              <div class="polaroid-caption">İlk An...</div>
            </div>` : ''}
          ${index === 2 ? `<div class="polaroid polaroid-2">
              <img src="romantic-couple-2.png" alt="Beraber">
              <div class="polaroid-caption">Sonsuzluğum ✨</div>
            </div>` : ''}
          <div class="page-content">
            <div class="page-meta">"""
content = content.replace(render_target, render_replacement)

# 7. Add JS for Cursor Logic
js_target = """    createHeartRain();"""
js_replacement = """
    const cursorGlow = document.getElementById("cursorGlow");
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    
    window.addEventListener("mousemove", (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    function animateCursor() {
      // smooth following
      let x = parseFloat(cursorGlow.style.left) || mouseX;
      let y = parseFloat(cursorGlow.style.top) || mouseY;
      x += (mouseX - x) * 0.15;
      y += (mouseY - y) * 0.15;
      cursorGlow.style.left = `${x}px`;
      cursorGlow.style.top = `${y}px`;
      requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Subtle hover effect over interactive elements
    document.querySelectorAll("button, select, input, textarea").forEach(el => {
      el.addEventListener("mouseenter", () => {
        cursorGlow.style.width = "500px";
        cursorGlow.style.height = "500px";
        cursorGlow.style.background = "radial-gradient(circle, rgba(142, 232, 234, 0.22) 0%, rgba(173, 124, 228, 0.12) 40%, transparent 60%)";
      });
      el.addEventListener("mouseleave", () => {
        cursorGlow.style.width = "400px";
        cursorGlow.style.height = "400px";
        cursorGlow.style.background = "radial-gradient(circle, rgba(142, 232, 234, 0.15) 0%, rgba(173, 124, 228, 0.08) 30%, transparent 60%)";
      });
    });

    createHeartRain();"""
content = content.replace(js_target, js_replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")
