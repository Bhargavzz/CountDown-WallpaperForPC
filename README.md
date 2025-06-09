# CountDown Wallpaper for PC
Automatically set your desktop wallpaper to display a countdown to any date. The wallpaper updates daily to show the remaining days.

## Features
- Automatic daily countdown calculation
- Customizable font, size, and position
- Optional background image support
- Dual-trigger automation (startup + logon)
- Battery-friendly operation
- Simple setup and configuration

## Prerequisites
- Python 3.x installed
- Windows OS (for automatic wallpaper setting)



## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/CountDown-WallpaperForPC.git
cd CountDown-WallpaperForPC
```

### Step 2: Install Required Packages
```bash
pip install pillow
```

## Configuration

### Step 3: Customize Countdown Settings
Open `countdown.py` and modify these settings:

```python
# Set your target date (YYYY, MM, DD)
target_date = date(2025, 12, 31)  # Replace with your target date

# Specify font path (default: Windows Arial)
font_path = r"C:\Windows\Fonts\arial.ttf"  # Update if using custom font

# Adjust font size (default: 150)
font_size = 150  # Modify as needed

# Custom background image (optional)
background_path = "default_background.jpg"  # Replace with your custom image
```

**Optional Customization**:
- Place custom background images in the project folder
- Adjust text position or color by modifying corresponding variables
- Change countdown text format (e.g., add hours/minutes)

## Manual Execution
Test the script immediately:
```bash
python countdown.py
```
Your wallpaper should update with the number of days remaining.

## Automated Daily Updates (Recommended)

### Step 4: Configure Task Scheduler
Set up automatic daily updates:

1. Open **Task Scheduler** (search in Windows Start menu)
2. Click **Create Task** (not Basic Task)

#### General Tab
- Name: `Daily Countdown Update`
- Check: "Run whether user is logged on or not"
- Check: "Run with highest privileges"

#### Triggers Tab → New
- Begin the task: `At startup`
- Enabled: `Yes`

→ Click **New** again to add second trigger:
- Begin the task: `At log on`
- Enabled: `Yes`

#### Conditions Tab
- **Uncheck**: "Start the task only if the computer is on AC power"
- **Uncheck**: "Start only if the computer is idle"
- **Uncheck**: "Stop if the computer ceases to be idle"
- **Check**: "Wake the computer to run this task"

#### Actions Tab → New
- Action: "Start a program"
- Configure:
  ```
  Program/script: "C:\Path\To\Python\python.exe"
  Add arguments: "C:\Path\To\CountDown-WallpaperForPC\countdown.py"
  Start in: "C:\Path\To\CountDown-WallpaperForPC"
  ```

#### Settings Tab
- Allow task to be run on demand
- Stop task if running longer than: `1 hour`
- If running task fails: Restart every `5 minutes` (max 3 times)

**Important Path Notes**:
- Find Python path with: `where python` in Command Prompt
- Use your actual script location for arguments
- Example paths:
  ```
  Program/script: "C:\Python39\python.exe"
  Add arguments: "C:\Users\YourName\Documents\CountDown-WallpaperForPC\countdown.py"
  Start in: "C:\Users\YourName\Documents\CountDown-WallpaperForPC"
  ```

## Verification
After setup:
1. Reboot your computer
2. Immediately after startup/login, your wallpaper should update
3. Verify in Task Scheduler:
   - Right-click task → **Run** to test immediately
   - Check **Last Run Result** (should show 0x0 for success)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Wallpaper not updating** | Run script manually to verify paths<br>Check Python permissions<br>Run Task Scheduler as Admin |
| **Font errors** | Verify font path in script<br>Use absolute path to font file |
| **Countdown text position** | Adjust `text_x` and `text_y` values<br>Use smaller font size for different resolutions |
| **Task fails to run** | Confirm all trigger conditions are disabled<br>Check "Run with highest privileges"<br>Verify Python path is correct |
| **Custom background not loading** | Ensure image is in project folder<br>Confirm filename matches script<br>Use supported formats (JPG/PNG) |
| **Script runs too early** | Add a 10-30 second delay in triggers if needed<br>Check system performance during startup |

> **Note**: The script must remain in its folder with any required assets (fonts/images) for daily updates to work correctly.

## Customization Options
Edit these variables in `countdown.py`:
```python
# Text customization
text_color = (255, 255, 255)  # RGB values (white)
shadow_color = (0, 0, 0)       # Text shadow (black)
text_x = 100                   # Horizontal position
text_y = 200                   # Vertical position

# Countdown format
days_only = False              # Set True for "X days" format
```

## Uninstallation
1. Open Task Scheduler
2. Find and delete "Daily Countdown Update" task
3. Delete the CountDown-WallpaperForPC folder
4. Manually reset your wallpaper via Windows Settings

## Support
For additional help:
- [Report issues on GitHub](https://github.com/yourusername/CountDown-WallpaperForPC/issues)
- Check Windows Event Viewer → Applications and Services Logs → Microsoft → Windows → TaskScheduler

---

**Enjoy your custom countdown wallpaper!** The script will automatically update daily until your target date is reached.
