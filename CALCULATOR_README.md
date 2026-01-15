# Nigerian Tax Calculator - Nigeria Tax Act 2025

## 📥 Download & Installation Instructions

### ⚠️ Important: Effective Date
**The Nigeria Tax Act, 2025 was signed on June 26, 2025 and takes effect on January 1, 2026.**
This calculator reflects the new tax laws that will be in effect starting 2026.

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
   - Total Fixed Assets (required - for Small Company determination)

2. **Add Employee Information**
   - Enter annual salary for each employee
   - Enter annual rent paid by employee (for Rent Relief calculation)
   - Click "Add Another Employee" to add more employees
   - PAYE is calculated automatically using the new progressive tax bands

3. **Enter Other Tax Information** (Optional)
   - Asset disposal proceeds and cost basis (for CGT)
   - VAT-taxable sales
   - Withholding tax income and payments

4. **Calculate**
   - Click the "Calculate Taxes" button
   - View comprehensive results on the right panel

5. **Review Results**
   - Company status (Small Company exemption if applicable)
   - Revenue breakdown
   - Company tax liability (CIT, Development Levy, CGT, Min ETR)
   - Employee PAYE breakdown with tax-free status
   - VAT and WHT information
   - Net income (monthly and annual)

---

## 📊 What This Calculator Does

### Taxes Calculated (Nigeria Tax Act 2025):

1. **Company Income Tax (CIT)** - 30% of assessable profit
2. **Development Levy** - 4% of assessable profit (replaces TET, NASENI, IT Levy, Police Trust Fund)
3. **Capital Gains Tax (CGT)** - 30% on chargeable gains (increased from 10%)
4. **Pay As You Earn (PAYE)** - Progressive rates: 0%, 15%, 18%, 21%, 23%, 25%
5. **Value Added Tax (VAT)** - 7.5% (informational)
6. **Withholding Tax (WHT)** - 10% standard rate (credit against CIT)
7. **Minimum Tax** - 0.5% of turnover (when no profit)
8. **Minimum Effective Tax Rate** - 15% for large companies (₦20B+ revenue)

### Key Features:

✅ **Tax-Free Threshold** - First ₦800,000 of taxable income is tax-free!
✅ **Small Company Exemption** - Companies with ≤₦50M turnover and ≤₦250M fixed assets are exempt from CIT, CGT, Development Levy, and WHT
✅ **Rent Relief** - Replaces CRA: 20% of annual rent, capped at ₦500,000
✅ **Accurate PAYE** - Uses new progressive tax bands with updated rates
✅ **Large Company Minimum ETR** - Companies with ₦20B+ revenue must maintain 15% effective tax rate
✅ **Per-Employee PAYE Breakdown** - Individual calculations showing tax-free status
✅ **Professional UI** - Clean, modern interface with color-coded results
✅ **100% Offline** - No internet connection required after download
✅ **Mobile Friendly** - Responsive design works on all devices

---

## 📋 Tax Rates Reference (Nigeria Tax Act 2025)

### PAYE Progressive Bands (Effective Jan 1, 2026):

| Taxable Income Range | Tax Rate |
|---------------------|----------|
| First ₦800,000 | **0%** (Tax-Free!) |
| ₦800,001 - ₦3,000,000 | 15% |
| ₦3,000,001 - ₦10,000,000 | 18% |
| ₦10,000,001 - ₦25,000,000 | 21% |
| ₦25,000,001 - ₦50,000,000 | 23% |
| Above ₦50,000,000 | 25% |

### Relief Allowance Changes:
- **OLD (Pre-2026)**: Consolidated Relief Allowance (CRA) = max(1% of gross, ₦200k + 20% of gross)
- **NEW (2026+)**: Rent Relief = 20% of annual rent paid, capped at ₦500,000

### Company Tax Rates:
- **CIT**: 30% (retained)
- **VAT**: 7.5% (retained)
- **CGT**: **30%** (increased from 10%)
- **Development Levy**: **4%** (replaces TET at 2%)
- **WHT**: 10% standard rate (various rates by transaction type)
- **Minimum Tax**: 0.5% of gross turnover
- **Minimum ETR**: 15% for companies with ₦20B+ annual revenue

### Small Company Definition (Tax-Exempt):
- Annual turnover ≤ ₦50,000,000 **AND**
- Total fixed assets ≤ ₦250,000,000

