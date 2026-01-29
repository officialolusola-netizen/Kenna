#!/usr/bin/env python3
"""
Nigerian Tax Calculator 2025 - Launcher Script
Opens the offline calculator in your default web browser
"""

import webbrowser
import os
import sys

def launch_calculator():
    """Launch the Nigerian Tax Calculator in the default web browser."""

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the HTML calculator
    calculator_path = os.path.join(script_dir, 'nigerian_tax_calculator.html')

    # Check if the file exists
    if not os.path.exists(calculator_path):
        print("❌ Error: nigerian_tax_calculator.html not found!")
        print(f"   Looking for: {calculator_path}")
        print("\nPlease ensure the HTML file is in the same directory as this script.")
        sys.exit(1)

    # Convert to file:// URL
    calculator_url = f"file://{calculator_path}"

    print("🚀 Nigerian Tax Calculator 2025")
    print("=" * 60)
    print(f"📂 Location: {calculator_path}")
    print(f"🌐 Opening in browser: {calculator_url}")
    print("=" * 60)

    try:
        # Open in default web browser
        webbrowser.open(calculator_url)
        print("\n✅ Calculator opened successfully!")
        print("   If the browser doesn't open, you can manually open:")
        print(f"   {calculator_path}")
        print("\n💡 Tip: Bookmark the calculator for quick access!")

    except Exception as e:
        print(f"\n❌ Error opening browser: {e}")
        print("\nPlease open the file manually:")
        print(f"   {calculator_path}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        launch_calculator()
    except KeyboardInterrupt:
        print("\n\n⚠️  Launch cancelled by user")
        sys.exit(0)
