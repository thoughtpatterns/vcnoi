{
  description = "Developer shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python313;
        virtiofsd = pkgs.writeShellScriptBin "virtiofsd" ''
          exec ${pkgs.virtiofsd}/bin/virtiofsd \
            --translate-uid "map:1000:$('${pkgs.coreutils}/bin/id' -u):1" \
            --translate-gid "map:1000:$('${pkgs.coreutils}/bin/id' -g):1" \
            "$@"
        '';
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            cairo
            cmake
            gpac
            mpv
            ninja
            pango
            pkg-config
            podman
            python
            qemu
            uv
            virtiofsd
          ];

          CONTAINER_CONNECTION = "podman-machine-default";

          shellHook = ''
            if ! [ -d .venv ]
            then uv venv -p ${python}/bin/python
            fi

            unset VIRTUAL_ENV
            . .venv/bin/activate

            export PATH="$(realpath ./bin):$PATH"
          '';
        };
      }
    );
}
