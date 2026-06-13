#!/usr/bin/env bash

if [[ $# -eq 0 ]]; then
  echo "Usage: source ./skill.sh <skill-name>"
  echo "Available skills: base-logo-generator mascot-logo-generator logo-colorway-generator"
  return 0 2>/dev/null || exit 0
fi

case "$1" in
  base-logo-generator)
    echo "skills/base-logo-generator/SKILL.md"
    ;;
  mascot-logo-generator)
    echo "skills/mascot-logo-generator/SKILL.md"
    ;;
  logo-colorway-generator)
    echo "skills/logo-colorway-generator/SKILL.md"
    ;;
  *)
    echo "Unknown skill: $1" >&2
    echo "Available skills: base-logo-generator mascot-logo-generator logo-colorway-generator" >&2
    return 1 2>/dev/null || exit 1
    ;;
esac
