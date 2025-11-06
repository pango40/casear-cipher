import os
import time

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def show_banner():
    print(f"{Colors.CYAN}")
    print("  ════════════════════════════════════════════════════════════")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}           ██████╗ ██████╗ ██╗████████╗ ██████╗           {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██╔═══██╗██╔══██╗██║╚══██╔══╝██╔═══██╗          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██║   ██║██████╔╝██║   ██║   ██║   ██║          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ██║   ██║██╔══██╗██║   ██║   ██║   ██║          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}          ╚██████╔╝██████╔╝██║   ██║   ╚██████╔╝          {Colors.CYAN}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}           ╚═════╝ ╚═════╝ ╚═╝   ╚═╝    ╚═════╝           {Colors.CYAN}")
    print("  ────────────────────────────────────────────────────────")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}                O B I T Ō   C I P H E R                  {Colors.CYAN}")
    print("  ────────────────────────────────────────────────────────")
    print(f"  {Colors.YELLOW}            Caesar Cipher Tool v1.0                  {Colors.CYAN}")
    print(f"  {Colors.GREEN}              Secure Text Transformation              {Colors.CYAN}")
    print("  ════════════════════════════════════════════════════════════")
    print(f"{Colors.END}")
    
    print(f"{Colors.BLUE}{'═' * 60}{Colors.END}")
    print(f"{Colors.WHITE}    Secure  •  Fast  •  Interactive  •  Reliable{Colors.END}")
    print(f"{Colors.BLUE}{'═' * 60}{Colors.END}\n")

chars = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_animation_frame(current_char, current_pos, target_pos, shift, is_encoding=True):
    clear_screen()
    show_banner()

    print(f"{Colors.YELLOW}{'ENCODING Process' if is_encoding else 'DECODING Process'} | Shift: {shift}{Colors.END}")
    print(f"{Colors.BLUE}============================================================{Colors.END}")

    print(f"\n{Colors.MAGENTA}{Colors.BOLD}Character Map:{Colors.END}")
    print(f"{Colors.BLUE}    ===================================================={Colors.END}")

    print("      ", end="")
    for i, char in enumerate(chars[:14]):
        if i == current_pos:
            print(f"{Colors.RED}{Colors.BOLD} {char}  {Colors.END}", end="")
        elif i == target_pos:
            print(f"{Colors.GREEN}{Colors.BOLD} {char}  {Colors.END}", end="")
        else:
            print(f"{Colors.WHITE} {char}  {Colors.END}", end="")

    print("\n      ", end="")
    for i, char in enumerate(chars[14:], 14):
        if i == current_pos:
            print(f"{Colors.RED}{Colors.BOLD} {char}  {Colors.END}", end="")
        elif i == target_pos:
            print(f"{Colors.GREEN}{Colors.BOLD} {char}  {Colors.END}", end="")
        else:
            if char == " ":
                print(f"{Colors.WHITE} SP {Colors.END}", end=" ")
            else:
                print(f"{Colors.WHITE} {char}  {Colors.END}", end="")

    print(f"\n{Colors.BLUE}    ===================================================={Colors.END}")

    print(f"\n{Colors.YELLOW}    Current: {Colors.RED}[{chars[current_pos]}]{Colors.YELLOW} at position {current_pos}{Colors.END}")
    print(f"{Colors.YELLOW}    Target:  {Colors.GREEN}[{chars[target_pos]}]{Colors.YELLOW} at position {target_pos}{Colors.END}")

    progress = abs(current_pos - target_pos)
    total_steps = shift if is_encoding else (len(chars) - shift) % len(chars)
    bar_length = 30
    filled = int((progress / total_steps) * bar_length) if total_steps > 0 else bar_length
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n{Colors.CYAN}    Progress: [{bar}] {progress}/{total_steps} steps{Colors.END}")

    if current_pos < target_pos:
        direction = "→" * min(3, target_pos - current_pos)
    elif current_pos > target_pos:
        direction = "←" * min(3, current_pos - target_pos)
    else:
        direction = "✓"

    print(f"{Colors.MAGENTA}    Direction: {direction}{Colors.END}")

def animate_encoding(char, shift):
    if char not in chars:
        return char

    start_pos = chars.index(char)
    target_pos = (start_pos + shift) % len(chars)

    print(f"\n{Colors.CYAN}Processing: '{char}' → '{chars[target_pos]}'{Colors.END}")
    print(f"{Colors.WHITE}   Path: {start_pos} + {shift} = {target_pos} (mod {len(chars)}){Colors.END}")
    print(f"\n{Colors.BLUE}──────────────────────────────────────────────────{Colors.END}")

    current_pos = start_pos
    steps = shift

    for step in range(steps + 1):
        show_animation_frame(char, current_pos, target_pos, shift, True)

        if step < steps:
            print(f"\n{Colors.YELLOW}    Step {step + 1}/{steps}: Moving from {current_pos} to {(current_pos + 1) % len(chars)}{Colors.END}")
            time.sleep(0.8)
            current_pos = (current_pos + 1) % len(chars)
        else:
            print(f"\n{Colors.GREEN}    Complete! '{char}' → '{chars[target_pos]}'{Colors.END}")
            time.sleep(1)

    return chars[target_pos]

