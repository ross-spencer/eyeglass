eyeglass
========

Sample 'file format' specification and applications for understanding issues in digital preservation. The format stores the information required for an eyeglass prescription for a single patient.

###Specification

    Eyeglass Format Specification 1.0
    ---
    Magic number    - 14 bytes  - String
    Version         - 1 bytes   - Unsigned Char
    Big-endian      - 1 byte    - Bool
    Date/time       - 19 bytes  - String #YYYY-MM-DDTHH:MM:SS
    Expansion room  - 88 bytes  - Undefined
    Sphere          - 8 bytes   - R: Float   L: Float
    Cylinder        - 8 bytes   - R: Float   L: Float
    Axis            - 8 bytes   - R: Integer L: Integer
    Prism           - 8 bytes   - R: Float   L: Float
    Base            - 8 bytes   - R: Float   L: Float
    Distance acuity - 8 bytes   - R: Float   L: Float
    Near acuity     - 8 bytes   - R: Integer L: Integer
    Purpose         - 140 bytes - String
    Observation     - 255 bytes - String
    Next checkup    - 4 bytes   - Float
    End of file     - 4 bytes   - String