import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

css_updates = """
    /* Origami Crane Animation CSS */
    .origami-crane {
      position: fixed;
      pointer-events: none;
      z-index: 50;
      opacity: 0;
      filter: drop-shadow(0 15px 15px rgba(0, 0, 0, 0.4));
      animation: flyCrane var(--fly-dur) ease-in-out forwards;
      transform-origin: center;
    }
    .crane-svg {
      width: 100%;
      height: 100%;
      fill: #ebe2f5;
      animation: flapWings var(--flap-dur) infinite alternate ease-in-out;
    }
    .crane-svg polygon {
      stroke: rgba(255, 255, 255, 0.5);
      stroke-width: 0.5;
    }
    .wing-right { fill: #f8f1ff; }
    .wing-left { fill: #d1bce6; }
    .body { fill: #ab8ec7; }
    .tail { fill: #bfa6d9; }
    .head { fill: #ebe2f5; }

    @keyframes flyCrane {
      0% {
        transform: translate(-100px, var(--start-y)) scale(var(--crane-scale)) rotate(10deg);
        opacity: 0;
      }
      10% { opacity: 0.6; }
      90% { opacity: 0.4; }
      100% {
        transform: translate(calc(100vw + 100px), var(--end-y)) scale(var(--crane-scale)) rotate(-10deg);
        opacity: 0;
      }
    }
    @keyframes flapWings {
      0% { transform: scaleY(1); }
      100% { transform: scaleY(0.4); }
    }
"""

js_updates = """
    // Flying Origami Cranes Logic
    function createCrane() {
      const crane = document.createElement("div");
      crane.className = "origami-crane";
      
      const scale = 0.4 + Math.random() * 0.4; // 0.4 to 0.8
      const startY = (Math.random() * window.innerHeight * 0.8) + "px";
      const endY = (Math.random() * window.innerHeight * 0.8) + "px";
      const flyDur = 15 + Math.random() * 20; // 15 to 35 seconds
      const flapDur = 0.8 + Math.random() * 0.5; // 0.8 to 1.3 seconds
      
      crane.style.setProperty("--crane-scale", scale);
      crane.style.setProperty("--start-y", startY);
      crane.style.setProperty("--end-y", endY);
      crane.style.setProperty("--fly-dur", flyDur + "s");
      crane.style.setProperty("--flap-dur", flapDur + "s");
      
      crane.style.width = "60px";
      crane.style.height = "60px";

      crane.innerHTML = `
        <svg class="crane-svg" viewBox="0 0 100 100">
          <polygon class="wing-left" points="50,40 20,10 10,40 40,60" />
          <polygon class="wing-right" points="50,40 80,10 90,40 60,60" />
          <polygon class="body" points="40,60 60,60 50,75 50,90" />
          <polygon class="tail" points="30,85 40,60 50,75" />
          <polygon class="head" points="70,25 60,60 50,50" />
        </svg>
      `;

      document.body.appendChild(crane);
      
      // Cleanup after fly animation
      setTimeout(() => crane.remove(), flyDur * 1000);
    }

    // Spawn cranes occasionally
    setInterval(() => {
      // Create a crane only sporadically (30% chance every 4 seconds) to keep it rare and magical
      if(Math.random() < 0.3) {
        createCrane();
      }
    }, 4000);
    
    // Create first crane immediately
    createCrane();
"""

content = content.replace('</style>', f'{css_updates}\n</style>')
content = content.replace('</script>', f'{js_updates}\n</script>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Origami Cranes added successfully")
