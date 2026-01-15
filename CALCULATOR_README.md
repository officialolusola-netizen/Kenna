# Nigerian Tax Calculator 2025 - Offline Version

## 📥 Download & Installation Instructions

### Option 1: Direct Download (Recommended)
1. **Download the file**: Right-click on `nigerian_tax_calculator.html` and select "Save As" or "Download"
2. **Save to your computer**: Choose a location (e.g., Desktop, Documents)
3. **Open the calculator**: Double-click the downloaded HTML file
4. **That's it!** The calculator will open in your default web browser and works completely offline

### Option 2: Use from Repository
1. Clone or download this repository
2. Navigate to the folder containing `nigerian_tax_calculator.html`
3. Double-click the file to open it in your browser

### Option 3: Use Python Launcher (If Available)
```bash
python launch_calculator.py
```

---

## 🚀 Quick Start Guide

### Step-by-Step Instructions:

1. **Enter Company Information**
   - Annual Gross Income/Revenue (required)
   - Operating Expenses (required)

2. **Add Employee Information**
   - Enter annual salary for each employee
   - Click "Add Another Employee" to add more employees
   - PAYE is calculated automatically using progressive tax bands

3. **Enter Other Tax Information** (Optional)
   - Asset disposal proceeds and cost basis (for CGT)
   - VAT-taxable sales
   - Withholding tax income and payments

4. **Calculate**
   - Click the "Calculate Taxes" button
   - View comprehensive results on the right panel

5. **Review Results**
   - Revenue breakdown
   - Company tax liability (CIT, Tertiary Education Tax, CGT)
   - Employee PAYE breakdown
   - VAT and WHT information
   - Net income (monthly and annual)

---

## 📊 What This Calculator Does

### Taxes Calculated:

1. **Company Income Tax (CIT)** - 30% of assessable profit
2. **Tertiary Education Tax** - 2% of assessable profit
3. **Capital Gains Tax (CGT)** - 10% of chargeable gains
4. **Pay As You Earn (PAYE)** - Progressive rates (7% to 24%)
5. **Value Added Tax (VAT)** - 7.5% (informational)
6. **Withholding Tax (WHT)** - Credit against CIT
7. **Minimum Tax** - 0.5% of turnover (when no profit)

### Key Features:

✅ **Accurate PAYE Calculation** - Uses Nigerian progressive tax bands with CRA
✅ **WHT Credit System** - Properly credits WHT against CIT liability
✅ **Minimum Tax** - Automatically applies when company has no profit
✅ **Per-Employee Breakdown** - Individual PAYE calculations for each employee
✅ **Professional UI** - Clean, modern interface with clear results
✅ **100% Offline** - No internet connection required after download
✅ **Mobile Friendly** - Responsive design works on all devices

---

## 🔧 Technical Details

### Technologies Used:
- **HTML5** - Structure
- **CSS3** - Styling (embedded)
- **JavaScript** - Calculations (embedded)
- **No external dependencies** - Everything is self-contained

### Browser Compatibility:
- ✅ Google Chrome
- ✅ Mozilla Firefox
- ✅ Microsoft Edge
- ✅ Safari
- ✅ Opera
- ⚠️ Internet Explorer (not recommended)

### File Size:
- ~50KB (single HTML file)
- No external resources required
- Fast loading time

---

## 📋 Tax Rates Reference (2025)

### PAYE Progressive Bands:
| Taxable Income Range | Tax Rate |
|---------------------|----------|
| First ₦300,000 | 7% |
| Next ₦300,000 | 11% |
| Next ₦500,000 | 15% |
| Next ₦500,000 | 19% |
| Next ₦1,600,000 | 21% |
| Above ₦3,200,000 | 24% |

### Other Tax Rates:
- **CIT**: 30% of assessable profit
- **VAT**: 7.5% of taxable supplies
- **WHT**: 10% (standard rate, varies by transaction type)
- **CGT**: 10% of chargeable gains
- **Tertiary Education Tax**: 2% of assessable profit
- **Minimum Tax**: 0.5% of gross turnover

### Consolidated Relief Allowance (CRA):
- Higher of:
  - 1% of gross income, OR
  - ₦200,000 + 20% of gross income

---

## 💡 Usage Examples

### Example 1: Small Business
```
Annual Gross Income: ₦10,000,000
Operating Expenses: ₦4,000,000
Employees: 2 (₦2,400,000 and ₦1,800,000 annually)
```

### Example 2: Medium Enterprise
```
Annual Gross Income: ₦150,000,000
Operating Expenses: ₦80,000,000
Employees: 10 (various salaries)
VAT-Taxable Sales: ₦120,000,000
Asset Disposal: ₦5,000,000 (Cost: ₦3,000,000)
```

### Example 3: Large Corporation
```
Annual Gross Income: ₦500,000,000
Operating Expenses: ₦300,000,000
Employees: 50+ (various salaries)
WHT Income: ₦50,000,000
WHT Paid: ₦5,000,000
```

---

## ⚠️ Important Notes

1. **For Informational Purposes Only**
   - This calculator provides estimates based on Nigerian Tax Act 2025
   - Always consult a qualified tax professional for official advice
   - Tax laws may change; verify rates with FIRS

2. **Simplified Calculations**
   - Some tax calculations may involve additional complexities
   - Capital allowances, loss carry-forward, and other deductions are not included
   - Industry-specific tax rates may vary

3. **Data Privacy**
   - All calculations are performed locally in your browser
   - No data is sent to any server
   - Your financial information remains private

4. **Accuracy**
   - Based on available information as of January 2025
   - Progressive PAYE rates verified against FIRS guidelines
   - CRA calculation follows standard formula

---

## 🆘 Troubleshooting

### Calculator Won't Open:
- Make sure you have a modern web browser installed
- Try right-clicking the file and select "Open with" → Choose your browser
- Check that JavaScript is enabled in your browser

### Results Not Showing:
- Ensure you've filled in the required fields (marked with *)
- Check that all numbers are positive
- Try clicking "Reset Form" and re-entering data

### Display Issues:
- Try zooming in/out in your browser (Ctrl/Cmd + or -)
- Refresh the page (F5 or Ctrl/Cmd + R)
- Clear browser cache if necessary

### Performance Issues:
- The calculator is lightweight and should run smoothly
- If adding many employees (50+), calculation may take a second
- Close other browser tabs if experiencing slowness

---

## 📞 Support & Feedback

For questions, suggestions, or to report issues:
- Create an issue in this repository
- Contact: [Your Contact Information]

---

## 📜 License & Disclaimer

**Disclaimer**: This calculator is provided "as is" for informational and educational purposes only. The authors make no warranties about the accuracy, completeness, or reliability of the calculations. Users should consult qualified tax professionals for official tax advice and compliance.

**Copyright**: © 2025 Olusola's AI Assistant

---

## 🔄 Version History

### Version 1.0 (January 2025)
- ✨ Initial release
- 🏢 Company Income Tax calculation
- 👥 PAYE with progressive bands
- 📊 VAT and WHT information
- 💰 CGT and Tertiary Education Tax
- 🎨 Modern, responsive UI
- 📱 Mobile-friendly design

---

## 🎯 Future Enhancements (Planned)

- [ ] Print/Export PDF report
- [ ] Save calculations locally
- [ ] Compare multiple scenarios
- [ ] Tax planning recommendations
- [ ] Industry-specific templates
- [ ] Multi-year projections
- [ ] Dark mode theme

---

Made with ❤️ for Nigerian businesses
