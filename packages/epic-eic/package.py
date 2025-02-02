from spack import *


class EpicEic(CMakePackage):
    """The EPIC Detector at IP6 of the Electron-Ion Collider."""

    homepage = "https://epic-eic.org"
    url = "https://github.com/eic/epic/archive/refs/tags/22.10.0.zip"
    list_url = "https://github.com/eic/epic/tags"
    git = "https://github.com/eic/epic"

    maintainers = ["wdconinc"]

    tags = ["eic"]

    version("main", branch="main")
    version(
        "23.10.0",
        sha256="abf833eea328afb749c1eabbc83072c1382f02fc547ce7e9291e0616db552a0e",
    )
    version(
        "23.09.1",
        sha256="1fc30d36461e5acc3a54f475e9c01132aca12e74cc2fbec78fb3073fa83782b5",
    )
    version(
        "23.09.0",
        sha256="6f2ced07ead619ad4096246966383f7362d34fb140f8c0f3f60e775401deb303",
    )
    version(
        "23.08.0",
        sha256="1a8f82ef75d19dfad7228fcb437736622fc984caf0cf06466209124a8559d968",
    )
    version(
        "23.07.2",
        sha256="e80c31a338e41766aecc76441ac7aed7d53ddf401c7ca8773b0124536096ef2d",
    )
    version(
        "23.07.1",
        sha256="7e5908b3a64941ca2ff81195d62b3da6c8a20c4431f903a3c1bdda30bd39fac3",
    )
    version(
        "23.07.0",
        sha256="3b2fd83ee1664cb6bb47e45098c0357649d33526bac1e8637118bec4cd88295e",
    )
    version(
        "23.06.1",
        sha256="c78a756f84f34c6bb7b39e2bb104ffa7bcb2c7d0dcbdaa7905fe44f81e7b17aa",
    )
    version(
        "23.06.0",
        sha256="3e9825457920b97cab1bc73f44b8cfc45130f66a5d00c4acde4f8b9079a661b1",
    )
    version(
        "23.05.2",
        sha256="afb31d076a7859bd4cd94d9eed237f402a5cc56100c53c933ed4a024c8ef997b",
    )
    version(
        "23.05.1",
        sha256="4cac31b2619b3aafaaa9cc6a43923a97d04d74b753eb580990d569d1ef94c94d",
    )
    version(
        "23.05.0",
        sha256="a72774ffc3176178b128a4069d2a7bebfebde91192d971d0ccd3ab3392ff7977",
    )
    version(
        "23.03.0",
        sha256="16badb2418531250a81931f920e145c4be9ef93411f091d93202c23e36e91129",
    )
    version(
        "23.01.0",
        sha256="56e1d9a9ca3d81e64127f4d14fd45733dad07f6ffdec8387e6cae5e729525399",
    )
    version(
        "22.12.0",
        sha256="9de036b47ab8d0c97ab32fc788dd8300132014413013a1b19c2a3f8f3883a7ae",
    )
    version(
        "22.11.3",
        sha256="5cea46de7edf4868a361c5a75749f6c0f3d3ee941a33b956b2507581aa638232",
    )
    version(
        "22.11.2",
        sha256="f53aa7a4d992ddfb7549abedd4d6b87d61569b9530691b99640c6a635f2545c2",
    )
    version(
        "22.11.1",
        sha256="c8aded71dc707185a06557a76060661c57f24ed5eeb4a39b0ebcc63c9fc0a4fe",
    )
    version(
        "22.11.0",
        sha256="f683ed9e26b303ea428dc513d6e841efeeaa584cec44121f6a28116693d13065",
    )
    version(
        "22.10.1",
        sha256="dbd70d2d5ab42f3979ba4e7cda87cbb8cc48b37c4d13a887bbf96c3b32c347e9",
    )
    version(
        "22.10.0",
        sha256="f683ed9e26b303ea428dc513d6e841efeeaa584cec44121f6a28116693d13065",
    )

    variant(
        "ip",
        default="6",
        values=("6"),
        when="@:22.11",
        description="Interaction point design",
    )

    depends_on("dd4hep@1.21: +ddg4 +ddrec", when="@:23.03.0")
    depends_on("dd4hep@1.21: +ddrec", when="@23.05.0:")

    depends_on("acts-dd4hep", when="@:23.01.0")

    depends_on("fmt +shared")
    depends_on("py-pyyaml")
    depends_on("py-jinja2")

    depends_on("eic-ip6", when="@:22.11 ip=6")

    with when("@:22.11"):
        phases = ["cmake", "build", "install", "postinstall"]
    with when("@22.12:"):
        phases = ["cmake", "build", "install"]

    @when("@:22.11")
    def postinstall(self, spec, prefix):
        ip = "ip" + spec.variants["ip"].value
        # Symlinks are not copied to view, so we have to make a full copy
        # Ref: https://github.com/spack/spack/issues/19531#issuecomment-793012461
        # symlink(join_path(self.spec['eic-' + ip].prefix, 'share', ip, ip),
        #        join_path(prefix, 'share/epic', ip))
        # FIXME: when issue above is resolved, go back to symlinking
        copy_tree(
            join_path(self.spec["eic-" + ip].prefix, "share", ip, ip),
            join_path(prefix, "share/epic", ip),
        )

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("JUGGLER_DETECTOR_PATH", join_path(self.prefix.share, "epic"))
        env.set("JUGGLER_DETECTOR", "epic")
        env.set("JUGGLER_DETECTOR_CONFIG", "epic")
        env.set("JUGGLER_DETECTOR_VERSION", str(self.spec.version))
        env.set("DETECTOR_PATH", join_path(self.prefix.share, "epic"))
        env.set("DETECTOR", "epic")
        env.set("DETECTOR_CONFIG", "epic")
        env.set("DETECTOR_VERSION", str(self.spec.version))
