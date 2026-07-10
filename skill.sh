#!/usr/bin/env bash

if [[ $# -eq 0 ]]; then
  echo "Usage: source ./skill.sh <skill-name>"
  echo "Available skills: brand-orchestrator brand-agent-roles brand-architect base-logo-generator mascot-logo-generator logo-colorway-generator content-copy-validator typography-system-designer japanese-typography-consultant corporate-website-generator social_media_skill design-runtime-v2"
  return 0 2>/dev/null || exit 0
fi

case "$1" in
  brand-orchestrator)
    echo "skills/brand-orchestrator/SKILL.md"
    ;;
  brand-agent-roles)
    echo "skills/brand-agent-roles/SKILL.md"
    ;;
  brand-architect)
    echo "skills/brand-architect/SKILL.md"
    ;;
  base-logo-generator)
    echo "skills/base-logo-generator/SKILL.md"
    ;;
  mascot-logo-generator)
    echo "skills/mascot-logo-generator/SKILL.md"
    ;;
  logo-colorway-generator)
    echo "skills/logo-colorway-generator/SKILL.md"
    ;;
  content-copy-validator)
    echo "skills/content-copy-validator/SKILL.md"
    ;;
  typography-system-designer)
    echo "skills/typography-system-designer/SKILL.md"
    ;;
  japanese-typography-consultant)
    echo "skills/japanese-typography-consultant/SKILL.md"
    ;;
  corporate-website-generator)
    echo "skills/corporate-website-generator/SKILL.md"
    ;;
  social_media_skill)
    echo "skills/social_media_skill.py"
    ;;
  design-runtime-v2)
    echo "core/runtime.py"
    ;;
  *)
    echo "Unknown skill: $1" >&2
    echo "Available skills: brand-orchestrator brand-agent-roles brand-architect base-logo-generator mascot-logo-generator logo-colorway-generator content-copy-validator typography-system-designer japanese-typography-consultant corporate-website-generator social_media_skill design-runtime-v2" >&2
    return 1 2>/dev/null || exit 1
    ;;
esac
