from __future__ import annotations

from dotenv import load_dotenv

from app.validation.compile_runner import DBTRunner


def main() -> None:
    load_dotenv()
    runner = DBTRunner(project_dir="dbt_project")

    print("\n== dbt seed ==")
    seed_result = runner.seed()
    print(seed_result["stdout"])
    if seed_result["stderr"]:
        print(seed_result["stderr"])

    print("\n== dbt compile ==")
    compile_result = runner.compile()
    print(compile_result["stdout"])
    if compile_result["stderr"]:
        print(compile_result["stderr"])

    print("\n== dbt test ==")
    test_result = runner.test()
    print(test_result["stdout"])
    if test_result["stderr"]:
        print(test_result["stderr"])


if __name__ == "__main__":
    main()