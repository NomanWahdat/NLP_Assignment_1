import re
import tkinter as tk  # Import tkinter as tk to use tk.END
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
from tkinter import messagebox


# Custom classes for each task
class CustomRegex:
    @staticmethod
    def extract_domain(url):
        pattern = r"https?://(www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]+"
        match = re.search(pattern, url)
        return match.group(2) if match else "No domain found."


class DateExtractor:
    @staticmethod
    def extract_dates(text):
        pattern = r"\b(\d{2}|\d{4})[-/](\d{2})[-/](\d{2}|\d{4})\b"
        matches = re.findall(pattern, text)
        formatted_dates = []
        for match in matches:
            if len(match[0]) == 4:
                year, month, day = match
            elif len(match[2]) == 4:
                day, month, year = match
            else:
                month, day, year = match
            formatted_dates.append(f"{year}-{month}-{day}")
        return formatted_dates if formatted_dates else "No dates found."


class PriceExtractor:
    @staticmethod
    def extract_prices(text):
        pattern = r"(\$|€|¥)(\d+(?:\.\d{2})?)"
        return re.findall(pattern, text) or "No prices found."


class HyperlinkExtractor:
    @staticmethod
    def extract_links(html):
        pattern = r'<a\s+href=["\'](http[^"\']+)["\']'
        return re.findall(pattern, html) or "No hyperlinks found."


class SpellingCorrector:
    @staticmethod
    def correct_spelling(text):
        corrections = {r"\bteh\b": "the", r"\brecieve\b": "receive"}
        for mistake, correction in corrections.items():
            text = re.sub(mistake, correction, text)
        return text


class AddressExtractor:
    @staticmethod
    def extract_addresses(text):
        pattern = r"\b\d+\s+\w+\s+(Street|St|Avenue|Ave|Road|Rd|Lane|Ln)\b"
        matches = re.findall(pattern, text)
        return matches if matches else "No addresses found."


class HexColorExtractor:
    @staticmethod
    def extract_hex_colors(css_text):
        pattern = r"#([A-Fa-f0-9]{6})\b"
        matches = re.findall(pattern, css_text)
        return matches if matches else "No hex color codes found."


# GUI Application Class
class AdvancedRegexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Regex Tool")
        self.root.geometry("700x500")

        # Create a styled notebook (tabbed interface)
        self.tabs = ttk.Notebook(root, bootstyle="dark")
        self.tabs.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Initialize tabs for each task
        self.create_task_tab("Extract Domain", CustomRegex.extract_domain, "Enter URL:")
        self.create_task_tab("Extract Dates", DateExtractor.extract_dates, "Enter Text with Dates:")
        self.create_task_tab("Extract Prices", PriceExtractor.extract_prices, "Enter Text with Prices:")
        self.create_task_tab("Extract Hyperlinks", HyperlinkExtractor.extract_links, "Enter HTML Code:")
        self.create_task_tab("Correct Spelling", SpellingCorrector.correct_spelling, "Enter Text with Mistakes:")
        self.create_task_tab("Extract Addresses", AddressExtractor.extract_addresses, "Enter Text with Addresses:")
        self.create_task_tab("Extract Hex Colors", HexColorExtractor.extract_hex_colors, "Enter CSS Text:")

    def create_task_tab(self, title, function, input_label):
        # Create a frame for each task
        tab_frame = ttk.Frame(self.tabs, padding=20)
        self.tabs.add(tab_frame, text=title)

        # Label for input
        input_lbl = ttk.Label(tab_frame, text=input_label, font=("Helvetica", 10))
        input_lbl.pack(anchor=W, pady=5)

        # Text area for input
        input_text = ttk.Text(tab_frame, height=5, width=70)
        input_text.pack(fill=X, pady=10)

        # Process button
        process_button = ttk.Button(
            tab_frame,
            text="Process",
            bootstyle="primary",
            command=lambda: self.process_task(input_text, function, output_text)
        )
        process_button.pack(pady=5)

        # Output display area
        output_lbl = ttk.Label(tab_frame, text="Output:", font=("Helvetica", 10))
        output_lbl.pack(anchor=W, pady=5)

        output_text = ttk.Text(tab_frame, height=7, width=70, state="disabled")
        output_text.pack(fill=X, pady=5)

    def process_task(self, input_text_widget, function, output_text_widget):
        # Get input text
        input_text = input_text_widget.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Required", "Please enter the input data.")
            return

        # Process and get output based on the function passed
        output = function(input_text)

        # Display output
        output_text_widget.config(state="normal")
        output_text_widget.delete("1.0", tk.END)
        output_text_widget.insert(tk.END, output if isinstance(output, str) else "\n".join(map(str, output)))
        output_text_widget.config(state="disabled")


# Main function to run the GUI application
def main():
    root = ttk.Window(themename="darkly")
    app = AdvancedRegexApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
