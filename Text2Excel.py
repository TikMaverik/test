import pandas as pd

def parse_shortcuts_to_excel(input_text, excel_file_path):
    # Split the input text into sections based on headers
    sections = input_text.split("\n\n")
    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
        for section in sections:
            lines = section.split("\n")
            if len(lines) > 1:  # Check if section contains more than the title
                header = lines[0]  # First line is the category title
                shortcuts = [line.split(": ", 1) for line in lines[1:] if ": " in line]  # Split each line into shortcut and action
                if shortcuts:
                    df = pd.DataFrame(shortcuts, columns=["Shortcut", "Action"])  # Create DataFrame
                    df.to_excel(writer, sheet_name=header[:31], index=False)  # Write to sheet, sheet name limited to 31 chars

# Example usage
input_text = """
Control-Option-Command-8: invert colours.
Control-Option-Command-Comma (,) and Control-Option-Command-Full stop (.): reduce contrast and increase contrast.
Note: Use these shortcuts to change keyboard focus. To use some of these shortcuts, first choose Apple menu  > System Settings (or System Preferences), then click Keyboard. Click Keyboard Shortcuts, select Keyboard on the left then select the shortcut’s setting on the right.
Control-F2 or Fn-Control-F2: move focus to the menu bar. You can then use the arrow keys to navigate the menu, press Return to open a selected menu or choose a selected menu item, or enter the menu item’s name to jump to that item in the selected menu.
Control-F3 or Fn-Control-F3: move focus to the Dock.
Control-F4 or Fn-Control-F4: move focus to the active window or next window.
Control-F5 or Fn-Control-F5: move focus to the window toolbar.
Control-F6 or Fn-Control-F6: move focus to the floating window.
Control-Shift-F6: move focus to the previous panel.
Control-F7 or Fn-Control-F7: change the way Tab moves focus – between navigation of all controls on the screen, or only text boxes and lists.
Control-F8 or Fn-Control-F8: move focus to the status menu in the menu bar
Command-Grave accent (`): activate the next open window in the front app.
Shift-Command-Grave accent (`): activate the previous open window in the front app
Option-Command-Grave accent (`): move the focus to the window drawer.
Tab and Shift-Tab: move to the next control, move to the previous control.
Control-Tab: move to the next control when a text field is selected.
Control-Shift-Tab: move to the previous grouping of controls.
Arrow keys: move to the adjacent item in a list, tab group or menu, or move sliders and adjusters (Up Arrow to increase values, Down Arrow to decrease values)
Control-Arrow keys: move to a control adjacent to the text field.
"""

excel_file_path = "Mac_Keyboard_Shortcuts.xlsx"
parse_shortcuts_to_excel(input_text, excel_file_path)


#test