def animate_decoding(char, shift):
    if char not in chars:
        return char

    start_pos = chars.index(char)
    target_pos = (start_pos - shift) % len(chars)

    print(f"\n{Colors.CYAN}Processing: '{char}' → '{chars[target_pos]}'{Colors.END}")
    print(f"{Colors.WHITE}   Path: {start_pos} - {shift} = {target_pos} (mod {len(chars)}){Colors.END}")
    print(f"\n{Colors.BLUE}──────────────────────────────────────────────────{Colors.END}")

    current_pos = start_pos
    steps = shift

    for step in range(steps + 1):
        show_animation_frame(char, current_pos, target_pos, shift, False)

        if step < steps:
            print(f"\n{Colors.YELLOW}    Step {step + 1}/{steps}: Moving from {current_pos} to {(current_pos - 1) % len(chars)}{Colors.END}")
            time.sleep(0.8)
            current_pos = (current_pos - 1) % len(chars)
        else:
            print(f"\n{Colors.GREEN}    Complete! '{char}' → '{chars[target_pos]}'{Colors.END}")
            time.sleep(1)

    return chars[target_pos]

def encode_with_animation(text, shift):
    text = text.upper()
    encoded_text = ""

    print(f"\n{Colors.MAGENTA}Starting ENCODING animation for: '{text}'{Colors.END}")
    print(f"{Colors.WHITE}   Shift value: {shift}{Colors.END}")
    input(f"\n{Colors.YELLOW}   Press Enter to start animation...{Colors.END}")

    for i, char in enumerate(text):
        if char in chars:
            encoded_char = animate_encoding(char, shift)
            encoded_text += encoded_char
        else:
            encoded_text += char
            print(f"\n{Colors.RED}Skipping '{char}' - not in character list{Colors.END}")
            time.sleep(1)

    return encoded_text

def decode_with_animation(text, shift):
    text = text.upper()
    decoded_text = ""

    print(f"\n{Colors.MAGENTA}Starting DECODING animation for: '{text}'{Colors.END}")
    print(f"{Colors.WHITE}   Shift value: {shift}{Colors.END}")
    input(f"\n{Colors.YELLOW}   Press Enter to start animation...{Colors.END}")

    for i, char in enumerate(text):
        if char in chars:
            decoded_char = animate_decoding(char, shift)
            decoded_text += decoded_char
        else:
            decoded_text += char
            print(f"\n{Colors.RED}Skipping '{char}' - not in character list{Colors.END}")
            time.sleep(1)

    return decoded_text

def show_character_map():
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}Character Map:{Colors.END}")
    print(f"{Colors.BLUE}======================================================={Colors.END}")

    print(f"{Colors.CYAN}Characters:  {Colors.END}", end="")
    for char in chars[:14]:
        print(f"{Colors.WHITE} {char}  {Colors.END}", end="")

    print(f"\n{Colors.CYAN}Characters:  {Colors.END}", end="")
    for char in chars[14:]:
        if char == " ":
            print(f"{Colors.WHITE} SP {Colors.END}", end=" ")
        else:
            print(f"{Colors.WHITE} {char}  {Colors.END}", end="")

    print(f"\n{Colors.BLUE}======================================================={Colors.END}")

def main():
    while True:
        clear_screen()
        show_banner()
        
        print(f"{Colors.GREEN}1. Encode text {Colors.END}")
        print(f"{Colors.GREEN}2. Decode text {Colors.END}")
        print(f"{Colors.YELLOW}3. Show character map{Colors.END}")
        print(f"{Colors.MAGENTA}4. Quick demo{Colors.END}")
        print(f"{Colors.RED}5. Exit{Colors.END}")

        choice = input(f"\n{Colors.WHITE}Choose option (1-5): {Colors.END}")

        if choice == "1":
            show_character_map()
            text = input(f"\n{Colors.WHITE}Enter text to encode: {Colors.END}")
            try:
                shift = int(input(f"{Colors.WHITE}Enter shift key: {Colors.END}"))
                result = encode_with_animation(text, shift)
                print(f"\n{Colors.GREEN}FINAL RESULT:{Colors.END}")
                print(f"{Colors.CYAN}Original: {text}{Colors.END}")
                print(f"{Colors.YELLOW}Shift: {shift}{Colors.END}")
                print(f"{Colors.GREEN}Encoded: {result}{Colors.END}")
                input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Error: Please enter a valid number{Colors.END}")
                time.sleep(2)

        elif choice == "2":
            show_character_map()
            text = input(f"\n{Colors.WHITE}Enter text to decode: {Colors.END}")
            try:
                shift = int(input(f"{Colors.WHITE}Enter shift key: {Colors.END}"))
                result = decode_with_animation(text, shift)
                print(f"\n{Colors.GREEN}FINAL RESULT:{Colors.END}")
                print(f"{Colors.CYAN}Encoded: {text}{Colors.END}")
                print(f"{Colors.YELLOW}Shift: {shift}{Colors.END}")
                print(f"{Colors.GREEN}Decoded: {result}{Colors.END}")
                input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Error: Please enter a valid number{Colors.END}")
                time.sleep(2)

        elif choice == "3":
            show_character_map()
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")

        elif choice == "4":
            print(f"\n{Colors.MAGENTA}Running demo: 'HELLO' with shift 3{Colors.END}")
            time.sleep(2)
            result = encode_with_animation("HELLO", 3)
            print(f"\n{Colors.GREEN}Demo complete! 'HELLO' → '{result}'{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")

        elif choice == "5":
            print(f"{Colors.CYAN}Goodbye!{Colors.END}")
            break

        else:
            print(f"{Colors.RED}Invalid choice{Colors.END}")
            time.sleep(1)

if __name__ == "__main__":
    main()