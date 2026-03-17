"""Console output formatting."""
import re

# ANSI colors (Windows 10+ supports)
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"


def section(title: str):
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'='*60}{RESET}\n")


def agent_action(role: str, action: str):
    role_colors = {"CEO": MAGENTA, "Engineer": GREEN, "Marketing": YELLOW, "Sales": CYAN}
    color = role_colors.get(role, RESET)
    print(f"{color}[{role}]{RESET} {action}")


def agent_result(role: str, result: str, max_len: int = 300):
    preview = result[:max_len] + "..." if len(result) > max_len else result
    print(f"{DIM}{preview}{RESET}\n")
