"""Script to create three sample eygl files.

  * default using basic constructor values
  * big-endian file using sample prescription
  * little-endian file using same prescription
"""

import eyeglass


def main():
    """Primary entry point for this script."""
    eygl = eyeglass.Eyeglass()
    eygl.save("default-sample-1.0-be")  # default constructor output
    # prescription taken from the following Wiki link and augmented for
    # creative purposes: http://en.wikipedia.org/wiki/File:Specrx-prescription2.jpg
    eygl.set_sphere(-3.35, +0.50)
    eygl.set_cylinder(-0.25, -1.00)
    eygl.set_axis(130, 80)
    eygl.set_prism(0, 0)
    eygl.set_base(0, 0)
    eygl.set_distance_acuity(0.66, 0.5)
    eygl.set_near_acuity(12, 12)
    eygl.set_purpose("Distance and Close Work.")
    eygl.set_observations(
        "Patient's eyesight needs correction. History of diabetes in family but indicators found. Standard checkup interval recommended."
    )
    eygl.set_next_checkup(1)
    eygl.save("prescription-sample-1.0-be", True)  # big-endian
    eygl.save("prescription-sample-1.0-le", False)  # little-endian


if __name__ == "__main__":
    main()
