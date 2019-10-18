from conans import ConanFile, tools


class TurtleConan(ConanFile):

    name = "turtle"
    version = tools.load("version.txt").rstrip()
    license = "Boost Software License 1.0"
    author = "David Callu ledocc at gmail.com"
    url = "https://github.com/ledocc/conan-turtle"
    description = "C++ mock object library for Boost http://turtle.sourceforge.net and Catch2"
    topics = ("c++", "test", "mock")
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True
    exports = ("version.txt")
    requires = "boost/1.69.0@conan/stable"

    def source(self):
        tools.get('https://github.com/mat007/turtle/archive/v{}.tar.gz'.format( self.version ),
                  sha256='1ea10600a4046286a781c898ed3110d48fdab473f5320dc48cc2775353039b8b')

    def package(self):
        source_dir = "{}-{}".format(self.name, self.version)
        self.copy("*.hpp", src="{}/include".format(source_dir), dst="include")
        self.copy("LICENSE_1_0.txt", src=source_dir, dst="licenses")

    def package_id(self):
        self.info.header_only()
