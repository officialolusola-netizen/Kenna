# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Choose Your Design

We've created three design variations for you:

1. **letterhead.html** - Full modern design with sample content
   - Best for: Seeing the complete design with examples
   - Features: Wave footer, gradient borders, professional styling

2. **letterhead-blank.html** - Clean template ready for your content
   - Best for: Creating new letters quickly
   - Features: Same design as above, no sample content

3. **letterhead-minimal.html** - Simplified, clean design
   - Best for: Those preferring subtle, minimalist aesthetics
   - Features: Flat colors, simple borders, clean look

### Step 2: Add Your Logo

1. Save your new circular logo to `assets/new-logo.png`
2. Open your chosen HTML file in a text editor
3. Find the logo section (look for `<!-- Replace with your logo -->`)
4. Uncomment this line:
   ```html
   <img src="assets/new-logo.png" alt="The Intellingentsia Nigeria Logo">
   ```
5. Save the file

### Step 3: Create Your Letter

1. Open the HTML file in a web browser (double-click it)
2. Verify your logo appears correctly
3. Edit the content in a text editor
4. Save and refresh browser to see changes
5. Print to PDF (Ctrl+P → Save as PDF)

## 📁 What's Included

```
letterhead/
├── letterhead.html              # Main template with sample content
├── letterhead-blank.html        # Blank template for quick use
├── letterhead-minimal.html      # Minimalist design variation
├── README.md                    # Full documentation
├── USAGE_GUIDE.md              # Detailed step-by-step instructions
├── DESIGN_NOTES.md             # Design decisions and rationale
├── QUICKSTART.md               # This file
└── assets/                     # Place your logo here
    └── .gitkeep
```

## 🎯 Common Tasks

### Create Your First Letter
1. Copy `letterhead-blank.html` → `my-letter.html`
2. Add your logo (see Step 2 above)
3. Edit content between `<div class="content">` tags
4. Open in browser and export to PDF

### Change Colors
Look for these in the CSS (in `<style>` section):
- Green: `#1B5E20`
- Gold: `#D4AF37`

### Adjust Logo Size
Find `.logo-placeholder` and change:
```css
width: 180px;  /* Change this */
height: 180px; /* And this */
```

### Update Contact Info
Find the footer section and update:
- Phone: `+234 803 332 5647`
- Address: `39 Yaounde Street, Abuja, Nigeria`

## 💡 Tips

- ✅ Always enable "Background graphics" when printing
- ✅ Use "Print to PDF" for best results
- ✅ Keep one master copy unchanged
- ✅ Test in browser before printing
- ✅ Use high-resolution logo (500px+)

## 📄 Need More Help?

- **Detailed Instructions**: See `USAGE_GUIDE.md`
- **Design Information**: See `DESIGN_NOTES.md`
- **Full Documentation**: See `README.md`

## ⚡ Super Quick Method

Just want to see it now?

1. Double-click `letterhead.html`
2. It opens in your browser with sample content
3. That's the design with a placeholder for your logo!

---

**Happy letterhead creating!** 🎉

For technical support: +234 803 332 5647
