from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')


name = "py-elastic-integration-testing"
module_name = "py_elastic_int_testing"
default_task = "publish"
version = "0.1"


@init
def set_properties(project):
    project.set_property("dir_source_unittest_python", "src/test/python")
    project.set_property("unittest_module_glob", "test_*.py")
    project.depends_on_requirements("requirements.txt")
