from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='giacomo',
    maintainer_email='giacomo.mutti@studenti.unitn.it',
    description='package for a distributed system of rovers sending relative position to an anchor which suns an MDS algorithm to find the platoon configuration',
    license='Apache License 2.0',
    tests_require=['pytest'],
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
                'rover = mds_rover.rover:main'
                'anchor = mds_rover.anchor:main'
        ],
},
)