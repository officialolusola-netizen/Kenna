# Nigerian PAYE Calculator - Nigeria Tax Act 2025

---

> **⚠️ THIS IS DOCUMENTATION - NOT THE CALCULATOR!**
>
> **To use the calculator, open one of these files:**
> - `index.html` (recommended - main entry point)
> - `nigerian_tax_calculator.html` (direct calculator)
>
> **Do NOT open this file** - This is just a guide/manual.

---

## 📥 Download & Installation Instructions

### ⚠️ Important: Effective Date
**The Nigeria Tax Act, 2025 was signed on June 26, 2025 and takes effect on January 1, 2026.**
This calculator uses the new PAYE (Personal Income Tax) rates that take effect in 2026.

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

1. **Enter Salary Information**
   - Annual gross salary (required)
   - Annual rent paid (optional - for Rent Relief calculation)

2. **Add Multiple Employees** (Optional)
   - Click "Add Another Employee/Salary" to calculate for multiple people
   - Each employee can have different salary and rent amounts

3. **Calculate**
   - Click the "Calculate PAYE" button
   - View detailed results below

4. **Review Results**
   - See if employee qualifies for tax-free status (≤₦800k taxable income)
   - View annual and monthly breakdown
   - See detailed tax calculation per band
   - Review Rent Relief applied (if any)

---

## 📊 What This Calculator Does

### PAYE (Pay As You Earn) - Personal Income Tax

This calculator computes **employee personal income tax** based on the Nigeria Tax Act 2025:

✅ **Progressive Tax Bands** - 0%, 15%, 18%, 21%, 23%, 25%
✅ **Tax-Free Threshold** - First ₦800,000 completely tax-free!
✅ **Rent Relief** - 20% of annual rent, capped at ₦500,000
✅ **Monthly Breakdown** - Shows monthly gross, PAYE, and net salary
✅ **Detailed Tax Calculation** - Per-band breakdown showing exactly how tax is calculated
✅ **Tax-Free Status** - Automatic detection when taxable income ≤₦800,000
✅ **Multi-Employee** - Calculate PAYE for multiple employees at once
✅ **100% Offline** - No internet connection required after download
✅ **Mobile Friendly** - Responsive design works on all devices

---

## 📋 PAYE Tax Bands (Nigeria Tax Act 2025)

### Progressive Tax Rates (Effective Jan 1, 2026):

| Taxable Income Range | Tax Rate |
|---------------------|----------|
| First ₦800,000 | **0%** (Tax-Free! 🎉) |
| ₦800,001 - ₦3,000,000 | 15% |
| ₦3,000,001 - ₦10,000,000 | 18% |
| ₦10,000,001 - ₦25,000,000 | 21% |
| ₦25,000,001 - ₦50,000,000 | 23% |
| Above ₦50,000,000 | 25% |

### How It Works:
The tax is calculated **progressively**, meaning:
- You only pay the rate for income within each band
- Lower income is always taxed at lower rates
- Example: ₦5M salary pays 0% on first ₦800k, 15% on next ₦2.2M, then 18% on remaining ₦2M

### Relief Allowance:
- **OLD (Pre-2026)**: Consolidated Relief Allowance (CRA) = max(1% of gross, ₦200k + 20% of gross)
- **NEW (2026+)**: **Rent Relief** = 20% of annual rent paid, capped at ₦500,000

---

## 💡 Usage Examples

### Example 1: Low-Income Earner (Tax-Free!)
```
Annual Gross Salary: ₦750,000
Annual Rent Paid: ₦0

Result:
- Rent Relief: ₦0
- Taxable Income: ₦750,000
- PAYE: ₦0 (TAX-FREE! 🎉)
- Net Salary: ₦750,000
- Monthly Net: ₦62,500
```

### Example 2: Mid-Level Employee with Rent
```
Annual Gross Salary: ₦3,600,000
Annual Rent Paid: ₦1,200,000

Calculation:
- Rent Relief: ₦240,000 (20% of ₦1.2M, max ₦500k)
- Taxable Income: ₦3,360,000

Tax Breakdown:
- First ₦800,000 @ 0% = ₦0
- Next ₦2,200,000 @ 15% = ₦330,000
- Next ₦360,000 @ 18% = ₦64,800
- Total PAYE: ₦394,800

Result:
- Annual Net Salary: ₦3,205,200
- Monthly Net: ₦267,100
```

### Example 3: High-Income Earner
```
Annual Gross Salary: ₦15,000,000
Annual Rent Paid: ₦3,000,000

Calculation:
- Rent Relief: ₦500,000 (20% of ₦3M, capped at ₦500k)
- Taxable Income: ₦14,500,000

Tax Breakdown:
- First ₦800,000 @ 0% = ₦0
- Next ₦2,200,000 @ 15% = ₦330,000
- Next ₦7,000,000 @ 18% = ₦1,260,000
- Next ₦4,500,000 @ 21% = ₦945,000
- Total PAYE: ₦2,535,000

Result:
- Annual Net Salary: ₦12,465,000
- Monthly Net: ₦1,038,750
```

---

## 🎯 What's New in Nigeria Tax Act 2025

### Major PAYE Changes:

1. **Tax-Free Threshold Introduced** ✨
   - **NEW**: First ₦800,000 is completely tax-free
   - Massive benefit for low and middle-income earners
   - Replaces complex calculation with simple threshold

2. **PAYE Rate Changes**
   - **OLD Rates**: 7%, 11%, 15%, 19%, 21%, 24%
   - **NEW Rates**: 0%, 15%, 18%, 21%, 23%, 25%
   - Fewer bands, simpler calculation
   - Top rate increased from 24% to 25%

