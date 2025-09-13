#!/usr/bin/env python3
"""
DSA Practice CLI Tool
====================

Command-line interface for managing DSA solutions, similar to npm scripts.
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# from rich import print as rprint  # Unused import

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def main():
    """DSA Practice CLI - Manage your DSA solutions with ease!"""
    pass


@main.command()
@click.option(
    "--platform",
    "-p",
    default="leetcode",
    type=click.Choice(["leetcode", "codeforces", "topcoder", "codechef"]),
    help="Platform name (default: leetcode)",
)
@click.option(
    "--difficulty",
    "-d",
    type=click.Choice(["easy", "medium", "hard"]),
    help="Difficulty level (for LeetCode)",
)
@click.option(
    "--division",
    "-div",
    type=click.Choice(["div1", "div2", "div3", "div4"]),
    help="Division (for Codeforces)",
)
@click.option(
    "--contest",
    "-c",
    type=click.Choice(["srm", "marathon"]),
    help="Contest type (for TopCoder)",
)
@click.option(
    "--type",
    "-t",
    type=click.Choice(["long", "short", "cookoff", "lunchtime"]),
    help="Contest type (for CodeChef)",
)
@click.argument("question_number", type=int)
@click.argument("problem_name")
def create(
    platform: str,
    difficulty: Optional[str],
    division: Optional[str],
    contest: Optional[str],
    type: Optional[str],
    question_number: int,
    problem_name: str,
):
    """Create a new solution with all necessary files.

    Examples:
        dsa create 1 two-sum
        dsa create --platform codeforces --division div2 1000 problem-a
        dsa create --platform leetcode --difficulty medium 15 3sum
    """
    # Format question number with zero padding
    formatted_number = f"{question_number:04d}"

    # Determine directory structure based on platform
    if platform == "leetcode":
        if not difficulty:
            difficulty = "easy"  # Default to easy
        target_dir = f"src/platforms/leetcode/{difficulty}"
        template_file = "src/platforms/leetcode/template.py"
    elif platform == "codeforces":
        if not division:
            division = "div2"  # Default to div2
        target_dir = f"src/platforms/codeforces/{division}"
        template_file = "src/platforms/codeforces/template.py"
    elif platform == "topcoder":
        if not contest:
            contest = "srm"  # Default to srm
        target_dir = f"src/platforms/topcoder/{contest}"
        template_file = "src/platforms/topcoder/template.py"
    elif platform == "codechef":
        if not type:
            type = "long"  # Default to long
        target_dir = f"src/platforms/codechef/{type}"
        template_file = "src/platforms/codechef/template.py"

    # Create solution file
    solution_filename = f"{formatted_number}.{problem_name}.py"
    solution_path = project_root / target_dir / solution_filename

    # Create test file
    test_filename = f"{formatted_number}.{problem_name}.toml"
    test_path = project_root / "data" / "test_cases" / test_filename

    # Create directories if they don't exist
    solution_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.parent.mkdir(parents=True, exist_ok=True)

    # Copy template and customize
    if (project_root / template_file).exists():
        template_content = (project_root / template_file).read_text()

        # Customize the template
        class_name = problem_name.replace("-", "_").replace("_", " ").title().replace(" ", "")
        problem_title = problem_name.replace("-", " ").title()
        customized_content = (
            template_content.replace(
                "class Solution(BaseSolution):",
                f"class {class_name}(BaseSolution):",
            )
            .replace(
                'super().__init__("Your Problem Name")',
                f'super().__init__("{problem_title}")',
            )
            .replace(
                "data/test_cases/0001.your_problem.toml",
                f"data/test_cases/{test_filename}",
            )
        )

        solution_path.write_text(customized_content)
        rel_path = solution_path.relative_to(project_root)
        console.print(f"✅ Created solution: {rel_path}")
    else:
        console.print(f"❌ Template not found: {template_file}")
        return

    # Create TOML test file
    problem_title = problem_name.replace("-", " ").title()
    test_content = f"""# {problem_title} Test Cases
# ==========================
# Test cases for {platform.title()} {question_number}: {problem_title}

[problem]
name = "{problem_title}"
description = "Problem description goes here"
difficulty = "{difficulty or 'medium'}"
platform = "{platform.title()}"
problem_id = {question_number}

[[test_cases]]
description = "Basic example"
input = [1, 2, 3]
expected = [0, 1]
timeout = 1.0

