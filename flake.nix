{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-stable";

  outputs = {
    self,
    nixpkgs,
  }: let
    supportedSystems = ["x86_64-linux"];
    forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
    pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
  in {
    packages =
      forAllSystems (system: {
      });

    devShells = forAllSystems (system: {
      default = pkgs.${system}.mkShell {
        packages = with pkgs.python3.withPackages; [
          python-pkgs.pygame
        ];
      };
    });
  };
}
