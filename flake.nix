{
  description = "my project description";

  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = nixpkgs.legacyPackages.${system}; in
        {
          devShells.default = pkgs.mkShell {
            packages = [
              (pkgs.python3.withPackages (python-pkgs: [
                python-pkgs.flask
                python-pkgs.flask-sqlalchemy
              ]))
            ];
          };
        });
}