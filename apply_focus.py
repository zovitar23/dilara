import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- CSS FOR FOCUS MODE ---
css_updates = """
    /* Focus Mode Toggle Button */
    .focus-toggle {
      position: fixed;
      bottom: 24px;
      left: 24px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(142, 232, 234, 0.05);
      border: 1px solid rgba(142, 232, 234, 0.2);
      color: rgba(255, 255, 255, 0.6);
      display: grid;
      place-items: center;
      cursor: pointer;
      z-index: 1000;
      transition: all 0.4s ease;
      font-size: 1.2rem;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .focus-toggle:hover {
      background: rgba(142, 232, 234, 0.15);
      color: #fff;
      transform: scale(1.1);
      box-shadow: 0 0 15px rgba(142, 232, 234, 0.4);
    }

    /* Focus Mode Overlay Transitions */
    body {
      transition: background-color 2.5s ease;
    }
    
    body.is-focused .layout-bg {
      opacity: 0.1;
      filter: blur(20px);
      transition: all 2.5s ease;
    }
    
    body.is-focused .heart-drop,
    body.is-focused .origami-crane,
    body.is-focused .love-counter,
    body.is-focused .music-toggle,
    body.is-focused .twin-star {
      opacity: 0.02 !important;
      transition: opacity 2.5s ease;
    }
    
    body.is-focused .envelope-flap, 
    body.is-focused .wax-seal,
    body.is-focused .envelope-body {
      opacity: 0;
      transition: opacity 2.5s ease;
    }
    
    body.is-focused .book {
      background: transparent !important;
      box-shadow: none !important;
      border: none !important;
      transition: all 2.5s ease;
    }
    
    body.is-focused .book::before,
    body.is-focused .book::after {
      opacity: 0;
    }

    body.is-focused .page-number,
    body.is-focused .page-date,
    body.is-focused .controls {
      opacity: 0.1;
      transition: opacity 2.5s ease;
    }

    body.is-focused .quote {
      color: #f1edfa !important;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.8), 0 0 10px #72e4e7 !important;
      transform: scale(1.1);
      transition: all 2.5s ease;
      mix-blend-mode: normal;
    }

    body.is-focused .quote-note {
      color: #72e4e7;
      text-shadow: 0 0 10px rgba(114, 228, 231, 0.6);
      transition: all 2.5s;
    }
"""
content = content.replace('</style>', f'{css_updates}\n</style>')

# --- HTML FOR FOCUS BUTTON ---
# Let's insert the toggle directly into body before the script tags
html_button = """
  <!-- Focus Mode Toggle -->
  <button class="focus-toggle" id="focusToggle" type="button" aria-label="Odak Modu" title="Sadece Şiire Odaklan">
    🌑
  </button>
"""
content = content.replace('<script>', f'{html_button}\n  <script>')

# --- JS FOR FOCUS LOGIC ---
js_updates = """
    // Focus Mode Logic
    const focusToggle = document.getElementById("focusToggle");
    let isFocused = false;
    
    focusToggle.addEventListener("click", () => {
      isFocused = !isFocused;
      if (isFocused) {
        document.body.classList.add("is-focused");
        focusToggle.textContent = "✨";
        focusToggle.title = "Karanlıktan Çık";
      } else {
        document.body.classList.remove("is-focused");
        focusToggle.textContent = "🌑";
        focusToggle.title = "Sadece Şiire Odaklan";
      }
    });
"""
content = content.replace('</script>', f'{js_updates}\n</script>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Focus Mode feature added successfully")
