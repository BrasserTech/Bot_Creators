import json
import shutil
import os
import subprocess

def gerar_bot(json_path, nome_saida):
    with open(json_path, 'r') as f:
        cliques = json.load(f)

    with open('template_bot.py', 'r') as f:
        template = f.read()

    # Substitui o marcador pelo JSON real
    novo_codigo = template.replace('"__CLIQUES__"', json.dumps(cliques, indent=2))

    with open('bot_temp.py', 'w') as f:
        f.write(novo_codigo)

    # Gera o executável
    subprocess.run([
        'pyinstaller', '--onefile',
        '--distpath', 'bots',
        '--name', nome_saida,
        'bot_temp.py'
    ])

    # Limpeza
    os.remove('bot_temp.py')
    os.remove(f'{nome_saida}.spec')
    shutil.rmtree('build')
    shutil.rmtree('__pycache__')

if __name__ == "__main__":
    gerar_bot('scripts_salvos/exemplo.json', 'bot_gerado')
