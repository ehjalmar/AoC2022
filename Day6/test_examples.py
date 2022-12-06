from part1 import *
from part2 import *

class TestClass:
    def test_part1_example1(self):
        assert findStartOfPacket("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    
    def test_part1_example2(self):
        assert findStartOfPacket("nppdvjthqldpwncqszvftbrmjlhg") == 6

    def test_part1_example3(self):
        assert findStartOfPacket("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10

    def test_part1_example4(self):
        assert findStartOfPacket("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    def test_pear_should_be_isorgam(self):
        assert is_isogram('pear') == True
    
    def test_apple_should__NOT_be_isorgam(self):
        assert is_isogram('apple') == False
    
    def test_part2_example1(self):
        assert findStartOfMessage("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    
    def test_part2_example2(self):
        assert findStartOfMessage("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23

    def test_part2_example3(self):
        assert findStartOfMessage("nppdvjthqldpwncqszvftbrmjlhg") == 23

    def test_part2_example4(self):
        assert findStartOfMessage("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    
    def test_part2_example5(self):
        assert findStartOfMessage("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
