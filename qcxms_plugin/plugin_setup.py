import qiime2
from qiime2.plugin import SemanticType
from qiime2.sdk import Artifact
from qcxms_plugin.QCxMSPlugin import QCxMSPlugin

plugin = QCxMSPlugin()
# Define a custom semantic type for your output data
MyCustomType = SemanticType('MyCustomType')

def qcxms_plugin_function() -> MyCustomType:
    # Your function code here
    print("this is a qcxms plugin")
    # Create and return an artifact of your custom semantic type
    return MyCustomType()

plugin = qiime2.plugin.Plugin(
    name='qcxms-plugin',
    version='0.1.0',
    website='https://example.com',
    package='qcxms_plugin',
    description='A QIIME 2 plugin for QCxMS.',
    short_description='Plugin for QCxMS analysis.',
)

plugin.methods.register_function(
    function=qcxms_plugin_function,
    inputs={},
    outputs=[('output', MyCustomType)],
    input_descriptions={},
    output_descriptions={},
    parameters={},
    name='qcxms-plugin-function',
    description='A description of your function.',
)
