import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Sparks CSS
css_updates = """
    /* Spark Animation */
    .magic-spark {
      position: absolute;
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #ffd700;
      box-shadow: 0 0 10px #ff8c00, 0 0 20px #ff8c00;
      opacity: 1;
      pointer-events: none;
      animation: scatterSpark var(--spark-dur, 1s) cubic-bezier(0.2, 0.8, 0.3, 1) forwards;
      z-index: 999;
    }
    @keyframes scatterSpark {
      0% {
        transform: translate(0, 0) scale(1);
        opacity: 1;
      }
      100% {
        transform: translate(var(--tx), var(--ty)) scale(0);
        opacity: 0;
      }
    }
    .page.is-disintegrating {
      animation: disintegratePage 1.2s forwards;
    }
    @keyframes disintegratePage {
      0% {
        opacity: 1;
        filter: blur(0) sepia(0);
        transform: scale(1) translateX(0);
      }
      30% {
        filter: blur(2px) sepia(0.8) hue-rotate(-15deg);
        opacity: 0.8;
      }
      100% {
        opacity: 0;
        filter: blur(8px) sepia(1) brightness(1.5);
        transform: scale(0.95) translateX(-30px);
      }
    }
"""
content = content.replace('</style>', f'{css_updates}\n</style>')

# 2. Modify goToPage explicitly
js_target = """    function goToPage(nextIndex) {
      if (nextIndex === currentIndex || nextIndex < 0 || nextIndex >= quotes.length) return;
      const currentPage = pageStack.querySelector(".page.is-current");
      if (currentPage) {
        currentPage.classList.remove("is-flipping");
        void currentPage.offsetWidth;
        currentPage.classList.add("is-flipping");
      }
      currentIndex = nextIndex;
      updateBook();
      playPageFlip();
      syncEditorFields();
    }"""

js_replacement = """    function goToPage(nextIndex) {
      if (nextIndex === currentIndex || nextIndex < 0 || nextIndex >= quotes.length) return;
      const currentPage = pageStack.querySelector(".page.is-current");
      
      // Magical sparks feature
      if (currentPage) {
        currentPage.classList.add("is-disintegrating");
        for (let i = 0; i < 40; i++) {
          const spark = document.createElement("div");
          spark.className = "magic-spark";
          spark.style.left = (Math.random() * 100) + "%";
          spark.style.top = (Math.random() * 100) + "%";
          spark.style.setProperty("--tx", (Math.random() * 200 - 100) + "px");
          spark.style.setProperty("--ty", (Math.random() * -200) + "px");
          spark.style.setProperty("--spark-dur", (0.8 + Math.random() * 0.6) + "s");
          currentPage.appendChild(spark);
          
          setTimeout(() => spark.remove(), 1500);
        }
      }

      setTimeout(() => {
         currentIndex = nextIndex;
         updateBook();
         syncEditorFields();
      }, 500); // Delay the real flip so disintegration is visible

      playPageFlip();
    }"""
content = content.replace(js_target, js_replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Sparks applied successfully")
