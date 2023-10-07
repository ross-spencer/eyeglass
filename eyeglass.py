"""Eyeglass reference implementation.

  * useful reference: http://www.dwp.gov.uk/publications/specialist-guides/medical-conditions/a-z-of-medical-conditions/vision/visual-acuity-vision.shtml
  * wikipedia-acuity: http://en.wikipedia.org/wiki/Visual_acuity
  * wikipedia-eyeglass: http://en.wikipedia.org/wiki/Eyeglass_prescription
  * recommended extension: eygl
"""

import datetime
import struct


# pylint: disable=R0902,R0904
class Eyeglass:
    """Eyeglass Object Definition."""

    ISODATETIMELEN = 19  # LENGTH OF DATETIME STRING

    def __init__(self):
        """Eyeglass initialization."""

        self.eof_bof()
        self.date_today()

        # right: oculus dexter (OD)
        # left:  oculus sinister (OS)
        # both:  oculus uterque (OU)

        # Amount of short/long sightedness plus/minus (float)
        self.sphere = {
            "right": 0,
            "left": 0,
        }
        # Amount of astigmatism (float)
        self.cylinder = {"right": 0, "left": 0}
        # Orientation of cylinder (integer)
        self.axis = {"right": 0, "left": 0}
        # Correction required to help muscles of eyes coordinate
        # (usually blank: float(?))
        self.prism = {
            "right": 0,
            "left": 0,
        }
        # Direction in which prism is placed (usually blank: float(?))
        self.base = {
            "right": 0,
            "left": 0,
        }
        # 6 divided by...60 36 24 18 12 9 6 5
        self.distance_acuity = {
            "right": 0,
            "left": 0,
        }
        # N...24 18 14 12 10 8 6 5	(integer)
        self.near_acuity = {"right": 0, "left": 0}
        # Purpose of the eyewear (140 characters)
        self.purpose = ""
        # Optician's observations (255 characters)
        self.observations = ""
        # Next recommended checkup: (Years (Float))
        self.next_checkup = 0
        # Big endian flag.
        self.bigendian = None

        # Endianness fields.
        self.float = None
        self.bool = None
        self.byte = None
        self.int = None

    def eof_bof(self):
        """End of file, beginning of file setters."""
        self.magic = b"\xBB\x0D\x0A\x65\x79\x65\x67\x6C\x61\x73\x73\x1A\x0A\xAB"  # 00 01 0D 0A eyeglass 1A 0A
        self.expansion = ""
        self.eof = b"\xBB\x65\x6f\x66"  # EOF
        self.version = 1

    def date_today(self):
        """Set the date of the new Eyeglass object.

        Example:

         * 2012-11-07T00:44:41

        """
        datetime.time(microsecond=0)
        date = datetime.datetime.now()
        self.datetime = date.isoformat("T")[: self.ISODATETIMELEN]

    def __endian__(self, bigendian):
        """Private function to help demonstrate endianness to callers of
        the script.
        """
        self.bigendian = bigendian
        if bigendian is not True:
            self.float = "<f"
            self.bool = "<?"
            self.byte = "<B"
            self.int = "<i"
            return
        self.float = ">f"
        self.bool = ">?"
        self.byte = ">B"
        self.int = ">i"
        return

    def save(self, filename, bigendian=True):
        """Save an Eyeglass file object."""

        self.__endian__(bigendian)

        with open(filename + ".eygl", "wb") as file:
            file.write(struct.pack("14s", self.magic))
            file.write(struct.pack(self.byte, self.version))  # unsigned char
            file.write(struct.pack(self.bool, self.bigendian))  # bool
            file.write(f"{self.datetime}".encode())

            # padding
            file.write(struct.pack(">88s", f"{self.expansion}".encode()))

            # sphere
            file.write(struct.pack(self.float, self.sphere["right"]))
            file.write(struct.pack(self.float, self.sphere["left"]))

            # cylinder
            file.write(struct.pack(self.float, self.cylinder["right"]))
            file.write(struct.pack(self.float, self.cylinder["left"]))

            # axis
            file.write(struct.pack(self.int, self.axis["right"]))
            file.write(struct.pack(self.int, self.axis["left"]))

            # prism
            file.write(struct.pack(self.float, self.prism["right"]))
            file.write(struct.pack(self.float, self.prism["left"]))

            # base
            file.write(struct.pack(self.float, self.base["right"]))
            file.write(struct.pack(self.float, self.base["left"]))

            # distance acuity
            file.write(struct.pack(self.float, self.distance_acuity["right"]))
            file.write(struct.pack(self.float, self.distance_acuity["left"]))

            # near acuity
            file.write(struct.pack(self.int, self.near_acuity["right"]))
            file.write(struct.pack(self.int, self.near_acuity["left"]))

            # addendum
            file.write(
                struct.pack("140s", f"{self.purpose}".encode())
            )  # 140 characters.
            file.write(
                struct.pack("255s", f"{self.observations}".encode())
            )  # 255 characters.
            file.write(struct.pack(self.float, self.next_checkup))

            # eof
            file.write(struct.pack("4s", self.eof))

    # Setters.
    def set_sphere(self, right, left):
        """Set sphere variable in Eyeglass record."""
        self.sphere["right"] = right
        self.sphere["left"] = left

    def set_cylinder(self, right, left):
        """Set cylinder variable in Eyeglass record."""
        self.cylinder["right"] = right
        self.cylinder["left"] = left

    def set_axis(self, right, left):
        """Set axis variable in Eyeglass record."""
        self.axis["right"] = right
        self.axis["left"] = left

    def set_prism(self, right, left):
        """Set prism variable in Eyeglass record."""
        self.prism["right"] = right
        self.prism["left"] = left

    def set_base(self, right, left):
        """Set base variable in Eyeglass record."""
        self.base["right"] = right
        self.base["left"] = left

    def set_distance_acuity(self, right, left):
        """Set distance acuity variable in Eyeglass record."""
        self.distance_acuity["right"] = right
        self.distance_acuity["left"] = left

    def set_near_acuity(self, right, left):
        """Set near acuity variable in Eyeglass record."""
        self.near_acuity["right"] = right
        self.near_acuity["left"] = left

    def set_purpose(self, purpose):
        """Set the Eyewear purpose."""
        self.purpose = purpose

    def set_observations(self, observations):
        """Set the observations by the Optician."""
        self.observations = observations

    def set_next_checkup(self, next_checkup):
        """Set the date (years) for the next checkup."""
        self.next_checkup = next_checkup

    # Getters.
    def get_sphere(self):
        """Get the sphere value from the Eyeglass record."""
        return self.sphere

    def get_cylinder(self):
        """Get the cylinder value from the Eyeglass record."""
        return self.cylinder

    def get_axis(self):
        """Get the axis value from the Eyeglass record."""
        return self.axis

    def get_prism(self):
        """Get the prism value from the Eyeglass record."""
        return self.prism

    def get_base(self):
        """Get the base variable from the Eyeglass record."""
        return self.base

    def get_distance_acuity(self):
        """Get the distance acuity value from the Eyeglass record."""
        return self.distance_acuity

    def get_near_acuity(self):
        """Get the near acuity value from the Eyeglass record."""
        return self.near_acuity

    def get_purpose(self):
        """Get the purpose of the Eyewear value from the Eyeglass
        record."""
        return self.purpose

    def get_observations(self):
        """Get the optician's observations from the Eyeglass record."""
        return self.observations

    def get_next_checkup(self):
        """Get the value for the next checup from the Eyeglass record."""
        return self.next_checkup
