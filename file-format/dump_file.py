from test_record import TestRecord

data = TestRecord.from_file('record.dat')

for r in data.records:
    print(f'name = "{r.name.strip()}", id_number = "{r.id_number}"')

