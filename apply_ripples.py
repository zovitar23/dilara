import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Ripple CSS
css_updates = """
    .ripple-effect {
      position: fixed;
      border-radius: 50%;
      border: 1.5px solid rgba(142, 232, 234, 0.4);
      background: radial-gradient(circle, rgba(142,232,234,0.1), rgba(173,124,228,0.2), transparent);
      box-shadow: 0 0 10px rgba(142, 232, 234, 0.2);
      transform: translate(-50%, -50%) scale(0);
      animation: rippleAnim 1.4s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
      pointer-events: none;
      z-index: 9999;
    }
    @keyframes rippleAnim {
      100% {
        transform: translate(-50%, -50%) scale(4);
        opacity: 0;
      }
    }
    
    .book, .envelope {
      transition: transform 0.1s ease-out; /* smoothen parallax */
    }
"""
content = content.replace('</style>', f'{css_updates}\n</style>')

# 2. Add Ripple & Parallax JS
js_updates = """
    // Ripple Effect
    window.addEventListener("pointerdown", function(e) {
      const ripple = document.createElement("div");
      ripple.className = "ripple-effect";
      ripple.style.left = e.clientX + "px";
      ripple.style.top = e.clientY + "px";
      ripple.style.width = "40px";
      ripple.style.height = "40px";
      document.body.appendChild(ripple);
      setTimeout(() => ripple.remove(), 1400);
    });

    // 3D Parallax Effect
    const theBook = document.querySelector(".book");
    let targetX = 0, targetY = 0;
    let currentX = 0, currentY = 0;

    window.addEventListener("mousemove", (e) => {
      targetX = (window.innerWidth / 2 - e.clientX) / 45;
      targetY = (window.innerHeight / 2 - e.clientY) / 45;
    });

    function renderParallax() {
      currentX += (targetX - currentX) * 0.1;
      currentY += (targetY - currentY) * 0.1;
      
      const envelope = document.querySelector(".envelope");
      
      if(theBook) {
        theBook.style.transform = `perspective(1600px) rotateX(${-currentY}deg) rotateY(${-currentX}deg)`;
      }
      if(envelope) {
        envelope.style.transform = `perspective(1600px) rotateX(${-currentY * 1.6}deg) rotateY(${-currentX * 1.6}deg)`;
      }
      
      requestAnimationFrame(renderParallax);
    }
    renderParallax();
"""
content = content.replace('</script>', f'{js_updates}\n</script>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Ripples applied successfully")
