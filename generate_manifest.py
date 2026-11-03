#!/usr/bin/env python3
"""Regenerate skills.json and CATALOG.md from skills/*/SKILL.md frontmatter.

Run from anywhere: paths are resolved relative to this file.
"""
import os
import json
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
skills_dir = os.path.join(ROOT, 'skills')

categories_map = {
    'core-agy': {
        'title': 'Google Antigravity Core & Builtin Skills',
        'description': 'Official builtin Antigravity capabilities, customizations, guides, automations, and plugins.',
        'items': [
            'agy-customizations',
            'antigravity-guide',
            'automation',
            'generative-ui',
            'migrate-workflows',
            'permissioned-github',
            'plugin',
            'run-workflow',
            'ui-plugin-navigation'
        ]
    },
    'mobile-device': {
        'title': 'Mobile & Device Engineering',
        'description': 'Mobile test automation, ARTEMIS integration, Termux Android power-user tools, and mobile ERP.',
        'items': [
            'artemis-mobile-testing',
            'termux-android-poweruser',
            'lms-android-codebase'
        ]
    },
    'backend-cloud': {
        'title': 'Cloud, Database & Backend Architecture',
        'description': 'High-performance APIs, database optimization, cloud primitives, microservices, and security.',
        'items': [
            'neon',
            'neon-postgres',
            'database-optimizer',
            'postgresql',
            'fastapi-pro',
            'python-pro',
            'typescript-advanced-types',
            'api-design-principles',
            'backend-architect',
            'microservices-patterns',
            'auth-implementation-patterns',
            'stripe-integration'
        ]
    },
    'frontend-ui': {
        'title': 'Frontend, UI/UX & Design Systems',
        'description': 'Next.js App Router, modern React, state management, Tailwind design systems, UI/UX, and accessibility.',
        'items': [
            'nextjs-app-router-patterns',
            'react-modernization',
            'react-state-management',
            'tailwind-design-system',
            'ui-ux-designer',
            'wcag-audit-patterns',
            'preview'
        ]
    },
    'devops-workflows': {
        'title': 'DevOps, Quality & Workflow Acceleration',
        'description': 'Docker containerization, CI/CD pipelines, Git mastery, security auditing, refactoring, and AI engineering.',
        'items': [
            'docker-containerization-expert',
            'deployment-pipeline-design',
            'turborepo-caching',
            'e2e-testing-patterns',
            'debugging-strategies',
            'performance-engineer',
            'git-advanced-workflows',
            'git-pr-workflows-git-workflow',
            'security-auditor',
            'code-review-excellence',
            'code-refactoring-refactor-clean',
            'architecture-patterns',
            'mermaid-expert',
            'prompt-engineering-patterns',
            'seo-structure-architect',
            'antigravity-skills-manager'
        ]
    },
    'project-memories': {
        'title': 'Private Project Codebase Memories',
        'description': 'Specialized codebase memory packages preserving deep architectural context for user projects.',
        'items': [
            'emochipk-codebase',
            'msns-build-codebase',
            'msns-home-codebase',
            'syncbay-codebase'
        ]
    }
}

def get_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
    if not m:
        return {}, ''
    raw_yaml, body = m.group(1), m.group(2)
    try:
        import yaml  # PyYAML handles folded (>-) and quoted scalars correctly
        data = yaml.safe_load(raw_yaml) or {}
        return {'name': str(data.get('name', '')).strip(),
                'description': ' '.join(str(data.get('description', '')).split())}, body
    except ImportError:
        pass
    name_m = re.search(r'^name:\s*(.+)$', raw_yaml, re.MULTILINE)
    desc_m = re.search(r'^description:\s*(?:>-\s*)?(.*?)(?:\n[a-zA-Z0-9_-]+:|\Z)', raw_yaml, re.DOTALL | re.MULTILINE)
    name = name_m.group(1).strip() if name_m else ''
    desc = ' '.join(desc_m.group(1).strip().split()) if desc_m else ''
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1].strip()
    return {'name': name, 'description': desc}, body

manifest = {
    'name': 'h470skills',
    'version': '1.1.0',
    'author': 'h410m-h',
    'description': 'Curated master collection of Google Antigravity (AGY) core skills, power-user capabilities, full-stack playbooks, and codebase memories.',
    'categories': {}
}

total = sum(len(c['items']) for c in categories_map.values())
catalog_md = ['# 🚀 h470skills — Master AGY & AI Engineering Skills Catalog\n\n']
catalog_md.append(f'> A unified, battle-tested collection of **{total} Agent Skills** engineered for Google Antigravity (`agy`), Claude Code, and agentic workflows.\n\n---\n\n')

all_categorized = set()
for cat_id, cat_info in categories_map.items():
    manifest['categories'][cat_id] = {
        'title': cat_info['title'],
        'description': cat_info['description'],
        'skills': []
    }
    catalog_md.append(f"## 📦 {cat_info['title']}\n\n")
    catalog_md.append(f"{cat_info['description']}\n\n")
    catalog_md.append('| Skill | Slash Command | Description |\n| :--- | :--- | :--- |\n')

    for s_name in cat_info['items']:
        all_categorized.add(s_name)
        skill_path = os.path.join(skills_dir, s_name, 'SKILL.md')
        meta = {}
        if os.path.exists(skill_path):
            meta, _ = get_frontmatter(skill_path)
        desc = meta.get('description', '')
        short_desc = desc if len(desc) < 140 else desc[:137] + '...'
        short_desc = short_desc.replace('|', '\\|')
        catalog_md.append(f"| [`{s_name}`](./skills/{s_name}/SKILL.md) | `/{s_name}` | {short_desc} |\n")
        manifest['categories'][cat_id]['skills'].append({
            'id': s_name,
            'name': meta.get('name') or s_name,
            'path': f'skills/{s_name}',
            'description': desc
        })
    catalog_md.append('\n---\n\n')

all_dirs = set(d for d in os.listdir(skills_dir) if not os.path.islink(os.path.join(skills_dir, d)))
unassigned = all_dirs - all_categorized
missing = all_categorized - all_dirs
if unassigned:
    print('Unassigned skills (add them to categories_map):', sorted(unassigned))
if missing:
    print('Categorised skills with no directory:', sorted(missing))
if unassigned or missing:
    sys.exit(1)

manifest['count'] = total
with open(os.path.join(ROOT, 'skills.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
    f.write('\n')

with open(os.path.join(ROOT, 'CATALOG.md'), 'w', encoding='utf-8') as f:
    f.writelines(catalog_md)

print('Successfully generated skills.json and CATALOG.md!')
