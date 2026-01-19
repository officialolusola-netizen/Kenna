# Step-by-Step Usage Guide

## 🎯 Quick Setup (5 Minutes)

### Step 1: Add Your Logo

You have two options:

#### Option A: Use the Circular Logo Image
1. Save your new circular logo image file
2. Rename it to `new-logo.png` (or `new-logo.jpg` if JPEG)
3. Place it in the `letterhead/assets/` folder
4. Open `letterhead.html` in a text editor (Notepad, VS Code, etc.)
5. Find line 172 (in the logo section)
6. Change this:
   ```html
   <div class="logo-placeholder">
       <!-- Replace this div with your logo image -->
       <!-- <img src="assets/new-logo.png" alt="The Intellingentsia Nigeria Logo"> -->
       <div class="logo-text">
           PLACE NEW<br>CIRCULAR LOGO<br>HERE
       </div>
   </div>
   ```

   To this:
   ```html
   <div class="logo-placeholder">
       <img src="assets/new-logo.png" alt="The Intellingentsia Nigeria Logo">
   </div>
   ```

7. Save the file

#### Option B: Use Base64 Embedded Image (No External Files)
1. Convert your logo to base64 at https://www.base64-image.de/
2. Copy the base64 string
3. Replace the `src` attribute:
   ```html
   <img src="data:image/png;base64,YOUR_BASE64_STRING_HERE" alt="Logo">
   ```

### Step 2: Test the Letterhead

1. Double-click `letterhead.html` to open it in your default browser
2. Verify that your logo appears correctly
3. Check that all elements are properly aligned

### Step 3: Create Your First Letter

#### Using the Template with Sample Content:
1. Open `letterhead.html`
2. Edit the content section (starts around line 230)
3. Replace the sample text with your actual letter content
4. Save the file

#### Using the Blank Template:
1. Open `letterhead-blank.html`
2. Add your logo (same as Step 1)
3. Add your letter content in the content section
4. Save as a new file (e.g., `letter-2026-01-19.html`)

### Step 4: Export to PDF

#### Method 1: Print to PDF (Recommended)
1. Open the letterhead HTML file in Chrome or Firefox
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
3. Select "Save as PDF" as the destination
4. Important settings:
   - **Margins**: None or Minimum
   - **Background graphics**: Enabled (Important!)
   - **Scale**: 100%
5. Click "Save"

#### Method 2: Online Converter
1. Use a service like https://www.web2pdfconvert.com/
2. Upload your HTML file
3. Download the generated PDF

#### Method 3: Command Line (Advanced)
```bash
# Using wkhtmltopdf
wkhtmltopdf --enable-local-file-access letterhead.html letterhead.pdf

# Using Chrome headless
google-chrome --headless --print-to-pdf=letterhead.pdf letterhead.html
```

## 📝 Common Customizations

### Changing the Reference Number

Find this line (around line 188):
```html
<div class="reference-number">CAC/COM/2025/17648568222414</div>
```

Replace with your document reference number.

### Updating Contact Information

Find the footer section (around line 310) and update:

**Phone Number:**
```html
+234 803 332 5647
```

**Address:**
```html
39 Yaounde Street, Abuja, Nigeria
```

### Modifying Colors

Find the style section and change these CSS variables:

**Primary Green:**
```css
color: #1B5E20; /* Change to your preferred green */
```

**Gold Accent:**
```css
color: #D4AF37; /* Change to your preferred gold */
```

### Adjusting Logo Size

Find the `.logo-placeholder` style (around line 60):
```css
.logo-placeholder {
    width: 180px;  /* Change this */
    height: 180px; /* And this */
    /* ... */
}
```

Common sizes:
- Small: 140px
- Medium: 180px (default)
- Large: 220px

## 🔧 Advanced Usage

### Creating a Template System

For organizations that send many letters, create a template system:

1. **Create a Master Template**
   - Use `letterhead-blank.html` as base
   - Remove all content between `<div class="content">` tags
   - Save as `master-template.html`

