# CountDown-WallpaperForPC
Set Your Wallpaper to Display a Countdown for Any Date

# Wallpaper Countdown Setup

This project automatically sets your desktop wallpaper to display a countdown to any date you choose. The wallpaper updates daily to show the remaining days.

## Prerequisites
- Python 3.x installed
- Windows OS (for automatic wallpaper setting)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Step 2: Prepare Your Environment
Install the required Python library Pillow:
```bash
pip install pillow
```

## Configuration

### Step 3: Update the Script Settings
Open `countdown.py` and modify these settings:

```python
# Set your target date (YYYY, MM, DD)
target_date = date(2025, 12, 31)  # Replace with your target date

# Specify font path (default: Windows Arial)
font_path = r"C:\Windows\Fonts\arial.ttf"  # Update if using custom font

# Adjust font size (default: 150)
font = ImageFont.truetype(font_path, 150)  # Modify font size as needed
```

**Optional Customization**:
- Place a custom background image in the same folder and update the path in the script
- Adjust text position or color by modifying the corresponding variables

## Usage

### Step 4: Run the Script
```bash
python countdown.py
```
The wallpaper will update automatically with the number of days remaining.

## Automation (Optional)

### Step 5: Automate Daily Updates on Windows
1. Open **Task Scheduler**
2. Create a **Basic Task**
3. Set trigger to **Daily**
4. Set action to **Start a Program**
5. Configure:
   - Program/script: Path to your Python executable (`python.exe`)
   - Add arguments: Full path to your script (e.g. `"C:\Users\vishn\OneDrive\Desktop\Countdown\countdown.py"`)
   - Start in: Directory containing your script (e.g. `C:\Users\vishn\OneDrive\Desktop\Countdown\`)

## Troubleshooting
- **Font issues**: Verify the font file exists at the specified path
- **Wallpaper not updating**:
  - Ensure Python has permission to change system settings
  - Run script as administrator if needed
- **Custom background**:
  - Place image in project directory
  - Update `background_path` in the script
- **Script errors**:
  - Confirm Python 3 is installed
  - Verify all required packages are installed (`pip install pillow`)

## Features
- Automatic daily countdown calculation
- Customizable font, size, and position
- Optional background image support
- Simple setup and configuration

> **Note**: The script must remain in its folder with any required assets (fonts/images) for daily updates to work correctly.