[[test_cases]]
description = "Edge case"
input = []
expected = []
timeout = 1.0
"""

    test_path.write_text(test_content)
    test_rel_path = test_path.relative_to(project_root)
    console.print(f"✅ Created test file: {test_rel_path}")

    # Show next steps
    console.print(
        Panel(
            f"""
[bold green]Solution created successfully![/bold green]

[bold]Next steps:[/bold]
1. Edit the solution: [cyan]{solution_path.relative_to(project_root)}[/cyan]
2. Add test cases: [cyan]{test_path.relative_to(project_root)}[/cyan]
3. Run the solution: [cyan]dsa run {formatted_number}.{problem_name}[/cyan]
4. Test the solution: [cyan]dsa test {formatted_number}.{problem_name}[/cyan]

[bold]Quick commands:[/bold]
• [cyan]dsa run {formatted_number}.{problem_name}[/cyan] - Run the solution
• [cyan]dsa test {formatted_number}.{problem_name}[/cyan] - Run tests
• [cyan]dsa edit {formatted_number}.{problem_name}[/cyan] - Open in editor
""",
            title="🎉 Success",
            border_style="green",
        )
    )


@main.command()
@click.argument("solution_name")
def run(solution_name: str):
    """Run a solution with full analytics.

    Examples:
        dsa run 0001.two-sum
        dsa run 0002.add-two-numbers
    """
    solution_path = find_solution_file(solution_name)
    if not solution_path:
        console.print(f"❌ Solution not found: {solution_name}")
        return

    rel_path = solution_path.relative_to(project_root)
    console.print(f"🚀 Running solution: {rel_path}")
    try:
        subprocess.run([sys.executable, str(solution_path)], cwd=project_root, check=True)
        console.print("✅ Solution completed successfully!")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Solution failed with exit code {e.returncode}")
    except FileNotFoundError:
        console.print("❌ Python interpreter not found")


@main.command()
@click.argument("solution_name")
def test(solution_name: str):
    """Run tests for a solution.

    Examples:
        dsa test 0001.two-sum
        dsa test 0002.add-two-numbers
    """
    solution_path = find_solution_file(solution_name)
    if not solution_path:
        console.print(f"❌ Solution not found: {solution_name}")
        return

    rel_path = solution_path.relative_to(project_root)
    console.print(f"🧪 Running tests for: {rel_path}")
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                f"tests/unit/test_{solution_name.split('.')[1]}.py",
                "-v",
            ],
            cwd=project_root,
            check=True,
        )
        console.print("✅ Tests completed successfully!")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Tests failed with exit code {e.returncode}")
    except FileNotFoundError:
        console.print("❌ pytest not found. Install with: pip install pytest")


@main.command()
@click.argument("solution_name")
def edit(solution_name: str):
    """Open a solution in your default editor.

    Examples:
        dsa edit 0001.two-sum
        dsa edit 0002.add-two-numbers
    """
    solution_path = find_solution_file(solution_name)
    if not solution_path:
        console.print(f"❌ Solution not found: {solution_name}")
        return

    editor = os.environ.get("EDITOR", "code")  # Default to VS Code
    try:
        subprocess.run([editor, str(solution_path)], check=True)
        rel_path = solution_path.relative_to(project_root)
        console.print(f"✅ Opened {rel_path} in {editor}")
    except subprocess.CalledProcessError:
        console.print(f"❌ Failed to open editor: {editor}")
    except FileNotFoundError:
        console.print(f"❌ Editor not found: {editor}")


@main.command()
def list():
    """List all available solutions."""
    solutions = find_all_solutions()

    if not solutions:
        console.print("❌ No solutions found")
        return

    table = Table(title="Available Solutions")
    table.add_column("Platform", style="cyan")
    table.add_column("Difficulty/Type", style="magenta")
    table.add_column("Number", style="green")
    table.add_column("Name", style="yellow")
    table.add_column("File", style="blue")

    for solution in solutions:
        table.add_row(
            solution["platform"],
            solution["difficulty"],
            solution["number"],
            solution["name"],
            solution["file"],
        )

    console.print(table)


@main.command()
@click.option(
    "--platform",
    "-p",
    type=click.Choice(["leetcode", "codeforces", "topcoder", "codechef"]),
    help="Filter by platform",
)
@click.option(
    "--difficulty",
    "-d",
    type=click.Choice(["easy", "medium", "hard"]),
    help="Filter by difficulty (LeetCode only)",
)
def search(platform: Optional[str], difficulty: Optional[str]):
    """Search for solutions with filters.

    Examples:
        dsa search --platform leetcode
        dsa search --platform leetcode --difficulty easy
    """
    solutions = find_all_solutions()

    if platform:
        solutions = [s for s in solutions if s["platform"] == platform]

    if difficulty:
        solutions = [s for s in solutions if s["difficulty"] == difficulty]

    if not solutions:
        console.print("❌ No solutions found matching criteria")
        return

    table = Table(title=f"Search Results ({len(solutions)} found)")
    table.add_column("Platform", style="cyan")
    table.add_column("Difficulty/Type", style="magenta")
    table.add_column("Number", style="green")
    table.add_column("Name", style="yellow")
    table.add_column("File", style="blue")

    for solution in solutions:
        table.add_row(
            solution["platform"],
            solution["difficulty"],
            solution["number"],
            solution["name"],
            solution["file"],
        )

    console.print(table)


@main.command()
def clean():
    """Clean up generated files (cache, reports, etc.)."""
    console.print("🧹 Cleaning up generated files...")

    # Directories to clean
    cleanup_dirs = [
        "reports",
        "benchmark_results",
        "htmlcov",
        ".pytest_cache",
        "__pycache__",
        ".coverage",
    ]

    cleaned_count = 0
    for dir_name in cleanup_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            if dir_path.is_dir():
                import shutil

                shutil.rmtree(dir_path)
                console.print(f"✅ Removed directory: {dir_name}")
                cleaned_count += 1
            else:
                dir_path.unlink()
                console.print(f"✅ Removed file: {dir_name}")
                cleaned_count += 1

    console.print(f"🎉 Cleaned {cleaned_count} items")


@main.command()
def install():
    """Install all dependencies."""
    console.print("📦 Installing dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            cwd=project_root,
            check=True,
        )
        console.print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Installation failed with exit code {e.returncode}")


def find_solution_file(solution_name: str) -> Optional[Path]:
    """Find a solution file by name."""
    # Remove .py extension if present
    if solution_name.endswith(".py"):
        solution_name = solution_name[:-3]

    # Search in all solution directories
    search_dirs = [
        "src/platforms/leetcode/easy",
        "src/platforms/leetcode/medium",
        "src/platforms/leetcode/hard",
        "src/platforms/codeforces/div1",
        "src/platforms/codeforces/div2",
        "src/platforms/codeforces/div3",
        "src/platforms/codeforces/div4",
        "src/platforms/topcoder/srm",
        "src/platforms/topcoder/marathon",
        "src/platforms/codechef/long",
        "src/platforms/codechef/short",
        "src/platforms/codechef/cookoff",
        "src/platforms/codechef/lunchtime",
    ]

    for search_dir in search_dirs:
        solution_path = project_root / search_dir / f"{solution_name}.py"
        if solution_path.exists():
            return solution_path

    return None


def find_all_solutions() -> list:
    """Find all solution files."""
    solutions = []

    # Define platform mappings
    platform_mapping = {
        "src/platforms/leetcode/easy": ("leetcode", "easy"),
        "src/platforms/leetcode/medium": ("leetcode", "medium"),
        "src/platforms/leetcode/hard": ("leetcode", "hard"),
        "src/platforms/codeforces/div1": ("codeforces", "div1"),
        "src/platforms/codeforces/div2": ("codeforces", "div2"),
        "src/platforms/codeforces/div3": ("codeforces", "div3"),
        "src/platforms/codeforces/div4": ("codeforces", "div4"),
        "src/platforms/topcoder/srm": ("topcoder", "srm"),
        "src/platforms/topcoder/marathon": ("topcoder", "marathon"),
        "src/platforms/codechef/long": ("codechef", "long"),
        "src/platforms/codechef/short": ("codechef", "short"),
        "src/platforms/codechef/cookoff": ("codechef", "cookoff"),
        "src/platforms/codechef/lunchtime": ("codechef", "lunchtime"),
    }

    for search_dir, (platform, difficulty) in platform_mapping.items():
        dir_path = project_root / search_dir
        if dir_path.exists():
            for file_path in dir_path.glob("*.py"):
                if file_path.name != "__init__.py":
                    # Parse filename (e.g., "0001.two_sum.py")
                    parts = file_path.stem.split(".")
                    if len(parts) >= 2:
                        number = parts[0]
                        name = ".".join(parts[1:])

                        solutions.append(
                            {
                                "platform": platform,
                                "difficulty": difficulty,
                                "number": number,
                                "name": name,
                                "file": str(file_path.relative_to(project_root)),
                            }
                        )

    return sorted(solutions, key=lambda x: (x["platform"], x["number"]))


if __name__ == "__main__":
    main()
