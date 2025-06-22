import pytest
from pathlib import Path
from translate.main import translate_srt

def test_translate():
    print("Testing the translate_srt function...")

    input_path = str(Path(__file__).parent/"data/Love_Sucks-Licht_und_Schatten_(S01_E01)-0897185390.srt")
    translated = translate_srt(input_path=input_path)
    print(translated)
    assert translated[2] == '<font color = "#ffffff">* rain ripples. *</font>\n'
    assert translated[6] == '<font color = "#ffff00"> Zelda </font>\n'
    assert translated[10] == '<font color = "#00ffff"> ben </font>\n'
    assert translated[14] == '<font color = "#00ff00"> Theo </font>\n'
    assert translated[18] == '<font color = "#ffffff">* quiet </font>\n'
    assert translated[19] == '<font color = "#ffffff"> melancholic piano music *</font>\n'


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-s"]))