import os

file_path = r"c:\Users\zovit\OneDrive\Desktop\dilara\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will find the Focus Mode CSS section and replace it.
start_marker = "/* Focus Mode Overlay Transitions */"
end_marker = "</style>"

if start_marker in content and end_marker in content:
    pre = content[:content.find(start_marker)]
    post = content[content.find(end_marker):]
    
    new_css = """/* Focus Mode Overlay Transitions */
    body.is-focused {
      transition: background-color 2.5s ease;
      background-color: #030105 !important;
    }
    
    body.is-focused .ambient-glow,
    body.is-focused::after {
      opacity: 0.02;
      transition: opacity 2.5s ease;
    }
    
    body.is-focused .heart-drop,
    body.is-focused .origami-crane,
    body.is-focused .love-counter,
    body.is-focused .music-toggle,
    body.is-focused .twin-star {
      opacity: 0.01 !important;
      pointer-events: none;
      transition: opacity 2.5s ease;
    }
    
    body.is-focused .envelope-flap, 
    body.is-focused .wax-seal,
    body.is-focused .envelope-body,
    body.is-focused .introOverlay {
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

    body.is-focused .page {
      background: transparent !important;
      box-shadow: none !important;
      border-right: none !important;
      border-left: none !important;
      transition: all 2.5s ease;
    }

    body.is-focused .page-number,
    body.is-focused .page-date,
    body.is-focused .controls,
    body.is-focused .signature-image {
      opacity: 0.01;
      transition: opacity 2.5s ease;
    }

    body.is-focused .quote {
      color: #fff !important;
      text-shadow: 0 0 25px rgba(255, 255, 255, 0.4), 0 0 10px #72e4e7, 0 0 40px #9d81c4 !important;
      transform: scale(1.05);
      transition: all 2.5s ease;
    }

    body.is-focused .quote-note {
      color: #72e4e7;
      text-shadow: 0 0 10px rgba(114, 228, 231, 0.6);
      transition: all 2.5s;
    }
"""
    content = pre + new_css + post
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Focus Mode CSS Patched")
else:
    print("Could not find markers")
