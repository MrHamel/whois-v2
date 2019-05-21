from app.parsing.icann_parser import ICANNParser
from app.parsing import parse

with open('test/icann_format_data.txt') as f:
    icann_test_data = f.read()

#icann_parser = ICANNParser('as57782.net', icann_test_data)
#icann_parser.parse()
#print(icann_parser.get_data())
print(parse('as57782.net', icann_test_data))