3. **Relief Allowance Overhaul**
   - **❌ ELIMINATED**: Consolidated Relief Allowance (CRA)
   - **✨ NEW**: Rent Relief = 20% of annual rent, max ₦500,000
   - Much simpler to calculate
   - Directly benefits renters

4. **Progressive Tax Bands Updated**
   - **OLD**: Complex 6-band structure with varying thresholds
   - **NEW**: Simplified 6-band structure with clearer thresholds
   - Better alignment with current economic realities

### Comparison Table:

| Aspect | Pre-2026 (OLD) | 2026+ (NEW) |
|--------|---------------|-------------|
| Tax-Free Amount | ~₦200k-₦300k (via CRA) | **₦800,000** |
| Lowest Rate | 7% | **0%** |
| Highest Rate | 24% | **25%** |
| Relief Type | CRA (complex formula) | **Rent Relief (20% of rent)** |
| Tax Bands | 6 bands | 6 bands (new thresholds) |

---

## ⚠️ Important Notes

1. **Effective Date: January 1, 2026**
   - The Nigeria Tax Act, 2025 was signed on June 26, 2025
   - All PAYE provisions take effect from January 1, 2026
   - 2025 is a transition period

2. **For Informational Purposes Only**
   - This calculator provides estimates based on Nigeria Tax Act 2025
   - Always consult a qualified tax professional for official advice
   - Tax laws may be subject to interpretation and regulations

3. **Simplified Calculations**
   - Pension contributions and other deductions not included
   - Life insurance relief not included
   - National Housing Fund (NHF) deductions not included
   - Assumes employment income only

4. **Data Privacy**
   - All calculations are performed locally in your browser
   - No data is sent to any server
   - Your salary information remains completely private

5. **Accuracy**
   - Based on the Nigeria Tax Act, 2025 as published
   - Progressive PAYE rates verified against official sources
   - Rent Relief follows Section 30(vi) of the Act

6. **Rent Relief Requirements**
   - Must provide evidence of rent payment
   - Maximum ₦500,000 per year
   - Replaces the old Consolidated Relief Allowance

---

## 🆘 Troubleshooting

### Calculator Won't Open:
- Make sure you have a modern web browser (Chrome, Firefox, Edge, Safari)
- Try right-clicking and "Open with" → Choose browser
- Check that JavaScript is enabled

### Results Not Showing:
- Ensure you've entered annual gross salary
- Check that salary is a positive number
- Click "Calculate PAYE" button

### Unexpected Tax Amount:
- Remember: First ₦800k is tax-free!
- Check if Rent Relief is applied correctly
- Review the tax calculation breakdown table
- Verify your taxable income after rent relief

### Tax-Free Status Not Showing:
- Employee must have taxable income ≤₦800,000
- Taxable Income = Gross Salary - Rent Relief
- Rent Relief = 20% of annual rent, max ₦500k

---

## 📞 Support & Feedback

For questions, suggestions, or to report issues:
- Create an issue in this repository
- Mention "PAYE Calculator" in your query

---

## 📜 License & Disclaimer

**Disclaimer**: This calculator is provided "as is" for informational and educational purposes only. PAYE calculations are based on the Nigeria Tax Act, 2025 (Signed June 26, 2025 | Effective January 1, 2026). Users should consult qualified tax professionals for official tax advice and compliance.

**Copyright**: © 2025 Olusola's AI Assistant

---

## 🔄 Version History

### Version 2.1 (PAYE-Only) - January 2026
- 🔄 **Simplified to PAYE-only calculator**
- ✅ Removed company tax calculations (CIT, CGT, etc.)
- ✅ Focused on personal income tax (PAYE)
- ✅ Enhanced monthly breakdown display
- ✅ Added detailed tax calculation table
- ✅ Improved tax-free status detection
- ✅ Summary view for multiple employees
- ✅ Cleaner, simplified interface

### Version 2.0 (Full Tax Calculator) - January 2026
- 🔄 **MAJOR UPDATE**: Implemented Nigeria Tax Act 2025
- ✨ Company and personal tax calculations
- ✨ Small company exemptions
- ✨ Development Levy
- ✨ Minimum ETR for large companies

### Version 1.0 - DEPRECATED
- ❌ Used outdated pre-2025 tax rates

---

## 🎯 Calculator Accuracy

This calculator uses the **correct** PAYE provisions from the Nigeria Tax Act, 2025:

✅ PAYE progressive bands (0%, 15%, 18%, 21%, 23%, 25%)
✅ Tax-free threshold (₦800,000)
✅ Rent Relief (20% of rent, max ₦500k)
✅ Proper progressive tax calculation
✅ Monthly breakdown
✅ Tax-free status detection

---

## 📚 Official Sources

- [Nigeria Tax Act, 2025 (Official PDF)](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf)
- [Nigeria Tax Administration Act, 2025](https://tat.gov.ng/NIGERIA-TAX-ADMINISTRATION-ACT-2025.pdf)
- [EY - Nigeria Tax Act Highlights](https://www.ey.com/en_gl/technical/tax-alerts/nigeria-tax-act-2025-has-been-signed-highlights)
- [PWC - Nigerian Tax Reform Acts](https://www.pwc.com/ng/en/publications/the-nigerian-tax-reform-acts.html)
- [KPMG - Nigeria Tax Act Overview](https://assets.kpmg.com/content/dam/kpmg/ng/pdf/2025/06/The%20Nigeria%20Tax%20Act%20(NTA),%202025.pdf)
- [New PAYE Computation Guide](https://taxclearancecertificate.com/new-paye-computation-under-the-nigeria-tax-act-nta-2025-everything-you-need-to-know/)

---

Made with ❤️ for Nigerian workers and employers | Accurate as of Nigeria Tax Act, 2025
