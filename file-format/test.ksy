# Build parser with this command:
# kaitai-struct-compiler --target python test.ksy
meta:
  id: test_record
  endian: be
seq:
  - id: records
    type: record
    repeat: eos
types:
  record:
    seq:
      - id: name
        type: str
        size: 10
        encoding: UTF-8
      - id: id_number
        type: str
        size: 8
        encoding: UTF-8