**Exemptions for Small Companies:**
- Company Income Tax (CIT): 0%
- Capital Gains Tax (CGT): 0%
- Development Levy: 0%
- Withholding Tax (WHT): Exempt

### CGT Exemption Threshold:
- Asset disposal proceeds < ₦150,000,000 **AND**
- Chargeable gains < ₦10,000,000 in any 12 consecutive months

---

## 💡 Usage Examples

### Example 1: Small Business (Tax-Exempt!)
```
Annual Gross Income: ₦40,000,000
Operating Expenses: ₦25,000,000
Fixed Assets: ₦180,000,000
Employees: 2 (₦1,500,000 and ₦1,000,000 annually)

Result: QUALIFIES AS SMALL COMPANY
- Company Tax: ₦0 (EXEMPT)
- Only PAYE applies to employees
```

### Example 2: Medium Enterprise
```
Annual Gross Income: ₦150,000,000
Operating Expenses: ₦80,000,000
Fixed Assets: ₦300,000,000
Employees: 5 (various salaries)
VAT-Taxable Sales: ₦120,000,000

Company Taxes:
- CIT (30%): ₦21,000,000
- Development Levy (4%): ₦2,800,000
- Total: ₦23,800,000
```

### Example 3: Large Corporation (Minimum ETR Applies)
```
Annual Gross Income: ₦25,000,000,000
Operating Expenses: ₦18,000,000,000
Fixed Assets: ₦10,000,000,000
Employees: 100+ (various salaries)

Company Taxes:
- CIT (30%): ₦2,100,000,000
- Development Levy (4%): ₦280,000,000
- Effective Tax Rate: 34% (exceeds 15% minimum)
```

---

## 🎯 What's New in Nigeria Tax Act 2025

### Major Changes from Previous Law:

1. **PAYE Tax-Free Threshold**
   - ✨ NEW: First ₦800,000 completely tax-free
   - Simplifies tax calculation for low-income earners

2. **PAYE Rate Changes**
   - Reduced number of bands from 6 to 6 (but different thresholds)
   - New rates: 0%, 15%, 18%, 21%, 23%, 25%
   - Top rate increased from 24% to 25%

3. **Relief Allowance Overhaul**
   - ❌ ELIMINATED: Consolidated Relief Allowance (CRA)
   - ✨ NEW: Rent Relief (20% of rent, max ₦500k)

4. **Capital Gains Tax Increase**
   - OLD: 10%
   - NEW: 30% (matches CIT rate)
   - Added exemption threshold

5. **Development Levy** (Consolidation)
   - ❌ ELIMINATED: Tertiary Education Tax (2%)
   - ❌ ELIMINATED: NASENI Levy
   - ❌ ELIMINATED: IT Development Levy
   - ❌ ELIMINATED: Police Trust Fund Levy
   - ✨ NEW: Single Development Levy (4%)

6. **Small Company Exemption**
   - ✨ NEW: Full tax exemption for qualifying small companies
   - Criteria: ≤₦50M turnover AND ≤₦250M fixed assets

7. **Minimum Effective Tax Rate**
   - ✨ NEW: 15% minimum ETR for large companies (₦20B+ revenue)
   - Prevents low tax rates through aggressive planning

---

## ⚠️ Important Notes

1. **Effective Date: January 1, 2026**
   - The Nigeria Tax Act, 2025 was signed on June 26, 2025
   - All provisions take effect from January 1, 2026
   - 2025 is a transition period

2. **For Informational Purposes Only**
   - This calculator provides estimates based on Nigeria Tax Act 2025
   - Always consult a qualified tax professional for official advice
   - Tax laws may be subject to interpretation and additional regulations

3. **Simplified Calculations**
   - Some tax calculations may involve additional complexities
   - Capital allowances, loss carry-forward, and other deductions are not included
   - Industry-specific tax rates and special provisions may apply

4. **Data Privacy**
   - All calculations are performed locally in your browser
   - No data is sent to any server
   - Your financial information remains completely private

5. **Accuracy**
   - Based on the Nigeria Tax Act, 2025 as published
   - Progressive PAYE rates verified against official sources
   - Development Levy consolidates multiple previous levies

6. **Professional Services Exemption**
   - Professional services businesses do NOT qualify as small companies
   - Regardless of turnover or asset thresholds

---

## 🆘 Troubleshooting

