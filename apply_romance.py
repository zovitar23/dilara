import os
import re

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Overlay HTML
overlay_html = """
  <div id="introOverlay">
    <div class="envelope">
      <div class="envelope-flap"></div>
      <div class="wax-seal" id="waxSeal">
        <span>D&Z</span>
      </div>
      <div class="envelope-body">
        <p>Sizin İçin Bir Mektup...</p>
      </div>
    </div>
  </div>
"""
content = content.replace('<body>', f'<body>\n{overlay_html}')

# 2. CSS updates
css_updates = """
    /* Intro Overlay CSS */
    #introOverlay {
      position: fixed;
      inset: 0;
      background: #0f0a17;
      z-index: 1000;
      display: grid;
      place-items: center;
      transition: opacity 1.5s ease, visibility 1.5s ease;
    }
    #introOverlay.is-hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }
    .envelope {
      position: relative;
      width: 340px;
      height: 220px;
      background: #dfd3e8;
      border-radius: 8px;
      box-shadow: 0 30px 60px rgba(0,0,0,0.6);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .envelope-flap {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 50%;
      background: #d0c2db;
      clip-path: polygon(0 0, 100% 0, 50% 100%);
      border-radius: 8px 8px 0 0;
      z-index: 2;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      transform-origin: top;
      transition: transform 1.2s ease;
    }
    .envelope-body p {
      margin-top: 80px;
      font-family: "Playfair Display", serif;
      font-style: italic;
      color: #51406d;
      font-size: 1.1rem;
      letter-spacing: 1px;
    }
    .wax-seal {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 60px;
      height: 60px;
      background: radial-gradient(circle at 30% 30%, #b82132, #7a0e1c);
      border-radius: 50%;
      z-index: 3;
      display: grid;
      place-items: center;
      box-shadow: inset 0 0 10px rgba(0,0,0,0.3), 0 5px 15px rgba(0,0,0,0.5);
      cursor: pointer;
      transition: transform 0.3s ease, filter 0.3s ease;
    }
    .wax-seal::after {
      content: "";
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 1px solid rgba(184, 33, 50, 0.4);
    }
    .wax-seal:hover {
      transform: translate(-50%, -50%) scale(1.05);
      filter: brightness(1.2);
    }
    .wax-seal.is-broken {
      transform: translate(-50%, -50%) scale(1.2);
      opacity: 0;
      pointer-events: none;
      transition: transform 0.6s ease, opacity 0.6s ease;
    }
    .wax-seal span {
      font-family: "Georgia", serif;
      color: #fce8cd;
      font-size: 1.2rem;
      text-shadow: 0 1px 1px rgba(0,0,0,0.5);
    }

    /* Ink Reveal CSS */
    .page.is-current .quote {
      animation: inkReveal 2.2s cubic-bezier(0.2, 0.8, 0.3, 1) forwards;
      opacity: 0;
    }
    @keyframes inkReveal {
      0% {
        opacity: 0;
        filter: blur(14px) brightness(0.5);
        color: rgba(92, 73, 122, 0);
        transform: translateY(12px) scale(0.98);
      }
      40% {
        color: rgba(92, 73, 122, 0.3);
      }
      100% {
        opacity: 1;
        filter: blur(0) brightness(1);
        color: #180d24;
        transform: translateY(0) scale(1);
      }
    }

    /* Petal CSS replaces Heart css but we can keep both and just style the generic shape */
    .petal-shape {
      position: absolute;
      width: 100%;
      height: 100%;
      background: radial-gradient(ellipse at 50% 10%, #d83f5d 0%, #7d1c31 100%);
      border-radius: 20px 0 20px 0;
      box-shadow: inset 2px 2px 5px rgba(255,255,255,0.2);
      animation: spinPetal var(--spin-duration, 5s) linear infinite;
    }
    @keyframes spinPetal {
      0% { transform: rotate3d(1, 1, 1, 0deg); }
      100% { transform: rotate3d(1, 1, 1, 360deg); }
    }
"""
content = content.replace('</style>', f'{css_updates}\n</style>')

# 3. JS to handle the Wax Seal envelope
js_updates = """
    const introOverlay = document.getElementById("introOverlay");
    const waxSeal = document.getElementById("waxSeal");
    const envelopeFlap = document.querySelector(".envelope-flap");

    if (waxSeal) {
      waxSeal.addEventListener("click", () => {
        waxSeal.classList.add("is-broken");
        envelopeFlap.style.transform = "rotateX(180deg)";
        
        // Start background music naturally upon user interaction
        startBackgroundMusic(); 

        setTimeout(() => {
          introOverlay.classList.add("is-hidden");
        }, 1200);
      });
    }

    // Rewrite createHeartRain to make it create petals instead
    const _oldHeartRain = createHeartRain;
    createHeartRain = function() {
      const heartRain = document.getElementById("heartRain");
      if(!heartRain) return;
      const heartCount = window.innerWidth < 768 ? 20 : 40;
      heartRain.innerHTML = "";

      for (let index = 0; index < heartCount; index += 1) {
        const heart = document.createElement("span");
        heart.className = "heart-drop";
        heart.style.left = `${Math.random() * 100}%`;
        heart.style.setProperty("--size", `${12 + Math.random() * 15}px`);
        heart.style.setProperty("--duration", `${15 + Math.random() * 10}s`);
        heart.style.setProperty("--delay", `${Math.random() * -20}s`);
        heart.style.setProperty("--drift", `${-40 + Math.random() * 80}px`);
        
        const shape = document.createElement("div");
        shape.className = "petal-shape";
        shape.style.setProperty("--spin-duration", `${3 + Math.random() * 5}s`);
        // Color variation for petals
        if(index % 3 === 0) shape.style.filter = "brightness(0.8)";
        if(index % 4 === 0) shape.style.filter = "hue-rotate(-15deg)";

        heart.appendChild(shape);
        heartRain.appendChild(heart);
      }
    };
    createHeartRain();
"""
content = content.replace('</script>', f'{js_updates}\n</script>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")
