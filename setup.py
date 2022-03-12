from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='${version}',
    description='Blog System base on Django',
    author='shj',
    author_email='1027118385@qq.com',
    url='https://www.the5fire.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': [  # 方法一：打包数据文件 需要按目录层级匹配
        'themes/*/*/*/**',
    ]},
    # include_package_data = True,  #方法二：配合MANIFEST.in文件
    install_requires=[
        'django~=1.11',

    ],
    extras_require={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'typeidea/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage=manage:main',
        ]
    },
    classifiers=[  # Optional
        # 软件成熟度如何？一般有一下几种选项
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 指明项目的受众
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # 选择项目的许可证(License)
        'License :: OSI Approved :: MIT License',

        # 指定项目需要使用的Python版本
        'Programming Language :: Python :: 3.8',
    ],
)
