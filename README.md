# Kenna
All work pertaining to kenna

---

> **⚠️ THIS IS DOCUMENTATION - NOT THE CALCULATOR!**
>
> **To use the calculator:**
> - Open `index.html` OR `nigerian_tax_calculator.html` in your browser
> - Do NOT open this file (README.md) - it's just documentation
> - See `START_HERE.txt` for quick instructions

---

## 🧮 Nigerian PAYE Calculator - Nigeria Tax Act 2025

### Offline PAYE (Personal Income Tax) Calculator

A simple, offline-capable PAYE calculator based on the **Nigeria Tax Act, 2025** (Signed June 26, 2025 | Effective January 1, 2026). Calculates employee personal income tax with the new progressive rates and tax-free threshold.

### ⚠️ Important: Effective Date
**The Nigeria Tax Act, 2025 takes effect on January 1, 2026.** This calculator uses the new PAYE rates that apply starting 2026.

### 📥 Quick Access

**File**: `nigerian_tax_calculator.html`

**Download & Use**:
1. Download `nigerian_tax_calculator.html` to your computer
2. Double-click to open in your browser
3. Works completely offline - no internet required!

**OR use the Python launcher**:
```bash
python launch_calculator.py
```

### ✨ Key Features (Nigeria Tax Act 2025)

- ✅ **PAYE Progressive Bands** - **0%, 15%, 18%, 21%, 23%, 25%**
- ✅ **Tax-Free Threshold** - First **₦800,000** completely tax-free!
- ✅ **Rent Relief** - 20% of annual rent, max ₦500k (replaces CRA)
- ✅ **Monthly Breakdown** - Shows monthly gross, PAYE, and net salary
- ✅ **Detailed Tax Calculation** - Per-band breakdown table
- ✅ **Tax-Free Status Detection** - Automatic when taxable income ≤₦800k
- ✅ **Multi-Employee Support** - Calculate for multiple people at once
- ✅ **Summary View** - Total gross, PAYE, and net for all employees
- ✅ **Professional UI** - Clean, modern design with Nigerian colors
- ✅ **100% Offline** - No internet needed after download
- ✅ **Mobile Friendly** - Responsive design works on all devices

### 📖 Documentation

See [CALCULATOR_README.md](CALCULATOR_README.md) for:
- Detailed installation instructions
- PAYE tax rates reference (Nigeria Tax Act 2025)
- What's new compared to previous law
- Usage guide with examples
- Troubleshooting tips
- Official sources and references

### 🎯 What's Calculated

The calculator computes **PAYE (Personal Income Tax)** under the Nigeria Tax Act 2025:

1. **Rent Relief** - 20% of annual rent paid, capped at ₦500,000
2. **Taxable Income** - Gross salary minus rent relief
3. **PAYE Tax** - Using progressive bands (0%-25%)
4. **Net Salary** - Annual and monthly after-tax income
5. **Tax-Free Status** - Automatic detection if taxable income ≤₦800,000
6. **Detailed Breakdown** - Per-band tax calculation table

### 📊 PAYE Tax Bands (Nigeria Tax Act 2025)

| Taxable Income Range | Tax Rate |
|---------------------|----------|
| First ₦800,000 | **0%** (Tax-Free! 🎉) |
| ₦800,001 - ₦3,000,000 | 15% |
| ₦3,000,001 - ₦10,000,000 | 18% |
| ₦10,000,001 - ₦25,000,000 | 21% |
| ₦25,000,001 - ₦50,000,000 | 23% |
| Above ₦50,000,000 | 25% |

### 🎉 What's New in Nigeria Tax Act 2025

**Major PAYE Changes:**
- **Tax-Free Threshold**: First ₦800,000 is tax-free (NEW!)
- **PAYE Rates**: 0%, 15%, 18%, 21%, 23%, 25% (OLD: 7%, 11%, 15%, 19%, 21%, 24%)
- **Rent Relief**: Replaces the old Consolidated Relief Allowance (CRA)
- **Simpler Calculation**: Clearer thresholds and fewer complexities

### ⚠️ Disclaimer

This calculator is for informational purposes only and implements PAYE provisions from the Nigeria Tax Act, 2025 (Effective Jan 1, 2026). Always consult a qualified tax professional for official tax advice and compliance.

---

## 📂 Repository Contents

- `nigerian_tax_calculator.html` - Offline PAYE calculator (main file)
- `launch_calculator.py` - Python launcher script
- `CALCULATOR_README.md` - Comprehensive PAYE documentation
- `Credit_Facilitation_Nigeria.pptx` - Credit facilitation presentation
- `create_presentation.py` - Presentation generator script
