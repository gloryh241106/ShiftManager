"""Export the PA3 wireframes (Figures 6.2 to 6.12) from the prototype as PNG.

Edit ShiftManager-Prototype-PA3.html, then run:
    python capture_wireframes.py
Needs Microsoft Edge and Pillow (pip install pillow). Each screen opens with a
#shot=sXX hash that sets the user and screen shown in the figure.
"""
import os, subprocess, tempfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
PAGE = 'file:///' + os.path.join(HERE, 'ShiftManager-Prototype-PA3.html').replace('\\', '/')
SHOTS = {  # figure: (hash, file name)
    '6.2': ('s03', 'F6.2-S03-schedule-update.png'),
    '6.3': ('s04', 'F6.3-S04-weekly-scheduling.png'),
    '6.4': ('s07', 'F6.4-S07-absence-coverage.png'),
    '6.5': ('s09', 'F6.5-S09-employee-accounts.png'),
    '6.6': ('s10', 'F6.6-S10-availability-overtime.png'),
    '6.7': ('s01', 'F6.7-S01-login.png'),
    '6.8': ('s02', 'F6.8-S02-my-schedule.png'),
    '6.9': ('s05', 'F6.9-S05-team-schedule.png'),
    '6.10': ('s06', 'F6.10-S06-report-absence.png'),
    '6.11': ('s08', 'F6.11-S08-staffing-overview.png'),
    '6.12': ('s11', 'F6.12-S11-staffing-configuration.png'),
}


def capture(shot, out):
    prof = tempfile.mkdtemp(prefix='edge-wf-')
    for _ in range(3):
        try:
            subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1.5',
                            '--window-size=1120,2600', '--user-data-dir=' + prof, '--screenshot=' + out, PAGE + '#shot=' + shot],
                           timeout=60, capture_output=True)
        except subprocess.TimeoutExpired:
            continue
        if os.path.exists(out):
            break
    im = Image.open(out).convert('RGB')
    w, h = im.size
    px = im.load()
    bg = px[5, h - 5]
    y = h - 1
    while y > 0 and all(px[x, y] == bg for x in range(0, w, 7)):
        y -= 1
    im.crop((0, 0, w, min(h, y + 36))).save(out)


if __name__ == '__main__':
    for fig, (shot, name) in SHOTS.items():
        capture(shot, os.path.join(HERE, name))
        print('Figure', fig, name)
