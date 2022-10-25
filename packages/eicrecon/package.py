# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eicrecon(CMakePackage):
    """EIC Reconstruction - JANA based."""

    homepage = "https://github.com/eic/eicrecon"
    url = "https://github.com/eic/EICrecon/archive/refs/tags/v0.1.0.zip"
    git = "https://github.com/eic/eicrecon.git"
    list_url = "https://github.com/eic/EICrecon/tags"

    maintainers = ["wdconinc"]

    version("main", branch="main")
    version(
        "0.2.7",
        sha256="afcb8addea452c610b7ab1e5bfc179e062de0f1407605a7ae36b68bc55a2bc3a"
    )
    version(
        "0.2.6",
        sha256="819982d86cfb6f51661eb113af7eba337adda8d694cabfcd79dfc7f794f73226",
    )
    version(
        "0.2.5",
        sha256="c87970284130590049e4b40ad595fceab31daf22143e7e1afb08836b8c68170c",
    )
    version(
        "0.2.4",
        sha256="d8c55f54767f783eea8bf4939ef837fc73373ed71bd1509fdd5ae46aca4d8fa5",
    )
    version(
        "0.2.3",
        sha256="2660cb18272a932555ee1f690bcd904335feb1a6d8969859834307b24a937fd0",
    )
    version(
        "0.2.2",
        sha256="de8e5ef71465027226debfe4d42b8a4f883ffcb03ce2bfee0a0d247a4a1e89f2",
    )
    version(
        "0.2.1",
        sha256="097fef82cacd45453770f30e7e0ae382a11660b8bd4dfe478e7488a8988b8816",
    )
    version(
        "0.2.0",
        sha256="3fc0b812637d6bca9587cb4dadcd4b2ca386458ff6d46551ed8cf291335b4780",
    )
    version(
        "0.1.0",
        sha256="dcc8b60530a627c825413c07472659ba155600339ef8b8e742e3c997bcc504ae",
    )

    depends_on("cmake@3.16:", type="build")

    depends_on("jana2 +root +zmq")
    depends_on("dd4hep +ddrec +edm4hep")
    depends_on("edm4eic")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("acts +dd4hep +identification +tgeo")
    depends_on("root")
    depends_on("fmt")
    depends_on("spdlog")

    def setup_run_environment(self, env):
        env.prepend_path('JANA_PLUGIN_PATH', os.path.join(self.prefix, 'lib', 'EICrecon', 'plugins'))

