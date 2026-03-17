"""Smoke tests - no API required. Run: python scripts/check.py or python -m scripts.check"""
import sys
from pathlib import Path

# Ensure project root is on path when run as scripts/check.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def main():
    errors = []

    # 1. Imports
    try:
        from company import Company
        from policy import Policy
        from company.planner import parse_plan_tasks, get_default_tasks
        print("1. Imports: OK")
    except Exception as e:
        errors.append(f"Imports: {e}")
        return 1

    # 2. Policy heuristic
    try:
        p = Policy()
        assert p.choose_role_for_task("Build FastAPI backend") == "Engineer"
        assert p.choose_role_for_task("Create landing page") == "Marketing"
        assert p.choose_role_for_task("Write cold outreach emails") == "Sales"
        print("2. Policy heuristic: OK")
    except Exception as e:
        errors.append(f"Policy: {e}")

    # 3. Plan parsing
    try:
        plan = """
Engineer: Build API
Marketing: Landing page copy
Sales: Outreach emails
"""
        tasks = parse_plan_tasks(plan)
        assert len(tasks) == 3
        assert tasks[0] == ("Engineer", "Build API")
        print("3. Plan parsing: OK")
    except Exception as e:
        errors.append(f"Plan parsing: {e}")

    # 4. Default tasks
    try:
        tasks = get_default_tasks("TestCo")
        assert len(tasks) >= 3
        print("4. Default tasks: OK")
    except Exception as e:
        errors.append(f"Default tasks: {e}")

    # 5. Company init
    try:
        c = Company()
        assert c.memory is not None
        assert c.policy is not None
        print("5. Company init: OK")
    except Exception as e:
        errors.append(f"Company init: {e}")

    if errors:
        print("\nFAILED:", errors)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
