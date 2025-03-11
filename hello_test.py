import hello;
import io;

def test_hello(capsys):
    hello.main() 
    captured = capsys.readouterr()
    expected_output = "Hello\nWorld!"
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()

    assert  output == expected_output