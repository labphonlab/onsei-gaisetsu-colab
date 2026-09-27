#!/usr/bin/env python3
import ast, json, os, shutil, sys, traceback
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NBS=sorted((ROOT/'notebooks').glob('*.ipynb'))
REQUIRED={
    '0': ('About this Lab', 'この実習について'),
    '1': ('Learning Goals', '学習目標'),
    '2': ('Setup', '準備'),
    '3': ('Quick Demo', 'まず試す'),
    '4': ('Explore', '観察する'),
    '5': ('Manipulate', '条件を変える'),
    '6': ('Experiment / Simulation', '実験／シミュレーション'),
    '7': ('Analyze', '分析する'),
    '8': ('Interpret', '解釈する'),
    '9': ('Paper to Read', '文献を読む'),
    '10': ('Replicate', '追試する'),
    '11': ('Extend / Research Challenge', '発展課題／研究課題'),
    '12': ('Save / Export', '保存／書き出し'),
    '13': ('Technical Information', '技術情報'),
}
RESEARCH_REQUIRED={
    '1': ('Research Question', '研究課題'),
    '2': ('Background', '背景'),
    '3': ('Hypothesis', '仮説'),
    '4': ('Independent Variables', '独立変数'),
    '5': ('Dependent Variables', '従属変数'),
    '6': ('Stimuli', '刺激'),
    '7': ('Participants', '参加者'),
    '8': ('Experimental Design', '実験計画'),
    '9': ('Pilot', '予備実験'),
    '10': ('Data Collection', 'データ収集'),
    '11': ('Data Cleaning', 'データクリーニング'),
    '12': ('Analysis', '分析'),
    '13': ('Visualization', '可視化'),
    '14': ('Results', '結果'),
    '15': ('Interpretation', '解釈'),
    '16': ('Limitations', '限界'),
    '17': ('Follow-up Study', '後続研究'),
}
errors=[]
for path in NBS:
    obj=json.loads(path.read_text(encoding='utf-8'))
    if obj.get('nbformat')!=4: errors.append(f'{path.name}: invalid nbformat')
    codes=[]; markdown=[]
    for cell in obj.get('cells',[]):
        source=''.join(cell.get('source',[]))
        if cell.get('cell_type')=='code':
            codes.append(source)
            try: ast.parse(source)
            except SyntaxError as exc: errors.append(f'{path.name}: {exc}')
        elif cell.get('cell_type')=='markdown': markdown.append(source)
    joined='\n'.join(markdown)
    if 'Notebook version: 1.0.1' not in joined:
        errors.append(f'{path.name}: Notebook version is not 1.0.1')
    headings={line[3:].strip() for line in joined.splitlines() if line.startswith('## ')}
    if path.name.startswith('ch99_'):
        for number, titles in RESEARCH_REQUIRED.items():
            accepted={f'{number}. {title}' for title in titles}
            if headings.isdisjoint(accepted):
                errors.append(f"{path.name}: missing section {number} ({' / '.join(titles)})")
        ethics_titles={'Ethics and licensing gate', '倫理・ライセンス確認'}
        if headings.isdisjoint(ethics_titles):
            errors.append(f"{path.name}: missing ethics and licensing section")
        continue
    for number, titles in REQUIRED.items():
        accepted={f'{number}. {title}' for title in titles}
        if headings.isdisjoint(accepted):
            errors.append(f"{path.name}: missing section {number} ({' / '.join(titles)})")
    namespace={'__name__':'__lab_validation__'}; old=os.getcwd(); os.chdir(path.parent)
    try:
        for source in codes: exec(compile(source,str(path),'exec'),namespace)
    except Exception: errors.append(f'{path.name}: execution failed\n{traceback.format_exc()}')
    finally: os.chdir(old)
results=ROOT/'notebooks/results'
if results.exists(): shutil.rmtree(results)
print(f'notebooks={len(NBS)} errors={len(errors)}')
for error in errors: print(error)
sys.exit(bool(errors))
