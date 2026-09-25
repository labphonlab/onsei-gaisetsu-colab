#!/usr/bin/env python3
import ast, json, os, shutil, sys, traceback
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NBS=sorted((ROOT/'notebooks').glob('*.ipynb'))
REQUIRED=['0. About this Lab','1. Learning Goals','2. Setup','3. Quick Demo','4. Explore','5. Manipulate','6. Experiment / Simulation','7. Analyze','8. Interpret','9. Paper to Read','10. Replicate','11. Extend / Research Challenge','12. Save / Export','13. Technical Information']
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
    for heading in REQUIRED:
        if heading not in joined: errors.append(f'{path.name}: missing {heading}')
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
