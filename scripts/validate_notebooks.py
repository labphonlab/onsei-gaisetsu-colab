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
    if path.name.startswith('ch99_'): continue
    joined='\n'.join(markdown)
    headings={line[3:].strip() for line in joined.splitlines() if line.startswith('## ')}
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
