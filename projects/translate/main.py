import sys
from pathlib import Path
from tqdm import tqdm
from deep_translator import GoogleTranslator


def translate_srt(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []
    for line in tqdm(lines, desc=f"Translating {Path(input_path).name}"):
        if line.strip() and not line.strip().isdigit() and '-->' not in line:
            translated = GoogleTranslator(source='de', target='en').translate(line)
            translated_lines.append(translated + '\n')
        else:
            translated_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)


if __name__ == "__main__":    
    input_path = sys.argv[1] if len(sys.argv) > 1 else "yourfile.srt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "translated.srt"
    translate_srt(input_path=input_path, output_path=output_path)
