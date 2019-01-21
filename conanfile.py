from conans import ConanFile


class TurtleConan(ConanFile):
    commit_sha1 = "1b5d8c8"
    name = "turtle"
    version = "master-"+commit_sha1
    license = "Boost Software License 1.0"
    author = "David Callu ledocc.conan at gmail.com"
    url = ""
    description = "C++ mock object library for Boost http://turtle.sourceforge.net"
    topics = ("c++", "test", "mock")
    no_copy_source = True
    requires = "boost/1.69.0@conan/stable" # comma-separated list of requirements

    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code
        in the folder and use exports instead of retrieving it with this
        source() method
        '''
        self.run("git clone https://github.com/mat007/turtle.git")
        self.run("cd turtle && git checkout "+self.commit_sha1)

    def package(self):
        self.copy("*.hpp", src="turtle/include", dst="include")
        self.copy("LICENSE_1_0.txt", src="turtle", dst="licenses")

    def package_id(self):
        self.info.header_only()
