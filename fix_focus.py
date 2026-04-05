import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "/* Focus Mode Overlay Transitions */"
end_marker = "</style>"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    pre = content[:start_idx]
    post = content[end_idx:]
    
    new_css = """/* Focus Mode Overlay Transitions */
    body.is-focused {
      transition: background 2.5s ease;
      background: #030105 !important;
    }
    
    body.is-focused::before,
    body.is-focused::after,
    body.is-focused .ambient-glow {
      opacity: 0.02 !important;
    }
    
    body.is-focused .heart-drop,
    body.is-focused .origami-crane,
    body.is-focused .twin-star,
    body.is-focused .love-counter,
    body.is-focused .music-toggle,
    body.is-focused .admin-toggle {
      opacity: 0 !important;
      visibility: hidden !important;
      pointer-events: none !important;
      transition: all 1s ease;
    }
    
    body.is-focused .envelope-flap, 
    body.is-focused .wax-seal,
    body.is-focused .envelope-body,
    body.is-focused .introOverlay {
      display: none !important;
    }
    
    body.is-focused .book {
      background: transparent !important;
      box-shadow: none !important;
      border: none !important;
      transition: background 2.5s ease;
    }
    
    body.is-focused .book::before,
    body.is-focused .book::after {
      opacity: 0 !important;
      display: none !important;
    }

    body.is-focused .page {
      background: transparent !important;
      box-shadow: none !important;
      border: none !important;
      transition: background 2.5s ease;
    }
    
    body.is-focused .page:not(.is-current) {
      opacity: 0 !important;
      visibility: hidden !important;
      display: none !important;
    }

    body.is-focused .page-number,
    body.is-focused .page-date,
    body.is-focused .controls,
    body.is-focused .signature-image,
    body.is-focused .page-flip-dust,
    body.is-focused .page-corner {
      opacity: 0 !important;
      visibility: hidden !important;
      transition: all 1s ease;
    }

    body.is-focused .quote {
      color: #fff !important;
      text-shadow: 0 0 25px rgba(255, 255, 255, 0.4), 0 0 10px #72e4e7, 0 0 40px #9d81c4 !important;
      transform: scale(1.05);
      transition: all 2.5s ease;
      position: relative;
      z-index: 99;
    }

    body.is-focused .quote-note {
      color: #72e4e7 !important;
      text-shadow: 0 0 10px rgba(114, 228, 231, 0.6) !important;
      transition: all 2.5s;
    }
"""
    content = pre + new_css + post
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Focus Mode Fully Repaired")
else:
    print("Markers missing")
