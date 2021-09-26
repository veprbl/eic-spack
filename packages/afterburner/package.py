# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Afterburner(CMakePackage):
    """An EIC Monte Carlo Afterburner for beam effects."""

    homepage = "https://eicweb.phy.anl.gov/monte_carlo/afterburner"
    url      = "https://eicweb.phy.anl.gov/monte_carlo/afterburner/-/archive/v0.0.1/afterburner-v0.0.1.tar.gz"
    list_url = "https://eicweb.phy.anl.gov/monte_carlo/afterburner/-/tags"
    git      = "https://eicweb.phy.anl.gov/monte_carlo/afterburner"

    maintainers = ['wdconinc', 'DraTeots']

    version('main', branch='main')
    version('0.0.2', sha256='76cdd518c99f6d66d712b483e72ef8eb810635533441e126968961eabce53ea6')
    version('0.0.1', sha256='58074f917bbe8b007d08c80190b9087b1705136b99abbbed6ebf285656b3e5cf')

    variant('root', default=False, description='Support reading ROOT files')
    variant('zlib', default=True, description='Support reading compressed files')

    depends_on('gsl')
    depends_on('hepmc3')
    depends_on('clhep')
    depends_on('yaml-cpp')
    depends_on('root', when='+root')
    depends_on('zlib', when='+zlib')

    root_cmakelists_dir = 'cpp'

    def cmake_args(self):
        if '+root' in self.spec:
            cxxstd = self.spec['root'].variants['cxxstd'].value
        else:
            cxxstd = '11'
        args = [
            self.define("CMAKE_CXX_STANDARD", cxxstd)
        ]
        return args