### Calculator Won't Open:
- Make sure you have a modern web browser installed (Chrome, Firefox, Edge, Safari)
- Try right-clicking the file and select "Open with" → Choose your browser
- Check that JavaScript is enabled in your browser settings

### Results Not Showing:
- Ensure you've filled in the required fields marked with (*)
- Annual Gross Income, Operating Expenses, and Fixed Assets are required
- Check that all numbers are positive (no negative values)
- Try clicking "Reset Form" and re-entering data

### Display Issues:
- Try zooming in/out in your browser (Ctrl/Cmd + or -)
- Refresh the page (F5 or Ctrl/Cmd + R)
- Clear browser cache if necessary
- Try a different browser

### Unexpected Results:
- Verify Small Company status (turnover and asset thresholds)
- Check if Large Company Minimum ETR applies (₦20B+ revenue)
- Confirm employee salary inputs and rent amounts
- Review the per-employee breakdown for PAYE details

### Tax-Free Status Not Showing:
- Employee must have taxable income ≤₦800,000 (after rent relief)
- Rent Relief = 20% of annual rent, max ₦500k
- Check that rent amount is entered correctly

---

## 📞 Support & Feedback

For questions, suggestions, or to report issues:
- Create an issue in this repository
- Ensure you mention "Nigeria Tax Act 2025" in your query

---

## 📜 License & Disclaimer

**Disclaimer**: This calculator is provided "as is" for informational and educational purposes only. The authors make no warranties about the accuracy, completeness, or reliability of the calculations. Tax calculations are based on the Nigeria Tax Act, 2025 as signed on June 26, 2025, with an effective date of January 1, 2026. Users should consult qualified tax professionals for official tax advice and compliance.

**Copyright**: © 2025 Olusola's AI Assistant

---

## 🔄 Version History

### Version 2.0 (January 2026)
- 🔄 **MAJOR UPDATE**: Implemented Nigeria Tax Act 2025 provisions
- ✨ PAYE: New progressive bands (0%, 15%, 18%, 21%, 23%, 25%)
- ✨ Tax-free threshold: First ₦800,000 exempt
- ✨ Rent Relief: Replaced CRA with 20% of rent (max ₦500k)
- ✨ CGT: Increased from 10% to 30%
- ✨ Development Levy: 4% (replaces TET and other levies)
- ✨ Small Company Exemption: 0% tax for qualifying companies
- ✨ Minimum ETR: 15% for large companies (₦20B+)
- 🎨 Updated UI with Nigerian green color scheme
- 📋 Added comprehensive status indicators
- ✅ Fixed all tax calculation inaccuracies

### Version 1.0 (December 2025) - DEPRECATED
- ❌ Used outdated pre-2025 tax rates
- ❌ Incorrect PAYE bands
- ❌ Incorrect relief allowance (CRA)
- ❌ Incorrect CGT rate (10%)

---

## 🎯 Calculator Accuracy

This calculator now uses the **correct** provisions from the Nigeria Tax Act, 2025:

✅ PAYE progressive bands (0%, 15%, 18%, 21%, 23%, 25%)
✅ Tax-free threshold (₦800,000)
✅ Rent Relief (20% of rent, max ₦500k)
✅ CGT rate (30%)
✅ Development Levy (4%)
✅ Small Company exemption (≤₦50M turnover, ≤₦250M assets)
✅ Minimum ETR (15% for ₦20B+ companies)
✅ WHT credit system
✅ Minimum Tax (0.5%)
✅ VAT rate (7.5%)

---

## 📚 Official Sources

- [Nigeria Tax Act, 2025 (Official PDF)](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf)
- [Nigeria Tax Administration Act, 2025](https://tat.gov.ng/NIGERIA-TAX-ADMINISTRATION-ACT-2025.pdf)
- [EY - Nigeria Tax Act Highlights](https://www.ey.com/en_gl/technical/tax-alerts/nigeria-tax-act-2025-has-been-signed-highlights)
- [PWC - Nigerian Tax Reform Acts](https://www.pwc.com/ng/en/publications/the-nigerian-tax-reform-acts.html)
- [KPMG - Nigeria Tax Act Overview](https://assets.kpmg.com/content/dam/kpmg/ng/pdf/2025/06/The%20Nigeria%20Tax%20Act%20(NTA),%202025.pdf)

---

Made with ❤️ for Nigerian businesses | Accurate as of Nigeria Tax Act, 2025
