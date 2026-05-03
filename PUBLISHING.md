# Publishing

## 1. Configure Git identity

If this machine has not configured Git identity:

```bash
git config --global user.name "Tang Chao"
git config --global user.email "your-email@example.com"
```

Or configure only this repository:

```bash
git config user.name "Tang Chao"
git config user.email "your-email@example.com"
```

## 2. Commit

```bash
git add .
git commit -m "Initial ACSM sports nutrition coach skill"
```

## 3. Create GitHub repository

Create an empty GitHub repository, then connect and push:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_NAME/acsm-sports-nutrition-coach.git
git push -u origin main
```

## 4. Install path

The skill path inside the repository is:

```text
skills/acsm-sports-nutrition-coach
```

## 5. Pre-publish checks

Run:

```bash
cd skills/acsm-sports-nutrition-coach
python3 -m py_compile scripts/search_course.py
python3 scripts/search_course.py --limit 5 碳水
python3 scripts/search_course.py --limit 5 蛋白质
python3 scripts/search_course.py --limit 5 补剂
```

Before publishing, confirm the repository does not contain:

- Original textbook PDFs.
- Course videos or audio.
- Long copyrighted textbook excerpts.
- Private student information.
