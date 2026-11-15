from pathlib import Path

root = Path("skills")
failures: list[str] = []

for skill in sorted(root.iterdir()):
    if not skill.is_dir():
        continue
    guide = skill / "SKILL.md"
    metadata = skill / "agents" / "openai.yaml"
    if not guide.is_file():
        failures.append(f"{skill}: missing SKILL.md")
        continue
    text = guide.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
        failures.append(f"{guide}: missing required skill frontmatter")
    if not metadata.is_file():
        failures.append(f"{skill}: missing agents/openai.yaml")
        continue
    config = metadata.read_text(encoding="utf-8")
    if "default_prompt:" not in config or ("$" + skill.name) not in config:
        failures.append(f"{metadata}: default prompt must name the skill")

if failures:
    raise SystemExit("\n".join(failures))
print(f"Validated {len(list(root.iterdir()))} skill folders.")
