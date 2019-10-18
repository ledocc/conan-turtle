from cpt.packager import ConanMultiPackager, tools


if __name__ == "__main__":
    builder = ConanMultiPackager(
        reference="turtle/{}".format( tools.load("version.txt") )
    )
    builder.add_common_builds()
    builder.run()