2. **Create Individual Letters**
   - Copy `master-template.html` for each letter
   - Name them descriptively: `letter-to-client-abc-2026-01-19.html`
   - Add specific content to each

3. **Automate with Scripts** (Advanced)
   - Use Python, Node.js, or other scripting to populate templates
   - Example Python script:
   ```python
   from string import Template

   with open('master-template.html', 'r') as f:
       template = Template(f.read())

   content = {
       'recipient': 'John Doe',
       'date': '2026-01-19',
       'body': 'Your letter content here...'
   }

   output = template.substitute(content)

   with open('letter-output.html', 'w') as f:
       f.write(output)
   ```

### Batch PDF Generation

Using a simple bash script:

```bash
#!/bin/bash
for file in letter-*.html; do
    wkhtmltopdf --enable-local-file-access "$file" "${file%.html}.pdf"
done
```

### Integration with Mail Merge

For large-scale letter generation:

1. Export your data from Excel/CSV
2. Use a templating engine (Jinja2, Handlebars, etc.)
3. Generate HTML files from your template
4. Batch convert to PDF

## 🎨 Design Variations

### Variation 1: Minimal Footer

To create a simpler footer, modify the footer section:

```css
.footer-wave {
    display: none; /* Hide the wave */
}

.footer {
    background: #1B5E20; /* Solid color background */
}
```

### Variation 2: Centered Content

For centered letter format:

```css
.content {
    text-align: center;
    padding: 50px 100px; /* Wider margins */
}
```

### Variation 3: Larger Logo

For emphasis on branding:

```css
.logo-placeholder {
    width: 220px;
    height: 220px;
}
```

## 📱 Using with Microsoft Word

### Creating a Word Template

1. Generate a PDF of the blank letterhead
2. Open Microsoft Word
3. Insert the PDF as a background:
   - Design tab → Watermark → Custom Watermark → Picture
   - Select your letterhead PDF
   - Set Scale to 100%
4. Adjust margins to match the content area (50mm top/bottom, 60mm sides)
5. Save as a Word template (.dotx)

## 🐛 Troubleshooting

### Logo is too large/small
- Adjust the width/height in `.logo-placeholder` CSS
- Ensure your logo image is square for best results
- Try different sizes: 140px (small), 180px (medium), 220px (large)

### Footer is cut off when printing
- Check print margins are set to "None" or "Minimum"
- Ensure "Background graphics" is enabled
- Try adjusting `.footer` height in CSS

### Colors look different in PDF
- Make sure "Background graphics" is enabled in print settings
- Use RGB color values instead of color names
- Test with different PDF generators

### Text overlaps footer
- Adjust `.content` padding-bottom value
- Reduce content min-height
- Use page breaks for longer letters:
  ```html
  <div style="page-break-after: always;"></div>
  ```

### Fonts not displaying correctly
- Check internet connection (Google Fonts requires internet)
- For offline use, download fonts and link locally
- Alternative: Use system fonts like Arial, Georgia

## 💡 Best Practices

1. **Always test before printing**
   - View in browser first
   - Generate PDF and review
   - Print one test copy

2. **Maintain consistency**
   - Use the same template for all official letters
   - Keep color scheme consistent
   - Use identical logo across all documents

3. **File organization**
   - Name files with dates: `letter-2026-01-19-client-name.html`
   - Keep a master template unmodified
   - Archive PDFs separately from HTML sources

4. **Quality control**
   - Use high-resolution logo (at least 500×500px)
   - Proofread all text before converting to PDF
   - Check alignment on different devices

5. **Backup**
   - Keep copies of master templates
   - Save both HTML source and PDF outputs
   - Document any customizations made

## 📞 Need Help?

If you encounter issues:
1. Check this guide first
2. Review the main README.md
3. Verify all file paths are correct
4. Test in a different browser
5. Contact technical support if needed

---

**Last Updated**: 2026-01-19
**Version**: 1.0
