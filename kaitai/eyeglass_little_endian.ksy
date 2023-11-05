meta:
   id: eyeglass_format
   file-extension: eygl
   xref:
      wikidata: Q105858419
   endian: le
   tags:
    - digipres
   license: CC-BY-SA
doc: |
   The eyeglass file format. A digital preservation training format.
seq:
   - id: magic
     type: magic
     size: 14
   - id: version
     size: 1
   - id: endianness
     type: s1
   - id: datetime
     size: 19
     type: str
     doc: "the date this file was created"
     encoding: utf-8
   - id: format_expansion_room
     size: 88
     doc: "provides space to extend the format in future"
   - id: sphere_right_left
     type: f4
     repeat: expr
     repeat-expr: 2
   - id: cylinder_right_left
     type: f4
     repeat: expr
     repeat-expr: 2
   - id: axis_right_left
     type: s4
     repeat: expr
     repeat-expr: 2
   - id: prism_right_left
     type: f4
     repeat: expr
     repeat-expr: 2
   - id: base_right_left
     type: f4
     repeat: expr
     repeat-expr: 2
   - id: distance_acuity_right_left
     type: f4
     repeat: expr
     repeat-expr: 2
   - id: near_acuity_right_left
     type: s4
     repeat: expr
     repeat-expr: 2
   - id: purpose
     size: 140
     type: str
     encoding: utf-8
   - id: observation
     size: 255
     type: str
     encoding: utf-8
   - id: next_checkup_years
     type: f4
   - id: eof
     type: eof
     size: 4
types:
   magic:
      seq:
         - id: magic_1
           size: 3
           doc: "contains non-UTF-8 characters per the specification"
         - id: magic_2
           size: 8
           encoding: utf-8
           type: str
           doc: "string 'eyeglass'"
         - id: magic_3
           size: 3
           doc: "contains non-UTF-8 characters per the specification"
   eof:
      seq:
         - id: eof_1
           size: 1
           doc: "single non-UTF-8 character prefix"
         - id: eof_2
           size: 3
           type: str
           encoding: utf-8
           doc: "string 'eof'"
